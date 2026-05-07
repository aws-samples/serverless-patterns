import {
    withDurableExecution,
} from "@aws/durable-execution-sdk-js";
import { SNSClient, PublishCommand } from "@aws-sdk/client-sns";
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient, PutCommand } from "@aws-sdk/lib-dynamodb";
import { randomUUID } from 'crypto';

const snsClient = new SNSClient({});
const ddbClient = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(ddbClient);

const storeCallbackToken = async (callbackId, submission) => {
    const approvalId = randomUUID().split('-')[0]; // Short ID like "a1b2c3d4"
    // TTL matches callback timeout (1 hour) + 5 minute buffer
    const ttl = Math.floor(Date.now() / 1000) + (65 * 60); // 1 hour 5 minutes

    await docClient.send(new PutCommand({
        TableName: process.env.CALLBACK_TABLE_NAME,
        Item: {
            approvalId: approvalId,
            callbackId: callbackId,
            submissionId: submission.submissionId,
            submitterEmail: submission.submitter.email,
            ttl: ttl,
            createdAt: new Date().toISOString()
        }
    }));

    return approvalId;
};

const sendApprovalRequest = async (submission, callbackId) => {
    try {
        // Store callback token in DynamoDB and get short approval ID
        const approvalId = await storeCallbackToken(callbackId, submission);

        const baseUrl = `${process.env.API_URL}verify`;
        const approveUrl = `${baseUrl}?id=${approvalId}&action=approve`;
        const rejectUrl = `${baseUrl}?id=${approvalId}&action=reject`;

        // Format line items for email
        const itemsList = submission.document.items
            .map(item => `  • ${item.description}: $${item.amount.toFixed(2)}`)
            .join('\n');

        const message = `
            APPROVAL REQUIRED: ${submission.document.title}

            Submission ID: ${submission.submissionId}
            Submitted by: ${submission.submitter.name} (${submission.submitter.department})
            Employee ID: ${submission.submitter.employeeId}

            Document Details:
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            Category: ${submission.document.category}
            Total Amount: $${submission.document.amount.toFixed(2)} ${submission.document.currency}

            Description:
            ${submission.document.description}

            Expense Breakdown:
            ${itemsList}

            Attachments: ${submission.document.attachments.length} file(s)
            ${submission.document.attachments.map(a => `  • ${a.split('/').pop()}`).join('\n')}

            Submitted: ${new Date(submission.submittedAt).toLocaleString()}
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

            Please review and take action:

            ✓ APPROVE: ${approveUrl}

            ✗ REJECT: ${rejectUrl}

            This link will expire in 1 hour.

            Note: Approval ID for reference: ${approvalId}
        `.trim();

        const params = {
            TopicArn: process.env.SNS_TOPIC_ARN,
            Subject: `Approval Required: ${submission.document.title} - $${submission.document.amount.toFixed(2)}`,
            Message: message
        };
        const command = new PublishCommand(params);
        const result = await snsClient.send(command);
        return {
            status: "succeeded",
            result: result,
            approvalId: approvalId
        };
    } catch (error) {
        console.log("An error occurred sending approval request: ", error)
        return {
            status: "failed",
            error: error
        };
    }
};

const handler = async (event, context) => {
    try {
        // Use the context logger for structured logging
        context.logger.info("Starting HITL workflow for document submission", {
            submissionId: event.submissionId,
            submissionType: event.submissionType
        });

        // Validate required fields
        if (!event.submissionId) {
            return { error: "Missing submissionId" };
        }
        if (!event.submitter || !event.submitter.email || !event.submitter.name) {
            return { error: "Missing submitter information" };
        }
        if (!event.document) {
            return { error: "Missing document information" };
        }

        // Step 1: Validate and load submission data
        const submission = await context.step("validate-submission", async () => {
            context.logger.info("Validating submission", {
                submissionId: event.submissionId,
                amount: event.document.amount
            });

            return {
                submissionId: event.submissionId,
                submissionType: event.submissionType,
                submitter: event.submitter,
                document: event.document,
                submittedAt: event.submittedAt,
                status: "pending_approval"
            };
        });

        context.logger.info("Submission validated", {
            submissionId: submission.submissionId,
            status: submission.status
        });

        // Step 2: Send approval request and wait for human decision
        context.logger.info("Sending approval request to reviewer...");

        const approval_result = await context.waitForCallback(
            "wait-for-reviewer-approval",
            async (callbackId) => {
                await sendApprovalRequest(submission, callbackId);
            },
            {
                timeout: { hours: 1 }
            }
        );

        context.logger.info("Approval decision received", {
            approved: approval_result.approved,
            approvalId: approval_result.approvalId
        });

        // Step 3: Process the approval decision
        const result = await context.step("process-approval-decision", async () => {
            if (approval_result.approved === true) {
                context.logger.info(`Submission APPROVED`, {
                    submissionId: submission.submissionId,
                    submitter: submission.submitter.name
                });

                return {
                    status: "approved",
                    submissionId: submission.submissionId,
                    submitter: submission.submitter,
                    document: submission.document,
                    approvalDetails: {
                        approvedAt: approval_result.timestamp,
                        approvalId: approval_result.approvalId
                    },
                    nextSteps: [
                        "Payment processing initiated",
                        "Submitter notified",
                        "Documents archived"
                    ]
                };
            } else {
                context.logger.info(`Submission REJECTED`, {
                    submissionId: submission.submissionId,
                    submitter: submission.submitter.name
                });

                return {
                    status: "rejected",
                    submissionId: submission.submissionId,
                    submitter: submission.submitter,
                    document: submission.document,
                    rejectionDetails: {
                        rejectedAt: approval_result.timestamp,
                        approvalId: approval_result.approvalId
                    },
                    nextSteps: [
                        "Submitter notified of rejection",
                        "Resubmission instructions sent"
                    ]
                };
            }
        });

        context.logger.info("HITL workflow completed", {
            status: result.status,
            submissionId: result.submissionId
        });

        return result;
    } catch (error) {
        context.logger.error("Workflow failed", {
            error: error.message,
            stack: error.stack
        });
        throw error;
    }
};

export const lambdaHandler = withDurableExecution(handler);
