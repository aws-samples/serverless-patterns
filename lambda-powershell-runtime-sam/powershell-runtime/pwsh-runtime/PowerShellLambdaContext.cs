/*******************************************************************************
*   Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
*  
*  Licensed under the Apache License, Version 2.0 (the "License").
*  You may not use this file except in compliance with the License.
*  You may obtain a copy of the License at
*  
*      http://www.apache.org/licenses/LICENSE-2.0
*  
*  Unless required by applicable law or agreed to in writing, software
*  distributed under the License is distributed on an "AS IS" BASIS,
*  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*  See the License for the specific language governing permissions and
*  limitations under the License.
* *****************************************************************************/

namespace Amazon.Lambda.PowerShell.Internal
{
    using System;

    /// <summary>
    /// $LambdaContext object that allows you to access useful information available within the Lambda execution environment.
    /// </summary>
    public class LambdaContext
    {
        /// <summary>
        /// The AWS request ID associated with the request.
        /// This is the same ID returned to the client that called invoke().
        /// This ID is reused for retries on the same request.
        /// </summary>
        public string AwsRequestId { get; }

        /// <summary>
        /// Information about the client application and device when invoked
        /// through the AWS Mobile SDK. It can be null.
        /// Client context provides client information such as client ID,
        /// application title, version name, version code, and the application
        /// package name.
        /// </summary>
        public string ClientContext { get; }

        /// <summary>
        /// Name of the Lambda function that is running.
        /// </summary>
        public string FunctionName { get; }

        /// <summary>
        /// The Lambda function version that is executing.
        /// If an alias is used to invoke the function, then  will be
        /// the version the alias points to.
        /// </summary>
        public string FunctionVersion { get; }

        /// <summary>
        /// Information about the Amazon Cognito identity provider when
        /// invoked through the AWS Mobile SDK.
        /// Can be null.
        /// </summary>
        public string Identity { get; }
        /// ICognitoIdentity Identity { get; set; }

        /// <summary>
        /// The ARN used to invoke this function.
        /// It can be function ARN or alias ARN.
        /// An unqualified ARN executes the $LATEST version and aliases execute
        /// the function version they are pointing to.
        /// </summary>
        public string InvokedFunctionArn { get; }

        /// <summary>
        /// The CloudWatch log group name associated with the invoked function.
        /// It can be null if the IAM user provided does not have permission for
        /// CloudWatch actions.
        /// </summary>
        public string LogGroupName { get; }

        /// <summary>
        /// The CloudWatch log stream name for this function execution.
        /// It can be null if the IAM user provided does not have permission
        /// for CloudWatch actions.
        /// </summary>
        public string LogStreamName { get; }

        /// <summary>
        /// Memory limit, in MB, you configured for the Lambda function.
        /// </summary>
        public int MemoryLimitInMB { get; }

        /// <summary>
        /// Memory limit, in MB, you configured for the Lambda function.
        /// </summary>
        private DateTime _deadlineMS { get; }

        public LambdaContext(
            string FunctionName,
            string FunctionVersion,
            string InvokedFunctionArn,
            int MemoryLimitInMB,
            string AwsRequestId,
            string LogGroupName,
            string LogStreamName,
            string Identity,
            string ClientContext,
            double DeadlineMS
        )
        {
            this.FunctionName = FunctionName;
            this.FunctionVersion = FunctionVersion;
            this.InvokedFunctionArn = FunctionName;
            this.MemoryLimitInMB = MemoryLimitInMB;
            this.AwsRequestId = AwsRequestId;
            this.LogGroupName = LogGroupName;
            this.LogStreamName = LogStreamName;
            this.Identity = Identity;
            this.ClientContext = ClientContext;

            DateTime epoch = new DateTime(1970, 1, 1);
            this._deadlineMS = epoch.AddMilliseconds(DeadlineMS);

        }

        /// <summary>
        /// Remaining execution time till the function will be terminated.
        /// At the time you create the Lambda function you set maximum time
        /// limit, at which time AWS Lambda will terminate the function
        /// execution.
        /// Information about the remaining time of function execution can be
        /// used to specify function behavior when nearing the timeout.
        /// </summary>
        public TimeSpan RemainingTime
        {
            get => this._deadlineMS - DateTime.UtcNow;
        }
        /// <summary>
        /// Remaining execution time in Milliseconds until the function will be terminated.
        /// At the time you create the Lambda function you set maximum time
        /// limit, at which time AWS Lambda will terminate the function
        /// execution.
        /// Information about the remaining time of function execution can be
        /// used to specify function behavior when nearing the timeout.
        /// </summary>
        public Double GetRemainingTimeInMillis()
        {
            return Math.Round((this._deadlineMS - DateTime.UtcNow).TotalMilliseconds);
        }        
    }
}