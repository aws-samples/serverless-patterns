'''
# AWS::MWAA Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_mwaa as mwaa
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for MWAA construct libraries](https://constructs.dev/search?q=mwaa)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::MWAA resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MWAA.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::MWAA](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MWAA.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEnvironment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mwaa.CfnEnvironment",
):
    '''The ``AWS::MWAA::Environment`` resource creates an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mwaa as mwaa
        
        # airflow_configuration_options: Any
        # tags: Any
        
        cfn_environment = mwaa.CfnEnvironment(self, "MyCfnEnvironment",
            name="name",
        
            # the properties below are optional
            airflow_configuration_options=airflow_configuration_options,
            airflow_version="airflowVersion",
            dag_s3_path="dagS3Path",
            environment_class="environmentClass",
            execution_role_arn="executionRoleArn",
            kms_key="kmsKey",
            logging_configuration=mwaa.CfnEnvironment.LoggingConfigurationProperty(
                dag_processing_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                    enabled=False,
                    log_level="logLevel"
                ),
                scheduler_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                    enabled=False,
                    log_level="logLevel"
                ),
                task_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                    enabled=False,
                    log_level="logLevel"
                ),
                webserver_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                    enabled=False,
                    log_level="logLevel"
                ),
                worker_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                    enabled=False,
                    log_level="logLevel"
                )
            ),
            max_workers=123,
            min_workers=123,
            network_configuration=mwaa.CfnEnvironment.NetworkConfigurationProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"]
            ),
            plugins_s3_object_version="pluginsS3ObjectVersion",
            plugins_s3_path="pluginsS3Path",
            requirements_s3_object_version="requirementsS3ObjectVersion",
            requirements_s3_path="requirementsS3Path",
            schedulers=123,
            source_bucket_arn="sourceBucketArn",
            startup_script_s3_object_version="startupScriptS3ObjectVersion",
            startup_script_s3_path="startupScriptS3Path",
            tags=tags,
            webserver_access_mode="webserverAccessMode",
            weekly_maintenance_window_start="weeklyMaintenanceWindowStart"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        airflow_configuration_options: typing.Any = None,
        airflow_version: typing.Optional[builtins.str] = None,
        dag_s3_path: typing.Optional[builtins.str] = None,
        environment_class: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.LoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
        network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        plugins_s3_object_version: typing.Optional[builtins.str] = None,
        plugins_s3_path: typing.Optional[builtins.str] = None,
        requirements_s3_object_version: typing.Optional[builtins.str] = None,
        requirements_s3_path: typing.Optional[builtins.str] = None,
        schedulers: typing.Optional[jsii.Number] = None,
        source_bucket_arn: typing.Optional[builtins.str] = None,
        startup_script_s3_object_version: typing.Optional[builtins.str] = None,
        startup_script_s3_path: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        webserver_access_mode: typing.Optional[builtins.str] = None,
        weekly_maintenance_window_start: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of your Amazon MWAA environment.
        :param airflow_configuration_options: A list of key-value pairs containing the Airflow configuration options for your environment. For example, ``core.default_timezone: utc`` . To learn more, see `Apache Airflow configuration options <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html>`_ .
        :param airflow_version: The version of Apache Airflow to use for the environment. If no value is specified, defaults to the latest version. *Allowed Values* : ``2.0.2`` | ``1.10.12`` | ``2.2.2`` | ``2.4.3`` | ``2.5.1`` (latest)
        :param dag_s3_path: The relative path to the DAGs folder on your Amazon S3 bucket. For example, ``dags`` . To learn more, see `Adding or updating DAGs <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html>`_ .
        :param environment_class: The environment class type. Valid values: ``mw1.small`` , ``mw1.medium`` , ``mw1.large`` . To learn more, see `Amazon MWAA environment class <https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html>`_ .
        :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role in IAM that allows MWAA to access AWS resources in your environment. For example, ``arn:aws:iam::123456789:role/my-execution-role`` . To learn more, see `Amazon MWAA Execution role <https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html>`_ .
        :param kms_key: The AWS Key Management Service (KMS) key to encrypt and decrypt the data in your environment. You can use an AWS KMS key managed by MWAA, or a customer-managed KMS key (advanced).
        :param logging_configuration: The Apache Airflow logs being sent to CloudWatch Logs: ``DagProcessingLogs`` , ``SchedulerLogs`` , ``TaskLogs`` , ``WebserverLogs`` , ``WorkerLogs`` .
        :param max_workers: The maximum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the ``MaxWorkers`` field. For example, ``20`` . When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the one worker that is included with your environment, or the number you specify in ``MinWorkers`` .
        :param min_workers: The minimum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the ``MaxWorkers`` field. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the worker count you specify in the ``MinWorkers`` field. For example, ``2`` .
        :param network_configuration: The VPC networking components used to secure and enable network traffic between the AWS resources for your environment. To learn more, see `About networking on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`_ .
        :param plugins_s3_object_version: The version of the plugins.zip file on your Amazon S3 bucket. To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .
        :param plugins_s3_path: The relative path to the ``plugins.zip`` file on your Amazon S3 bucket. For example, ``plugins.zip`` . To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .
        :param requirements_s3_object_version: The version of the requirements.txt file on your Amazon S3 bucket. To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .
        :param requirements_s3_path: The relative path to the ``requirements.txt`` file on your Amazon S3 bucket. For example, ``requirements.txt`` . To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .
        :param schedulers: The number of schedulers that you want to run in your environment. Valid values:. - *v2* - Accepts between 2 to 5. Defaults to 2. - *v1* - Accepts 1.
        :param source_bucket_arn: The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored. For example, ``arn:aws:s3:::my-airflow-bucket-unique-name`` . To learn more, see `Create an Amazon S3 bucket for Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html>`_ .
        :param startup_script_s3_object_version: The version of the startup shell script in your Amazon S3 bucket. You must specify the `version ID <https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html>`_ that Amazon S3 assigns to the file every time you update the script. Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example: ``3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo`` For more information, see `Using a startup script <https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html>`_ .
        :param startup_script_s3_path: The relative path to the startup shell script in your Amazon S3 bucket. For example, ``s3://mwaa-environment/startup.sh`` . Amazon MWAA runs the script as your environment starts, and before running the Apache Airflow process. You can use this script to install dependencies, modify Apache Airflow configuration options, and set environment variables. For more information, see `Using a startup script <https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html>`_ .
        :param tags: The key-value tag pairs associated to your environment. For example, ``"Environment": "Staging"`` . To learn more, see `Tagging <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .
        :param webserver_access_mode: The Apache Airflow *Web server* access mode. To learn more, see `Apache Airflow access modes <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html>`_ . Valid values: ``PRIVATE_ONLY`` or ``PUBLIC_ONLY`` .
        :param weekly_maintenance_window_start: The day and time of the week to start weekly maintenance updates of your environment in the following format: ``DAY:HH:MM`` . For example: ``TUE:03:30`` . You can specify a start time in 30 minute increments only. Supported input includes the following: - MON|TUE|WED|THU|FRI|SAT|SUN:([01]\\d|2[0-3]):(00|30)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__558d6a60af086ab1a40ad8057fcb128456129bbbd328752ab90d8a6d573efb1c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentProps(
            name=name,
            airflow_configuration_options=airflow_configuration_options,
            airflow_version=airflow_version,
            dag_s3_path=dag_s3_path,
            environment_class=environment_class,
            execution_role_arn=execution_role_arn,
            kms_key=kms_key,
            logging_configuration=logging_configuration,
            max_workers=max_workers,
            min_workers=min_workers,
            network_configuration=network_configuration,
            plugins_s3_object_version=plugins_s3_object_version,
            plugins_s3_path=plugins_s3_path,
            requirements_s3_object_version=requirements_s3_object_version,
            requirements_s3_path=requirements_s3_path,
            schedulers=schedulers,
            source_bucket_arn=source_bucket_arn,
            startup_script_s3_object_version=startup_script_s3_object_version,
            startup_script_s3_path=startup_script_s3_path,
            tags=tags,
            webserver_access_mode=webserver_access_mode,
            weekly_maintenance_window_start=weekly_maintenance_window_start,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99fe3af42168ce58625550be04e1ab2f3619e791f954ebcc45ea31fac6418d74)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a60d7a2655a02c98c9d573b0523e09e82b17523acc47348eac66b5063684497a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN for the Amazon MWAA environment.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLoggingConfigurationDagProcessingLogsCloudWatchLogGroupArn")
    def attr_logging_configuration_dag_processing_logs_cloud_watch_log_group_arn(
        self,
    ) -> builtins.str:
        '''The ARN for the CloudWatch Logs group where the Apache Airflow DAG processing logs are published.

        :cloudformationAttribute: LoggingConfiguration.DagProcessingLogs.CloudWatchLogGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoggingConfigurationDagProcessingLogsCloudWatchLogGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLoggingConfigurationSchedulerLogsCloudWatchLogGroupArn")
    def attr_logging_configuration_scheduler_logs_cloud_watch_log_group_arn(
        self,
    ) -> builtins.str:
        '''The ARN for the CloudWatch Logs group where the Apache Airflow Scheduler logs are published.

        :cloudformationAttribute: LoggingConfiguration.SchedulerLogs.CloudWatchLogGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoggingConfigurationSchedulerLogsCloudWatchLogGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLoggingConfigurationTaskLogsCloudWatchLogGroupArn")
    def attr_logging_configuration_task_logs_cloud_watch_log_group_arn(
        self,
    ) -> builtins.str:
        '''The ARN for the CloudWatch Logs group where the Apache Airflow task logs are published.

        :cloudformationAttribute: LoggingConfiguration.TaskLogs.CloudWatchLogGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoggingConfigurationTaskLogsCloudWatchLogGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLoggingConfigurationWebserverLogsCloudWatchLogGroupArn")
    def attr_logging_configuration_webserver_logs_cloud_watch_log_group_arn(
        self,
    ) -> builtins.str:
        '''The ARN for the CloudWatch Logs group where the Apache Airflow Web server logs are published.

        :cloudformationAttribute: LoggingConfiguration.WebserverLogs.CloudWatchLogGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoggingConfigurationWebserverLogsCloudWatchLogGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLoggingConfigurationWorkerLogsCloudWatchLogGroupArn")
    def attr_logging_configuration_worker_logs_cloud_watch_log_group_arn(
        self,
    ) -> builtins.str:
        '''The ARN for the CloudWatch Logs group where the Apache Airflow Worker logs are published.

        :cloudformationAttribute: LoggingConfiguration.WorkerLogs.CloudWatchLogGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLoggingConfigurationWorkerLogsCloudWatchLogGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="attrWebserverUrl")
    def attr_webserver_url(self) -> builtins.str:
        '''The URL of your Apache Airflow UI.

        :cloudformationAttribute: WebserverUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWebserverUrl"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of your Amazon MWAA environment.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a37ddb6096a60d8065a1dc2caf7d063561818ed0c4e6e97ad86b9a3d907d4c8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="airflowConfigurationOptions")
    def airflow_configuration_options(self) -> typing.Any:
        '''A list of key-value pairs containing the Airflow configuration options for your environment.'''
        return typing.cast(typing.Any, jsii.get(self, "airflowConfigurationOptions"))

    @airflow_configuration_options.setter
    def airflow_configuration_options(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__476e2a2b5d2734b1339237aa0804e10a76308f821b346eabe830695103d4317b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "airflowConfigurationOptions", value)

    @builtins.property
    @jsii.member(jsii_name="airflowVersion")
    def airflow_version(self) -> typing.Optional[builtins.str]:
        '''The version of Apache Airflow to use for the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "airflowVersion"))

    @airflow_version.setter
    def airflow_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed975d4df99a5fde779ae3f2b186497fa36ce1bb285a1b7f55f1605d56390320)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "airflowVersion", value)

    @builtins.property
    @jsii.member(jsii_name="dagS3Path")
    def dag_s3_path(self) -> typing.Optional[builtins.str]:
        '''The relative path to the DAGs folder on your Amazon S3 bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dagS3Path"))

    @dag_s3_path.setter
    def dag_s3_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1a71a5a0b8013ee757182629297ba4a75e6806173de11972da672ba8f44967c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dagS3Path", value)

    @builtins.property
    @jsii.member(jsii_name="environmentClass")
    def environment_class(self) -> typing.Optional[builtins.str]:
        '''The environment class type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentClass"))

    @environment_class.setter
    def environment_class(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ceab871f965a8fc1ba17f7d497490fb21a3199979b4953a98322571ba6f88cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentClass", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the execution role in IAM that allows MWAA to access AWS resources in your environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54cc7f09d2b32c1f74a7f471eec9d0c7e97de13b8efd25ca2add91285402fdbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''The AWS Key Management Service (KMS) key to encrypt and decrypt the data in your environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20be4a6c2a8d23795165d89ef068fc76e8f67c6825b3108973093ddd02fa79ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.LoggingConfigurationProperty"]]:
        '''The Apache Airflow logs being sent to CloudWatch Logs: ``DagProcessingLogs`` , ``SchedulerLogs`` , ``TaskLogs`` , ``WebserverLogs`` , ``WorkerLogs`` .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.LoggingConfigurationProperty"]], jsii.get(self, "loggingConfiguration"))

    @logging_configuration.setter
    def logging_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.LoggingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc4cab34c101780b1065b32efa9590f9b8c2d6fa987fc778866acc8e135735b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="maxWorkers")
    def max_workers(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of workers that you want to run in your environment.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxWorkers"))

    @max_workers.setter
    def max_workers(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecb875076a1c8d331e4bdfcf6a1b5ea37cdddb27dc548d6ee55f94defe51ef6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="minWorkers")
    def min_workers(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of workers that you want to run in your environment.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minWorkers"))

    @min_workers.setter
    def min_workers(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a55d820acc52ddec2ba61ae2c198accc1e02d19de67a71e84a3356d7371702ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.NetworkConfigurationProperty"]]:
        '''The VPC networking components used to secure and enable network traffic between the AWS resources for your environment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.NetworkConfigurationProperty"]], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.NetworkConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa2a5da444619534928020a611413143accbcdd88aa14355626af4899385c73a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="pluginsS3ObjectVersion")
    def plugins_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''The version of the plugins.zip file on your Amazon S3 bucket. To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginsS3ObjectVersion"))

    @plugins_s3_object_version.setter
    def plugins_s3_object_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a99940c0cc4f750c45db524f9ae8daba6f5ad859ffcf11a0ae6fd25e322512f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginsS3ObjectVersion", value)

    @builtins.property
    @jsii.member(jsii_name="pluginsS3Path")
    def plugins_s3_path(self) -> typing.Optional[builtins.str]:
        '''The relative path to the ``plugins.zip`` file on your Amazon S3 bucket. For example, ``plugins.zip`` . To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pluginsS3Path"))

    @plugins_s3_path.setter
    def plugins_s3_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b495cb205cc5e30536d587e57390f5c1e099c11cf3fe0de627424066a4838f09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pluginsS3Path", value)

    @builtins.property
    @jsii.member(jsii_name="requirementsS3ObjectVersion")
    def requirements_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''The version of the requirements.txt file on your Amazon S3 bucket. To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requirementsS3ObjectVersion"))

    @requirements_s3_object_version.setter
    def requirements_s3_object_version(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b02f6a63345ee725961b4a13a94868c12933484401f8f4917745e0fc70e2039d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirementsS3ObjectVersion", value)

    @builtins.property
    @jsii.member(jsii_name="requirementsS3Path")
    def requirements_s3_path(self) -> typing.Optional[builtins.str]:
        '''The relative path to the ``requirements.txt`` file on your Amazon S3 bucket. For example, ``requirements.txt`` . To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requirementsS3Path"))

    @requirements_s3_path.setter
    def requirements_s3_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b21a132437156544547b8f9926353b399b2e201b2ec7c271b6a57dc6b63a840)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirementsS3Path", value)

    @builtins.property
    @jsii.member(jsii_name="schedulers")
    def schedulers(self) -> typing.Optional[jsii.Number]:
        '''The number of schedulers that you want to run in your environment.

        Valid values:.
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "schedulers"))

    @schedulers.setter
    def schedulers(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aefd5d0ab5fb759bc82b90e20d34dae2b9a92e035c60918d41a48b6f2a40f71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulers", value)

    @builtins.property
    @jsii.member(jsii_name="sourceBucketArn")
    def source_bucket_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceBucketArn"))

    @source_bucket_arn.setter
    def source_bucket_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aedd02a13d0dcf7970ae346c08229240911bc7b9d7cbf71d281e5995215d4aa6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceBucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="startupScriptS3ObjectVersion")
    def startup_script_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''The version of the startup shell script in your Amazon S3 bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startupScriptS3ObjectVersion"))

    @startup_script_s3_object_version.setter
    def startup_script_s3_object_version(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6027cf352b46c42abb5a9a07b830322d6a170945f459de6ceae996b6e0d3bf80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startupScriptS3ObjectVersion", value)

    @builtins.property
    @jsii.member(jsii_name="startupScriptS3Path")
    def startup_script_s3_path(self) -> typing.Optional[builtins.str]:
        '''The relative path to the startup shell script in your Amazon S3 bucket.

        For example, ``s3://mwaa-environment/startup.sh`` .
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startupScriptS3Path"))

    @startup_script_s3_path.setter
    def startup_script_s3_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9be888a29bdd036c7a17e6251a771f0f88b203aacc22033b8c42adc9dc7ed8c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startupScriptS3Path", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''The key-value tag pairs associated to your environment.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f022348b4c8dbea9004993f4e6a341f2e6f188d4320fbe4c6029630f93c61e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="webserverAccessMode")
    def webserver_access_mode(self) -> typing.Optional[builtins.str]:
        '''The Apache Airflow *Web server* access mode.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webserverAccessMode"))

    @webserver_access_mode.setter
    def webserver_access_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67d30d1c1ec781f42fa1686eff45aa7e4d79b300e393b02172f5d8d00e2b01b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webserverAccessMode", value)

    @builtins.property
    @jsii.member(jsii_name="weeklyMaintenanceWindowStart")
    def weekly_maintenance_window_start(self) -> typing.Optional[builtins.str]:
        '''The day and time of the week to start weekly maintenance updates of your environment in the following format: ``DAY:HH:MM`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "weeklyMaintenanceWindowStart"))

    @weekly_maintenance_window_start.setter
    def weekly_maintenance_window_start(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4b7b1ca9a0752d370dddfd37838d62fc0fdbdce81d79923961a78bfa58597a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weeklyMaintenanceWindowStart", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mwaa.CfnEnvironment.LoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dag_processing_logs": "dagProcessingLogs",
            "scheduler_logs": "schedulerLogs",
            "task_logs": "taskLogs",
            "webserver_logs": "webserverLogs",
            "worker_logs": "workerLogs",
        },
    )
    class LoggingConfigurationProperty:
        def __init__(
            self,
            *,
            dag_processing_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            scheduler_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            task_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            webserver_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            worker_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.ModuleLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The type of Apache Airflow logs to send to CloudWatch Logs.

            :param dag_processing_logs: Defines the processing logs sent to CloudWatch Logs and the logging level to send.
            :param scheduler_logs: Defines the scheduler logs sent to CloudWatch Logs and the logging level to send.
            :param task_logs: Defines the task logs sent to CloudWatch Logs and the logging level to send.
            :param webserver_logs: Defines the web server logs sent to CloudWatch Logs and the logging level to send.
            :param worker_logs: Defines the worker logs sent to CloudWatch Logs and the logging level to send.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mwaa as mwaa
                
                logging_configuration_property = mwaa.CfnEnvironment.LoggingConfigurationProperty(
                    dag_processing_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    scheduler_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    task_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    webserver_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    worker_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d823c014bd64bec48bc3afd2f5085d92c0e9f9e6f7641f491eeb3020665639f5)
                check_type(argname="argument dag_processing_logs", value=dag_processing_logs, expected_type=type_hints["dag_processing_logs"])
                check_type(argname="argument scheduler_logs", value=scheduler_logs, expected_type=type_hints["scheduler_logs"])
                check_type(argname="argument task_logs", value=task_logs, expected_type=type_hints["task_logs"])
                check_type(argname="argument webserver_logs", value=webserver_logs, expected_type=type_hints["webserver_logs"])
                check_type(argname="argument worker_logs", value=worker_logs, expected_type=type_hints["worker_logs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dag_processing_logs is not None:
                self._values["dag_processing_logs"] = dag_processing_logs
            if scheduler_logs is not None:
                self._values["scheduler_logs"] = scheduler_logs
            if task_logs is not None:
                self._values["task_logs"] = task_logs
            if webserver_logs is not None:
                self._values["webserver_logs"] = webserver_logs
            if worker_logs is not None:
                self._values["worker_logs"] = worker_logs

        @builtins.property
        def dag_processing_logs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ModuleLoggingConfigurationProperty"]]:
            '''Defines the processing logs sent to CloudWatch Logs and the logging level to send.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-dagprocessinglogs
            '''
            result = self._values.get("dag_processing_logs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ModuleLoggingConfigurationProperty"]], result)

        @builtins.property
        def scheduler_logs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ModuleLoggingConfigurationProperty"]]:
            '''Defines the scheduler logs sent to CloudWatch Logs and the logging level to send.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-schedulerlogs
            '''
            result = self._values.get("scheduler_logs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ModuleLoggingConfigurationProperty"]], result)

        @builtins.property
        def task_logs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ModuleLoggingConfigurationProperty"]]:
            '''Defines the task logs sent to CloudWatch Logs and the logging level to send.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-tasklogs
            '''
            result = self._values.get("task_logs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ModuleLoggingConfigurationProperty"]], result)

        @builtins.property
        def webserver_logs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ModuleLoggingConfigurationProperty"]]:
            '''Defines the web server logs sent to CloudWatch Logs and the logging level to send.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-webserverlogs
            '''
            result = self._values.get("webserver_logs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ModuleLoggingConfigurationProperty"]], result)

        @builtins.property
        def worker_logs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ModuleLoggingConfigurationProperty"]]:
            '''Defines the worker logs sent to CloudWatch Logs and the logging level to send.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-loggingconfiguration.html#cfn-mwaa-environment-loggingconfiguration-workerlogs
            '''
            result = self._values.get("worker_logs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ModuleLoggingConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_log_group_arn": "cloudWatchLogGroupArn",
            "enabled": "enabled",
            "log_level": "logLevel",
        },
    )
    class ModuleLoggingConfigurationProperty:
        def __init__(
            self,
            *,
            cloud_watch_log_group_arn: typing.Optional[builtins.str] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            log_level: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines the type of logs to send for the Apache Airflow log type (e.g. ``DagProcessingLogs`` ).

            :param cloud_watch_log_group_arn: The ARN of the CloudWatch Logs log group for each type of Apache Airflow log type that you have enabled. .. epigraph:: ``CloudWatchLogGroupArn`` is available only as a return value, accessible when specified as an attribute in the ```Fn:GetAtt`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#aws-resource-mwaa-environment-return-values>`_ intrinsic function. Any value you provide for ``CloudWatchLogGroupArn`` is discarded by Amazon MWAA.
            :param enabled: Indicates whether to enable the Apache Airflow log type (e.g. ``DagProcessingLogs`` ) in CloudWatch Logs.
            :param log_level: Defines the Apache Airflow logs to send for the log type (e.g. ``DagProcessingLogs`` ) to CloudWatch Logs. Valid values: ``CRITICAL`` , ``ERROR`` , ``WARNING`` , ``INFO`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mwaa as mwaa
                
                module_logging_configuration_property = mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                    enabled=False,
                    log_level="logLevel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c6a5117b2e48950b9cf3cb6591ccb275c4038c591a1df52effcf41e32ad5f232)
                check_type(argname="argument cloud_watch_log_group_arn", value=cloud_watch_log_group_arn, expected_type=type_hints["cloud_watch_log_group_arn"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument log_level", value=log_level, expected_type=type_hints["log_level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_log_group_arn is not None:
                self._values["cloud_watch_log_group_arn"] = cloud_watch_log_group_arn
            if enabled is not None:
                self._values["enabled"] = enabled
            if log_level is not None:
                self._values["log_level"] = log_level

        @builtins.property
        def cloud_watch_log_group_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the CloudWatch Logs log group for each type of Apache Airflow log type that you have enabled.

            .. epigraph::

               ``CloudWatchLogGroupArn`` is available only as a return value, accessible when specified as an attribute in the ```Fn:GetAtt`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#aws-resource-mwaa-environment-return-values>`_ intrinsic function. Any value you provide for ``CloudWatchLogGroupArn`` is discarded by Amazon MWAA.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-cloudwatchloggrouparn
            '''
            result = self._values.get("cloud_watch_log_group_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether to enable the Apache Airflow log type (e.g. ``DagProcessingLogs`` ) in CloudWatch Logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def log_level(self) -> typing.Optional[builtins.str]:
            '''Defines the Apache Airflow logs to send for the log type (e.g. ``DagProcessingLogs`` ) to CloudWatch Logs. Valid values: ``CRITICAL`` , ``ERROR`` , ``WARNING`` , ``INFO`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-moduleloggingconfiguration.html#cfn-mwaa-environment-moduleloggingconfiguration-loglevel
            '''
            result = self._values.get("log_level")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModuleLoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mwaa.CfnEnvironment.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The VPC networking components used to secure and enable network traffic between the AWS resources for your environment.

            To learn more, see `About networking on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`_ .

            :param security_group_ids: A list of one or more security group IDs. Accepts up to 5 security group IDs. A security group must be attached to the same VPC as the subnets. To learn more, see `Security in your VPC on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-security.html>`_ .
            :param subnet_ids: A list of subnet IDs. *Required* to create an environment. Must be private subnets in two different availability zones. A subnet must be attached to the same VPC as the security group. To learn more, see `About networking on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mwaa as mwaa
                
                network_configuration_property = mwaa.CfnEnvironment.NetworkConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8495822577cf5da4312474c3eb2f73589ac26428a858fe9413976d151aa232fc)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of one or more security group IDs.

            Accepts up to 5 security group IDs. A security group must be attached to the same VPC as the subnets. To learn more, see `Security in your VPC on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-security.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html#cfn-mwaa-environment-networkconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of subnet IDs.

            *Required* to create an environment. Must be private subnets in two different availability zones. A subnet must be attached to the same VPC as the security group. To learn more, see `About networking on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-networkconfiguration.html#cfn-mwaa-environment-networkconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mwaa.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "airflow_configuration_options": "airflowConfigurationOptions",
        "airflow_version": "airflowVersion",
        "dag_s3_path": "dagS3Path",
        "environment_class": "environmentClass",
        "execution_role_arn": "executionRoleArn",
        "kms_key": "kmsKey",
        "logging_configuration": "loggingConfiguration",
        "max_workers": "maxWorkers",
        "min_workers": "minWorkers",
        "network_configuration": "networkConfiguration",
        "plugins_s3_object_version": "pluginsS3ObjectVersion",
        "plugins_s3_path": "pluginsS3Path",
        "requirements_s3_object_version": "requirementsS3ObjectVersion",
        "requirements_s3_path": "requirementsS3Path",
        "schedulers": "schedulers",
        "source_bucket_arn": "sourceBucketArn",
        "startup_script_s3_object_version": "startupScriptS3ObjectVersion",
        "startup_script_s3_path": "startupScriptS3Path",
        "tags": "tags",
        "webserver_access_mode": "webserverAccessMode",
        "weekly_maintenance_window_start": "weeklyMaintenanceWindowStart",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        airflow_configuration_options: typing.Any = None,
        airflow_version: typing.Optional[builtins.str] = None,
        dag_s3_path: typing.Optional[builtins.str] = None,
        environment_class: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        kms_key: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        max_workers: typing.Optional[jsii.Number] = None,
        min_workers: typing.Optional[jsii.Number] = None,
        network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        plugins_s3_object_version: typing.Optional[builtins.str] = None,
        plugins_s3_path: typing.Optional[builtins.str] = None,
        requirements_s3_object_version: typing.Optional[builtins.str] = None,
        requirements_s3_path: typing.Optional[builtins.str] = None,
        schedulers: typing.Optional[jsii.Number] = None,
        source_bucket_arn: typing.Optional[builtins.str] = None,
        startup_script_s3_object_version: typing.Optional[builtins.str] = None,
        startup_script_s3_path: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        webserver_access_mode: typing.Optional[builtins.str] = None,
        weekly_maintenance_window_start: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironment``.

        :param name: The name of your Amazon MWAA environment.
        :param airflow_configuration_options: A list of key-value pairs containing the Airflow configuration options for your environment. For example, ``core.default_timezone: utc`` . To learn more, see `Apache Airflow configuration options <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html>`_ .
        :param airflow_version: The version of Apache Airflow to use for the environment. If no value is specified, defaults to the latest version. *Allowed Values* : ``2.0.2`` | ``1.10.12`` | ``2.2.2`` | ``2.4.3`` | ``2.5.1`` (latest)
        :param dag_s3_path: The relative path to the DAGs folder on your Amazon S3 bucket. For example, ``dags`` . To learn more, see `Adding or updating DAGs <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html>`_ .
        :param environment_class: The environment class type. Valid values: ``mw1.small`` , ``mw1.medium`` , ``mw1.large`` . To learn more, see `Amazon MWAA environment class <https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html>`_ .
        :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role in IAM that allows MWAA to access AWS resources in your environment. For example, ``arn:aws:iam::123456789:role/my-execution-role`` . To learn more, see `Amazon MWAA Execution role <https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html>`_ .
        :param kms_key: The AWS Key Management Service (KMS) key to encrypt and decrypt the data in your environment. You can use an AWS KMS key managed by MWAA, or a customer-managed KMS key (advanced).
        :param logging_configuration: The Apache Airflow logs being sent to CloudWatch Logs: ``DagProcessingLogs`` , ``SchedulerLogs`` , ``TaskLogs`` , ``WebserverLogs`` , ``WorkerLogs`` .
        :param max_workers: The maximum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the ``MaxWorkers`` field. For example, ``20`` . When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the one worker that is included with your environment, or the number you specify in ``MinWorkers`` .
        :param min_workers: The minimum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the ``MaxWorkers`` field. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the worker count you specify in the ``MinWorkers`` field. For example, ``2`` .
        :param network_configuration: The VPC networking components used to secure and enable network traffic between the AWS resources for your environment. To learn more, see `About networking on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`_ .
        :param plugins_s3_object_version: The version of the plugins.zip file on your Amazon S3 bucket. To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .
        :param plugins_s3_path: The relative path to the ``plugins.zip`` file on your Amazon S3 bucket. For example, ``plugins.zip`` . To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .
        :param requirements_s3_object_version: The version of the requirements.txt file on your Amazon S3 bucket. To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .
        :param requirements_s3_path: The relative path to the ``requirements.txt`` file on your Amazon S3 bucket. For example, ``requirements.txt`` . To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .
        :param schedulers: The number of schedulers that you want to run in your environment. Valid values:. - *v2* - Accepts between 2 to 5. Defaults to 2. - *v1* - Accepts 1.
        :param source_bucket_arn: The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored. For example, ``arn:aws:s3:::my-airflow-bucket-unique-name`` . To learn more, see `Create an Amazon S3 bucket for Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html>`_ .
        :param startup_script_s3_object_version: The version of the startup shell script in your Amazon S3 bucket. You must specify the `version ID <https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html>`_ that Amazon S3 assigns to the file every time you update the script. Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example: ``3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo`` For more information, see `Using a startup script <https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html>`_ .
        :param startup_script_s3_path: The relative path to the startup shell script in your Amazon S3 bucket. For example, ``s3://mwaa-environment/startup.sh`` . Amazon MWAA runs the script as your environment starts, and before running the Apache Airflow process. You can use this script to install dependencies, modify Apache Airflow configuration options, and set environment variables. For more information, see `Using a startup script <https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html>`_ .
        :param tags: The key-value tag pairs associated to your environment. For example, ``"Environment": "Staging"`` . To learn more, see `Tagging <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .
        :param webserver_access_mode: The Apache Airflow *Web server* access mode. To learn more, see `Apache Airflow access modes <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html>`_ . Valid values: ``PRIVATE_ONLY`` or ``PUBLIC_ONLY`` .
        :param weekly_maintenance_window_start: The day and time of the week to start weekly maintenance updates of your environment in the following format: ``DAY:HH:MM`` . For example: ``TUE:03:30`` . You can specify a start time in 30 minute increments only. Supported input includes the following: - MON|TUE|WED|THU|FRI|SAT|SUN:([01]\\d|2[0-3]):(00|30)

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mwaa as mwaa
            
            # airflow_configuration_options: Any
            # tags: Any
            
            cfn_environment_props = mwaa.CfnEnvironmentProps(
                name="name",
            
                # the properties below are optional
                airflow_configuration_options=airflow_configuration_options,
                airflow_version="airflowVersion",
                dag_s3_path="dagS3Path",
                environment_class="environmentClass",
                execution_role_arn="executionRoleArn",
                kms_key="kmsKey",
                logging_configuration=mwaa.CfnEnvironment.LoggingConfigurationProperty(
                    dag_processing_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    scheduler_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    task_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    webserver_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    ),
                    worker_logs=mwaa.CfnEnvironment.ModuleLoggingConfigurationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        enabled=False,
                        log_level="logLevel"
                    )
                ),
                max_workers=123,
                min_workers=123,
                network_configuration=mwaa.CfnEnvironment.NetworkConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                ),
                plugins_s3_object_version="pluginsS3ObjectVersion",
                plugins_s3_path="pluginsS3Path",
                requirements_s3_object_version="requirementsS3ObjectVersion",
                requirements_s3_path="requirementsS3Path",
                schedulers=123,
                source_bucket_arn="sourceBucketArn",
                startup_script_s3_object_version="startupScriptS3ObjectVersion",
                startup_script_s3_path="startupScriptS3Path",
                tags=tags,
                webserver_access_mode="webserverAccessMode",
                weekly_maintenance_window_start="weeklyMaintenanceWindowStart"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d7baed808ece1f6aca4fce5dbeac04c731d688aec6f3395e1f0892eae95adc4)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument airflow_configuration_options", value=airflow_configuration_options, expected_type=type_hints["airflow_configuration_options"])
            check_type(argname="argument airflow_version", value=airflow_version, expected_type=type_hints["airflow_version"])
            check_type(argname="argument dag_s3_path", value=dag_s3_path, expected_type=type_hints["dag_s3_path"])
            check_type(argname="argument environment_class", value=environment_class, expected_type=type_hints["environment_class"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument logging_configuration", value=logging_configuration, expected_type=type_hints["logging_configuration"])
            check_type(argname="argument max_workers", value=max_workers, expected_type=type_hints["max_workers"])
            check_type(argname="argument min_workers", value=min_workers, expected_type=type_hints["min_workers"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument plugins_s3_object_version", value=plugins_s3_object_version, expected_type=type_hints["plugins_s3_object_version"])
            check_type(argname="argument plugins_s3_path", value=plugins_s3_path, expected_type=type_hints["plugins_s3_path"])
            check_type(argname="argument requirements_s3_object_version", value=requirements_s3_object_version, expected_type=type_hints["requirements_s3_object_version"])
            check_type(argname="argument requirements_s3_path", value=requirements_s3_path, expected_type=type_hints["requirements_s3_path"])
            check_type(argname="argument schedulers", value=schedulers, expected_type=type_hints["schedulers"])
            check_type(argname="argument source_bucket_arn", value=source_bucket_arn, expected_type=type_hints["source_bucket_arn"])
            check_type(argname="argument startup_script_s3_object_version", value=startup_script_s3_object_version, expected_type=type_hints["startup_script_s3_object_version"])
            check_type(argname="argument startup_script_s3_path", value=startup_script_s3_path, expected_type=type_hints["startup_script_s3_path"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument webserver_access_mode", value=webserver_access_mode, expected_type=type_hints["webserver_access_mode"])
            check_type(argname="argument weekly_maintenance_window_start", value=weekly_maintenance_window_start, expected_type=type_hints["weekly_maintenance_window_start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if airflow_configuration_options is not None:
            self._values["airflow_configuration_options"] = airflow_configuration_options
        if airflow_version is not None:
            self._values["airflow_version"] = airflow_version
        if dag_s3_path is not None:
            self._values["dag_s3_path"] = dag_s3_path
        if environment_class is not None:
            self._values["environment_class"] = environment_class
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if logging_configuration is not None:
            self._values["logging_configuration"] = logging_configuration
        if max_workers is not None:
            self._values["max_workers"] = max_workers
        if min_workers is not None:
            self._values["min_workers"] = min_workers
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if plugins_s3_object_version is not None:
            self._values["plugins_s3_object_version"] = plugins_s3_object_version
        if plugins_s3_path is not None:
            self._values["plugins_s3_path"] = plugins_s3_path
        if requirements_s3_object_version is not None:
            self._values["requirements_s3_object_version"] = requirements_s3_object_version
        if requirements_s3_path is not None:
            self._values["requirements_s3_path"] = requirements_s3_path
        if schedulers is not None:
            self._values["schedulers"] = schedulers
        if source_bucket_arn is not None:
            self._values["source_bucket_arn"] = source_bucket_arn
        if startup_script_s3_object_version is not None:
            self._values["startup_script_s3_object_version"] = startup_script_s3_object_version
        if startup_script_s3_path is not None:
            self._values["startup_script_s3_path"] = startup_script_s3_path
        if tags is not None:
            self._values["tags"] = tags
        if webserver_access_mode is not None:
            self._values["webserver_access_mode"] = webserver_access_mode
        if weekly_maintenance_window_start is not None:
            self._values["weekly_maintenance_window_start"] = weekly_maintenance_window_start

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of your Amazon MWAA environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def airflow_configuration_options(self) -> typing.Any:
        '''A list of key-value pairs containing the Airflow configuration options for your environment.

        For example, ``core.default_timezone: utc`` . To learn more, see `Apache Airflow configuration options <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowconfigurationoptions
        '''
        result = self._values.get("airflow_configuration_options")
        return typing.cast(typing.Any, result)

    @builtins.property
    def airflow_version(self) -> typing.Optional[builtins.str]:
        '''The version of Apache Airflow to use for the environment.

        If no value is specified, defaults to the latest version.

        *Allowed Values* : ``2.0.2`` | ``1.10.12`` | ``2.2.2`` | ``2.4.3`` | ``2.5.1`` (latest)

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-airflowversion
        '''
        result = self._values.get("airflow_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dag_s3_path(self) -> typing.Optional[builtins.str]:
        '''The relative path to the DAGs folder on your Amazon S3 bucket.

        For example, ``dags`` . To learn more, see `Adding or updating DAGs <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-dags3path
        '''
        result = self._values.get("dag_s3_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_class(self) -> typing.Optional[builtins.str]:
        '''The environment class type.

        Valid values: ``mw1.small`` , ``mw1.medium`` , ``mw1.large`` . To learn more, see `Amazon MWAA environment class <https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-environmentclass
        '''
        result = self._values.get("environment_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the execution role in IAM that allows MWAA to access AWS resources in your environment.

        For example, ``arn:aws:iam::123456789:role/my-execution-role`` . To learn more, see `Amazon MWAA Execution role <https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''The AWS Key Management Service (KMS) key to encrypt and decrypt the data in your environment.

        You can use an AWS KMS key managed by MWAA, or a customer-managed KMS key (advanced).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-kmskey
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.LoggingConfigurationProperty]]:
        '''The Apache Airflow logs being sent to CloudWatch Logs: ``DagProcessingLogs`` , ``SchedulerLogs`` , ``TaskLogs`` , ``WebserverLogs`` , ``WorkerLogs`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-loggingconfiguration
        '''
        result = self._values.get("logging_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.LoggingConfigurationProperty]], result)

    @builtins.property
    def max_workers(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of workers that you want to run in your environment.

        MWAA scales the number of Apache Airflow workers up to the number you specify in the ``MaxWorkers`` field. For example, ``20`` . When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the one worker that is included with your environment, or the number you specify in ``MinWorkers`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-maxworkers
        '''
        result = self._values.get("max_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_workers(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of workers that you want to run in your environment.

        MWAA scales the number of Apache Airflow workers up to the number you specify in the ``MaxWorkers`` field. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the worker count you specify in the ``MinWorkers`` field. For example, ``2`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-minworkers
        '''
        result = self._values.get("min_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.NetworkConfigurationProperty]]:
        '''The VPC networking components used to secure and enable network traffic between the AWS resources for your environment.

        To learn more, see `About networking on Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.NetworkConfigurationProperty]], result)

    @builtins.property
    def plugins_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''The version of the plugins.zip file on your Amazon S3 bucket. To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3objectversion
        '''
        result = self._values.get("plugins_s3_object_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plugins_s3_path(self) -> typing.Optional[builtins.str]:
        '''The relative path to the ``plugins.zip`` file on your Amazon S3 bucket. For example, ``plugins.zip`` . To learn more, see `Installing custom plugins <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-pluginss3path
        '''
        result = self._values.get("plugins_s3_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requirements_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''The version of the requirements.txt file on your Amazon S3 bucket. To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3objectversion
        '''
        result = self._values.get("requirements_s3_object_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requirements_s3_path(self) -> typing.Optional[builtins.str]:
        '''The relative path to the ``requirements.txt`` file on your Amazon S3 bucket. For example, ``requirements.txt`` . To learn more, see `Installing Python dependencies <https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-requirementss3path
        '''
        result = self._values.get("requirements_s3_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedulers(self) -> typing.Optional[jsii.Number]:
        '''The number of schedulers that you want to run in your environment. Valid values:.

        - *v2* - Accepts between 2 to 5. Defaults to 2.
        - *v1* - Accepts 1.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-schedulers
        '''
        result = self._values.get("schedulers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def source_bucket_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored.

        For example, ``arn:aws:s3:::my-airflow-bucket-unique-name`` . To learn more, see `Create an Amazon S3 bucket for Amazon MWAA <https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-sourcebucketarn
        '''
        result = self._values.get("source_bucket_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def startup_script_s3_object_version(self) -> typing.Optional[builtins.str]:
        '''The version of the startup shell script in your Amazon S3 bucket.

        You must specify the `version ID <https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html>`_ that Amazon S3 assigns to the file every time you update the script.

        Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example:

        ``3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo``

        For more information, see `Using a startup script <https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-startupscripts3objectversion
        '''
        result = self._values.get("startup_script_s3_object_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def startup_script_s3_path(self) -> typing.Optional[builtins.str]:
        '''The relative path to the startup shell script in your Amazon S3 bucket. For example, ``s3://mwaa-environment/startup.sh`` .

        Amazon MWAA runs the script as your environment starts, and before running the Apache Airflow process. You can use this script to install dependencies, modify Apache Airflow configuration options, and set environment variables. For more information, see `Using a startup script <https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-startupscripts3path
        '''
        result = self._values.get("startup_script_s3_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''The key-value tag pairs associated to your environment.

        For example, ``"Environment": "Staging"`` . To learn more, see `Tagging <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def webserver_access_mode(self) -> typing.Optional[builtins.str]:
        '''The Apache Airflow *Web server* access mode.

        To learn more, see `Apache Airflow access modes <https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html>`_ . Valid values: ``PRIVATE_ONLY`` or ``PUBLIC_ONLY`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-webserveraccessmode
        '''
        result = self._values.get("webserver_access_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weekly_maintenance_window_start(self) -> typing.Optional[builtins.str]:
        '''The day and time of the week to start weekly maintenance updates of your environment in the following format: ``DAY:HH:MM`` .

        For example: ``TUE:03:30`` . You can specify a start time in 30 minute increments only. Supported input includes the following:

        - MON|TUE|WED|THU|FRI|SAT|SUN:([01]\\d|2[0-3]):(00|30)

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaa-environment.html#cfn-mwaa-environment-weeklymaintenancewindowstart
        '''
        result = self._values.get("weekly_maintenance_window_start")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEnvironment",
    "CfnEnvironmentProps",
]

publication.publish()

def _typecheckingstub__558d6a60af086ab1a40ad8057fcb128456129bbbd328752ab90d8a6d573efb1c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    airflow_configuration_options: typing.Any = None,
    airflow_version: typing.Optional[builtins.str] = None,
    dag_s3_path: typing.Optional[builtins.str] = None,
    environment_class: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    kms_key: typing.Optional[builtins.str] = None,
    logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_workers: typing.Optional[jsii.Number] = None,
    min_workers: typing.Optional[jsii.Number] = None,
    network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    plugins_s3_object_version: typing.Optional[builtins.str] = None,
    plugins_s3_path: typing.Optional[builtins.str] = None,
    requirements_s3_object_version: typing.Optional[builtins.str] = None,
    requirements_s3_path: typing.Optional[builtins.str] = None,
    schedulers: typing.Optional[jsii.Number] = None,
    source_bucket_arn: typing.Optional[builtins.str] = None,
    startup_script_s3_object_version: typing.Optional[builtins.str] = None,
    startup_script_s3_path: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    webserver_access_mode: typing.Optional[builtins.str] = None,
    weekly_maintenance_window_start: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99fe3af42168ce58625550be04e1ab2f3619e791f954ebcc45ea31fac6418d74(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a60d7a2655a02c98c9d573b0523e09e82b17523acc47348eac66b5063684497a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a37ddb6096a60d8065a1dc2caf7d063561818ed0c4e6e97ad86b9a3d907d4c8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__476e2a2b5d2734b1339237aa0804e10a76308f821b346eabe830695103d4317b(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed975d4df99a5fde779ae3f2b186497fa36ce1bb285a1b7f55f1605d56390320(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1a71a5a0b8013ee757182629297ba4a75e6806173de11972da672ba8f44967c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ceab871f965a8fc1ba17f7d497490fb21a3199979b4953a98322571ba6f88cf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54cc7f09d2b32c1f74a7f471eec9d0c7e97de13b8efd25ca2add91285402fdbc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20be4a6c2a8d23795165d89ef068fc76e8f67c6825b3108973093ddd02fa79ae(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc4cab34c101780b1065b32efa9590f9b8c2d6fa987fc778866acc8e135735b0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.LoggingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecb875076a1c8d331e4bdfcf6a1b5ea37cdddb27dc548d6ee55f94defe51ef6f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a55d820acc52ddec2ba61ae2c198accc1e02d19de67a71e84a3356d7371702ab(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa2a5da444619534928020a611413143accbcdd88aa14355626af4899385c73a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.NetworkConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a99940c0cc4f750c45db524f9ae8daba6f5ad859ffcf11a0ae6fd25e322512f2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b495cb205cc5e30536d587e57390f5c1e099c11cf3fe0de627424066a4838f09(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b02f6a63345ee725961b4a13a94868c12933484401f8f4917745e0fc70e2039d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b21a132437156544547b8f9926353b399b2e201b2ec7c271b6a57dc6b63a840(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aefd5d0ab5fb759bc82b90e20d34dae2b9a92e035c60918d41a48b6f2a40f71(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aedd02a13d0dcf7970ae346c08229240911bc7b9d7cbf71d281e5995215d4aa6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6027cf352b46c42abb5a9a07b830322d6a170945f459de6ceae996b6e0d3bf80(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9be888a29bdd036c7a17e6251a771f0f88b203aacc22033b8c42adc9dc7ed8c7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f022348b4c8dbea9004993f4e6a341f2e6f188d4320fbe4c6029630f93c61e8(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67d30d1c1ec781f42fa1686eff45aa7e4d79b300e393b02172f5d8d00e2b01b0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4b7b1ca9a0752d370dddfd37838d62fc0fdbdce81d79923961a78bfa58597a8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d823c014bd64bec48bc3afd2f5085d92c0e9f9e6f7641f491eeb3020665639f5(
    *,
    dag_processing_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.ModuleLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scheduler_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.ModuleLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.ModuleLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    webserver_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.ModuleLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    worker_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.ModuleLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6a5117b2e48950b9cf3cb6591ccb275c4038c591a1df52effcf41e32ad5f232(
    *,
    cloud_watch_log_group_arn: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    log_level: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8495822577cf5da4312474c3eb2f73589ac26428a858fe9413976d151aa232fc(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d7baed808ece1f6aca4fce5dbeac04c731d688aec6f3395e1f0892eae95adc4(
    *,
    name: builtins.str,
    airflow_configuration_options: typing.Any = None,
    airflow_version: typing.Optional[builtins.str] = None,
    dag_s3_path: typing.Optional[builtins.str] = None,
    environment_class: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    kms_key: typing.Optional[builtins.str] = None,
    logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_workers: typing.Optional[jsii.Number] = None,
    min_workers: typing.Optional[jsii.Number] = None,
    network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    plugins_s3_object_version: typing.Optional[builtins.str] = None,
    plugins_s3_path: typing.Optional[builtins.str] = None,
    requirements_s3_object_version: typing.Optional[builtins.str] = None,
    requirements_s3_path: typing.Optional[builtins.str] = None,
    schedulers: typing.Optional[jsii.Number] = None,
    source_bucket_arn: typing.Optional[builtins.str] = None,
    startup_script_s3_object_version: typing.Optional[builtins.str] = None,
    startup_script_s3_path: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    webserver_access_mode: typing.Optional[builtins.str] = None,
    weekly_maintenance_window_start: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
