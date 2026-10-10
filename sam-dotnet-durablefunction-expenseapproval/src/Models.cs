namespace ExpenseApproval;

/// <summary>
/// An expense report submitted for approval.
/// </summary>
public record ExpenseReport(
    string ExpenseId,
    string SubmittedBy,
    string Description,
    decimal Amount,
    string Currency,
    string ManagerEmail);

/// <summary>
/// The decision made by a manager on an expense report.
/// </summary>
public record ApprovalDecision(
    string ExpenseId,
    string Decision,      // "approved" or "rejected"
    string DecidedBy,
    string? Reason);

/// <summary>
/// Final result of the expense workflow.
/// </summary>
public record ExpenseResult(
    string ExpenseId,
    string Status,         // "approved", "rejected", or "timed_out"
    string? ApprovedBy,
    string? Reason,
    string? ReimbursementId,
    DateTime CompletedAt);
