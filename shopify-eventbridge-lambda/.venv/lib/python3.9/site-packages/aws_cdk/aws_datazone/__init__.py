'''
# AWS::DataZone Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_datazone as datazone
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DataZone construct libraries](https://constructs.dev/search?q=datazone)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DataZone resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DataZone.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DataZone](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DataZone.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

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
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnDataSource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource",
):
    '''The ``AWS::DataZone::DataSource`` resource specifies an Amazon DataZone data source that is used to import technical metadata of assets (data) from the source databases or data warehouses into Amazon DataZone.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html
    :cloudformationResource: AWS::DataZone::DataSource
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_data_source = datazone.CfnDataSource(self, "MyCfnDataSource",
            domain_identifier="domainIdentifier",
            environment_identifier="environmentIdentifier",
            name="name",
            project_identifier="projectIdentifier",
            type="type",
        
            # the properties below are optional
            asset_forms_input=[datazone.CfnDataSource.FormInputProperty(
                form_name="formName",
        
                # the properties below are optional
                content="content",
                type_identifier="typeIdentifier",
                type_revision="typeRevision"
            )],
            configuration=datazone.CfnDataSource.DataSourceConfigurationInputProperty(
                glue_run_configuration=datazone.CfnDataSource.GlueRunConfigurationInputProperty(
                    relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                        database_name="databaseName",
        
                        # the properties below are optional
                        filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                            expression="expression",
                            type="type"
                        )],
                        schema_name="schemaName"
                    )],
        
                    # the properties below are optional
                    auto_import_data_quality_result=False,
                    data_access_role="dataAccessRole"
                ),
                redshift_run_configuration=datazone.CfnDataSource.RedshiftRunConfigurationInputProperty(
                    redshift_credential_configuration=datazone.CfnDataSource.RedshiftCredentialConfigurationProperty(
                        secret_manager_arn="secretManagerArn"
                    ),
                    redshift_storage=datazone.CfnDataSource.RedshiftStorageProperty(
                        redshift_cluster_source=datazone.CfnDataSource.RedshiftClusterStorageProperty(
                            cluster_name="clusterName"
                        ),
                        redshift_serverless_source=datazone.CfnDataSource.RedshiftServerlessStorageProperty(
                            workgroup_name="workgroupName"
                        )
                    ),
                    relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                        database_name="databaseName",
        
                        # the properties below are optional
                        filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                            expression="expression",
                            type="type"
                        )],
                        schema_name="schemaName"
                    )],
        
                    # the properties below are optional
                    data_access_role="dataAccessRole"
                )
            ),
            description="description",
            enable_setting="enableSetting",
            publish_on_import=False,
            recommendation=datazone.CfnDataSource.RecommendationConfigurationProperty(
                enable_business_name_generation=False
            ),
            schedule=datazone.CfnDataSource.ScheduleConfigurationProperty(
                schedule="schedule",
                timezone="timezone"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_identifier: builtins.str,
        environment_identifier: builtins.str,
        name: builtins.str,
        project_identifier: builtins.str,
        type: builtins.str,
        asset_forms_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.FormInputProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.DataSourceConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_setting: typing.Optional[builtins.str] = None,
        publish_on_import: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        recommendation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RecommendationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.ScheduleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_identifier: The ID of the Amazon DataZone domain where the data source is created.
        :param environment_identifier: The unique identifier of the Amazon DataZone environment to which the data source publishes assets.
        :param name: The name of the data source.
        :param project_identifier: The identifier of the Amazon DataZone project in which you want to add this data source.
        :param type: The type of the data source.
        :param asset_forms_input: The metadata forms attached to the assets that the data source works with.
        :param configuration: The configuration of the data source.
        :param description: The description of the data source.
        :param enable_setting: Specifies whether the data source is enabled.
        :param publish_on_import: Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.
        :param recommendation: Specifies whether the business name generation is to be enabled for this data source.
        :param schedule: The schedule of the data source runs.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b74a6ac4c3e98c769e70eb9dc6e8b5f1e8f347a3615d992ea7f1c0d421505732)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataSourceProps(
            domain_identifier=domain_identifier,
            environment_identifier=environment_identifier,
            name=name,
            project_identifier=project_identifier,
            type=type,
            asset_forms_input=asset_forms_input,
            configuration=configuration,
            description=description,
            enable_setting=enable_setting,
            publish_on_import=publish_on_import,
            recommendation=recommendation,
            schedule=schedule,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33bcdad9dc3f66143343138916ff460345630898241997119efe034ff66c6a2d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__514e677208a85632dfb8a4fcf6a71bea051c78567845845ff000fb632aab7b5e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when the data source was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The ID of the Amazon DataZone domain in which the data source exists.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentId")
    def attr_environment_id(self) -> builtins.str:
        '''The ID of the environment in which the data source exists.

        :cloudformationAttribute: EnvironmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier of the data source run.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastRunAssetCount")
    def attr_last_run_asset_count(self) -> _IResolvable_da3f097b:
        '''The count of the assets created during the last data source run.

        :cloudformationAttribute: LastRunAssetCount
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLastRunAssetCount"))

    @builtins.property
    @jsii.member(jsii_name="attrLastRunAt")
    def attr_last_run_at(self) -> builtins.str:
        '''The timestamp of when the data source run was last performed.

        :cloudformationAttribute: LastRunAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastRunAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastRunStatus")
    def attr_last_run_status(self) -> builtins.str:
        '''The status of the last data source run.

        :cloudformationAttribute: LastRunStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastRunStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrProjectId")
    def attr_project_id(self) -> builtins.str:
        '''The project ID included in the data source run activity.

        :cloudformationAttribute: ProjectId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the data source.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp of when the data source was updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The ID of the Amazon DataZone domain where the data source is created.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a7af31e6c5b528548b0d530d4c772805fb61420d812ed44382c7c390086f11a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="environmentIdentifier")
    def environment_identifier(self) -> builtins.str:
        '''The unique identifier of the Amazon DataZone environment to which the data source publishes assets.'''
        return typing.cast(builtins.str, jsii.get(self, "environmentIdentifier"))

    @environment_identifier.setter
    def environment_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ed64595e5e156084952dfe11e1e064218cba6affcb8bf2736d3e0a177b08bea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the data source.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2821916d0fb71bfe9878d75d49136fb173b8984bb70e31a4a9720eebf6db3ab3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="projectIdentifier")
    def project_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone project in which you want to add this data source.'''
        return typing.cast(builtins.str, jsii.get(self, "projectIdentifier"))

    @project_identifier.setter
    def project_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__132e7e2cf26f81c0a6085283f4e8d4d9f57da8d3612dd55ee6749c192a2d2d48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the data source.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d073c13da920100b2d471eb086a45db9d741e4fba0dc8a0677ffe38913dffe2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="assetFormsInput")
    def asset_forms_input(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.FormInputProperty"]]]]:
        '''The metadata forms attached to the assets that the data source works with.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.FormInputProperty"]]]], jsii.get(self, "assetFormsInput"))

    @asset_forms_input.setter
    def asset_forms_input(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.FormInputProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd33f5216eca4a4d866e941b183a5ef445088a5e6ecec69e2fbc695f6b40c3c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetFormsInput", value)

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DataSourceConfigurationInputProperty"]]:
        '''The configuration of the data source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DataSourceConfigurationInputProperty"]], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DataSourceConfigurationInputProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89afb772730c8209e27316b8af14ef1a6fce9f26db9f31432460eff964f55b9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the data source.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7e5b5e600ceeed0171e7700fd1bb1de08837412c76a72396b54b2ddfcd29970)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enableSetting")
    def enable_setting(self) -> typing.Optional[builtins.str]:
        '''Specifies whether the data source is enabled.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enableSetting"))

    @enable_setting.setter
    def enable_setting(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c4b8af5e1647731587c5aaa0ac03d7e6980729c429135de819a778bb0e7a2eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSetting", value)

    @builtins.property
    @jsii.member(jsii_name="publishOnImport")
    def publish_on_import(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "publishOnImport"))

    @publish_on_import.setter
    def publish_on_import(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b8ce503c85a6ffdd243c0997e3ddab5dbbb39fc65cc2c74982964209c9e4eaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishOnImport", value)

    @builtins.property
    @jsii.member(jsii_name="recommendation")
    def recommendation(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RecommendationConfigurationProperty"]]:
        '''Specifies whether the business name generation is to be enabled for this data source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RecommendationConfigurationProperty"]], jsii.get(self, "recommendation"))

    @recommendation.setter
    def recommendation(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RecommendationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__213e25d07ce5c23cedc981ed540f97a1577533cd3dab4f6e0a08f166e38cfb49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recommendation", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.ScheduleConfigurationProperty"]]:
        '''The schedule of the data source runs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.ScheduleConfigurationProperty"]], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.ScheduleConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__693f7d02be84739f3d95375e94a3b4c964749b34e7dbf67ac0aa2b011ca3f625)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.DataSourceConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "glue_run_configuration": "glueRunConfiguration",
            "redshift_run_configuration": "redshiftRunConfiguration",
        },
    )
    class DataSourceConfigurationInputProperty:
        def __init__(
            self,
            *,
            glue_run_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.GlueRunConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            redshift_run_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RedshiftRunConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration of the data source.

            :param glue_run_configuration: The configuration of the AWS Glue data source.
            :param redshift_run_configuration: The configuration of the Amazon Redshift data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-datasourceconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                data_source_configuration_input_property = datazone.CfnDataSource.DataSourceConfigurationInputProperty(
                    glue_run_configuration=datazone.CfnDataSource.GlueRunConfigurationInputProperty(
                        relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                            database_name="databaseName",
                
                            # the properties below are optional
                            filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                                expression="expression",
                                type="type"
                            )],
                            schema_name="schemaName"
                        )],
                
                        # the properties below are optional
                        auto_import_data_quality_result=False,
                        data_access_role="dataAccessRole"
                    ),
                    redshift_run_configuration=datazone.CfnDataSource.RedshiftRunConfigurationInputProperty(
                        redshift_credential_configuration=datazone.CfnDataSource.RedshiftCredentialConfigurationProperty(
                            secret_manager_arn="secretManagerArn"
                        ),
                        redshift_storage=datazone.CfnDataSource.RedshiftStorageProperty(
                            redshift_cluster_source=datazone.CfnDataSource.RedshiftClusterStorageProperty(
                                cluster_name="clusterName"
                            ),
                            redshift_serverless_source=datazone.CfnDataSource.RedshiftServerlessStorageProperty(
                                workgroup_name="workgroupName"
                            )
                        ),
                        relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                            database_name="databaseName",
                
                            # the properties below are optional
                            filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                                expression="expression",
                                type="type"
                            )],
                            schema_name="schemaName"
                        )],
                
                        # the properties below are optional
                        data_access_role="dataAccessRole"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e9bda82e8d6905101b134276b283067e9b4fc8445ba4e98917ea7cd2937c5828)
                check_type(argname="argument glue_run_configuration", value=glue_run_configuration, expected_type=type_hints["glue_run_configuration"])
                check_type(argname="argument redshift_run_configuration", value=redshift_run_configuration, expected_type=type_hints["redshift_run_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if glue_run_configuration is not None:
                self._values["glue_run_configuration"] = glue_run_configuration
            if redshift_run_configuration is not None:
                self._values["redshift_run_configuration"] = redshift_run_configuration

        @builtins.property
        def glue_run_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.GlueRunConfigurationInputProperty"]]:
            '''The configuration of the AWS Glue data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-datasourceconfigurationinput.html#cfn-datazone-datasource-datasourceconfigurationinput-gluerunconfiguration
            '''
            result = self._values.get("glue_run_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.GlueRunConfigurationInputProperty"]], result)

        @builtins.property
        def redshift_run_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftRunConfigurationInputProperty"]]:
            '''The configuration of the Amazon Redshift data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-datasourceconfigurationinput.html#cfn-datazone-datasource-datasourceconfigurationinput-redshiftrunconfiguration
            '''
            result = self._values.get("redshift_run_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftRunConfigurationInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.FilterExpressionProperty",
        jsii_struct_bases=[],
        name_mapping={"expression": "expression", "type": "type"},
    )
    class FilterExpressionProperty:
        def __init__(self, *, expression: builtins.str, type: builtins.str) -> None:
            '''A filter expression in Amazon DataZone.

            :param expression: The search filter expression.
            :param type: The search filter explresison type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-filterexpression.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                filter_expression_property = datazone.CfnDataSource.FilterExpressionProperty(
                    expression="expression",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb2b40bf6229fe763c7c585fa978f99e3900fbd6916fc58d9065ddc99d90df18)
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "expression": expression,
                "type": type,
            }

        @builtins.property
        def expression(self) -> builtins.str:
            '''The search filter expression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-filterexpression.html#cfn-datazone-datasource-filterexpression-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The search filter explresison type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-filterexpression.html#cfn-datazone-datasource-filterexpression-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterExpressionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.FormInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "form_name": "formName",
            "content": "content",
            "type_identifier": "typeIdentifier",
            "type_revision": "typeRevision",
        },
    )
    class FormInputProperty:
        def __init__(
            self,
            *,
            form_name: builtins.str,
            content: typing.Optional[builtins.str] = None,
            type_identifier: typing.Optional[builtins.str] = None,
            type_revision: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details of a metadata form.

            :param form_name: The name of the metadata form.
            :param content: The content of the metadata form.
            :param type_identifier: The ID of the metadata form type.
            :param type_revision: The revision of the metadata form type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-forminput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                form_input_property = datazone.CfnDataSource.FormInputProperty(
                    form_name="formName",
                
                    # the properties below are optional
                    content="content",
                    type_identifier="typeIdentifier",
                    type_revision="typeRevision"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e39737bda51e6e9e0b04ce2c0598b00c495cf2dad8f53d4761c7a31ecf92227e)
                check_type(argname="argument form_name", value=form_name, expected_type=type_hints["form_name"])
                check_type(argname="argument content", value=content, expected_type=type_hints["content"])
                check_type(argname="argument type_identifier", value=type_identifier, expected_type=type_hints["type_identifier"])
                check_type(argname="argument type_revision", value=type_revision, expected_type=type_hints["type_revision"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "form_name": form_name,
            }
            if content is not None:
                self._values["content"] = content
            if type_identifier is not None:
                self._values["type_identifier"] = type_identifier
            if type_revision is not None:
                self._values["type_revision"] = type_revision

        @builtins.property
        def form_name(self) -> builtins.str:
            '''The name of the metadata form.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-forminput.html#cfn-datazone-datasource-forminput-formname
            '''
            result = self._values.get("form_name")
            assert result is not None, "Required property 'form_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def content(self) -> typing.Optional[builtins.str]:
            '''The content of the metadata form.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-forminput.html#cfn-datazone-datasource-forminput-content
            '''
            result = self._values.get("content")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type_identifier(self) -> typing.Optional[builtins.str]:
            '''The ID of the metadata form type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-forminput.html#cfn-datazone-datasource-forminput-typeidentifier
            '''
            result = self._values.get("type_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type_revision(self) -> typing.Optional[builtins.str]:
            '''The revision of the metadata form type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-forminput.html#cfn-datazone-datasource-forminput-typerevision
            '''
            result = self._values.get("type_revision")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FormInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.GlueRunConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "relational_filter_configurations": "relationalFilterConfigurations",
            "auto_import_data_quality_result": "autoImportDataQualityResult",
            "data_access_role": "dataAccessRole",
        },
    )
    class GlueRunConfigurationInputProperty:
        def __init__(
            self,
            *,
            relational_filter_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RelationalFilterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
            auto_import_data_quality_result: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            data_access_role: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration details of the AWS Glue data source.

            :param relational_filter_configurations: The relational filter configurations included in the configuration details of the AWS Glue data source.
            :param auto_import_data_quality_result: Specifies whether to automatically import data quality metrics as part of the data source run.
            :param data_access_role: The data access role included in the configuration details of the AWS Glue data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-gluerunconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                glue_run_configuration_input_property = datazone.CfnDataSource.GlueRunConfigurationInputProperty(
                    relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                        database_name="databaseName",
                
                        # the properties below are optional
                        filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                            expression="expression",
                            type="type"
                        )],
                        schema_name="schemaName"
                    )],
                
                    # the properties below are optional
                    auto_import_data_quality_result=False,
                    data_access_role="dataAccessRole"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ad6a5a243d0193849a3ba940cfbd956439268966f2ff08bff1fbcf5af20fe953)
                check_type(argname="argument relational_filter_configurations", value=relational_filter_configurations, expected_type=type_hints["relational_filter_configurations"])
                check_type(argname="argument auto_import_data_quality_result", value=auto_import_data_quality_result, expected_type=type_hints["auto_import_data_quality_result"])
                check_type(argname="argument data_access_role", value=data_access_role, expected_type=type_hints["data_access_role"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "relational_filter_configurations": relational_filter_configurations,
            }
            if auto_import_data_quality_result is not None:
                self._values["auto_import_data_quality_result"] = auto_import_data_quality_result
            if data_access_role is not None:
                self._values["data_access_role"] = data_access_role

        @builtins.property
        def relational_filter_configurations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RelationalFilterConfigurationProperty"]]]:
            '''The relational filter configurations included in the configuration details of the AWS Glue data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-gluerunconfigurationinput.html#cfn-datazone-datasource-gluerunconfigurationinput-relationalfilterconfigurations
            '''
            result = self._values.get("relational_filter_configurations")
            assert result is not None, "Required property 'relational_filter_configurations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RelationalFilterConfigurationProperty"]]], result)

        @builtins.property
        def auto_import_data_quality_result(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether to automatically import data quality metrics as part of the data source run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-gluerunconfigurationinput.html#cfn-datazone-datasource-gluerunconfigurationinput-autoimportdataqualityresult
            '''
            result = self._values.get("auto_import_data_quality_result")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def data_access_role(self) -> typing.Optional[builtins.str]:
            '''The data access role included in the configuration details of the AWS Glue data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-gluerunconfigurationinput.html#cfn-datazone-datasource-gluerunconfigurationinput-dataaccessrole
            '''
            result = self._values.get("data_access_role")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlueRunConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.RecommendationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_business_name_generation": "enableBusinessNameGeneration",
        },
    )
    class RecommendationConfigurationProperty:
        def __init__(
            self,
            *,
            enable_business_name_generation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The recommendation configuration for the data source.

            :param enable_business_name_generation: Specifies whether automatic business name generation is to be enabled or not as part of the recommendation configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-recommendationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                recommendation_configuration_property = datazone.CfnDataSource.RecommendationConfigurationProperty(
                    enable_business_name_generation=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b892cb470f7ea420aeb56956a5375b815b6b2a91d0e3d5aaa0a3461f5924b22)
                check_type(argname="argument enable_business_name_generation", value=enable_business_name_generation, expected_type=type_hints["enable_business_name_generation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable_business_name_generation is not None:
                self._values["enable_business_name_generation"] = enable_business_name_generation

        @builtins.property
        def enable_business_name_generation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether automatic business name generation is to be enabled or not as part of the recommendation configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-recommendationconfiguration.html#cfn-datazone-datasource-recommendationconfiguration-enablebusinessnamegeneration
            '''
            result = self._values.get("enable_business_name_generation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecommendationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.RedshiftClusterStorageProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_name": "clusterName"},
    )
    class RedshiftClusterStorageProperty:
        def __init__(self, *, cluster_name: builtins.str) -> None:
            '''The details of the Amazon Redshift cluster storage.

            :param cluster_name: The name of an Amazon Redshift cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftclusterstorage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                redshift_cluster_storage_property = datazone.CfnDataSource.RedshiftClusterStorageProperty(
                    cluster_name="clusterName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cf5e238c98cd0e25a8234c800e1db4699c482f8c18eb4b1a30bdf8afd3ca2718)
                check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cluster_name": cluster_name,
            }

        @builtins.property
        def cluster_name(self) -> builtins.str:
            '''The name of an Amazon Redshift cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftclusterstorage.html#cfn-datazone-datasource-redshiftclusterstorage-clustername
            '''
            result = self._values.get("cluster_name")
            assert result is not None, "Required property 'cluster_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftClusterStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.RedshiftCredentialConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"secret_manager_arn": "secretManagerArn"},
    )
    class RedshiftCredentialConfigurationProperty:
        def __init__(self, *, secret_manager_arn: builtins.str) -> None:
            '''The details of the credentials required to access an Amazon Redshift cluster.

            :param secret_manager_arn: The ARN of a secret manager for an Amazon Redshift cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftcredentialconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                redshift_credential_configuration_property = datazone.CfnDataSource.RedshiftCredentialConfigurationProperty(
                    secret_manager_arn="secretManagerArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1df8fcf30634f3b35250f98172cf307551610fbd637ef517691ae5581ccb5f66)
                check_type(argname="argument secret_manager_arn", value=secret_manager_arn, expected_type=type_hints["secret_manager_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "secret_manager_arn": secret_manager_arn,
            }

        @builtins.property
        def secret_manager_arn(self) -> builtins.str:
            '''The ARN of a secret manager for an Amazon Redshift cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftcredentialconfiguration.html#cfn-datazone-datasource-redshiftcredentialconfiguration-secretmanagerarn
            '''
            result = self._values.get("secret_manager_arn")
            assert result is not None, "Required property 'secret_manager_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftCredentialConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.RedshiftRunConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "redshift_credential_configuration": "redshiftCredentialConfiguration",
            "redshift_storage": "redshiftStorage",
            "relational_filter_configurations": "relationalFilterConfigurations",
            "data_access_role": "dataAccessRole",
        },
    )
    class RedshiftRunConfigurationInputProperty:
        def __init__(
            self,
            *,
            redshift_credential_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RedshiftCredentialConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            redshift_storage: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RedshiftStorageProperty", typing.Dict[builtins.str, typing.Any]]],
            relational_filter_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RelationalFilterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
            data_access_role: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The relational filter configurations included in the configuration details of the Amazon Redshift data source.

            :param redshift_credential_configuration: The details of the credentials required to access an Amazon Redshift cluster.
            :param redshift_storage: The details of the Amazon Redshift storage as part of the configuration of an Amazon Redshift data source run.
            :param relational_filter_configurations: The relational filter configurations included in the configuration details of the AWS Glue data source.
            :param data_access_role: The data access role included in the configuration details of the Amazon Redshift data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftrunconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                redshift_run_configuration_input_property = datazone.CfnDataSource.RedshiftRunConfigurationInputProperty(
                    redshift_credential_configuration=datazone.CfnDataSource.RedshiftCredentialConfigurationProperty(
                        secret_manager_arn="secretManagerArn"
                    ),
                    redshift_storage=datazone.CfnDataSource.RedshiftStorageProperty(
                        redshift_cluster_source=datazone.CfnDataSource.RedshiftClusterStorageProperty(
                            cluster_name="clusterName"
                        ),
                        redshift_serverless_source=datazone.CfnDataSource.RedshiftServerlessStorageProperty(
                            workgroup_name="workgroupName"
                        )
                    ),
                    relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                        database_name="databaseName",
                
                        # the properties below are optional
                        filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                            expression="expression",
                            type="type"
                        )],
                        schema_name="schemaName"
                    )],
                
                    # the properties below are optional
                    data_access_role="dataAccessRole"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5dd4c8b6216739fc8295ada55b58407d555982639c53118e9be94f72b8eb8e7c)
                check_type(argname="argument redshift_credential_configuration", value=redshift_credential_configuration, expected_type=type_hints["redshift_credential_configuration"])
                check_type(argname="argument redshift_storage", value=redshift_storage, expected_type=type_hints["redshift_storage"])
                check_type(argname="argument relational_filter_configurations", value=relational_filter_configurations, expected_type=type_hints["relational_filter_configurations"])
                check_type(argname="argument data_access_role", value=data_access_role, expected_type=type_hints["data_access_role"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "redshift_credential_configuration": redshift_credential_configuration,
                "redshift_storage": redshift_storage,
                "relational_filter_configurations": relational_filter_configurations,
            }
            if data_access_role is not None:
                self._values["data_access_role"] = data_access_role

        @builtins.property
        def redshift_credential_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftCredentialConfigurationProperty"]:
            '''The details of the credentials required to access an Amazon Redshift cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftrunconfigurationinput.html#cfn-datazone-datasource-redshiftrunconfigurationinput-redshiftcredentialconfiguration
            '''
            result = self._values.get("redshift_credential_configuration")
            assert result is not None, "Required property 'redshift_credential_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftCredentialConfigurationProperty"], result)

        @builtins.property
        def redshift_storage(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftStorageProperty"]:
            '''The details of the Amazon Redshift storage as part of the configuration of an Amazon Redshift data source run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftrunconfigurationinput.html#cfn-datazone-datasource-redshiftrunconfigurationinput-redshiftstorage
            '''
            result = self._values.get("redshift_storage")
            assert result is not None, "Required property 'redshift_storage' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftStorageProperty"], result)

        @builtins.property
        def relational_filter_configurations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RelationalFilterConfigurationProperty"]]]:
            '''The relational filter configurations included in the configuration details of the AWS Glue data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftrunconfigurationinput.html#cfn-datazone-datasource-redshiftrunconfigurationinput-relationalfilterconfigurations
            '''
            result = self._values.get("relational_filter_configurations")
            assert result is not None, "Required property 'relational_filter_configurations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RelationalFilterConfigurationProperty"]]], result)

        @builtins.property
        def data_access_role(self) -> typing.Optional[builtins.str]:
            '''The data access role included in the configuration details of the Amazon Redshift data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftrunconfigurationinput.html#cfn-datazone-datasource-redshiftrunconfigurationinput-dataaccessrole
            '''
            result = self._values.get("data_access_role")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftRunConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.RedshiftServerlessStorageProperty",
        jsii_struct_bases=[],
        name_mapping={"workgroup_name": "workgroupName"},
    )
    class RedshiftServerlessStorageProperty:
        def __init__(self, *, workgroup_name: builtins.str) -> None:
            '''The details of the Amazon Redshift Serverless workgroup storage.

            :param workgroup_name: The name of the Amazon Redshift Serverless workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftserverlessstorage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                redshift_serverless_storage_property = datazone.CfnDataSource.RedshiftServerlessStorageProperty(
                    workgroup_name="workgroupName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c58e081ae0c5b103243a5fb5e44d072e16021860d239dd719e8ecaa4696f2da8)
                check_type(argname="argument workgroup_name", value=workgroup_name, expected_type=type_hints["workgroup_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "workgroup_name": workgroup_name,
            }

        @builtins.property
        def workgroup_name(self) -> builtins.str:
            '''The name of the Amazon Redshift Serverless workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftserverlessstorage.html#cfn-datazone-datasource-redshiftserverlessstorage-workgroupname
            '''
            result = self._values.get("workgroup_name")
            assert result is not None, "Required property 'workgroup_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftServerlessStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.RedshiftStorageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "redshift_cluster_source": "redshiftClusterSource",
            "redshift_serverless_source": "redshiftServerlessSource",
        },
    )
    class RedshiftStorageProperty:
        def __init__(
            self,
            *,
            redshift_cluster_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RedshiftClusterStorageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            redshift_serverless_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.RedshiftServerlessStorageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The details of the Amazon Redshift storage as part of the configuration of an Amazon Redshift data source run.

            :param redshift_cluster_source: The details of the Amazon Redshift cluster source.
            :param redshift_serverless_source: The details of the Amazon Redshift Serverless workgroup source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftstorage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                redshift_storage_property = datazone.CfnDataSource.RedshiftStorageProperty(
                    redshift_cluster_source=datazone.CfnDataSource.RedshiftClusterStorageProperty(
                        cluster_name="clusterName"
                    ),
                    redshift_serverless_source=datazone.CfnDataSource.RedshiftServerlessStorageProperty(
                        workgroup_name="workgroupName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6959cf31dac7c5d3c9ee4d255059c5f6007a01d1da657810b6e3e44f31806173)
                check_type(argname="argument redshift_cluster_source", value=redshift_cluster_source, expected_type=type_hints["redshift_cluster_source"])
                check_type(argname="argument redshift_serverless_source", value=redshift_serverless_source, expected_type=type_hints["redshift_serverless_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if redshift_cluster_source is not None:
                self._values["redshift_cluster_source"] = redshift_cluster_source
            if redshift_serverless_source is not None:
                self._values["redshift_serverless_source"] = redshift_serverless_source

        @builtins.property
        def redshift_cluster_source(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftClusterStorageProperty"]]:
            '''The details of the Amazon Redshift cluster source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftstorage.html#cfn-datazone-datasource-redshiftstorage-redshiftclustersource
            '''
            result = self._values.get("redshift_cluster_source")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftClusterStorageProperty"]], result)

        @builtins.property
        def redshift_serverless_source(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftServerlessStorageProperty"]]:
            '''The details of the Amazon Redshift Serverless workgroup source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftstorage.html#cfn-datazone-datasource-redshiftstorage-redshiftserverlesssource
            '''
            result = self._values.get("redshift_serverless_source")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.RedshiftServerlessStorageProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.RelationalFilterConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_name": "databaseName",
            "filter_expressions": "filterExpressions",
            "schema_name": "schemaName",
        },
    )
    class RelationalFilterConfigurationProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            filter_expressions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.FilterExpressionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            schema_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The relational filter configuration for the data source.

            :param database_name: The database name specified in the relational filter configuration for the data source.
            :param filter_expressions: The filter expressions specified in the relational filter configuration for the data source.
            :param schema_name: The schema name specified in the relational filter configuration for the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-relationalfilterconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                relational_filter_configuration_property = datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                    database_name="databaseName",
                
                    # the properties below are optional
                    filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                        expression="expression",
                        type="type"
                    )],
                    schema_name="schemaName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b69950b3dd7224f1119f8c5e6a2c8675594377bc1e5845a101f3b5f210681258)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument filter_expressions", value=filter_expressions, expected_type=type_hints["filter_expressions"])
                check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database_name": database_name,
            }
            if filter_expressions is not None:
                self._values["filter_expressions"] = filter_expressions
            if schema_name is not None:
                self._values["schema_name"] = schema_name

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The database name specified in the relational filter configuration for the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-relationalfilterconfiguration.html#cfn-datazone-datasource-relationalfilterconfiguration-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def filter_expressions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.FilterExpressionProperty"]]]]:
            '''The filter expressions specified in the relational filter configuration for the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-relationalfilterconfiguration.html#cfn-datazone-datasource-relationalfilterconfiguration-filterexpressions
            '''
            result = self._values.get("filter_expressions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.FilterExpressionProperty"]]]], result)

        @builtins.property
        def schema_name(self) -> typing.Optional[builtins.str]:
            '''The schema name specified in the relational filter configuration for the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-relationalfilterconfiguration.html#cfn-datazone-datasource-relationalfilterconfiguration-schemaname
            '''
            result = self._values.get("schema_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RelationalFilterConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDataSource.ScheduleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"schedule": "schedule", "timezone": "timezone"},
    )
    class ScheduleConfigurationProperty:
        def __init__(
            self,
            *,
            schedule: typing.Optional[builtins.str] = None,
            timezone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details of the schedule of the data source runs.

            :param schedule: The schedule of the data source runs.
            :param timezone: The timezone of the data source run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-scheduleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                schedule_configuration_property = datazone.CfnDataSource.ScheduleConfigurationProperty(
                    schedule="schedule",
                    timezone="timezone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9fc1ad55dd2850c09e234b6cbea1fb383c32658a6b0f4b3e6c9ec1d67d8ae10c)
                check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
                check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if schedule is not None:
                self._values["schedule"] = schedule
            if timezone is not None:
                self._values["timezone"] = timezone

        @builtins.property
        def schedule(self) -> typing.Optional[builtins.str]:
            '''The schedule of the data source runs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-scheduleconfiguration.html#cfn-datazone-datasource-scheduleconfiguration-schedule
            '''
            result = self._values.get("schedule")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timezone(self) -> typing.Optional[builtins.str]:
            '''The timezone of the data source run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-scheduleconfiguration.html#cfn-datazone-datasource-scheduleconfiguration-timezone
            '''
            result = self._values.get("timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "environment_identifier": "environmentIdentifier",
        "name": "name",
        "project_identifier": "projectIdentifier",
        "type": "type",
        "asset_forms_input": "assetFormsInput",
        "configuration": "configuration",
        "description": "description",
        "enable_setting": "enableSetting",
        "publish_on_import": "publishOnImport",
        "recommendation": "recommendation",
        "schedule": "schedule",
    },
)
class CfnDataSourceProps:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        environment_identifier: builtins.str,
        name: builtins.str,
        project_identifier: builtins.str,
        type: builtins.str,
        asset_forms_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.FormInputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DataSourceConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        enable_setting: typing.Optional[builtins.str] = None,
        publish_on_import: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        recommendation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RecommendationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.ScheduleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataSource``.

        :param domain_identifier: The ID of the Amazon DataZone domain where the data source is created.
        :param environment_identifier: The unique identifier of the Amazon DataZone environment to which the data source publishes assets.
        :param name: The name of the data source.
        :param project_identifier: The identifier of the Amazon DataZone project in which you want to add this data source.
        :param type: The type of the data source.
        :param asset_forms_input: The metadata forms attached to the assets that the data source works with.
        :param configuration: The configuration of the data source.
        :param description: The description of the data source.
        :param enable_setting: Specifies whether the data source is enabled.
        :param publish_on_import: Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.
        :param recommendation: Specifies whether the business name generation is to be enabled for this data source.
        :param schedule: The schedule of the data source runs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_data_source_props = datazone.CfnDataSourceProps(
                domain_identifier="domainIdentifier",
                environment_identifier="environmentIdentifier",
                name="name",
                project_identifier="projectIdentifier",
                type="type",
            
                # the properties below are optional
                asset_forms_input=[datazone.CfnDataSource.FormInputProperty(
                    form_name="formName",
            
                    # the properties below are optional
                    content="content",
                    type_identifier="typeIdentifier",
                    type_revision="typeRevision"
                )],
                configuration=datazone.CfnDataSource.DataSourceConfigurationInputProperty(
                    glue_run_configuration=datazone.CfnDataSource.GlueRunConfigurationInputProperty(
                        relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                            database_name="databaseName",
            
                            # the properties below are optional
                            filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                                expression="expression",
                                type="type"
                            )],
                            schema_name="schemaName"
                        )],
            
                        # the properties below are optional
                        auto_import_data_quality_result=False,
                        data_access_role="dataAccessRole"
                    ),
                    redshift_run_configuration=datazone.CfnDataSource.RedshiftRunConfigurationInputProperty(
                        redshift_credential_configuration=datazone.CfnDataSource.RedshiftCredentialConfigurationProperty(
                            secret_manager_arn="secretManagerArn"
                        ),
                        redshift_storage=datazone.CfnDataSource.RedshiftStorageProperty(
                            redshift_cluster_source=datazone.CfnDataSource.RedshiftClusterStorageProperty(
                                cluster_name="clusterName"
                            ),
                            redshift_serverless_source=datazone.CfnDataSource.RedshiftServerlessStorageProperty(
                                workgroup_name="workgroupName"
                            )
                        ),
                        relational_filter_configurations=[datazone.CfnDataSource.RelationalFilterConfigurationProperty(
                            database_name="databaseName",
            
                            # the properties below are optional
                            filter_expressions=[datazone.CfnDataSource.FilterExpressionProperty(
                                expression="expression",
                                type="type"
                            )],
                            schema_name="schemaName"
                        )],
            
                        # the properties below are optional
                        data_access_role="dataAccessRole"
                    )
                ),
                description="description",
                enable_setting="enableSetting",
                publish_on_import=False,
                recommendation=datazone.CfnDataSource.RecommendationConfigurationProperty(
                    enable_business_name_generation=False
                ),
                schedule=datazone.CfnDataSource.ScheduleConfigurationProperty(
                    schedule="schedule",
                    timezone="timezone"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc5ec98207dd171531ba923ab77ceb4e9c095a2ac7eb083b5faef7393c183f86)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project_identifier", value=project_identifier, expected_type=type_hints["project_identifier"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument asset_forms_input", value=asset_forms_input, expected_type=type_hints["asset_forms_input"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enable_setting", value=enable_setting, expected_type=type_hints["enable_setting"])
            check_type(argname="argument publish_on_import", value=publish_on_import, expected_type=type_hints["publish_on_import"])
            check_type(argname="argument recommendation", value=recommendation, expected_type=type_hints["recommendation"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
            "name": name,
            "project_identifier": project_identifier,
            "type": type,
        }
        if asset_forms_input is not None:
            self._values["asset_forms_input"] = asset_forms_input
        if configuration is not None:
            self._values["configuration"] = configuration
        if description is not None:
            self._values["description"] = description
        if enable_setting is not None:
            self._values["enable_setting"] = enable_setting
        if publish_on_import is not None:
            self._values["publish_on_import"] = publish_on_import
        if recommendation is not None:
            self._values["recommendation"] = recommendation
        if schedule is not None:
            self._values["schedule"] = schedule

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The ID of the Amazon DataZone domain where the data source is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_identifier(self) -> builtins.str:
        '''The unique identifier of the Amazon DataZone environment to which the data source publishes assets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-environmentidentifier
        '''
        result = self._values.get("environment_identifier")
        assert result is not None, "Required property 'environment_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone project in which you want to add this data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-projectidentifier
        '''
        result = self._values.get("project_identifier")
        assert result is not None, "Required property 'project_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_forms_input(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataSource.FormInputProperty]]]]:
        '''The metadata forms attached to the assets that the data source works with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-assetformsinput
        '''
        result = self._values.get("asset_forms_input")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataSource.FormInputProperty]]]], result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DataSourceConfigurationInputProperty]]:
        '''The configuration of the data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-configuration
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DataSourceConfigurationInputProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_setting(self) -> typing.Optional[builtins.str]:
        '''Specifies whether the data source is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-enablesetting
        '''
        result = self._values.get("enable_setting")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publish_on_import(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-publishonimport
        '''
        result = self._values.get("publish_on_import")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def recommendation(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.RecommendationConfigurationProperty]]:
        '''Specifies whether the business name generation is to be enabled for this data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-recommendation
        '''
        result = self._values.get("recommendation")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.RecommendationConfigurationProperty]], result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.ScheduleConfigurationProperty]]:
        '''The schedule of the data source runs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html#cfn-datazone-datasource-schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.ScheduleConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnDomain(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnDomain",
):
    '''The ``AWS::DataZone::Domain`` resource specifies an Amazon DataZone domain.

    You can use domains to organize your assets, users, and their projects.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html
    :cloudformationResource: AWS::DataZone::Domain
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_domain = datazone.CfnDomain(self, "MyCfnDomain",
            domain_execution_role="domainExecutionRole",
            name="name",
        
            # the properties below are optional
            description="description",
            kms_key_identifier="kmsKeyIdentifier",
            single_sign_on=datazone.CfnDomain.SingleSignOnProperty(
                type="type",
                user_assignment="userAssignment"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_execution_role: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        single_sign_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.SingleSignOnProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_execution_role: The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the AWS account that houses the Amazon DataZone domain.
        :param name: The name of the Amazon DataZone domain.
        :param description: The description of the Amazon DataZone domain.
        :param kms_key_identifier: The identifier of the AWS Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.
        :param single_sign_on: The single sign-on details in Amazon DataZone.
        :param tags: The tags specified for the Amazon DataZone domain.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__047efef40bc572d080b2e64b8f32c1db40e40ba16fc7d29d887073e9c6b44c3f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainProps(
            domain_execution_role=domain_execution_role,
            name=name,
            description=description,
            kms_key_identifier=kms_key_identifier,
            single_sign_on=single_sign_on,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44ac286b6a265a7b8c549e9f75d607cdf3e71f300523940763c96adb368c15ac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__595689c850e768a74bf0e3147031e1acd033e20ab08856209edf9954aa010432)
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
        '''The ARN of the Amazon DataZone domain.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''A timestamp of when a Amazon DataZone domain was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the Amazon DataZone domain.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''A timestamp of when a Amazon DataZone domain was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrManagedAccountId")
    def attr_managed_account_id(self) -> builtins.str:
        '''The identifier of the AWS account that manages the domain.

        :cloudformationAttribute: ManagedAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrManagedAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrPortalUrl")
    def attr_portal_url(self) -> builtins.str:
        '''The data portal URL for the Amazon DataZone domain.

        :cloudformationAttribute: PortalUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPortalUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the Amazon DataZone domain.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainExecutionRole")
    def domain_execution_role(self) -> builtins.str:
        '''The domain execution role that is created when an Amazon DataZone domain is created.'''
        return typing.cast(builtins.str, jsii.get(self, "domainExecutionRole"))

    @domain_execution_role.setter
    def domain_execution_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f0f91db144dcd37dc91c4f005e5e179143c7d40165baf625ef7e284af70358e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainExecutionRole", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the Amazon DataZone domain.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb44fad9b00c8b94e0193e65a7d6e38fbf79595a0c367032211eb3ddcec54145)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the Amazon DataZone domain.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb0d62a189dbc4d1b327c1e7f651b95f580a2f6196abce203f4709bcca75c7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the AWS Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdentifier"))

    @kms_key_identifier.setter
    def kms_key_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49d22f79e701c8bd8ae540b270f397204f2285f1dc76ab7d1556d659a050f38b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="singleSignOn")
    def single_sign_on(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.SingleSignOnProperty"]]:
        '''The single sign-on details in Amazon DataZone.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.SingleSignOnProperty"]], jsii.get(self, "singleSignOn"))

    @single_sign_on.setter
    def single_sign_on(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.SingleSignOnProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee4595d765303396b66c3b59368637f839b950667fb4c707c509ac63e084f20b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singleSignOn", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags specified for the Amazon DataZone domain.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d899e2a4a220703956ab7f56e7c810107ec736f8c6281bedb3bc027e6ddb2ba4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnDomain.SingleSignOnProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "user_assignment": "userAssignment"},
    )
    class SingleSignOnProperty:
        def __init__(
            self,
            *,
            type: typing.Optional[builtins.str] = None,
            user_assignment: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The single sign-on details in Amazon DataZone.

            :param type: The type of single sign-on in Amazon DataZone.
            :param user_assignment: The single sign-on user assignment in Amazon DataZone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-domain-singlesignon.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                single_sign_on_property = datazone.CfnDomain.SingleSignOnProperty(
                    type="type",
                    user_assignment="userAssignment"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7f4cd03b79bceb07fb9f1366c739ee9cc49b8cbf6b9077a564689e81698df16)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument user_assignment", value=user_assignment, expected_type=type_hints["user_assignment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if type is not None:
                self._values["type"] = type
            if user_assignment is not None:
                self._values["user_assignment"] = user_assignment

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of single sign-on in Amazon DataZone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-domain-singlesignon.html#cfn-datazone-domain-singlesignon-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_assignment(self) -> typing.Optional[builtins.str]:
            '''The single sign-on user assignment in Amazon DataZone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-domain-singlesignon.html#cfn-datazone-domain-singlesignon-userassignment
            '''
            result = self._values.get("user_assignment")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SingleSignOnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnDomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_execution_role": "domainExecutionRole",
        "name": "name",
        "description": "description",
        "kms_key_identifier": "kmsKeyIdentifier",
        "single_sign_on": "singleSignOn",
        "tags": "tags",
    },
)
class CfnDomainProps:
    def __init__(
        self,
        *,
        domain_execution_role: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_identifier: typing.Optional[builtins.str] = None,
        single_sign_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SingleSignOnProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDomain``.

        :param domain_execution_role: The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the AWS account that houses the Amazon DataZone domain.
        :param name: The name of the Amazon DataZone domain.
        :param description: The description of the Amazon DataZone domain.
        :param kms_key_identifier: The identifier of the AWS Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.
        :param single_sign_on: The single sign-on details in Amazon DataZone.
        :param tags: The tags specified for the Amazon DataZone domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_domain_props = datazone.CfnDomainProps(
                domain_execution_role="domainExecutionRole",
                name="name",
            
                # the properties below are optional
                description="description",
                kms_key_identifier="kmsKeyIdentifier",
                single_sign_on=datazone.CfnDomain.SingleSignOnProperty(
                    type="type",
                    user_assignment="userAssignment"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d98e07f58a8aeb53fe8b36894639594f83be43ac8d182e1c384572cf0038d27)
            check_type(argname="argument domain_execution_role", value=domain_execution_role, expected_type=type_hints["domain_execution_role"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument kms_key_identifier", value=kms_key_identifier, expected_type=type_hints["kms_key_identifier"])
            check_type(argname="argument single_sign_on", value=single_sign_on, expected_type=type_hints["single_sign_on"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_execution_role": domain_execution_role,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if kms_key_identifier is not None:
            self._values["kms_key_identifier"] = kms_key_identifier
        if single_sign_on is not None:
            self._values["single_sign_on"] = single_sign_on
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def domain_execution_role(self) -> builtins.str:
        '''The domain execution role that is created when an Amazon DataZone domain is created.

        The domain execution role is created in the AWS account that houses the Amazon DataZone domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html#cfn-datazone-domain-domainexecutionrole
        '''
        result = self._values.get("domain_execution_role")
        assert result is not None, "Required property 'domain_execution_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the Amazon DataZone domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html#cfn-datazone-domain-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the Amazon DataZone domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html#cfn-datazone-domain-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the AWS Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html#cfn-datazone-domain-kmskeyidentifier
        '''
        result = self._values.get("kms_key_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_sign_on(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.SingleSignOnProperty]]:
        '''The single sign-on details in Amazon DataZone.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html#cfn-datazone-domain-singlesignon
        '''
        result = self._values.get("single_sign_on")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.SingleSignOnProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags specified for the Amazon DataZone domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html#cfn-datazone-domain-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEnvironment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironment",
):
    '''The ``AWS::DataZone::Environment`` resource specifies an Amazon DataZone environment, which is a collection of zero or more configured resources with a given set of IAM principals who can operate on those resources.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html
    :cloudformationResource: AWS::DataZone::Environment
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_environment = datazone.CfnEnvironment(self, "MyCfnEnvironment",
            domain_identifier="domainIdentifier",
            environment_profile_identifier="environmentProfileIdentifier",
            name="name",
            project_identifier="projectIdentifier",
        
            # the properties below are optional
            description="description",
            glossary_terms=["glossaryTerms"],
            user_parameters=[datazone.CfnEnvironment.EnvironmentParameterProperty(
                name="name",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_identifier: builtins.str,
        environment_profile_identifier: builtins.str,
        name: builtins.str,
        project_identifier: builtins.str,
        description: typing.Optional[builtins.str] = None,
        glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.EnvironmentParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_identifier: The identifier of the Amazon DataZone domain in which the environment is created.
        :param environment_profile_identifier: The identifier of the environment profile that is used to create this Amazon DataZone environment.
        :param name: The name of the Amazon DataZone environment.
        :param project_identifier: The identifier of the Amazon DataZone project in which this environment is created.
        :param description: The description of the environment.
        :param glossary_terms: The glossary terms that can be used in this Amazon DataZone environment.
        :param user_parameters: The user parameters of this Amazon DataZone environment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9dbab782927b08354bbafa4881abe3f775c9141395be836e6450777f8729b9b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentProps(
            domain_identifier=domain_identifier,
            environment_profile_identifier=environment_profile_identifier,
            name=name,
            project_identifier=project_identifier,
            description=description,
            glossary_terms=glossary_terms,
            user_parameters=user_parameters,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a28a39a0c7ba040029b6d28481def84a1131453e9259d7f220a8d8f9a9562fcf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7a663cc771f3c58655975db4a99b46784c16b0b96c4bb006217531f931854d1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAwsAccountId")
    def attr_aws_account_id(self) -> builtins.str:
        '''The identifier of the AWS account in which an environment exists.

        :cloudformationAttribute: AwsAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAwsAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrAwsAccountRegion")
    def attr_aws_account_region(self) -> builtins.str:
        '''The AWS Region in which an environment exists.

        :cloudformationAttribute: AwsAccountRegion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAwsAccountRegion"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when the environment was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> builtins.str:
        '''The Amazon DataZone user who created the environment.

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the environment exists.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentBlueprintId")
    def attr_environment_blueprint_id(self) -> builtins.str:
        '''The identifier of a blueprint with which an environment profile is created.

        :cloudformationAttribute: EnvironmentBlueprintId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentBlueprintId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentProfileId")
    def attr_environment_profile_id(self) -> builtins.str:
        '''The identifier of the environment profile with which the environment was created.

        :cloudformationAttribute: EnvironmentProfileId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentProfileId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier of the environment.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrProjectId")
    def attr_project_id(self) -> builtins.str:
        '''The identifier of the project in which the environment exists.

        :cloudformationAttribute: ProjectId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectId"))

    @builtins.property
    @jsii.member(jsii_name="attrProvider")
    def attr_provider(self) -> builtins.str:
        '''The provider of the environment.

        :cloudformationAttribute: Provider
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProvider"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the environment.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp of when the environment was updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the environment is created.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b36a4aa57667467b8bda95ca761a942a6f67e34e8549cd2dccc7a61d8399e9b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="environmentProfileIdentifier")
    def environment_profile_identifier(self) -> builtins.str:
        '''The identifier of the environment profile that is used to create this Amazon DataZone environment.'''
        return typing.cast(builtins.str, jsii.get(self, "environmentProfileIdentifier"))

    @environment_profile_identifier.setter
    def environment_profile_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__123d0e6b3ed252019ec79f09a380206e446d8155ba73fc8e7518fbd3dbac8c2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentProfileIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the Amazon DataZone environment.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4376356ce7178baaec6de65e59f567c3496e08605a27833ed8e83bfe0ff4be4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="projectIdentifier")
    def project_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone project in which this environment is created.'''
        return typing.cast(builtins.str, jsii.get(self, "projectIdentifier"))

    @project_identifier.setter
    def project_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baefbe7e97d72065b3b2c6be4e97a54bf9298376bb60dcac92eb7191397e306b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00e90ff4028654f7f45c97804aa061515407ac2ce2e55a21a1a4e4ff76fefd60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="glossaryTerms")
    def glossary_terms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The glossary terms that can be used in this Amazon DataZone environment.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "glossaryTerms"))

    @glossary_terms.setter
    def glossary_terms(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d52d21b9ab0852f8793f985e6f12ccea104ddc7e138f30b744d739af3c46b742)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "glossaryTerms", value)

    @builtins.property
    @jsii.member(jsii_name="userParameters")
    def user_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.EnvironmentParameterProperty"]]]]:
        '''The user parameters of this Amazon DataZone environment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.EnvironmentParameterProperty"]]]], jsii.get(self, "userParameters"))

    @user_parameters.setter
    def user_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.EnvironmentParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d345163e4f1ef89a409f470c896454213d0735fe6e5011e7ec6df4ead799556d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userParameters", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironment.EnvironmentParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class EnvironmentParameterProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The parameter details of the environment.

            :param name: The name of the environment parameter.
            :param value: The value of the environment parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environment-environmentparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                environment_parameter_property = datazone.CfnEnvironment.EnvironmentParameterProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d32a764f93482ecbfe18350874389b17ae96f3d5f78686bae5b55a2dcdfc012b)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the environment parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environment-environmentparameter.html#cfn-datazone-environment-environmentparameter-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the environment parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environment-environmentparameter.html#cfn-datazone-environment-environmentparameter-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnEnvironmentBlueprintConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentBlueprintConfiguration",
):
    '''The configuration details of an environment blueprint.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html
    :cloudformationResource: AWS::DataZone::EnvironmentBlueprintConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_environment_blueprint_configuration = datazone.CfnEnvironmentBlueprintConfiguration(self, "MyCfnEnvironmentBlueprintConfiguration",
            domain_identifier="domainIdentifier",
            enabled_regions=["enabledRegions"],
            environment_blueprint_identifier="environmentBlueprintIdentifier",
        
            # the properties below are optional
            manage_access_role_arn="manageAccessRoleArn",
            provisioning_role_arn="provisioningRoleArn",
            regional_parameters=[datazone.CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty(
                parameters={
                    "parameters_key": "parameters"
                },
                region="region"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_identifier: builtins.str,
        enabled_regions: typing.Sequence[builtins.str],
        environment_blueprint_identifier: builtins.str,
        manage_access_role_arn: typing.Optional[builtins.str] = None,
        provisioning_role_arn: typing.Optional[builtins.str] = None,
        regional_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_identifier: The identifier of the Amazon DataZone domain in which an environment blueprint exists.
        :param enabled_regions: The enabled AWS Regions specified in a blueprint configuration.
        :param environment_blueprint_identifier: The identifier of the environment blueprint. In the current release, only the following values are supported: ``DefaultDataLake`` and ``DefaultDataWarehouse`` .
        :param manage_access_role_arn: The ARN of the manage access role.
        :param provisioning_role_arn: The ARN of the provisioning role.
        :param regional_parameters: The regional parameters of the environment blueprint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48d8677ae22ff2da132402ace39f998c6b914f7464ce38abe9373fdbc550c445)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentBlueprintConfigurationProps(
            domain_identifier=domain_identifier,
            enabled_regions=enabled_regions,
            environment_blueprint_identifier=environment_blueprint_identifier,
            manage_access_role_arn=manage_access_role_arn,
            provisioning_role_arn=provisioning_role_arn,
            regional_parameters=regional_parameters,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeb5ba3f6738d175b0ca7714e77b6af191ccad2c9967480252920cb95dc6cb8f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__86364c1d7caa870da909a60996d646dde31c0e41cb594d0e952262cd925d5bdf)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when an environment blueprint was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which an environment blueprint exists.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentBlueprintId")
    def attr_environment_blueprint_id(self) -> builtins.str:
        '''The identifier of the environment blueprint.

        This identifier should be used when creating environment profiles.

        :cloudformationAttribute: EnvironmentBlueprintId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentBlueprintId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp of when the environment blueprint was updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which an environment blueprint exists.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e6a26e61dc0bca0a16da5100bf8f8cfcb05985dcd52fd83afd7818c62445836)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="enabledRegions")
    def enabled_regions(self) -> typing.List[builtins.str]:
        '''The enabled AWS Regions specified in a blueprint configuration.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enabledRegions"))

    @enabled_regions.setter
    def enabled_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9064df9af275b8a17afb82a8fc271f7b6e0ab19cdf01da41f144bac4832180e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledRegions", value)

    @builtins.property
    @jsii.member(jsii_name="environmentBlueprintIdentifier")
    def environment_blueprint_identifier(self) -> builtins.str:
        '''The identifier of the environment blueprint.'''
        return typing.cast(builtins.str, jsii.get(self, "environmentBlueprintIdentifier"))

    @environment_blueprint_identifier.setter
    def environment_blueprint_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db2bf9c4c7f25403fe2aa03be854b8b8b1f530f8d53a317f87b2fb9470d906a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentBlueprintIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="manageAccessRoleArn")
    def manage_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the manage access role.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "manageAccessRoleArn"))

    @manage_access_role_arn.setter
    def manage_access_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13a80be3403ea5113203d40c0843c4e4965600487d58b5f1e83bf1b8a9fc3d11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="provisioningRoleArn")
    def provisioning_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the provisioning role.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "provisioningRoleArn"))

    @provisioning_role_arn.setter
    def provisioning_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09c1e18144766c7e8d72f080dbe9de88dc085cfbdaa47a10b50cf7e235be8d65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioningRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="regionalParameters")
    def regional_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty"]]]]:
        '''The regional parameters of the environment blueprint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty"]]]], jsii.get(self, "regionalParameters"))

    @regional_parameters.setter
    def regional_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93fe5a214b768cb7201e2f47a6073bdec0303c4cda4d1d0b739b124ba7858574)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionalParameters", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"parameters": "parameters", "region": "region"},
    )
    class RegionalParameterProperty:
        def __init__(
            self,
            *,
            parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The regional parameters in the environment blueprint.

            :param parameters: A string to string map containing parameters for the region.
            :param region: The region specified in the environment parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentblueprintconfiguration-regionalparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                regional_parameter_property = datazone.CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty(
                    parameters={
                        "parameters_key": "parameters"
                    },
                    region="region"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__563b6d6aa110d6b77fcca8e42c3020852fa0c12036e1ba7f6ee62b2ce30826ff)
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if parameters is not None:
                self._values["parameters"] = parameters
            if region is not None:
                self._values["region"] = region

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''A string to string map containing parameters for the region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentblueprintconfiguration-regionalparameter.html#cfn-datazone-environmentblueprintconfiguration-regionalparameter-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''The region specified in the environment parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentblueprintconfiguration-regionalparameter.html#cfn-datazone-environmentblueprintconfiguration-regionalparameter-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegionalParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentBlueprintConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "enabled_regions": "enabledRegions",
        "environment_blueprint_identifier": "environmentBlueprintIdentifier",
        "manage_access_role_arn": "manageAccessRoleArn",
        "provisioning_role_arn": "provisioningRoleArn",
        "regional_parameters": "regionalParameters",
    },
)
class CfnEnvironmentBlueprintConfigurationProps:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        enabled_regions: typing.Sequence[builtins.str],
        environment_blueprint_identifier: builtins.str,
        manage_access_role_arn: typing.Optional[builtins.str] = None,
        provisioning_role_arn: typing.Optional[builtins.str] = None,
        regional_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironmentBlueprintConfiguration``.

        :param domain_identifier: The identifier of the Amazon DataZone domain in which an environment blueprint exists.
        :param enabled_regions: The enabled AWS Regions specified in a blueprint configuration.
        :param environment_blueprint_identifier: The identifier of the environment blueprint. In the current release, only the following values are supported: ``DefaultDataLake`` and ``DefaultDataWarehouse`` .
        :param manage_access_role_arn: The ARN of the manage access role.
        :param provisioning_role_arn: The ARN of the provisioning role.
        :param regional_parameters: The regional parameters of the environment blueprint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_environment_blueprint_configuration_props = datazone.CfnEnvironmentBlueprintConfigurationProps(
                domain_identifier="domainIdentifier",
                enabled_regions=["enabledRegions"],
                environment_blueprint_identifier="environmentBlueprintIdentifier",
            
                # the properties below are optional
                manage_access_role_arn="manageAccessRoleArn",
                provisioning_role_arn="provisioningRoleArn",
                regional_parameters=[datazone.CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty(
                    parameters={
                        "parameters_key": "parameters"
                    },
                    region="region"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca96f6fc24dc164f6fafb08d94645f48f6b4fc5c0a2ad8a3b95e170935e7353a)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument enabled_regions", value=enabled_regions, expected_type=type_hints["enabled_regions"])
            check_type(argname="argument environment_blueprint_identifier", value=environment_blueprint_identifier, expected_type=type_hints["environment_blueprint_identifier"])
            check_type(argname="argument manage_access_role_arn", value=manage_access_role_arn, expected_type=type_hints["manage_access_role_arn"])
            check_type(argname="argument provisioning_role_arn", value=provisioning_role_arn, expected_type=type_hints["provisioning_role_arn"])
            check_type(argname="argument regional_parameters", value=regional_parameters, expected_type=type_hints["regional_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "enabled_regions": enabled_regions,
            "environment_blueprint_identifier": environment_blueprint_identifier,
        }
        if manage_access_role_arn is not None:
            self._values["manage_access_role_arn"] = manage_access_role_arn
        if provisioning_role_arn is not None:
            self._values["provisioning_role_arn"] = provisioning_role_arn
        if regional_parameters is not None:
            self._values["regional_parameters"] = regional_parameters

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which an environment blueprint exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html#cfn-datazone-environmentblueprintconfiguration-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled_regions(self) -> typing.List[builtins.str]:
        '''The enabled AWS Regions specified in a blueprint configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html#cfn-datazone-environmentblueprintconfiguration-enabledregions
        '''
        result = self._values.get("enabled_regions")
        assert result is not None, "Required property 'enabled_regions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def environment_blueprint_identifier(self) -> builtins.str:
        '''The identifier of the environment blueprint.

        In the current release, only the following values are supported: ``DefaultDataLake`` and ``DefaultDataWarehouse`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html#cfn-datazone-environmentblueprintconfiguration-environmentblueprintidentifier
        '''
        result = self._values.get("environment_blueprint_identifier")
        assert result is not None, "Required property 'environment_blueprint_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def manage_access_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the manage access role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html#cfn-datazone-environmentblueprintconfiguration-manageaccessrolearn
        '''
        result = self._values.get("manage_access_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provisioning_role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the provisioning role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html#cfn-datazone-environmentblueprintconfiguration-provisioningrolearn
        '''
        result = self._values.get("provisioning_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regional_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty]]]]:
        '''The regional parameters of the environment blueprint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html#cfn-datazone-environmentblueprintconfiguration-regionalparameters
        '''
        result = self._values.get("regional_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentBlueprintConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEnvironmentProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentProfile",
):
    '''The details of an environment profile.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html
    :cloudformationResource: AWS::DataZone::EnvironmentProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_environment_profile = datazone.CfnEnvironmentProfile(self, "MyCfnEnvironmentProfile",
            aws_account_id="awsAccountId",
            aws_account_region="awsAccountRegion",
            domain_identifier="domainIdentifier",
            environment_blueprint_identifier="environmentBlueprintIdentifier",
            name="name",
            project_identifier="projectIdentifier",
        
            # the properties below are optional
            description="description",
            user_parameters=[datazone.CfnEnvironmentProfile.EnvironmentParameterProperty(
                name="name",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        aws_account_id: builtins.str,
        aws_account_region: builtins.str,
        domain_identifier: builtins.str,
        environment_blueprint_identifier: builtins.str,
        name: builtins.str,
        project_identifier: builtins.str,
        description: typing.Optional[builtins.str] = None,
        user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironmentProfile.EnvironmentParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param aws_account_id: The identifier of an AWS account in which an environment profile exists.
        :param aws_account_region: The AWS Region in which an environment profile exists.
        :param domain_identifier: The identifier of the Amazon DataZone domain in which the environment profile exists.
        :param environment_blueprint_identifier: The identifier of a blueprint with which an environment profile is created.
        :param name: The name of the environment profile.
        :param project_identifier: The identifier of a project in which an environment profile exists.
        :param description: The description of the environment profile.
        :param user_parameters: The user parameters of this Amazon DataZone environment profile.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a22dac59a328e3776825e07c2891d034e7e205eeeb00866d9086cf2f1dceb4f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentProfileProps(
            aws_account_id=aws_account_id,
            aws_account_region=aws_account_region,
            domain_identifier=domain_identifier,
            environment_blueprint_identifier=environment_blueprint_identifier,
            name=name,
            project_identifier=project_identifier,
            description=description,
            user_parameters=user_parameters,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b72ea9dd66a1ceac9aed426988a2df917e784879f21b1f6f0c19ca29b30b31b0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d250e5f9b10cd5d865865b560ea448ee7860153a35651b00d758f6634aba260)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when an environment profile was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> builtins.str:
        '''The Amazon DataZone user who created the environment profile.

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the environment profile exists.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentBlueprintId")
    def attr_environment_blueprint_id(self) -> builtins.str:
        '''The identifier of a blueprint with which an environment profile is created.

        :cloudformationAttribute: EnvironmentBlueprintId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentBlueprintId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier of the environment profile.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrProjectId")
    def attr_project_id(self) -> builtins.str:
        '''The identifier of a project in which an environment profile exists.

        :cloudformationAttribute: ProjectId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp of when the environment profile was updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> builtins.str:
        '''The identifier of an AWS account in which an environment profile exists.'''
        return typing.cast(builtins.str, jsii.get(self, "awsAccountId"))

    @aws_account_id.setter
    def aws_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de45320506b6ea6065d4e8de40a649bf205ae44ef01638670599709d45fde670)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="awsAccountRegion")
    def aws_account_region(self) -> builtins.str:
        '''The AWS Region in which an environment profile exists.'''
        return typing.cast(builtins.str, jsii.get(self, "awsAccountRegion"))

    @aws_account_region.setter
    def aws_account_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__929764ebd8bf0a538d63bf5bea864a4c6a1f1fa57874f35c72ee4cb0c977cdf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsAccountRegion", value)

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the environment profile exists.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9311c317e06fadb8c96c0e621239f5e4ce23903cdc1515f8f48973321817bc6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="environmentBlueprintIdentifier")
    def environment_blueprint_identifier(self) -> builtins.str:
        '''The identifier of a blueprint with which an environment profile is created.'''
        return typing.cast(builtins.str, jsii.get(self, "environmentBlueprintIdentifier"))

    @environment_blueprint_identifier.setter
    def environment_blueprint_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40d0761ec5bd844c4a1859c609961ac63da5ca2a42154f19f8cdf0482693545f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentBlueprintIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the environment profile.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__894c00430dd4f51ab95f6ed5db99418bdfe03c4cd5e70df92930998dc03b23e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="projectIdentifier")
    def project_identifier(self) -> builtins.str:
        '''The identifier of a project in which an environment profile exists.'''
        return typing.cast(builtins.str, jsii.get(self, "projectIdentifier"))

    @project_identifier.setter
    def project_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32f0a4cae84b8e4e478646d80c611ae0d63fbea35bd054197eaeb64b33b624c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__537f0658d3e004344b5e150e1c4182f64abe6101e2d21aaf1644347b19d27116)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="userParameters")
    def user_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentProfile.EnvironmentParameterProperty"]]]]:
        '''The user parameters of this Amazon DataZone environment profile.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentProfile.EnvironmentParameterProperty"]]]], jsii.get(self, "userParameters"))

    @user_parameters.setter
    def user_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironmentProfile.EnvironmentParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f091fadf5731901077c11ba7bce182eb007b6bd8b291bb6a4676fd3fa8e0e689)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userParameters", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentProfile.EnvironmentParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class EnvironmentParameterProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The parameter details of an environment profile.

            :param name: The name specified in the environment parameter.
            :param value: The value of the environment profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentprofile-environmentparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                environment_parameter_property = datazone.CfnEnvironmentProfile.EnvironmentParameterProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7d9a0947f6555aed5fe498e71fb0065f6dff69f004c35341f60523d1de281e5f)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name specified in the environment parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentprofile-environmentparameter.html#cfn-datazone-environmentprofile-environmentparameter-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the environment profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentprofile-environmentparameter.html#cfn-datazone-environmentprofile-environmentparameter-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "aws_account_region": "awsAccountRegion",
        "domain_identifier": "domainIdentifier",
        "environment_blueprint_identifier": "environmentBlueprintIdentifier",
        "name": "name",
        "project_identifier": "projectIdentifier",
        "description": "description",
        "user_parameters": "userParameters",
    },
)
class CfnEnvironmentProfileProps:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        aws_account_region: builtins.str,
        domain_identifier: builtins.str,
        environment_blueprint_identifier: builtins.str,
        name: builtins.str,
        project_identifier: builtins.str,
        description: typing.Optional[builtins.str] = None,
        user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentProfile.EnvironmentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironmentProfile``.

        :param aws_account_id: The identifier of an AWS account in which an environment profile exists.
        :param aws_account_region: The AWS Region in which an environment profile exists.
        :param domain_identifier: The identifier of the Amazon DataZone domain in which the environment profile exists.
        :param environment_blueprint_identifier: The identifier of a blueprint with which an environment profile is created.
        :param name: The name of the environment profile.
        :param project_identifier: The identifier of a project in which an environment profile exists.
        :param description: The description of the environment profile.
        :param user_parameters: The user parameters of this Amazon DataZone environment profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_environment_profile_props = datazone.CfnEnvironmentProfileProps(
                aws_account_id="awsAccountId",
                aws_account_region="awsAccountRegion",
                domain_identifier="domainIdentifier",
                environment_blueprint_identifier="environmentBlueprintIdentifier",
                name="name",
                project_identifier="projectIdentifier",
            
                # the properties below are optional
                description="description",
                user_parameters=[datazone.CfnEnvironmentProfile.EnvironmentParameterProperty(
                    name="name",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24d37d0c5f53a77c5e5be4ffa574af7dd3da85d8b5eb31bff30362d6c63ac36b)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument aws_account_region", value=aws_account_region, expected_type=type_hints["aws_account_region"])
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument environment_blueprint_identifier", value=environment_blueprint_identifier, expected_type=type_hints["environment_blueprint_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project_identifier", value=project_identifier, expected_type=type_hints["project_identifier"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument user_parameters", value=user_parameters, expected_type=type_hints["user_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "aws_account_region": aws_account_region,
            "domain_identifier": domain_identifier,
            "environment_blueprint_identifier": environment_blueprint_identifier,
            "name": name,
            "project_identifier": project_identifier,
        }
        if description is not None:
            self._values["description"] = description
        if user_parameters is not None:
            self._values["user_parameters"] = user_parameters

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The identifier of an AWS account in which an environment profile exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-awsaccountid
        '''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_region(self) -> builtins.str:
        '''The AWS Region in which an environment profile exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-awsaccountregion
        '''
        result = self._values.get("aws_account_region")
        assert result is not None, "Required property 'aws_account_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the environment profile exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_blueprint_identifier(self) -> builtins.str:
        '''The identifier of a blueprint with which an environment profile is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-environmentblueprintidentifier
        '''
        result = self._values.get("environment_blueprint_identifier")
        assert result is not None, "Required property 'environment_blueprint_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the environment profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_identifier(self) -> builtins.str:
        '''The identifier of a project in which an environment profile exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-projectidentifier
        '''
        result = self._values.get("project_identifier")
        assert result is not None, "Required property 'project_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentProfile.EnvironmentParameterProperty]]]]:
        '''The user parameters of this Amazon DataZone environment profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html#cfn-datazone-environmentprofile-userparameters
        '''
        result = self._values.get("user_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentProfile.EnvironmentParameterProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "environment_profile_identifier": "environmentProfileIdentifier",
        "name": "name",
        "project_identifier": "projectIdentifier",
        "description": "description",
        "glossary_terms": "glossaryTerms",
        "user_parameters": "userParameters",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        environment_profile_identifier: builtins.str,
        name: builtins.str,
        project_identifier: builtins.str,
        description: typing.Optional[builtins.str] = None,
        glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.EnvironmentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironment``.

        :param domain_identifier: The identifier of the Amazon DataZone domain in which the environment is created.
        :param environment_profile_identifier: The identifier of the environment profile that is used to create this Amazon DataZone environment.
        :param name: The name of the Amazon DataZone environment.
        :param project_identifier: The identifier of the Amazon DataZone project in which this environment is created.
        :param description: The description of the environment.
        :param glossary_terms: The glossary terms that can be used in this Amazon DataZone environment.
        :param user_parameters: The user parameters of this Amazon DataZone environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_environment_props = datazone.CfnEnvironmentProps(
                domain_identifier="domainIdentifier",
                environment_profile_identifier="environmentProfileIdentifier",
                name="name",
                project_identifier="projectIdentifier",
            
                # the properties below are optional
                description="description",
                glossary_terms=["glossaryTerms"],
                user_parameters=[datazone.CfnEnvironment.EnvironmentParameterProperty(
                    name="name",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52cb17aae6cf0b0cbeef010a71f7f53573517f0a8e973b5881ae34c1691d672b)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument environment_profile_identifier", value=environment_profile_identifier, expected_type=type_hints["environment_profile_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project_identifier", value=project_identifier, expected_type=type_hints["project_identifier"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument glossary_terms", value=glossary_terms, expected_type=type_hints["glossary_terms"])
            check_type(argname="argument user_parameters", value=user_parameters, expected_type=type_hints["user_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "environment_profile_identifier": environment_profile_identifier,
            "name": name,
            "project_identifier": project_identifier,
        }
        if description is not None:
            self._values["description"] = description
        if glossary_terms is not None:
            self._values["glossary_terms"] = glossary_terms
        if user_parameters is not None:
            self._values["user_parameters"] = user_parameters

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the environment is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_profile_identifier(self) -> builtins.str:
        '''The identifier of the environment profile that is used to create this Amazon DataZone environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-environmentprofileidentifier
        '''
        result = self._values.get("environment_profile_identifier")
        assert result is not None, "Required property 'environment_profile_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the Amazon DataZone environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone project in which this environment is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-projectidentifier
        '''
        result = self._values.get("project_identifier")
        assert result is not None, "Required property 'project_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def glossary_terms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The glossary terms that can be used in this Amazon DataZone environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-glossaryterms
        '''
        result = self._values.get("glossary_terms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def user_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.EnvironmentParameterProperty]]]]:
        '''The user parameters of this Amazon DataZone environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html#cfn-datazone-environment-userparameters
        '''
        result = self._values.get("user_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.EnvironmentParameterProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnGroupProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnGroupProfile",
):
    '''Group profiles represent groups of Amazon DataZone users.

    Groups can be manually created, or mapped to Active Directory groups of enterprise customers. In Amazon DataZone, groups serve two purposes. First, a group can map to a team of users in the organizational chart, and thus reduce the administrative work of a Amazon DataZone project owner when there are new employees joining or leaving a team. Second, corporate administrators use Active Directory groups to manage and update user statuses and so Amazon DataZone domain administrators can use these group memberships to implement Amazon DataZone domain policies.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-groupprofile.html
    :cloudformationResource: AWS::DataZone::GroupProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_group_profile = datazone.CfnGroupProfile(self, "MyCfnGroupProfile",
            domain_identifier="domainIdentifier",
            group_identifier="groupIdentifier",
        
            # the properties below are optional
            status="status"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_identifier: builtins.str,
        group_identifier: builtins.str,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_identifier: The identifier of the Amazon DataZone domain in which the group profile would be created.
        :param group_identifier: The ID of the group.
        :param status: The status of the group profile.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bccafb3ac5ccb0c73cc0aaea6cf365a78e841d8d731ffbfa84165d7f8100f7a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupProfileProps(
            domain_identifier=domain_identifier,
            group_identifier=group_identifier,
            status=status,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3064788268855f6623aaf3b52a7be17022b3d0c8d206428bb22e10d7bd9791de)
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
            type_hints = typing.get_type_hints(_typecheckingstub__66e617beac92ae83db2859cea30504a6e86d11714b8584d4212fe2f5634055e4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the group profile is created.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrGroupName")
    def attr_group_name(self) -> builtins.str:
        '''The group-name of the Group Profile.

        :cloudformationAttribute: GroupName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGroupName"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the Amazon DataZone group profile.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the group profile would be created.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bfce5f937e19aa12105a026759b48056e8cb9facac990d4a84ae9ebf754349a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="groupIdentifier")
    def group_identifier(self) -> builtins.str:
        '''The ID of the group.'''
        return typing.cast(builtins.str, jsii.get(self, "groupIdentifier"))

    @group_identifier.setter
    def group_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4cfe59401594c99ca6ed491e080ab3526afa6a5fbfa200d918455779f2c060f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the group profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__489105c9239ff5a560f37a1c161dc9de12874e97ca98bb0ac4df8139e29b6727)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnGroupProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "group_identifier": "groupIdentifier",
        "status": "status",
    },
)
class CfnGroupProfileProps:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        group_identifier: builtins.str,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnGroupProfile``.

        :param domain_identifier: The identifier of the Amazon DataZone domain in which the group profile would be created.
        :param group_identifier: The ID of the group.
        :param status: The status of the group profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-groupprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_group_profile_props = datazone.CfnGroupProfileProps(
                domain_identifier="domainIdentifier",
                group_identifier="groupIdentifier",
            
                # the properties below are optional
                status="status"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f4f2d05f4850cb07cd88e6e5af875d2c16fa3ae4bcbc384b9a51f7f0d0ca2e4)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument group_identifier", value=group_identifier, expected_type=type_hints["group_identifier"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "group_identifier": group_identifier,
        }
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the group profile would be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-groupprofile.html#cfn-datazone-groupprofile-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_identifier(self) -> builtins.str:
        '''The ID of the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-groupprofile.html#cfn-datazone-groupprofile-groupidentifier
        '''
        result = self._values.get("group_identifier")
        assert result is not None, "Required property 'group_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the group profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-groupprofile.html#cfn-datazone-groupprofile-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnProject(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnProject",
):
    '''The ``AWS::DataZone::Project`` resource specifies an Amazon DataZone project.

    Projects enable a group of users to collaborate on various business use cases that involve publishing, discovering, subscribing to, and consuming data in the Amazon DataZone catalog. Project members consume assets from the Amazon DataZone catalog and produce new assets using one or more analytical workflows.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html
    :cloudformationResource: AWS::DataZone::Project
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_project = datazone.CfnProject(self, "MyCfnProject",
            domain_identifier="domainIdentifier",
            name="name",
        
            # the properties below are optional
            description="description",
            glossary_terms=["glossaryTerms"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_identifier: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_identifier: The identifier of a Amazon DataZone domain where the project exists.
        :param name: The name of a project.
        :param description: The description of a project.
        :param glossary_terms: The glossary terms that can be used in this Amazon DataZone project.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dd190e348e5421f499a11e44b2fb0c69295587e5e7717b13a56786a897efe7f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectProps(
            domain_identifier=domain_identifier,
            name=name,
            description=description,
            glossary_terms=glossary_terms,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dec99f127bfd691b7b1ab5260c233568e5b335a316a646dd759686435ab2eb32)
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
            type_hints = typing.get_type_hints(_typecheckingstub__81361e533bde98a7e424eedf14591a679c836493433a44301b63cbf3357e5369)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when a project was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> builtins.str:
        '''The Amazon DataZone user who created the project.

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The identifier of a Amazon DataZone domain where the project exists.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier of a project.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The timestamp of when the project was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The identifier of a Amazon DataZone domain where the project exists.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c4440504b53716f23143b92e80a5ea3dcfaddd707d93cad9b77c33e5e19e7a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of a project.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7972d56cc7ec2cdd1800b8f0d6a79f7b4ad88633cf64a2e04f072fab6c9454b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of a project.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbb0277c9bfd29282afdae45a284966770345575b2854ec5cd9e6c04dffbac96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="glossaryTerms")
    def glossary_terms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The glossary terms that can be used in this Amazon DataZone project.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "glossaryTerms"))

    @glossary_terms.setter
    def glossary_terms(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed99a8f1a094dd4883e961330ac91acc714a4a5fd200b2d53a52d4113d5a34f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "glossaryTerms", value)


@jsii.implements(_IInspectable_c2943556)
class CfnProjectMembership(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnProjectMembership",
):
    '''Definition of AWS::DataZone::ProjectMembership Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectmembership.html
    :cloudformationResource: AWS::DataZone::ProjectMembership
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_project_membership = datazone.CfnProjectMembership(self, "MyCfnProjectMembership",
            designation="designation",
            domain_identifier="domainIdentifier",
            member=datazone.CfnProjectMembership.MemberProperty(
                group_identifier="groupIdentifier",
                user_identifier="userIdentifier"
            ),
            project_identifier="projectIdentifier"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        designation: builtins.str,
        domain_identifier: builtins.str,
        member: typing.Union[_IResolvable_da3f097b, typing.Union["CfnProjectMembership.MemberProperty", typing.Dict[builtins.str, typing.Any]]],
        project_identifier: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param designation: 
        :param domain_identifier: 
        :param member: 
        :param project_identifier: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__227cc3d5649ee98fd5579f9e1870652d6de5250e0390e91fec524565dc07c0b9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectMembershipProps(
            designation=designation,
            domain_identifier=domain_identifier,
            member=member,
            project_identifier=project_identifier,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e6a7791d79b9b8f15baba0f04bddbfa77afbfbdd8d2872a6e46acd2ccee79c4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e37a11438611477027ae5dde4a091dc361c7dc56ba7538221e222ef9083be907)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="designation")
    def designation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "designation"))

    @designation.setter
    def designation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71ec417c1a2abac8b6037b5bfedeb8520a3be4a0844d46c1862cb259465e45f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "designation", value)

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66d809e4462dc85243bcc1ab3799cc4a5180f2f4119683718081fa5f79530ac7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="member")
    def member(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnProjectMembership.MemberProperty"]:
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnProjectMembership.MemberProperty"], jsii.get(self, "member"))

    @member.setter
    def member(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnProjectMembership.MemberProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50f6e6b64e6349a5c9d740955a9ccac88cf9da161bf02038bc9e12572958a93f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "member", value)

    @builtins.property
    @jsii.member(jsii_name="projectIdentifier")
    def project_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectIdentifier"))

    @project_identifier.setter
    def project_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da845d5c47de18f48a6a2e21aa5b41e5193d4b3faad962602fc4d3b98d677eb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectIdentifier", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnProjectMembership.MemberProperty",
        jsii_struct_bases=[],
        name_mapping={
            "group_identifier": "groupIdentifier",
            "user_identifier": "userIdentifier",
        },
    )
    class MemberProperty:
        def __init__(
            self,
            *,
            group_identifier: typing.Optional[builtins.str] = None,
            user_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param group_identifier: 
            :param user_identifier: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectmembership-member.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                member_property = datazone.CfnProjectMembership.MemberProperty(
                    group_identifier="groupIdentifier",
                    user_identifier="userIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2184a0c3aa18e8899e2cb70b944b79d781e689bd543ac2140e9176025c2fa864)
                check_type(argname="argument group_identifier", value=group_identifier, expected_type=type_hints["group_identifier"])
                check_type(argname="argument user_identifier", value=user_identifier, expected_type=type_hints["user_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if group_identifier is not None:
                self._values["group_identifier"] = group_identifier
            if user_identifier is not None:
                self._values["user_identifier"] = user_identifier

        @builtins.property
        def group_identifier(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectmembership-member.html#cfn-datazone-projectmembership-member-groupidentifier
            '''
            result = self._values.get("group_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_identifier(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-projectmembership-member.html#cfn-datazone-projectmembership-member-useridentifier
            '''
            result = self._values.get("user_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemberProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnProjectMembershipProps",
    jsii_struct_bases=[],
    name_mapping={
        "designation": "designation",
        "domain_identifier": "domainIdentifier",
        "member": "member",
        "project_identifier": "projectIdentifier",
    },
)
class CfnProjectMembershipProps:
    def __init__(
        self,
        *,
        designation: builtins.str,
        domain_identifier: builtins.str,
        member: typing.Union[_IResolvable_da3f097b, typing.Union[CfnProjectMembership.MemberProperty, typing.Dict[builtins.str, typing.Any]]],
        project_identifier: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnProjectMembership``.

        :param designation: 
        :param domain_identifier: 
        :param member: 
        :param project_identifier: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectmembership.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_project_membership_props = datazone.CfnProjectMembershipProps(
                designation="designation",
                domain_identifier="domainIdentifier",
                member=datazone.CfnProjectMembership.MemberProperty(
                    group_identifier="groupIdentifier",
                    user_identifier="userIdentifier"
                ),
                project_identifier="projectIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b25f4db16efa2b368a4cf197bdf102ccdf0c613db5654c1186f9404f9259e4d7)
            check_type(argname="argument designation", value=designation, expected_type=type_hints["designation"])
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument member", value=member, expected_type=type_hints["member"])
            check_type(argname="argument project_identifier", value=project_identifier, expected_type=type_hints["project_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "designation": designation,
            "domain_identifier": domain_identifier,
            "member": member,
            "project_identifier": project_identifier,
        }

    @builtins.property
    def designation(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectmembership.html#cfn-datazone-projectmembership-designation
        '''
        result = self._values.get("designation")
        assert result is not None, "Required property 'designation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectmembership.html#cfn-datazone-projectmembership-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnProjectMembership.MemberProperty]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectmembership.html#cfn-datazone-projectmembership-member
        '''
        result = self._values.get("member")
        assert result is not None, "Required property 'member' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnProjectMembership.MemberProperty], result)

    @builtins.property
    def project_identifier(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-projectmembership.html#cfn-datazone-projectmembership-projectidentifier
        '''
        result = self._values.get("project_identifier")
        assert result is not None, "Required property 'project_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectMembershipProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "name": "name",
        "description": "description",
        "glossary_terms": "glossaryTerms",
    },
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProject``.

        :param domain_identifier: The identifier of a Amazon DataZone domain where the project exists.
        :param name: The name of a project.
        :param description: The description of a project.
        :param glossary_terms: The glossary terms that can be used in this Amazon DataZone project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_project_props = datazone.CfnProjectProps(
                domain_identifier="domainIdentifier",
                name="name",
            
                # the properties below are optional
                description="description",
                glossary_terms=["glossaryTerms"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d519699f8d5d172880216006cab9e8c1595fc99339cf485d2be1f6c37bbc5a4c)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument glossary_terms", value=glossary_terms, expected_type=type_hints["glossary_terms"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if glossary_terms is not None:
            self._values["glossary_terms"] = glossary_terms

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The identifier of a Amazon DataZone domain where the project exists.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html#cfn-datazone-project-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of a project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html#cfn-datazone-project-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of a project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html#cfn-datazone-project-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def glossary_terms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The glossary terms that can be used in this Amazon DataZone project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html#cfn-datazone-project-glossaryterms
        '''
        result = self._values.get("glossary_terms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSubscriptionTarget(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnSubscriptionTarget",
):
    '''The ``AWS::DataZone::SubscriptionTarget`` resource specifies an Amazon DataZone subscription target.

    Subscription targets enable you to access the data to which you have subscribed in your projects. A subscription target specifies the location (for example, a database or a schema) and the required permissions (for example, an IAM role) that Amazon DataZone can use to establish a connection with the source data and to create the necessary grants so that members of the Amazon DataZone project can start querying the data to which they have subscribed.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html
    :cloudformationResource: AWS::DataZone::SubscriptionTarget
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_subscription_target = datazone.CfnSubscriptionTarget(self, "MyCfnSubscriptionTarget",
            applicable_asset_types=["applicableAssetTypes"],
            authorized_principals=["authorizedPrincipals"],
            domain_identifier="domainIdentifier",
            environment_identifier="environmentIdentifier",
            manage_access_role="manageAccessRole",
            name="name",
            subscription_target_config=[datazone.CfnSubscriptionTarget.SubscriptionTargetFormProperty(
                content="content",
                form_name="formName"
            )],
            type="type",
        
            # the properties below are optional
            provider="provider"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        applicable_asset_types: typing.Sequence[builtins.str],
        authorized_principals: typing.Sequence[builtins.str],
        domain_identifier: builtins.str,
        environment_identifier: builtins.str,
        manage_access_role: builtins.str,
        name: builtins.str,
        subscription_target_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSubscriptionTarget.SubscriptionTargetFormProperty", typing.Dict[builtins.str, typing.Any]]]]],
        type: builtins.str,
        provider: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param applicable_asset_types: The asset types included in the subscription target.
        :param authorized_principals: The authorized principals included in the subscription target.
        :param domain_identifier: The ID of the Amazon DataZone domain in which subscription target is created.
        :param environment_identifier: The ID of the environment in which subscription target is created.
        :param manage_access_role: The manage access role that is used to create the subscription target.
        :param name: The name of the subscription target.
        :param subscription_target_config: The configuration of the subscription target.
        :param type: The type of the subscription target.
        :param provider: The provider of the subscription target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c61b5cfe149791a4c62bad0056737a365bdf72f7f99e6e72c71be1058e91604d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSubscriptionTargetProps(
            applicable_asset_types=applicable_asset_types,
            authorized_principals=authorized_principals,
            domain_identifier=domain_identifier,
            environment_identifier=environment_identifier,
            manage_access_role=manage_access_role,
            name=name,
            subscription_target_config=subscription_target_config,
            type=type,
            provider=provider,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1ffb846a6baf7f8d43c947f31440c264738eb11477a914e6234e72e512226a7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__867dc79750bd91424b54ba2d5f7eca4a8d13f7f3c9f4ffc4effe5dae834ed869)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp of when the subscription target was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> builtins.str:
        '''The Amazon DataZone user who created the subscription target.

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the subscription target exists.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentId")
    def attr_environment_id(self) -> builtins.str:
        '''The identifier of the environment of the subscription target.

        :cloudformationAttribute: EnvironmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier of the subscription target.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrProjectId")
    def attr_project_id(self) -> builtins.str:
        '''The identifier of the project specified in the subscription target.

        :cloudformationAttribute: ProjectId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp of when the subscription target was updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedBy")
    def attr_updated_by(self) -> builtins.str:
        '''The Amazon DataZone user who updated the subscription target.

        :cloudformationAttribute: UpdatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedBy"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="applicableAssetTypes")
    def applicable_asset_types(self) -> typing.List[builtins.str]:
        '''The asset types included in the subscription target.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "applicableAssetTypes"))

    @applicable_asset_types.setter
    def applicable_asset_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6db9fad0cfe2726fd2714cfa52499e265af46d2cacf4be9daa6378bd8c673b5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicableAssetTypes", value)

    @builtins.property
    @jsii.member(jsii_name="authorizedPrincipals")
    def authorized_principals(self) -> typing.List[builtins.str]:
        '''The authorized principals included in the subscription target.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "authorizedPrincipals"))

    @authorized_principals.setter
    def authorized_principals(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ec38d6c0d885e0ae64427a2407f691f11cd764f198652ece23783772c2611fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizedPrincipals", value)

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The ID of the Amazon DataZone domain in which subscription target is created.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77bccb41f1eb7b5a32710e03ae6cfec74eb17bf3129bd372a11c92f7f67f5dc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="environmentIdentifier")
    def environment_identifier(self) -> builtins.str:
        '''The ID of the environment in which subscription target is created.'''
        return typing.cast(builtins.str, jsii.get(self, "environmentIdentifier"))

    @environment_identifier.setter
    def environment_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20ed34c3b416019570831200db233eb4c407b91b53464c36e9fbdbdcd4a6da82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="manageAccessRole")
    def manage_access_role(self) -> builtins.str:
        '''The manage access role that is used to create the subscription target.'''
        return typing.cast(builtins.str, jsii.get(self, "manageAccessRole"))

    @manage_access_role.setter
    def manage_access_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83f19af57790aab3ddc6c4e1f64e1f68cf69073e46da8ac997fc9f0c83e93198)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageAccessRole", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the subscription target.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc691c403b67912db7216c5f5fddda4101316ca719bd90e37c92640197c61004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionTargetConfig")
    def subscription_target_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSubscriptionTarget.SubscriptionTargetFormProperty"]]]:
        '''The configuration of the subscription target.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSubscriptionTarget.SubscriptionTargetFormProperty"]]], jsii.get(self, "subscriptionTargetConfig"))

    @subscription_target_config.setter
    def subscription_target_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSubscriptionTarget.SubscriptionTargetFormProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a19c0f2213973750a6cc503429c6ef8619a3d0885a2df0f54aad48a00a3c6f46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionTargetConfig", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the subscription target.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8961cb77429dad851472db6b14a76c77606d0bffdc98a0cbb3cffd227c3ec500)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="provider")
    def provider(self) -> typing.Optional[builtins.str]:
        '''The provider of the subscription target.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "provider"))

    @provider.setter
    def provider(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4526f8f71696c8c7bf040cd042cda55182de538f2ebf276253751b5a497c037)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provider", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnSubscriptionTarget.SubscriptionTargetFormProperty",
        jsii_struct_bases=[],
        name_mapping={"content": "content", "form_name": "formName"},
    )
    class SubscriptionTargetFormProperty:
        def __init__(self, *, content: builtins.str, form_name: builtins.str) -> None:
            '''The details of the subscription target configuration.

            :param content: The content of the subscription target configuration.
            :param form_name: The form name included in the subscription target configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-subscriptiontarget-subscriptiontargetform.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                subscription_target_form_property = datazone.CfnSubscriptionTarget.SubscriptionTargetFormProperty(
                    content="content",
                    form_name="formName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__720cbd7aa436c84d94877993fe56ec1a54389edd9936074e71ebf65a3caffa9b)
                check_type(argname="argument content", value=content, expected_type=type_hints["content"])
                check_type(argname="argument form_name", value=form_name, expected_type=type_hints["form_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "content": content,
                "form_name": form_name,
            }

        @builtins.property
        def content(self) -> builtins.str:
            '''The content of the subscription target configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-subscriptiontarget-subscriptiontargetform.html#cfn-datazone-subscriptiontarget-subscriptiontargetform-content
            '''
            result = self._values.get("content")
            assert result is not None, "Required property 'content' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def form_name(self) -> builtins.str:
            '''The form name included in the subscription target configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-subscriptiontarget-subscriptiontargetform.html#cfn-datazone-subscriptiontarget-subscriptiontargetform-formname
            '''
            result = self._values.get("form_name")
            assert result is not None, "Required property 'form_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubscriptionTargetFormProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnSubscriptionTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "applicable_asset_types": "applicableAssetTypes",
        "authorized_principals": "authorizedPrincipals",
        "domain_identifier": "domainIdentifier",
        "environment_identifier": "environmentIdentifier",
        "manage_access_role": "manageAccessRole",
        "name": "name",
        "subscription_target_config": "subscriptionTargetConfig",
        "type": "type",
        "provider": "provider",
    },
)
class CfnSubscriptionTargetProps:
    def __init__(
        self,
        *,
        applicable_asset_types: typing.Sequence[builtins.str],
        authorized_principals: typing.Sequence[builtins.str],
        domain_identifier: builtins.str,
        environment_identifier: builtins.str,
        manage_access_role: builtins.str,
        name: builtins.str,
        subscription_target_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriptionTarget.SubscriptionTargetFormProperty, typing.Dict[builtins.str, typing.Any]]]]],
        type: builtins.str,
        provider: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSubscriptionTarget``.

        :param applicable_asset_types: The asset types included in the subscription target.
        :param authorized_principals: The authorized principals included in the subscription target.
        :param domain_identifier: The ID of the Amazon DataZone domain in which subscription target is created.
        :param environment_identifier: The ID of the environment in which subscription target is created.
        :param manage_access_role: The manage access role that is used to create the subscription target.
        :param name: The name of the subscription target.
        :param subscription_target_config: The configuration of the subscription target.
        :param type: The type of the subscription target.
        :param provider: The provider of the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_subscription_target_props = datazone.CfnSubscriptionTargetProps(
                applicable_asset_types=["applicableAssetTypes"],
                authorized_principals=["authorizedPrincipals"],
                domain_identifier="domainIdentifier",
                environment_identifier="environmentIdentifier",
                manage_access_role="manageAccessRole",
                name="name",
                subscription_target_config=[datazone.CfnSubscriptionTarget.SubscriptionTargetFormProperty(
                    content="content",
                    form_name="formName"
                )],
                type="type",
            
                # the properties below are optional
                provider="provider"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b970b38bc2b99a7ed3ef3830dfa5721ecc9ee442e5d627e01abfdcb22600151)
            check_type(argname="argument applicable_asset_types", value=applicable_asset_types, expected_type=type_hints["applicable_asset_types"])
            check_type(argname="argument authorized_principals", value=authorized_principals, expected_type=type_hints["authorized_principals"])
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
            check_type(argname="argument manage_access_role", value=manage_access_role, expected_type=type_hints["manage_access_role"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument subscription_target_config", value=subscription_target_config, expected_type=type_hints["subscription_target_config"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "applicable_asset_types": applicable_asset_types,
            "authorized_principals": authorized_principals,
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
            "manage_access_role": manage_access_role,
            "name": name,
            "subscription_target_config": subscription_target_config,
            "type": type,
        }
        if provider is not None:
            self._values["provider"] = provider

    @builtins.property
    def applicable_asset_types(self) -> typing.List[builtins.str]:
        '''The asset types included in the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-applicableassettypes
        '''
        result = self._values.get("applicable_asset_types")
        assert result is not None, "Required property 'applicable_asset_types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def authorized_principals(self) -> typing.List[builtins.str]:
        '''The authorized principals included in the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-authorizedprincipals
        '''
        result = self._values.get("authorized_principals")
        assert result is not None, "Required property 'authorized_principals' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The ID of the Amazon DataZone domain in which subscription target is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_identifier(self) -> builtins.str:
        '''The ID of the environment in which subscription target is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-environmentidentifier
        '''
        result = self._values.get("environment_identifier")
        assert result is not None, "Required property 'environment_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def manage_access_role(self) -> builtins.str:
        '''The manage access role that is used to create the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-manageaccessrole
        '''
        result = self._values.get("manage_access_role")
        assert result is not None, "Required property 'manage_access_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscription_target_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSubscriptionTarget.SubscriptionTargetFormProperty]]]:
        '''The configuration of the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-subscriptiontargetconfig
        '''
        result = self._values.get("subscription_target_config")
        assert result is not None, "Required property 'subscription_target_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSubscriptionTarget.SubscriptionTargetFormProperty]]], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def provider(self) -> typing.Optional[builtins.str]:
        '''The provider of the subscription target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html#cfn-datazone-subscriptiontarget-provider
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSubscriptionTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnUserProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_datazone.CfnUserProfile",
):
    '''A user profile represents Amazon DataZone users.

    Amazon DataZone supports both IAM roles and SSO identities to interact with the Amazon DataZone Management Console and the data portal for different purposes. Domain administrators use IAM roles to perform the initial administrative domain-related work in the Amazon DataZone Management Console, including creating new Amazon DataZone domains, configuring metadata form types, and implementing policies. Data workers use their SSO corporate identities via Identity Center to log into the Amazon DataZone Data Portal and access projects where they have memberships.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-userprofile.html
    :cloudformationResource: AWS::DataZone::UserProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_datazone as datazone
        
        cfn_user_profile = datazone.CfnUserProfile(self, "MyCfnUserProfile",
            domain_identifier="domainIdentifier",
            user_identifier="userIdentifier",
        
            # the properties below are optional
            status="status",
            user_type="userType"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_identifier: builtins.str,
        user_identifier: builtins.str,
        status: typing.Optional[builtins.str] = None,
        user_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_identifier: The identifier of the Amazon DataZone domain in which the user profile would be created.
        :param user_identifier: The ID of the user.
        :param status: The status of the user profile.
        :param user_type: The type of the user.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43948fd61004932aa31394de53e9c49e34aa425f3682404de5d5f6a249734d82)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserProfileProps(
            domain_identifier=domain_identifier,
            user_identifier=user_identifier,
            status=status,
            user_type=user_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62409db933bd1f83a26e4a296f90a5aa33de9e2cd9f82db4084d8f1cb0f382e4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bac3d345ed2cf85373ed12e71655921f20ce2575e0f95a05a3dd29cfa7e804e0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDetails")
    def attr_details(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Details
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrDetails"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the user profile is created.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the Amazon DataZone user profile.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''The type of the user profile.

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainIdentifier")
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the user profile would be created.'''
        return typing.cast(builtins.str, jsii.get(self, "domainIdentifier"))

    @domain_identifier.setter
    def domain_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57dc87f9b5d4209a76a54e631bab548eddbecf73d3a0cb39b30030a99c20dbb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="userIdentifier")
    def user_identifier(self) -> builtins.str:
        '''The ID of the user.'''
        return typing.cast(builtins.str, jsii.get(self, "userIdentifier"))

    @user_identifier.setter
    def user_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bc695cbd1d290ebde7514044903060b533b99cd4f724f387512ffb614625693)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the user profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f391a63fdbc6b7a8aefbb3664fddfe91481bce941965f274ecad0166152935ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="userType")
    def user_type(self) -> typing.Optional[builtins.str]:
        '''The type of the user.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userType"))

    @user_type.setter
    def user_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b560448b79c8df59777bf516743c73a776fe419d2c08183dd62546f1fc65ae4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userType", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnUserProfile.IamUserProfileDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class IamUserProfileDetailsProperty:
        def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
            '''The details of the IAM User Profile.

            :param arn: The ARN of the IAM User Profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-iamuserprofiledetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                iam_user_profile_details_property = datazone.CfnUserProfile.IamUserProfileDetailsProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3fd3b9b642370fd3593445a459418ba3df5f97586bee6446bed499fa533a4022)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the IAM User Profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-iamuserprofiledetails.html#cfn-datazone-userprofile-iamuserprofiledetails-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamUserProfileDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnUserProfile.SsoUserProfileDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "first_name": "firstName",
            "last_name": "lastName",
            "username": "username",
        },
    )
    class SsoUserProfileDetailsProperty:
        def __init__(
            self,
            *,
            first_name: typing.Optional[builtins.str] = None,
            last_name: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details of the SSO User Profile.

            :param first_name: The First Name of the IAM User Profile.
            :param last_name: The Last Name of the IAM User Profile.
            :param username: The username of the SSO User Profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-ssouserprofiledetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                sso_user_profile_details_property = datazone.CfnUserProfile.SsoUserProfileDetailsProperty(
                    first_name="firstName",
                    last_name="lastName",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__07963e9a65d43152452195ee221d80669fe4707d48ffd231ffc947c240448dbd)
                check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
                check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if first_name is not None:
                self._values["first_name"] = first_name
            if last_name is not None:
                self._values["last_name"] = last_name
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def first_name(self) -> typing.Optional[builtins.str]:
            '''The First Name of the IAM User Profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-ssouserprofiledetails.html#cfn-datazone-userprofile-ssouserprofiledetails-firstname
            '''
            result = self._values.get("first_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def last_name(self) -> typing.Optional[builtins.str]:
            '''The Last Name of the IAM User Profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-ssouserprofiledetails.html#cfn-datazone-userprofile-ssouserprofiledetails-lastname
            '''
            result = self._values.get("last_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''The username of the SSO User Profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-ssouserprofiledetails.html#cfn-datazone-userprofile-ssouserprofiledetails-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SsoUserProfileDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_datazone.CfnUserProfile.UserProfileDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"iam": "iam", "sso": "sso"},
    )
    class UserProfileDetailsProperty:
        def __init__(
            self,
            *,
            iam: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnUserProfile.IamUserProfileDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sso: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnUserProfile.SsoUserProfileDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param iam: The details of the IAM User Profile.
            :param sso: The details of the SSO User Profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-userprofiledetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_datazone as datazone
                
                user_profile_details_property = datazone.CfnUserProfile.UserProfileDetailsProperty(
                    iam=datazone.CfnUserProfile.IamUserProfileDetailsProperty(
                        arn="arn"
                    ),
                    sso=datazone.CfnUserProfile.SsoUserProfileDetailsProperty(
                        first_name="firstName",
                        last_name="lastName",
                        username="username"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1a1351a79d8a8cf0246c7e7591c1c0736de90dfd896392c833f9cb3530c63997)
                check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
                check_type(argname="argument sso", value=sso, expected_type=type_hints["sso"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if iam is not None:
                self._values["iam"] = iam
            if sso is not None:
                self._values["sso"] = sso

        @builtins.property
        def iam(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUserProfile.IamUserProfileDetailsProperty"]]:
            '''The details of the IAM User Profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-userprofiledetails.html#cfn-datazone-userprofile-userprofiledetails-iam
            '''
            result = self._values.get("iam")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUserProfile.IamUserProfileDetailsProperty"]], result)

        @builtins.property
        def sso(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUserProfile.SsoUserProfileDetailsProperty"]]:
            '''The details of the SSO User Profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-userprofile-userprofiledetails.html#cfn-datazone-userprofile-userprofiledetails-sso
            '''
            result = self._values.get("sso")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUserProfile.SsoUserProfileDetailsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserProfileDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_datazone.CfnUserProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "user_identifier": "userIdentifier",
        "status": "status",
        "user_type": "userType",
    },
)
class CfnUserProfileProps:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        user_identifier: builtins.str,
        status: typing.Optional[builtins.str] = None,
        user_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnUserProfile``.

        :param domain_identifier: The identifier of the Amazon DataZone domain in which the user profile would be created.
        :param user_identifier: The ID of the user.
        :param status: The status of the user profile.
        :param user_type: The type of the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-userprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_datazone as datazone
            
            cfn_user_profile_props = datazone.CfnUserProfileProps(
                domain_identifier="domainIdentifier",
                user_identifier="userIdentifier",
            
                # the properties below are optional
                status="status",
                user_type="userType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__431134ef647ba94f8eb72ef3985b514bb86c42b53ca933a9fd51ea529bd0fec8)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument user_identifier", value=user_identifier, expected_type=type_hints["user_identifier"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument user_type", value=user_type, expected_type=type_hints["user_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "user_identifier": user_identifier,
        }
        if status is not None:
            self._values["status"] = status
        if user_type is not None:
            self._values["user_type"] = user_type

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The identifier of the Amazon DataZone domain in which the user profile would be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-userprofile.html#cfn-datazone-userprofile-domainidentifier
        '''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_identifier(self) -> builtins.str:
        '''The ID of the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-userprofile.html#cfn-datazone-userprofile-useridentifier
        '''
        result = self._values.get("user_identifier")
        assert result is not None, "Required property 'user_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the user profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-userprofile.html#cfn-datazone-userprofile-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_type(self) -> typing.Optional[builtins.str]:
        '''The type of the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-userprofile.html#cfn-datazone-userprofile-usertype
        '''
        result = self._values.get("user_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataSource",
    "CfnDataSourceProps",
    "CfnDomain",
    "CfnDomainProps",
    "CfnEnvironment",
    "CfnEnvironmentBlueprintConfiguration",
    "CfnEnvironmentBlueprintConfigurationProps",
    "CfnEnvironmentProfile",
    "CfnEnvironmentProfileProps",
    "CfnEnvironmentProps",
    "CfnGroupProfile",
    "CfnGroupProfileProps",
    "CfnProject",
    "CfnProjectMembership",
    "CfnProjectMembershipProps",
    "CfnProjectProps",
    "CfnSubscriptionTarget",
    "CfnSubscriptionTargetProps",
    "CfnUserProfile",
    "CfnUserProfileProps",
]

publication.publish()

def _typecheckingstub__b74a6ac4c3e98c769e70eb9dc6e8b5f1e8f347a3615d992ea7f1c0d421505732(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_identifier: builtins.str,
    environment_identifier: builtins.str,
    name: builtins.str,
    project_identifier: builtins.str,
    type: builtins.str,
    asset_forms_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.FormInputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DataSourceConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    enable_setting: typing.Optional[builtins.str] = None,
    publish_on_import: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    recommendation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RecommendationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.ScheduleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33bcdad9dc3f66143343138916ff460345630898241997119efe034ff66c6a2d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__514e677208a85632dfb8a4fcf6a71bea051c78567845845ff000fb632aab7b5e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a7af31e6c5b528548b0d530d4c772805fb61420d812ed44382c7c390086f11a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ed64595e5e156084952dfe11e1e064218cba6affcb8bf2736d3e0a177b08bea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2821916d0fb71bfe9878d75d49136fb173b8984bb70e31a4a9720eebf6db3ab3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__132e7e2cf26f81c0a6085283f4e8d4d9f57da8d3612dd55ee6749c192a2d2d48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d073c13da920100b2d471eb086a45db9d741e4fba0dc8a0677ffe38913dffe2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd33f5216eca4a4d866e941b183a5ef445088a5e6ecec69e2fbc695f6b40c3c8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataSource.FormInputProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89afb772730c8209e27316b8af14ef1a6fce9f26db9f31432460eff964f55b9d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DataSourceConfigurationInputProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7e5b5e600ceeed0171e7700fd1bb1de08837412c76a72396b54b2ddfcd29970(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c4b8af5e1647731587c5aaa0ac03d7e6980729c429135de819a778bb0e7a2eb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b8ce503c85a6ffdd243c0997e3ddab5dbbb39fc65cc2c74982964209c9e4eaa(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__213e25d07ce5c23cedc981ed540f97a1577533cd3dab4f6e0a08f166e38cfb49(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.RecommendationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__693f7d02be84739f3d95375e94a3b4c964749b34e7dbf67ac0aa2b011ca3f625(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.ScheduleConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9bda82e8d6905101b134276b283067e9b4fc8445ba4e98917ea7cd2937c5828(
    *,
    glue_run_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.GlueRunConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift_run_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RedshiftRunConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb2b40bf6229fe763c7c585fa978f99e3900fbd6916fc58d9065ddc99d90df18(
    *,
    expression: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e39737bda51e6e9e0b04ce2c0598b00c495cf2dad8f53d4761c7a31ecf92227e(
    *,
    form_name: builtins.str,
    content: typing.Optional[builtins.str] = None,
    type_identifier: typing.Optional[builtins.str] = None,
    type_revision: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad6a5a243d0193849a3ba940cfbd956439268966f2ff08bff1fbcf5af20fe953(
    *,
    relational_filter_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RelationalFilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    auto_import_data_quality_result: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    data_access_role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b892cb470f7ea420aeb56956a5375b815b6b2a91d0e3d5aaa0a3461f5924b22(
    *,
    enable_business_name_generation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf5e238c98cd0e25a8234c800e1db4699c482f8c18eb4b1a30bdf8afd3ca2718(
    *,
    cluster_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1df8fcf30634f3b35250f98172cf307551610fbd637ef517691ae5581ccb5f66(
    *,
    secret_manager_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dd4c8b6216739fc8295ada55b58407d555982639c53118e9be94f72b8eb8e7c(
    *,
    redshift_credential_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RedshiftCredentialConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    redshift_storage: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RedshiftStorageProperty, typing.Dict[builtins.str, typing.Any]]],
    relational_filter_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RelationalFilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    data_access_role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c58e081ae0c5b103243a5fb5e44d072e16021860d239dd719e8ecaa4696f2da8(
    *,
    workgroup_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6959cf31dac7c5d3c9ee4d255059c5f6007a01d1da657810b6e3e44f31806173(
    *,
    redshift_cluster_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RedshiftClusterStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift_serverless_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RedshiftServerlessStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b69950b3dd7224f1119f8c5e6a2c8675594377bc1e5845a101f3b5f210681258(
    *,
    database_name: builtins.str,
    filter_expressions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.FilterExpressionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    schema_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fc1ad55dd2850c09e234b6cbea1fb383c32658a6b0f4b3e6c9ec1d67d8ae10c(
    *,
    schedule: typing.Optional[builtins.str] = None,
    timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc5ec98207dd171531ba923ab77ceb4e9c095a2ac7eb083b5faef7393c183f86(
    *,
    domain_identifier: builtins.str,
    environment_identifier: builtins.str,
    name: builtins.str,
    project_identifier: builtins.str,
    type: builtins.str,
    asset_forms_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.FormInputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DataSourceConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    enable_setting: typing.Optional[builtins.str] = None,
    publish_on_import: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    recommendation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.RecommendationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.ScheduleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__047efef40bc572d080b2e64b8f32c1db40e40ba16fc7d29d887073e9c6b44c3f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_execution_role: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kms_key_identifier: typing.Optional[builtins.str] = None,
    single_sign_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SingleSignOnProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44ac286b6a265a7b8c549e9f75d607cdf3e71f300523940763c96adb368c15ac(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__595689c850e768a74bf0e3147031e1acd033e20ab08856209edf9954aa010432(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f0f91db144dcd37dc91c4f005e5e179143c7d40165baf625ef7e284af70358e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb44fad9b00c8b94e0193e65a7d6e38fbf79595a0c367032211eb3ddcec54145(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb0d62a189dbc4d1b327c1e7f651b95f580a2f6196abce203f4709bcca75c7c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49d22f79e701c8bd8ae540b270f397204f2285f1dc76ab7d1556d659a050f38b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee4595d765303396b66c3b59368637f839b950667fb4c707c509ac63e084f20b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.SingleSignOnProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d899e2a4a220703956ab7f56e7c810107ec736f8c6281bedb3bc027e6ddb2ba4(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7f4cd03b79bceb07fb9f1366c739ee9cc49b8cbf6b9077a564689e81698df16(
    *,
    type: typing.Optional[builtins.str] = None,
    user_assignment: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d98e07f58a8aeb53fe8b36894639594f83be43ac8d182e1c384572cf0038d27(
    *,
    domain_execution_role: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kms_key_identifier: typing.Optional[builtins.str] = None,
    single_sign_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.SingleSignOnProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9dbab782927b08354bbafa4881abe3f775c9141395be836e6450777f8729b9b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_identifier: builtins.str,
    environment_profile_identifier: builtins.str,
    name: builtins.str,
    project_identifier: builtins.str,
    description: typing.Optional[builtins.str] = None,
    glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.EnvironmentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a28a39a0c7ba040029b6d28481def84a1131453e9259d7f220a8d8f9a9562fcf(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7a663cc771f3c58655975db4a99b46784c16b0b96c4bb006217531f931854d1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b36a4aa57667467b8bda95ca761a942a6f67e34e8549cd2dccc7a61d8399e9b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__123d0e6b3ed252019ec79f09a380206e446d8155ba73fc8e7518fbd3dbac8c2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4376356ce7178baaec6de65e59f567c3496e08605a27833ed8e83bfe0ff4be4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baefbe7e97d72065b3b2c6be4e97a54bf9298376bb60dcac92eb7191397e306b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00e90ff4028654f7f45c97804aa061515407ac2ce2e55a21a1a4e4ff76fefd60(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d52d21b9ab0852f8793f985e6f12ccea104ddc7e138f30b744d739af3c46b742(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d345163e4f1ef89a409f470c896454213d0735fe6e5011e7ec6df4ead799556d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.EnvironmentParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d32a764f93482ecbfe18350874389b17ae96f3d5f78686bae5b55a2dcdfc012b(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48d8677ae22ff2da132402ace39f998c6b914f7464ce38abe9373fdbc550c445(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_identifier: builtins.str,
    enabled_regions: typing.Sequence[builtins.str],
    environment_blueprint_identifier: builtins.str,
    manage_access_role_arn: typing.Optional[builtins.str] = None,
    provisioning_role_arn: typing.Optional[builtins.str] = None,
    regional_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeb5ba3f6738d175b0ca7714e77b6af191ccad2c9967480252920cb95dc6cb8f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86364c1d7caa870da909a60996d646dde31c0e41cb594d0e952262cd925d5bdf(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e6a26e61dc0bca0a16da5100bf8f8cfcb05985dcd52fd83afd7818c62445836(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9064df9af275b8a17afb82a8fc271f7b6e0ab19cdf01da41f144bac4832180e0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db2bf9c4c7f25403fe2aa03be854b8b8b1f530f8d53a317f87b2fb9470d906a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13a80be3403ea5113203d40c0843c4e4965600487d58b5f1e83bf1b8a9fc3d11(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09c1e18144766c7e8d72f080dbe9de88dc085cfbdaa47a10b50cf7e235be8d65(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93fe5a214b768cb7201e2f47a6073bdec0303c4cda4d1d0b739b124ba7858574(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__563b6d6aa110d6b77fcca8e42c3020852fa0c12036e1ba7f6ee62b2ce30826ff(
    *,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca96f6fc24dc164f6fafb08d94645f48f6b4fc5c0a2ad8a3b95e170935e7353a(
    *,
    domain_identifier: builtins.str,
    enabled_regions: typing.Sequence[builtins.str],
    environment_blueprint_identifier: builtins.str,
    manage_access_role_arn: typing.Optional[builtins.str] = None,
    provisioning_role_arn: typing.Optional[builtins.str] = None,
    regional_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentBlueprintConfiguration.RegionalParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a22dac59a328e3776825e07c2891d034e7e205eeeb00866d9086cf2f1dceb4f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    aws_account_id: builtins.str,
    aws_account_region: builtins.str,
    domain_identifier: builtins.str,
    environment_blueprint_identifier: builtins.str,
    name: builtins.str,
    project_identifier: builtins.str,
    description: typing.Optional[builtins.str] = None,
    user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentProfile.EnvironmentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b72ea9dd66a1ceac9aed426988a2df917e784879f21b1f6f0c19ca29b30b31b0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d250e5f9b10cd5d865865b560ea448ee7860153a35651b00d758f6634aba260(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de45320506b6ea6065d4e8de40a649bf205ae44ef01638670599709d45fde670(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__929764ebd8bf0a538d63bf5bea864a4c6a1f1fa57874f35c72ee4cb0c977cdf1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9311c317e06fadb8c96c0e621239f5e4ce23903cdc1515f8f48973321817bc6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40d0761ec5bd844c4a1859c609961ac63da5ca2a42154f19f8cdf0482693545f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__894c00430dd4f51ab95f6ed5db99418bdfe03c4cd5e70df92930998dc03b23e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32f0a4cae84b8e4e478646d80c611ae0d63fbea35bd054197eaeb64b33b624c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__537f0658d3e004344b5e150e1c4182f64abe6101e2d21aaf1644347b19d27116(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f091fadf5731901077c11ba7bce182eb007b6bd8b291bb6a4676fd3fa8e0e689(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironmentProfile.EnvironmentParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d9a0947f6555aed5fe498e71fb0065f6dff69f004c35341f60523d1de281e5f(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24d37d0c5f53a77c5e5be4ffa574af7dd3da85d8b5eb31bff30362d6c63ac36b(
    *,
    aws_account_id: builtins.str,
    aws_account_region: builtins.str,
    domain_identifier: builtins.str,
    environment_blueprint_identifier: builtins.str,
    name: builtins.str,
    project_identifier: builtins.str,
    description: typing.Optional[builtins.str] = None,
    user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironmentProfile.EnvironmentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52cb17aae6cf0b0cbeef010a71f7f53573517f0a8e973b5881ae34c1691d672b(
    *,
    domain_identifier: builtins.str,
    environment_profile_identifier: builtins.str,
    name: builtins.str,
    project_identifier: builtins.str,
    description: typing.Optional[builtins.str] = None,
    glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.EnvironmentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bccafb3ac5ccb0c73cc0aaea6cf365a78e841d8d731ffbfa84165d7f8100f7a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_identifier: builtins.str,
    group_identifier: builtins.str,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3064788268855f6623aaf3b52a7be17022b3d0c8d206428bb22e10d7bd9791de(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66e617beac92ae83db2859cea30504a6e86d11714b8584d4212fe2f5634055e4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bfce5f937e19aa12105a026759b48056e8cb9facac990d4a84ae9ebf754349a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4cfe59401594c99ca6ed491e080ab3526afa6a5fbfa200d918455779f2c060f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__489105c9239ff5a560f37a1c161dc9de12874e97ca98bb0ac4df8139e29b6727(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f4f2d05f4850cb07cd88e6e5af875d2c16fa3ae4bcbc384b9a51f7f0d0ca2e4(
    *,
    domain_identifier: builtins.str,
    group_identifier: builtins.str,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dd190e348e5421f499a11e44b2fb0c69295587e5e7717b13a56786a897efe7f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_identifier: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dec99f127bfd691b7b1ab5260c233568e5b335a316a646dd759686435ab2eb32(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81361e533bde98a7e424eedf14591a679c836493433a44301b63cbf3357e5369(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c4440504b53716f23143b92e80a5ea3dcfaddd707d93cad9b77c33e5e19e7a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7972d56cc7ec2cdd1800b8f0d6a79f7b4ad88633cf64a2e04f072fab6c9454b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbb0277c9bfd29282afdae45a284966770345575b2854ec5cd9e6c04dffbac96(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed99a8f1a094dd4883e961330ac91acc714a4a5fd200b2d53a52d4113d5a34f8(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__227cc3d5649ee98fd5579f9e1870652d6de5250e0390e91fec524565dc07c0b9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    designation: builtins.str,
    domain_identifier: builtins.str,
    member: typing.Union[_IResolvable_da3f097b, typing.Union[CfnProjectMembership.MemberProperty, typing.Dict[builtins.str, typing.Any]]],
    project_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e6a7791d79b9b8f15baba0f04bddbfa77afbfbdd8d2872a6e46acd2ccee79c4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e37a11438611477027ae5dde4a091dc361c7dc56ba7538221e222ef9083be907(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71ec417c1a2abac8b6037b5bfedeb8520a3be4a0844d46c1862cb259465e45f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66d809e4462dc85243bcc1ab3799cc4a5180f2f4119683718081fa5f79530ac7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50f6e6b64e6349a5c9d740955a9ccac88cf9da161bf02038bc9e12572958a93f(
    value: typing.Union[_IResolvable_da3f097b, CfnProjectMembership.MemberProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da845d5c47de18f48a6a2e21aa5b41e5193d4b3faad962602fc4d3b98d677eb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2184a0c3aa18e8899e2cb70b944b79d781e689bd543ac2140e9176025c2fa864(
    *,
    group_identifier: typing.Optional[builtins.str] = None,
    user_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b25f4db16efa2b368a4cf197bdf102ccdf0c613db5654c1186f9404f9259e4d7(
    *,
    designation: builtins.str,
    domain_identifier: builtins.str,
    member: typing.Union[_IResolvable_da3f097b, typing.Union[CfnProjectMembership.MemberProperty, typing.Dict[builtins.str, typing.Any]]],
    project_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d519699f8d5d172880216006cab9e8c1595fc99339cf485d2be1f6c37bbc5a4c(
    *,
    domain_identifier: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    glossary_terms: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c61b5cfe149791a4c62bad0056737a365bdf72f7f99e6e72c71be1058e91604d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    applicable_asset_types: typing.Sequence[builtins.str],
    authorized_principals: typing.Sequence[builtins.str],
    domain_identifier: builtins.str,
    environment_identifier: builtins.str,
    manage_access_role: builtins.str,
    name: builtins.str,
    subscription_target_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriptionTarget.SubscriptionTargetFormProperty, typing.Dict[builtins.str, typing.Any]]]]],
    type: builtins.str,
    provider: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1ffb846a6baf7f8d43c947f31440c264738eb11477a914e6234e72e512226a7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__867dc79750bd91424b54ba2d5f7eca4a8d13f7f3c9f4ffc4effe5dae834ed869(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6db9fad0cfe2726fd2714cfa52499e265af46d2cacf4be9daa6378bd8c673b5a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ec38d6c0d885e0ae64427a2407f691f11cd764f198652ece23783772c2611fb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77bccb41f1eb7b5a32710e03ae6cfec74eb17bf3129bd372a11c92f7f67f5dc0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20ed34c3b416019570831200db233eb4c407b91b53464c36e9fbdbdcd4a6da82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83f19af57790aab3ddc6c4e1f64e1f68cf69073e46da8ac997fc9f0c83e93198(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc691c403b67912db7216c5f5fddda4101316ca719bd90e37c92640197c61004(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a19c0f2213973750a6cc503429c6ef8619a3d0885a2df0f54aad48a00a3c6f46(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSubscriptionTarget.SubscriptionTargetFormProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8961cb77429dad851472db6b14a76c77606d0bffdc98a0cbb3cffd227c3ec500(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4526f8f71696c8c7bf040cd042cda55182de538f2ebf276253751b5a497c037(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__720cbd7aa436c84d94877993fe56ec1a54389edd9936074e71ebf65a3caffa9b(
    *,
    content: builtins.str,
    form_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b970b38bc2b99a7ed3ef3830dfa5721ecc9ee442e5d627e01abfdcb22600151(
    *,
    applicable_asset_types: typing.Sequence[builtins.str],
    authorized_principals: typing.Sequence[builtins.str],
    domain_identifier: builtins.str,
    environment_identifier: builtins.str,
    manage_access_role: builtins.str,
    name: builtins.str,
    subscription_target_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSubscriptionTarget.SubscriptionTargetFormProperty, typing.Dict[builtins.str, typing.Any]]]]],
    type: builtins.str,
    provider: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43948fd61004932aa31394de53e9c49e34aa425f3682404de5d5f6a249734d82(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_identifier: builtins.str,
    user_identifier: builtins.str,
    status: typing.Optional[builtins.str] = None,
    user_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62409db933bd1f83a26e4a296f90a5aa33de9e2cd9f82db4084d8f1cb0f382e4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bac3d345ed2cf85373ed12e71655921f20ce2575e0f95a05a3dd29cfa7e804e0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57dc87f9b5d4209a76a54e631bab548eddbecf73d3a0cb39b30030a99c20dbb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bc695cbd1d290ebde7514044903060b533b99cd4f724f387512ffb614625693(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f391a63fdbc6b7a8aefbb3664fddfe91481bce941965f274ecad0166152935ce(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b560448b79c8df59777bf516743c73a776fe419d2c08183dd62546f1fc65ae4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fd3b9b642370fd3593445a459418ba3df5f97586bee6446bed499fa533a4022(
    *,
    arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07963e9a65d43152452195ee221d80669fe4707d48ffd231ffc947c240448dbd(
    *,
    first_name: typing.Optional[builtins.str] = None,
    last_name: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a1351a79d8a8cf0246c7e7591c1c0736de90dfd896392c833f9cb3530c63997(
    *,
    iam: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUserProfile.IamUserProfileDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sso: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUserProfile.SsoUserProfileDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__431134ef647ba94f8eb72ef3985b514bb86c42b53ca933a9fd51ea529bd0fec8(
    *,
    domain_identifier: builtins.str,
    user_identifier: builtins.str,
    status: typing.Optional[builtins.str] = None,
    user_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
