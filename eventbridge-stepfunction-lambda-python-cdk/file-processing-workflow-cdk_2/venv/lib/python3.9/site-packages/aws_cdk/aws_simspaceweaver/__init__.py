'''
# AWS::SimSpaceWeaver Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_simspaceweaver as simspaceweaver
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SimSpaceWeaver construct libraries](https://constructs.dev/search?q=simspaceweaver)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SimSpaceWeaver resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SimSpaceWeaver.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SimSpaceWeaver](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SimSpaceWeaver.html).

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
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnSimulation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_simspaceweaver.CfnSimulation",
):
    '''Use the ``AWS::SimSpaceWeaver::Simulation`` resource to specify a simulation that AWS CloudFormation starts in the AWS Cloud , in your AWS account .

    In the resource properties section of your template, provide the name of an existing IAM role configured with the proper permissions, and the name of an existing Amazon S3 bucket. Your account must have permissions to read the Amazon S3 bucket. The Amazon S3 bucket must contain a valid schema. The schema must refer to simulation assets that are already uploaded to the AWS Cloud . For more information, see the `detailed tutorial <https://docs.aws.amazon.com/simspaceweaver/latest/userguide/getting-started_detailed.html>`_ in the *AWS SimSpace Weaver User Guide* .

    Specify a ``SnapshotS3Location`` to start a simulation from a snapshot instead of from a schema. When you start a simulation from a snapshot, SimSpace Weaver initializes the entity data in the State Fabric with data saved in the snapshot, starts the spatial and service apps that were running when the snapshot was created, and restores the clock to the appropriate tick. Your app zip files must be in the same location in Amazon S3 as they were in for the original simulation. You must start any custom apps separately. For more information about snapshots, see `Snapshots <https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_snapshots.html>`_ in the *AWS SimSpace Weaver User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_simspaceweaver as simspaceweaver
        
        cfn_simulation = simspaceweaver.CfnSimulation(self, "MyCfnSimulation",
            name="name",
            role_arn="roleArn",
        
            # the properties below are optional
            maximum_duration="maximumDuration",
            schema_s3_location=simspaceweaver.CfnSimulation.S3LocationProperty(
                bucket_name="bucketName",
                object_key="objectKey"
            ),
            snapshot_s3_location=simspaceweaver.CfnSimulation.S3LocationProperty(
                bucket_name="bucketName",
                object_key="objectKey"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        role_arn: builtins.str,
        maximum_duration: typing.Optional[builtins.str] = None,
        schema_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSimulation.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        snapshot_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSimulation.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the simulation.
        :param role_arn: The Amazon Resource Name (ARN) of the AWS Identity and Access Management ( IAM ) role that the simulation assumes to perform actions. For more information about ARNs, see `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* . For more information about IAM roles, see `IAM roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`_ in the *AWS Identity and Access Management User Guide* .
        :param maximum_duration: The maximum running time of the simulation, specified as a number of minutes (m or M), hours (h or H), or days (d or D). The simulation stops when it reaches this limit. The maximum value is ``14D`` , or its equivalent in the other units. The default value is ``14D`` . A value equivalent to ``0`` makes the simulation immediately transition to ``STOPPING`` as soon as it reaches ``STARTED`` .
        :param schema_s3_location: The location of the simulation schema in Amazon Simple Storage Service ( Amazon S3 ). For more information about Amazon S3 , see the `*Amazon Simple Storage Service User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html>`_ . Provide a ``SchemaS3Location`` to start your simulation from a schema. If you provide a ``SchemaS3Location`` then you can't provide a ``SnapshotS3Location`` .
        :param snapshot_s3_location: The location of the snapshot in Amazon Simple Storage Service ( Amazon S3 ). For more information about Amazon S3 , see the `*Amazon Simple Storage Service User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html>`_ . Provide a ``SnapshotS3Location`` to start your simulation from a snapshot. If you provide a ``SnapshotS3Location`` then you can't provide a ``SchemaS3Location`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49a18eff4f0bb5a69b0bd9ec4308865d3a99b9833d34d09dc1d10808b54c7b66)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSimulationProps(
            name=name,
            role_arn=role_arn,
            maximum_duration=maximum_duration,
            schema_s3_location=schema_s3_location,
            snapshot_s3_location=snapshot_s3_location,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5e211ad7b3d49f5cb4da59f7dc84b6d22a3e802292f57f2c44fe93c3c9ff344)
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
            type_hints = typing.get_type_hints(_typecheckingstub__65af4962335a3edb9ad4f69b98f35694c832172a61202cc9cfed67b004c64dca)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDescribePayload")
    def attr_describe_payload(self) -> builtins.str:
        '''The JSON blob that the `DescribeSimulation <https://docs.aws.amazon.com/simspaceweaver/latest/APIReference/API_DescribeSimulation.html>`_ action returns.

        :cloudformationAttribute: DescribePayload
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDescribePayload"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the simulation.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cee178cc692dbe490816570d9a4e2e7a1337df4dada160c359d1e63f9610a019)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AWS Identity and Access Management ( IAM ) role that the simulation assumes to perform actions.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cf80826f07ceb33872e230ca4db5787964200674ba7f1acac6b09dd5c724ba1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="maximumDuration")
    def maximum_duration(self) -> typing.Optional[builtins.str]:
        '''The maximum running time of the simulation, specified as a number of minutes (m or M), hours (h or H), or days (d or D).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumDuration"))

    @maximum_duration.setter
    def maximum_duration(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a94aed77c22b4214ad09ce3c32e695147377205b63da1699fb7e1e3b97467dc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumDuration", value)

    @builtins.property
    @jsii.member(jsii_name="schemaS3Location")
    def schema_s3_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimulation.S3LocationProperty"]]:
        '''The location of the simulation schema in Amazon Simple Storage Service ( Amazon S3 ).'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimulation.S3LocationProperty"]], jsii.get(self, "schemaS3Location"))

    @schema_s3_location.setter
    def schema_s3_location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimulation.S3LocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19e5b9acd452852f4eb9cb770f11aaf43e111ff00ccb82a5824b65ae6869ef67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotS3Location")
    def snapshot_s3_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimulation.S3LocationProperty"]]:
        '''The location of the snapshot in Amazon Simple Storage Service ( Amazon S3 ).'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimulation.S3LocationProperty"]], jsii.get(self, "snapshotS3Location"))

    @snapshot_s3_location.setter
    def snapshot_s3_location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimulation.S3LocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eae2ce65a01ef04b46cbcb9953c071289e4b3d8a6e8631a73da64120010bc9c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotS3Location", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_simspaceweaver.CfnSimulation.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName", "object_key": "objectKey"},
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            object_key: builtins.str,
        ) -> None:
            '''A location in Amazon Simple Storage Service ( Amazon S3 ) where SimSpace Weaver stores simulation data, such as your app .zip files and schema file. For more information about Amazon S3 , see the `*Amazon Simple Storage Service User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html>`_ .

            :param bucket_name: The name of an Amazon S3 bucket. For more information about buckets, see `Creating, configuring, and working with Amazon S3 buckets <https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html>`_ in the *Amazon Simple Storage Service User Guide* .
            :param object_key: The key name of an object in Amazon S3 . For more information about Amazon S3 objects and object keys, see `Uploading, downloading, and working with objects in Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/userguide/uploading-downloading-objects.html>`_ in the *Amazon Simple Storage Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-simspaceweaver-simulation-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_simspaceweaver as simspaceweaver
                
                s3_location_property = simspaceweaver.CfnSimulation.S3LocationProperty(
                    bucket_name="bucketName",
                    object_key="objectKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9bb956d9a2c736c24db9fd8ada0f1dbf623d28b2a7e7a0086505b12c3381d40d)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument object_key", value=object_key, expected_type=type_hints["object_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
                "object_key": object_key,
            }

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The name of an Amazon S3 bucket.

            For more information about buckets, see `Creating, configuring, and working with Amazon S3 buckets <https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html>`_ in the *Amazon Simple Storage Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-simspaceweaver-simulation-s3location.html#cfn-simspaceweaver-simulation-s3location-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_key(self) -> builtins.str:
            '''The key name of an object in Amazon S3 .

            For more information about Amazon S3 objects and object keys, see `Uploading, downloading, and working with objects in Amazon S3 <https://docs.aws.amazon.com/AmazonS3/latest/userguide/uploading-downloading-objects.html>`_ in the *Amazon Simple Storage Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-simspaceweaver-simulation-s3location.html#cfn-simspaceweaver-simulation-s3location-objectkey
            '''
            result = self._values.get("object_key")
            assert result is not None, "Required property 'object_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_simspaceweaver.CfnSimulationProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "role_arn": "roleArn",
        "maximum_duration": "maximumDuration",
        "schema_s3_location": "schemaS3Location",
        "snapshot_s3_location": "snapshotS3Location",
    },
)
class CfnSimulationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        role_arn: builtins.str,
        maximum_duration: typing.Optional[builtins.str] = None,
        schema_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulation.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        snapshot_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulation.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSimulation``.

        :param name: The name of the simulation.
        :param role_arn: The Amazon Resource Name (ARN) of the AWS Identity and Access Management ( IAM ) role that the simulation assumes to perform actions. For more information about ARNs, see `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* . For more information about IAM roles, see `IAM roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`_ in the *AWS Identity and Access Management User Guide* .
        :param maximum_duration: The maximum running time of the simulation, specified as a number of minutes (m or M), hours (h or H), or days (d or D). The simulation stops when it reaches this limit. The maximum value is ``14D`` , or its equivalent in the other units. The default value is ``14D`` . A value equivalent to ``0`` makes the simulation immediately transition to ``STOPPING`` as soon as it reaches ``STARTED`` .
        :param schema_s3_location: The location of the simulation schema in Amazon Simple Storage Service ( Amazon S3 ). For more information about Amazon S3 , see the `*Amazon Simple Storage Service User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html>`_ . Provide a ``SchemaS3Location`` to start your simulation from a schema. If you provide a ``SchemaS3Location`` then you can't provide a ``SnapshotS3Location`` .
        :param snapshot_s3_location: The location of the snapshot in Amazon Simple Storage Service ( Amazon S3 ). For more information about Amazon S3 , see the `*Amazon Simple Storage Service User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html>`_ . Provide a ``SnapshotS3Location`` to start your simulation from a snapshot. If you provide a ``SnapshotS3Location`` then you can't provide a ``SchemaS3Location`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_simspaceweaver as simspaceweaver
            
            cfn_simulation_props = simspaceweaver.CfnSimulationProps(
                name="name",
                role_arn="roleArn",
            
                # the properties below are optional
                maximum_duration="maximumDuration",
                schema_s3_location=simspaceweaver.CfnSimulation.S3LocationProperty(
                    bucket_name="bucketName",
                    object_key="objectKey"
                ),
                snapshot_s3_location=simspaceweaver.CfnSimulation.S3LocationProperty(
                    bucket_name="bucketName",
                    object_key="objectKey"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffc14fdb1da790b4cfe1614eb2f8982246ef563b4e0f372f8730236621b7952b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument maximum_duration", value=maximum_duration, expected_type=type_hints["maximum_duration"])
            check_type(argname="argument schema_s3_location", value=schema_s3_location, expected_type=type_hints["schema_s3_location"])
            check_type(argname="argument snapshot_s3_location", value=snapshot_s3_location, expected_type=type_hints["snapshot_s3_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "role_arn": role_arn,
        }
        if maximum_duration is not None:
            self._values["maximum_duration"] = maximum_duration
        if schema_s3_location is not None:
            self._values["schema_s3_location"] = schema_s3_location
        if snapshot_s3_location is not None:
            self._values["snapshot_s3_location"] = snapshot_s3_location

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the simulation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.html#cfn-simspaceweaver-simulation-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AWS Identity and Access Management ( IAM ) role that the simulation assumes to perform actions.

        For more information about ARNs, see `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* . For more information about IAM roles, see `IAM roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`_ in the *AWS Identity and Access Management User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.html#cfn-simspaceweaver-simulation-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def maximum_duration(self) -> typing.Optional[builtins.str]:
        '''The maximum running time of the simulation, specified as a number of minutes (m or M), hours (h or H), or days (d or D).

        The simulation stops when it reaches this limit. The maximum value is ``14D`` , or its equivalent in the other units. The default value is ``14D`` . A value equivalent to ``0`` makes the simulation immediately transition to ``STOPPING`` as soon as it reaches ``STARTED`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.html#cfn-simspaceweaver-simulation-maximumduration
        '''
        result = self._values.get("maximum_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_s3_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimulation.S3LocationProperty]]:
        '''The location of the simulation schema in Amazon Simple Storage Service ( Amazon S3 ).

        For more information about Amazon S3 , see the `*Amazon Simple Storage Service User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html>`_ .

        Provide a ``SchemaS3Location`` to start your simulation from a schema.

        If you provide a ``SchemaS3Location`` then you can't provide a ``SnapshotS3Location`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.html#cfn-simspaceweaver-simulation-schemas3location
        '''
        result = self._values.get("schema_s3_location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimulation.S3LocationProperty]], result)

    @builtins.property
    def snapshot_s3_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimulation.S3LocationProperty]]:
        '''The location of the snapshot in Amazon Simple Storage Service ( Amazon S3 ).

        For more information about Amazon S3 , see the `*Amazon Simple Storage Service User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html>`_ .

        Provide a ``SnapshotS3Location`` to start your simulation from a snapshot.

        If you provide a ``SnapshotS3Location`` then you can't provide a ``SchemaS3Location`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.html#cfn-simspaceweaver-simulation-snapshots3location
        '''
        result = self._values.get("snapshot_s3_location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimulation.S3LocationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSimulationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnSimulation",
    "CfnSimulationProps",
]

publication.publish()

def _typecheckingstub__49a18eff4f0bb5a69b0bd9ec4308865d3a99b9833d34d09dc1d10808b54c7b66(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    role_arn: builtins.str,
    maximum_duration: typing.Optional[builtins.str] = None,
    schema_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulation.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snapshot_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulation.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5e211ad7b3d49f5cb4da59f7dc84b6d22a3e802292f57f2c44fe93c3c9ff344(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65af4962335a3edb9ad4f69b98f35694c832172a61202cc9cfed67b004c64dca(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cee178cc692dbe490816570d9a4e2e7a1337df4dada160c359d1e63f9610a019(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cf80826f07ceb33872e230ca4db5787964200674ba7f1acac6b09dd5c724ba1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a94aed77c22b4214ad09ce3c32e695147377205b63da1699fb7e1e3b97467dc9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19e5b9acd452852f4eb9cb770f11aaf43e111ff00ccb82a5824b65ae6869ef67(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimulation.S3LocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eae2ce65a01ef04b46cbcb9953c071289e4b3d8a6e8631a73da64120010bc9c2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimulation.S3LocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb956d9a2c736c24db9fd8ada0f1dbf623d28b2a7e7a0086505b12c3381d40d(
    *,
    bucket_name: builtins.str,
    object_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffc14fdb1da790b4cfe1614eb2f8982246ef563b4e0f372f8730236621b7952b(
    *,
    name: builtins.str,
    role_arn: builtins.str,
    maximum_duration: typing.Optional[builtins.str] = None,
    schema_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulation.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snapshot_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulation.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
