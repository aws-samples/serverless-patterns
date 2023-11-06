'''
# AWS RoboMaker Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_robomaker as robomaker
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for RoboMaker construct libraries](https://constructs.dev/search?q=robomaker)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::RoboMaker resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RoboMaker.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::RoboMaker](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RoboMaker.html).

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
class CfnFleet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_robomaker.CfnFleet",
):
    '''.. epigraph::

   The following resource is now deprecated.

    This resource can no longer be provisioned via stack create or update operations, and should not be included in your stack templates.
    .. epigraph::

       We recommend migrating to AWS IoT Greengrass Version 2. For more information, see `Support Changes: May 2, 2022 <https://docs.aws.amazon.com/robomaker/latest/dg/chapter-support-policy.html#software-support-policy-may2022>`_ in the *AWS RoboMaker Developer Guide* .

    The ``AWS::RoboMaker::Fleet`` resource creates an AWS RoboMaker fleet. Fleets contain robots and can receive deployments.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-fleet.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_robomaker as robomaker
        
        cfn_fleet = robomaker.CfnFleet(self, "MyCfnFleet",
            name="name",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the fleet.
        :param tags: The list of all tags added to the fleet.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cf67028db50fbc82ea8f4501fdb4ee36d1ed66bd90e1e13e635239c75a407a8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFleetProps(name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79e824f817a2c25a6f542667057e9a4525e47750a2d9bc44f093375b07e8d178)
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
            type_hints = typing.get_type_hints(_typecheckingstub__195f1c8f4daafc0d71dbb26762ed99292b6f283831024397d9845964e6edd9c6)
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
        '''The Amazon Resource Name (ARN) of the fleet, such as ``arn:aws:robomaker:us-west-2:123456789012:deployment-fleet/MyFleet/1539894765711`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb2b0f115fd155ec1867ebdfab524eabaa919c39920655bedef657815f3fe35b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The list of all tags added to the fleet.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4a9d74f73ceaf3ae033517a44602efdc6fd84668be6992907ba5276fd26df0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_robomaker.CfnFleetProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "tags": "tags"},
)
class CfnFleetProps:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFleet``.

        :param name: The name of the fleet.
        :param tags: The list of all tags added to the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-fleet.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_robomaker as robomaker
            
            cfn_fleet_props = robomaker.CfnFleetProps(
                name="name",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5c8fc3b81304b565bf3da303dec523f47216f807e13ba1e0ddcc46ceb848df8)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-fleet.html#cfn-robomaker-fleet-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The list of all tags added to the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-fleet.html#cfn-robomaker-fleet-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFleetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRobot(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_robomaker.CfnRobot",
):
    '''.. epigraph::

   The following resource is now deprecated.

    This resource can no longer be provisioned via stack create or update operations, and should not be included in your stack templates.
    .. epigraph::

       We recommend migrating to AWS IoT Greengrass Version 2. For more information, see `Support Changes: May 2, 2022 <https://docs.aws.amazon.com/robomaker/latest/dg/chapter-support-policy.html#software-support-policy-may2022>`_ in the *AWS RoboMaker Developer Guide* .

    The ``AWS::RoboMaker::RobotApplication`` resource creates an AWS RoboMaker robot.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_robomaker as robomaker
        
        cfn_robot = robomaker.CfnRobot(self, "MyCfnRobot",
            architecture="architecture",
            greengrass_group_id="greengrassGroupId",
        
            # the properties below are optional
            fleet="fleet",
            name="name",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        architecture: builtins.str,
        greengrass_group_id: builtins.str,
        fleet: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param architecture: The architecture of the robot.
        :param greengrass_group_id: The Greengrass group associated with the robot.
        :param fleet: The Amazon Resource Name (ARN) of the fleet to which the robot will be registered.
        :param name: The name of the robot.
        :param tags: A map that contains tag keys and tag values that are attached to the robot.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49131f852e25508f2191103f967b740a3a43d115f73e1b3a287cc2e4a396694f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRobotProps(
            architecture=architecture,
            greengrass_group_id=greengrass_group_id,
            fleet=fleet,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__712f9da34bf6ddea1b6cd2b92a14c93de456aa09838fcb1df12120caab354dc4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__708276af184c2e226238ae52977a6357dc19766ae0a17f9abee37238a2200248)
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
        '''The Amazon Resource Name (ARN) of the robot.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="architecture")
    def architecture(self) -> builtins.str:
        '''The architecture of the robot.'''
        return typing.cast(builtins.str, jsii.get(self, "architecture"))

    @architecture.setter
    def architecture(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f36dbab08fea8dace0765ee7ba8b7d3ff9ee4c48d947b5303f3631f8a0369b5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "architecture", value)

    @builtins.property
    @jsii.member(jsii_name="greengrassGroupId")
    def greengrass_group_id(self) -> builtins.str:
        '''The Greengrass group associated with the robot.'''
        return typing.cast(builtins.str, jsii.get(self, "greengrassGroupId"))

    @greengrass_group_id.setter
    def greengrass_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50de460acfd3a8dbfb6259513c1df0e835e46e80422bd7d50197066f46adcf42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "greengrassGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="fleet")
    def fleet(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the fleet to which the robot will be registered.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fleet"))

    @fleet.setter
    def fleet(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8da9d8bd6e5845fb5ae85a5c0ecb127eb3120f33b979743f160cc5912ff26766)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fleet", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the robot.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db28cc7abf10f25ceb48539af3bff17364e26eb389639b29457ab05b7d152425)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map that contains tag keys and tag values that are attached to the robot.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__197f65220e7c1b22bb2750ecd4cf89b82125f1abad27a9e9cc4881b988b6ba6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRobotApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_robomaker.CfnRobotApplication",
):
    '''The ``AWS::RoboMaker::RobotApplication`` resource creates an AWS RoboMaker robot application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_robomaker as robomaker
        
        cfn_robot_application = robomaker.CfnRobotApplication(self, "MyCfnRobotApplication",
            robot_software_suite=robomaker.CfnRobotApplication.RobotSoftwareSuiteProperty(
                name="name",
        
                # the properties below are optional
                version="version"
            ),
        
            # the properties below are optional
            current_revision_id="currentRevisionId",
            environment="environment",
            name="name",
            sources=[robomaker.CfnRobotApplication.SourceConfigProperty(
                architecture="architecture",
                s3_bucket="s3Bucket",
                s3_key="s3Key"
            )],
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        robot_software_suite: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRobotApplication.RobotSoftwareSuiteProperty", typing.Dict[builtins.str, typing.Any]]],
        current_revision_id: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRobotApplication.SourceConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param robot_software_suite: The robot software suite used by the robot application.
        :param current_revision_id: The current revision id.
        :param environment: The environment of the robot application.
        :param name: The name of the robot application.
        :param sources: The sources of the robot application.
        :param tags: A map that contains tag keys and tag values that are attached to the robot application.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71fa9826def616b855a7d14f7c7a68432b3206eba76bd02b308db61a08332bc3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRobotApplicationProps(
            robot_software_suite=robot_software_suite,
            current_revision_id=current_revision_id,
            environment=environment,
            name=name,
            sources=sources,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42dcfe9a23f9087a5360cc6bd5cc1baa70c7249dcef1085237c5953641683f2b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ffda1b22518fe7e5746795534fa3f401eb6e2cd22e88b8c529a08a6830ac889)
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
        '''The Amazon Resource Name (ARN) of the robot application.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCurrentRevisionId")
    def attr_current_revision_id(self) -> builtins.str:
        '''The current revision id.

        :cloudformationAttribute: CurrentRevisionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCurrentRevisionId"))

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
    @jsii.member(jsii_name="robotSoftwareSuite")
    def robot_software_suite(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRobotApplication.RobotSoftwareSuiteProperty"]:
        '''The robot software suite used by the robot application.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRobotApplication.RobotSoftwareSuiteProperty"], jsii.get(self, "robotSoftwareSuite"))

    @robot_software_suite.setter
    def robot_software_suite(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnRobotApplication.RobotSoftwareSuiteProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a0183b45e0172b50d6049b802258f5f54543ee36f6ff14d04a41472f312ff04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "robotSoftwareSuite", value)

    @builtins.property
    @jsii.member(jsii_name="currentRevisionId")
    def current_revision_id(self) -> typing.Optional[builtins.str]:
        '''The current revision id.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "currentRevisionId"))

    @current_revision_id.setter
    def current_revision_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a68af59eeb167d0c020946ad9c700418dc6f280bb64690a231f2609770e55ce2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "currentRevisionId", value)

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> typing.Optional[builtins.str]:
        '''The environment of the robot application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environment"))

    @environment.setter
    def environment(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8346429cd042f143075e82bff1b46a5acd3b5c22740614aae1093279051fdea9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the robot application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69012b559357369e35caab49e8a89325e4bc8994f10edb7261ac37badc83f089)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRobotApplication.SourceConfigProperty"]]]]:
        '''The sources of the robot application.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRobotApplication.SourceConfigProperty"]]]], jsii.get(self, "sources"))

    @sources.setter
    def sources(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRobotApplication.SourceConfigProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__921f41fab15ec19f628942a860f0c537326ffdf47bee9bc67baf283fbf524254)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map that contains tag keys and tag values that are attached to the robot application.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edcc90e709ec9cc68d63a3735570140617851fcd19e7a37393d2056e644b8f64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_robomaker.CfnRobotApplication.RobotSoftwareSuiteProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "version": "version"},
    )
    class RobotSoftwareSuiteProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about a robot software suite.

            :param name: The name of the robot software suite. ``General`` is the only supported value.
            :param version: The version of the robot software suite. Not applicable for General software suite.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-robotsoftwaresuite.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_robomaker as robomaker
                
                robot_software_suite_property = robomaker.CfnRobotApplication.RobotSoftwareSuiteProperty(
                    name="name",
                
                    # the properties below are optional
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d5f4a9729bdb2de5e225d5dd7073cee6d93bde41ad65d4c7658935ca7308a1d6)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the robot software suite.

            ``General`` is the only supported value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-robotsoftwaresuite.html#cfn-robomaker-robotapplication-robotsoftwaresuite-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The version of the robot software suite.

            Not applicable for General software suite.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-robotsoftwaresuite.html#cfn-robomaker-robotapplication-robotsoftwaresuite-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RobotSoftwareSuiteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_robomaker.CfnRobotApplication.SourceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "architecture": "architecture",
            "s3_bucket": "s3Bucket",
            "s3_key": "s3Key",
        },
    )
    class SourceConfigProperty:
        def __init__(
            self,
            *,
            architecture: builtins.str,
            s3_bucket: builtins.str,
            s3_key: builtins.str,
        ) -> None:
            '''Information about a source configuration.

            :param architecture: The target processor architecture for the application.
            :param s3_bucket: The Amazon S3 bucket name.
            :param s3_key: The s3 object key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-sourceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_robomaker as robomaker
                
                source_config_property = robomaker.CfnRobotApplication.SourceConfigProperty(
                    architecture="architecture",
                    s3_bucket="s3Bucket",
                    s3_key="s3Key"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4e42633c14584fa1496504e90fc71f70fc9e79eb18701f96962e855cd1caf4c0)
                check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
                check_type(argname="argument s3_key", value=s3_key, expected_type=type_hints["s3_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "architecture": architecture,
                "s3_bucket": s3_bucket,
                "s3_key": s3_key,
            }

        @builtins.property
        def architecture(self) -> builtins.str:
            '''The target processor architecture for the application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-sourceconfig.html#cfn-robomaker-robotapplication-sourceconfig-architecture
            '''
            result = self._values.get("architecture")
            assert result is not None, "Required property 'architecture' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''The Amazon S3 bucket name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-sourceconfig.html#cfn-robomaker-robotapplication-sourceconfig-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_key(self) -> builtins.str:
            '''The s3 object key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-robotapplication-sourceconfig.html#cfn-robomaker-robotapplication-sourceconfig-s3key
            '''
            result = self._values.get("s3_key")
            assert result is not None, "Required property 's3_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_robomaker.CfnRobotApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "robot_software_suite": "robotSoftwareSuite",
        "current_revision_id": "currentRevisionId",
        "environment": "environment",
        "name": "name",
        "sources": "sources",
        "tags": "tags",
    },
)
class CfnRobotApplicationProps:
    def __init__(
        self,
        *,
        robot_software_suite: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRobotApplication.RobotSoftwareSuiteProperty, typing.Dict[builtins.str, typing.Any]]],
        current_revision_id: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRobotApplication.SourceConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRobotApplication``.

        :param robot_software_suite: The robot software suite used by the robot application.
        :param current_revision_id: The current revision id.
        :param environment: The environment of the robot application.
        :param name: The name of the robot application.
        :param sources: The sources of the robot application.
        :param tags: A map that contains tag keys and tag values that are attached to the robot application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_robomaker as robomaker
            
            cfn_robot_application_props = robomaker.CfnRobotApplicationProps(
                robot_software_suite=robomaker.CfnRobotApplication.RobotSoftwareSuiteProperty(
                    name="name",
            
                    # the properties below are optional
                    version="version"
                ),
            
                # the properties below are optional
                current_revision_id="currentRevisionId",
                environment="environment",
                name="name",
                sources=[robomaker.CfnRobotApplication.SourceConfigProperty(
                    architecture="architecture",
                    s3_bucket="s3Bucket",
                    s3_key="s3Key"
                )],
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52a4130d82e25da60f30538ac27bda30b72380a78b4ec426daeb7a4e2863826c)
            check_type(argname="argument robot_software_suite", value=robot_software_suite, expected_type=type_hints["robot_software_suite"])
            check_type(argname="argument current_revision_id", value=current_revision_id, expected_type=type_hints["current_revision_id"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "robot_software_suite": robot_software_suite,
        }
        if current_revision_id is not None:
            self._values["current_revision_id"] = current_revision_id
        if environment is not None:
            self._values["environment"] = environment
        if name is not None:
            self._values["name"] = name
        if sources is not None:
            self._values["sources"] = sources
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def robot_software_suite(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnRobotApplication.RobotSoftwareSuiteProperty]:
        '''The robot software suite used by the robot application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-robotsoftwaresuite
        '''
        result = self._values.get("robot_software_suite")
        assert result is not None, "Required property 'robot_software_suite' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnRobotApplication.RobotSoftwareSuiteProperty], result)

    @builtins.property
    def current_revision_id(self) -> typing.Optional[builtins.str]:
        '''The current revision id.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-currentrevisionid
        '''
        result = self._values.get("current_revision_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(self) -> typing.Optional[builtins.str]:
        '''The environment of the robot application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-environment
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the robot application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRobotApplication.SourceConfigProperty]]]]:
        '''The sources of the robot application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-sources
        '''
        result = self._values.get("sources")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRobotApplication.SourceConfigProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map that contains tag keys and tag values that are attached to the robot application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html#cfn-robomaker-robotapplication-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRobotApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnRobotApplicationVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_robomaker.CfnRobotApplicationVersion",
):
    '''The ``AWS::RoboMaker::RobotApplicationVersion`` resource creates an AWS RoboMaker robot version.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplicationversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_robomaker as robomaker
        
        cfn_robot_application_version = robomaker.CfnRobotApplicationVersion(self, "MyCfnRobotApplicationVersion",
            application="application",
        
            # the properties below are optional
            current_revision_id="currentRevisionId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application: builtins.str,
        current_revision_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application: The application information for the robot application.
        :param current_revision_id: The current revision id for the robot application. If you provide a value and it matches the latest revision ID, a new version will be created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcd53a9dcf33d743031271af0ba72420a6333fce186b7796423fce7cf2a11edd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRobotApplicationVersionProps(
            application=application, current_revision_id=current_revision_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f118e60d84017d23b3757c090962ce180837d00a2391556fe9327256ecdf94ed)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7da9089e8e01d3ff2ab5341d8a934fa39bd9fa51321b5b272c94e36ae7a45d5c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationVersion")
    def attr_application_version(self) -> builtins.str:
        '''The robot application version.

        :cloudformationAttribute: ApplicationVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the robot application version.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> builtins.str:
        '''The application information for the robot application.'''
        return typing.cast(builtins.str, jsii.get(self, "application"))

    @application.setter
    def application(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d3b0a1f324aaccd7abc5e6810329e257f4a7cd3179c5afcaf2b8abd6f7990af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "application", value)

    @builtins.property
    @jsii.member(jsii_name="currentRevisionId")
    def current_revision_id(self) -> typing.Optional[builtins.str]:
        '''The current revision id for the robot application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "currentRevisionId"))

    @current_revision_id.setter
    def current_revision_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a12b8570cf31b8187dcb0dd326c52f7ca4075a70971d81e139f25383d48acad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "currentRevisionId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_robomaker.CfnRobotApplicationVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "application": "application",
        "current_revision_id": "currentRevisionId",
    },
)
class CfnRobotApplicationVersionProps:
    def __init__(
        self,
        *,
        application: builtins.str,
        current_revision_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnRobotApplicationVersion``.

        :param application: The application information for the robot application.
        :param current_revision_id: The current revision id for the robot application. If you provide a value and it matches the latest revision ID, a new version will be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplicationversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_robomaker as robomaker
            
            cfn_robot_application_version_props = robomaker.CfnRobotApplicationVersionProps(
                application="application",
            
                # the properties below are optional
                current_revision_id="currentRevisionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ac07a372688198f4d1e1276b33a860cf9f2a1a35ffcb9183bd7e8544e85528a)
            check_type(argname="argument application", value=application, expected_type=type_hints["application"])
            check_type(argname="argument current_revision_id", value=current_revision_id, expected_type=type_hints["current_revision_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application": application,
        }
        if current_revision_id is not None:
            self._values["current_revision_id"] = current_revision_id

    @builtins.property
    def application(self) -> builtins.str:
        '''The application information for the robot application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplicationversion.html#cfn-robomaker-robotapplicationversion-application
        '''
        result = self._values.get("application")
        assert result is not None, "Required property 'application' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def current_revision_id(self) -> typing.Optional[builtins.str]:
        '''The current revision id for the robot application.

        If you provide a value and it matches the latest revision ID, a new version will be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplicationversion.html#cfn-robomaker-robotapplicationversion-currentrevisionid
        '''
        result = self._values.get("current_revision_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRobotApplicationVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_robomaker.CfnRobotProps",
    jsii_struct_bases=[],
    name_mapping={
        "architecture": "architecture",
        "greengrass_group_id": "greengrassGroupId",
        "fleet": "fleet",
        "name": "name",
        "tags": "tags",
    },
)
class CfnRobotProps:
    def __init__(
        self,
        *,
        architecture: builtins.str,
        greengrass_group_id: builtins.str,
        fleet: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRobot``.

        :param architecture: The architecture of the robot.
        :param greengrass_group_id: The Greengrass group associated with the robot.
        :param fleet: The Amazon Resource Name (ARN) of the fleet to which the robot will be registered.
        :param name: The name of the robot.
        :param tags: A map that contains tag keys and tag values that are attached to the robot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_robomaker as robomaker
            
            cfn_robot_props = robomaker.CfnRobotProps(
                architecture="architecture",
                greengrass_group_id="greengrassGroupId",
            
                # the properties below are optional
                fleet="fleet",
                name="name",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb8dba61a5cbbdf07aaff4068a7feeb8d793259512cbf888a9f053970335df52)
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument greengrass_group_id", value=greengrass_group_id, expected_type=type_hints["greengrass_group_id"])
            check_type(argname="argument fleet", value=fleet, expected_type=type_hints["fleet"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "architecture": architecture,
            "greengrass_group_id": greengrass_group_id,
        }
        if fleet is not None:
            self._values["fleet"] = fleet
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def architecture(self) -> builtins.str:
        '''The architecture of the robot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html#cfn-robomaker-robot-architecture
        '''
        result = self._values.get("architecture")
        assert result is not None, "Required property 'architecture' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def greengrass_group_id(self) -> builtins.str:
        '''The Greengrass group associated with the robot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html#cfn-robomaker-robot-greengrassgroupid
        '''
        result = self._values.get("greengrass_group_id")
        assert result is not None, "Required property 'greengrass_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fleet(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the fleet to which the robot will be registered.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html#cfn-robomaker-robot-fleet
        '''
        result = self._values.get("fleet")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the robot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html#cfn-robomaker-robot-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map that contains tag keys and tag values that are attached to the robot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html#cfn-robomaker-robot-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRobotProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSimulationApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_robomaker.CfnSimulationApplication",
):
    '''The ``AWS::RoboMaker::SimulationApplication`` resource creates an AWS RoboMaker simulation application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_robomaker as robomaker
        
        cfn_simulation_application = robomaker.CfnSimulationApplication(self, "MyCfnSimulationApplication",
            robot_software_suite=robomaker.CfnSimulationApplication.RobotSoftwareSuiteProperty(
                name="name",
        
                # the properties below are optional
                version="version"
            ),
            simulation_software_suite=robomaker.CfnSimulationApplication.SimulationSoftwareSuiteProperty(
                name="name",
        
                # the properties below are optional
                version="version"
            ),
        
            # the properties below are optional
            current_revision_id="currentRevisionId",
            environment="environment",
            name="name",
            rendering_engine=robomaker.CfnSimulationApplication.RenderingEngineProperty(
                name="name",
                version="version"
            ),
            sources=[robomaker.CfnSimulationApplication.SourceConfigProperty(
                architecture="architecture",
                s3_bucket="s3Bucket",
                s3_key="s3Key"
            )],
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        robot_software_suite: typing.Union[_IResolvable_da3f097b, typing.Union["CfnSimulationApplication.RobotSoftwareSuiteProperty", typing.Dict[builtins.str, typing.Any]]],
        simulation_software_suite: typing.Union[_IResolvable_da3f097b, typing.Union["CfnSimulationApplication.SimulationSoftwareSuiteProperty", typing.Dict[builtins.str, typing.Any]]],
        current_revision_id: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        rendering_engine: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSimulationApplication.RenderingEngineProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSimulationApplication.SourceConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param robot_software_suite: The robot software suite used by the simulation application.
        :param simulation_software_suite: The simulation software suite used by the simulation application.
        :param current_revision_id: The current revision id.
        :param environment: The environment of the simulation application.
        :param name: The name of the simulation application.
        :param rendering_engine: The rendering engine for the simulation application.
        :param sources: The sources of the simulation application.
        :param tags: A map that contains tag keys and tag values that are attached to the simulation application.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__114d0219b7d523418f9fb7d4285a959f76159ce8240b820cfc0b5539281cab1b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSimulationApplicationProps(
            robot_software_suite=robot_software_suite,
            simulation_software_suite=simulation_software_suite,
            current_revision_id=current_revision_id,
            environment=environment,
            name=name,
            rendering_engine=rendering_engine,
            sources=sources,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b07bcabc30b161a3b27df47d8e7cf734f9002a200932fd1c1777c3f3ef03939b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad67c7d83c9fcbd3cf4c7511d49a2bd7f2c52ed6ce1dc68063ded3b42c6bbb6b)
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
        '''The Amazon Resource Name (ARN) of the simulation application.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCurrentRevisionId")
    def attr_current_revision_id(self) -> builtins.str:
        '''The current revision id.

        :cloudformationAttribute: CurrentRevisionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCurrentRevisionId"))

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
    @jsii.member(jsii_name="robotSoftwareSuite")
    def robot_software_suite(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnSimulationApplication.RobotSoftwareSuiteProperty"]:
        '''The robot software suite used by the simulation application.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnSimulationApplication.RobotSoftwareSuiteProperty"], jsii.get(self, "robotSoftwareSuite"))

    @robot_software_suite.setter
    def robot_software_suite(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnSimulationApplication.RobotSoftwareSuiteProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5eddba1cd6f8159da95d199756aece7189ac992724326ee1649fe22981dd1e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "robotSoftwareSuite", value)

    @builtins.property
    @jsii.member(jsii_name="simulationSoftwareSuite")
    def simulation_software_suite(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnSimulationApplication.SimulationSoftwareSuiteProperty"]:
        '''The simulation software suite used by the simulation application.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnSimulationApplication.SimulationSoftwareSuiteProperty"], jsii.get(self, "simulationSoftwareSuite"))

    @simulation_software_suite.setter
    def simulation_software_suite(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnSimulationApplication.SimulationSoftwareSuiteProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__003dd21a203873e85f6980fecd86a94b0531507d8242c4a61748ccddd022255b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "simulationSoftwareSuite", value)

    @builtins.property
    @jsii.member(jsii_name="currentRevisionId")
    def current_revision_id(self) -> typing.Optional[builtins.str]:
        '''The current revision id.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "currentRevisionId"))

    @current_revision_id.setter
    def current_revision_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__068a8613a5e63c82ab19c78d5802a5b6611d12defd9ede2d2533997b03d365e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "currentRevisionId", value)

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> typing.Optional[builtins.str]:
        '''The environment of the simulation application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environment"))

    @environment.setter
    def environment(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69efbbc8b0b296d56da5d877f246f08f0fb859b0450a0b5284f1318fae1eca2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the simulation application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c61e246fbb83f216937d12b47511a45dd9e3bbb9db8340e1bc7fc1b0134da507)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="renderingEngine")
    def rendering_engine(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimulationApplication.RenderingEngineProperty"]]:
        '''The rendering engine for the simulation application.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimulationApplication.RenderingEngineProperty"]], jsii.get(self, "renderingEngine"))

    @rendering_engine.setter
    def rendering_engine(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimulationApplication.RenderingEngineProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c52139e81e980013fe63c79055c9c5a430c7b60d4f73dab46a912bb62fccda4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renderingEngine", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSimulationApplication.SourceConfigProperty"]]]]:
        '''The sources of the simulation application.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSimulationApplication.SourceConfigProperty"]]]], jsii.get(self, "sources"))

    @sources.setter
    def sources(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSimulationApplication.SourceConfigProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__351059f5bb1169ead5062e07e9d73fd8ac37f0cbad54a1d4e8e137cf716e9fae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map that contains tag keys and tag values that are attached to the simulation application.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf0913d8e33389ea9f4a231680314b73532bf04cbe505a502315b25accf25846)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_robomaker.CfnSimulationApplication.RenderingEngineProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "version": "version"},
    )
    class RenderingEngineProperty:
        def __init__(self, *, name: builtins.str, version: builtins.str) -> None:
            '''Information about a rendering engine.

            :param name: The name of the rendering engine.
            :param version: The version of the rendering engine.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-renderingengine.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_robomaker as robomaker
                
                rendering_engine_property = robomaker.CfnSimulationApplication.RenderingEngineProperty(
                    name="name",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2863a3bc28feec06755c7b41ee081ad65e91ff48f9cf3a5d86d2f922abd3f95e)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "version": version,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the rendering engine.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-renderingengine.html#cfn-robomaker-simulationapplication-renderingengine-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> builtins.str:
            '''The version of the rendering engine.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-renderingengine.html#cfn-robomaker-simulationapplication-renderingengine-version
            '''
            result = self._values.get("version")
            assert result is not None, "Required property 'version' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RenderingEngineProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_robomaker.CfnSimulationApplication.RobotSoftwareSuiteProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "version": "version"},
    )
    class RobotSoftwareSuiteProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about a robot software suite.

            :param name: The name of the robot software suite. ``General`` is the only supported value.
            :param version: The version of the robot software suite. Not applicable for General software suite.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-robotsoftwaresuite.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_robomaker as robomaker
                
                robot_software_suite_property = robomaker.CfnSimulationApplication.RobotSoftwareSuiteProperty(
                    name="name",
                
                    # the properties below are optional
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6c7cb9f4548e568c687370645ce34e3fd9ab505e3e7033e502d4e523d4d36e54)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the robot software suite.

            ``General`` is the only supported value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-robotsoftwaresuite.html#cfn-robomaker-simulationapplication-robotsoftwaresuite-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The version of the robot software suite.

            Not applicable for General software suite.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-robotsoftwaresuite.html#cfn-robomaker-simulationapplication-robotsoftwaresuite-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RobotSoftwareSuiteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_robomaker.CfnSimulationApplication.SimulationSoftwareSuiteProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "version": "version"},
    )
    class SimulationSoftwareSuiteProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about a simulation software suite.

            :param name: The name of the simulation software suite. ``SimulationRuntime`` is the only supported value.
            :param version: The version of the simulation software suite. Not applicable for ``SimulationRuntime`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-simulationsoftwaresuite.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_robomaker as robomaker
                
                simulation_software_suite_property = robomaker.CfnSimulationApplication.SimulationSoftwareSuiteProperty(
                    name="name",
                
                    # the properties below are optional
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__42d44db48959e7b025183126f780f02ee10acdabda8e42593c0b8a1f0fe622a1)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the simulation software suite.

            ``SimulationRuntime`` is the only supported value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-simulationsoftwaresuite.html#cfn-robomaker-simulationapplication-simulationsoftwaresuite-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The version of the simulation software suite.

            Not applicable for ``SimulationRuntime`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-simulationsoftwaresuite.html#cfn-robomaker-simulationapplication-simulationsoftwaresuite-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SimulationSoftwareSuiteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_robomaker.CfnSimulationApplication.SourceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "architecture": "architecture",
            "s3_bucket": "s3Bucket",
            "s3_key": "s3Key",
        },
    )
    class SourceConfigProperty:
        def __init__(
            self,
            *,
            architecture: builtins.str,
            s3_bucket: builtins.str,
            s3_key: builtins.str,
        ) -> None:
            '''Information about a source configuration.

            :param architecture: The target processor architecture for the application.
            :param s3_bucket: The Amazon S3 bucket name.
            :param s3_key: The s3 object key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-sourceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_robomaker as robomaker
                
                source_config_property = robomaker.CfnSimulationApplication.SourceConfigProperty(
                    architecture="architecture",
                    s3_bucket="s3Bucket",
                    s3_key="s3Key"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4112adca6d32fda1641015d764412ce99d316d904ecd3983541c923ad04c55b8)
                check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
                check_type(argname="argument s3_key", value=s3_key, expected_type=type_hints["s3_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "architecture": architecture,
                "s3_bucket": s3_bucket,
                "s3_key": s3_key,
            }

        @builtins.property
        def architecture(self) -> builtins.str:
            '''The target processor architecture for the application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-sourceconfig.html#cfn-robomaker-simulationapplication-sourceconfig-architecture
            '''
            result = self._values.get("architecture")
            assert result is not None, "Required property 'architecture' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''The Amazon S3 bucket name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-sourceconfig.html#cfn-robomaker-simulationapplication-sourceconfig-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_key(self) -> builtins.str:
            '''The s3 object key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-robomaker-simulationapplication-sourceconfig.html#cfn-robomaker-simulationapplication-sourceconfig-s3key
            '''
            result = self._values.get("s3_key")
            assert result is not None, "Required property 's3_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_robomaker.CfnSimulationApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "robot_software_suite": "robotSoftwareSuite",
        "simulation_software_suite": "simulationSoftwareSuite",
        "current_revision_id": "currentRevisionId",
        "environment": "environment",
        "name": "name",
        "rendering_engine": "renderingEngine",
        "sources": "sources",
        "tags": "tags",
    },
)
class CfnSimulationApplicationProps:
    def __init__(
        self,
        *,
        robot_software_suite: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulationApplication.RobotSoftwareSuiteProperty, typing.Dict[builtins.str, typing.Any]]],
        simulation_software_suite: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulationApplication.SimulationSoftwareSuiteProperty, typing.Dict[builtins.str, typing.Any]]],
        current_revision_id: typing.Optional[builtins.str] = None,
        environment: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        rendering_engine: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulationApplication.RenderingEngineProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulationApplication.SourceConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSimulationApplication``.

        :param robot_software_suite: The robot software suite used by the simulation application.
        :param simulation_software_suite: The simulation software suite used by the simulation application.
        :param current_revision_id: The current revision id.
        :param environment: The environment of the simulation application.
        :param name: The name of the simulation application.
        :param rendering_engine: The rendering engine for the simulation application.
        :param sources: The sources of the simulation application.
        :param tags: A map that contains tag keys and tag values that are attached to the simulation application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_robomaker as robomaker
            
            cfn_simulation_application_props = robomaker.CfnSimulationApplicationProps(
                robot_software_suite=robomaker.CfnSimulationApplication.RobotSoftwareSuiteProperty(
                    name="name",
            
                    # the properties below are optional
                    version="version"
                ),
                simulation_software_suite=robomaker.CfnSimulationApplication.SimulationSoftwareSuiteProperty(
                    name="name",
            
                    # the properties below are optional
                    version="version"
                ),
            
                # the properties below are optional
                current_revision_id="currentRevisionId",
                environment="environment",
                name="name",
                rendering_engine=robomaker.CfnSimulationApplication.RenderingEngineProperty(
                    name="name",
                    version="version"
                ),
                sources=[robomaker.CfnSimulationApplication.SourceConfigProperty(
                    architecture="architecture",
                    s3_bucket="s3Bucket",
                    s3_key="s3Key"
                )],
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4fc5092e924ca6ac9045b6bf857cc7c5e8af28f105a1752b871bed705eac2ca)
            check_type(argname="argument robot_software_suite", value=robot_software_suite, expected_type=type_hints["robot_software_suite"])
            check_type(argname="argument simulation_software_suite", value=simulation_software_suite, expected_type=type_hints["simulation_software_suite"])
            check_type(argname="argument current_revision_id", value=current_revision_id, expected_type=type_hints["current_revision_id"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rendering_engine", value=rendering_engine, expected_type=type_hints["rendering_engine"])
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "robot_software_suite": robot_software_suite,
            "simulation_software_suite": simulation_software_suite,
        }
        if current_revision_id is not None:
            self._values["current_revision_id"] = current_revision_id
        if environment is not None:
            self._values["environment"] = environment
        if name is not None:
            self._values["name"] = name
        if rendering_engine is not None:
            self._values["rendering_engine"] = rendering_engine
        if sources is not None:
            self._values["sources"] = sources
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def robot_software_suite(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnSimulationApplication.RobotSoftwareSuiteProperty]:
        '''The robot software suite used by the simulation application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-robotsoftwaresuite
        '''
        result = self._values.get("robot_software_suite")
        assert result is not None, "Required property 'robot_software_suite' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnSimulationApplication.RobotSoftwareSuiteProperty], result)

    @builtins.property
    def simulation_software_suite(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnSimulationApplication.SimulationSoftwareSuiteProperty]:
        '''The simulation software suite used by the simulation application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-simulationsoftwaresuite
        '''
        result = self._values.get("simulation_software_suite")
        assert result is not None, "Required property 'simulation_software_suite' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnSimulationApplication.SimulationSoftwareSuiteProperty], result)

    @builtins.property
    def current_revision_id(self) -> typing.Optional[builtins.str]:
        '''The current revision id.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-currentrevisionid
        '''
        result = self._values.get("current_revision_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(self) -> typing.Optional[builtins.str]:
        '''The environment of the simulation application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-environment
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the simulation application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rendering_engine(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimulationApplication.RenderingEngineProperty]]:
        '''The rendering engine for the simulation application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-renderingengine
        '''
        result = self._values.get("rendering_engine")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimulationApplication.RenderingEngineProperty]], result)

    @builtins.property
    def sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSimulationApplication.SourceConfigProperty]]]]:
        '''The sources of the simulation application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-sources
        '''
        result = self._values.get("sources")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSimulationApplication.SourceConfigProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map that contains tag keys and tag values that are attached to the simulation application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html#cfn-robomaker-simulationapplication-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSimulationApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSimulationApplicationVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_robomaker.CfnSimulationApplicationVersion",
):
    '''The ``AWS::RoboMaker::SimulationApplicationVersion`` resource creates a version of an AWS RoboMaker simulation application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplicationversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_robomaker as robomaker
        
        cfn_simulation_application_version = robomaker.CfnSimulationApplicationVersion(self, "MyCfnSimulationApplicationVersion",
            application="application",
        
            # the properties below are optional
            current_revision_id="currentRevisionId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application: builtins.str,
        current_revision_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application: The application information for the simulation application.
        :param current_revision_id: The current revision id for the simulation application. If you provide a value and it matches the latest revision ID, a new version will be created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b488a5e64a5298aa8517c15f71537daeb5f5871632b79431660409e31044cdbc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSimulationApplicationVersionProps(
            application=application, current_revision_id=current_revision_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ead7db1870da4a55103971c097c2a0d658c0d64ba83064ca8e31b5e901ad912)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd075a23d16770c89bb7c07707cebfaee1999ac239256aecc881a91f2c392efc)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationVersion")
    def attr_application_version(self) -> builtins.str:
        '''The simulation application version.

        :cloudformationAttribute: ApplicationVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the simulation application version.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> builtins.str:
        '''The application information for the simulation application.'''
        return typing.cast(builtins.str, jsii.get(self, "application"))

    @application.setter
    def application(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9b594cec8275a90b1fc93b7ade9da7c6565f24e659e6aed511135526226f540)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "application", value)

    @builtins.property
    @jsii.member(jsii_name="currentRevisionId")
    def current_revision_id(self) -> typing.Optional[builtins.str]:
        '''The current revision id for the simulation application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "currentRevisionId"))

    @current_revision_id.setter
    def current_revision_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4436c869d1e97db1310a07c8709c1c39527703571128932c8cdb4b5bea7f3ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "currentRevisionId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_robomaker.CfnSimulationApplicationVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "application": "application",
        "current_revision_id": "currentRevisionId",
    },
)
class CfnSimulationApplicationVersionProps:
    def __init__(
        self,
        *,
        application: builtins.str,
        current_revision_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSimulationApplicationVersion``.

        :param application: The application information for the simulation application.
        :param current_revision_id: The current revision id for the simulation application. If you provide a value and it matches the latest revision ID, a new version will be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplicationversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_robomaker as robomaker
            
            cfn_simulation_application_version_props = robomaker.CfnSimulationApplicationVersionProps(
                application="application",
            
                # the properties below are optional
                current_revision_id="currentRevisionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33d944589c147bd94eb24d591728491c11d414786b189bb1a955add8599bfacf)
            check_type(argname="argument application", value=application, expected_type=type_hints["application"])
            check_type(argname="argument current_revision_id", value=current_revision_id, expected_type=type_hints["current_revision_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application": application,
        }
        if current_revision_id is not None:
            self._values["current_revision_id"] = current_revision_id

    @builtins.property
    def application(self) -> builtins.str:
        '''The application information for the simulation application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplicationversion.html#cfn-robomaker-simulationapplicationversion-application
        '''
        result = self._values.get("application")
        assert result is not None, "Required property 'application' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def current_revision_id(self) -> typing.Optional[builtins.str]:
        '''The current revision id for the simulation application.

        If you provide a value and it matches the latest revision ID, a new version will be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplicationversion.html#cfn-robomaker-simulationapplicationversion-currentrevisionid
        '''
        result = self._values.get("current_revision_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSimulationApplicationVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnFleet",
    "CfnFleetProps",
    "CfnRobot",
    "CfnRobotApplication",
    "CfnRobotApplicationProps",
    "CfnRobotApplicationVersion",
    "CfnRobotApplicationVersionProps",
    "CfnRobotProps",
    "CfnSimulationApplication",
    "CfnSimulationApplicationProps",
    "CfnSimulationApplicationVersion",
    "CfnSimulationApplicationVersionProps",
]

publication.publish()

def _typecheckingstub__4cf67028db50fbc82ea8f4501fdb4ee36d1ed66bd90e1e13e635239c75a407a8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79e824f817a2c25a6f542667057e9a4525e47750a2d9bc44f093375b07e8d178(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__195f1c8f4daafc0d71dbb26762ed99292b6f283831024397d9845964e6edd9c6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb2b0f115fd155ec1867ebdfab524eabaa919c39920655bedef657815f3fe35b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4a9d74f73ceaf3ae033517a44602efdc6fd84668be6992907ba5276fd26df0c(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5c8fc3b81304b565bf3da303dec523f47216f807e13ba1e0ddcc46ceb848df8(
    *,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49131f852e25508f2191103f967b740a3a43d115f73e1b3a287cc2e4a396694f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    architecture: builtins.str,
    greengrass_group_id: builtins.str,
    fleet: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__712f9da34bf6ddea1b6cd2b92a14c93de456aa09838fcb1df12120caab354dc4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__708276af184c2e226238ae52977a6357dc19766ae0a17f9abee37238a2200248(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f36dbab08fea8dace0765ee7ba8b7d3ff9ee4c48d947b5303f3631f8a0369b5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50de460acfd3a8dbfb6259513c1df0e835e46e80422bd7d50197066f46adcf42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8da9d8bd6e5845fb5ae85a5c0ecb127eb3120f33b979743f160cc5912ff26766(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db28cc7abf10f25ceb48539af3bff17364e26eb389639b29457ab05b7d152425(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__197f65220e7c1b22bb2750ecd4cf89b82125f1abad27a9e9cc4881b988b6ba6d(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71fa9826def616b855a7d14f7c7a68432b3206eba76bd02b308db61a08332bc3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    robot_software_suite: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRobotApplication.RobotSoftwareSuiteProperty, typing.Dict[builtins.str, typing.Any]]],
    current_revision_id: typing.Optional[builtins.str] = None,
    environment: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRobotApplication.SourceConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42dcfe9a23f9087a5360cc6bd5cc1baa70c7249dcef1085237c5953641683f2b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ffda1b22518fe7e5746795534fa3f401eb6e2cd22e88b8c529a08a6830ac889(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a0183b45e0172b50d6049b802258f5f54543ee36f6ff14d04a41472f312ff04(
    value: typing.Union[_IResolvable_da3f097b, CfnRobotApplication.RobotSoftwareSuiteProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a68af59eeb167d0c020946ad9c700418dc6f280bb64690a231f2609770e55ce2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8346429cd042f143075e82bff1b46a5acd3b5c22740614aae1093279051fdea9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69012b559357369e35caab49e8a89325e4bc8994f10edb7261ac37badc83f089(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__921f41fab15ec19f628942a860f0c537326ffdf47bee9bc67baf283fbf524254(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRobotApplication.SourceConfigProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edcc90e709ec9cc68d63a3735570140617851fcd19e7a37393d2056e644b8f64(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5f4a9729bdb2de5e225d5dd7073cee6d93bde41ad65d4c7658935ca7308a1d6(
    *,
    name: builtins.str,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e42633c14584fa1496504e90fc71f70fc9e79eb18701f96962e855cd1caf4c0(
    *,
    architecture: builtins.str,
    s3_bucket: builtins.str,
    s3_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52a4130d82e25da60f30538ac27bda30b72380a78b4ec426daeb7a4e2863826c(
    *,
    robot_software_suite: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRobotApplication.RobotSoftwareSuiteProperty, typing.Dict[builtins.str, typing.Any]]],
    current_revision_id: typing.Optional[builtins.str] = None,
    environment: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRobotApplication.SourceConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcd53a9dcf33d743031271af0ba72420a6333fce186b7796423fce7cf2a11edd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application: builtins.str,
    current_revision_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f118e60d84017d23b3757c090962ce180837d00a2391556fe9327256ecdf94ed(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7da9089e8e01d3ff2ab5341d8a934fa39bd9fa51321b5b272c94e36ae7a45d5c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3b0a1f324aaccd7abc5e6810329e257f4a7cd3179c5afcaf2b8abd6f7990af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a12b8570cf31b8187dcb0dd326c52f7ca4075a70971d81e139f25383d48acad(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ac07a372688198f4d1e1276b33a860cf9f2a1a35ffcb9183bd7e8544e85528a(
    *,
    application: builtins.str,
    current_revision_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb8dba61a5cbbdf07aaff4068a7feeb8d793259512cbf888a9f053970335df52(
    *,
    architecture: builtins.str,
    greengrass_group_id: builtins.str,
    fleet: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__114d0219b7d523418f9fb7d4285a959f76159ce8240b820cfc0b5539281cab1b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    robot_software_suite: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulationApplication.RobotSoftwareSuiteProperty, typing.Dict[builtins.str, typing.Any]]],
    simulation_software_suite: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulationApplication.SimulationSoftwareSuiteProperty, typing.Dict[builtins.str, typing.Any]]],
    current_revision_id: typing.Optional[builtins.str] = None,
    environment: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    rendering_engine: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulationApplication.RenderingEngineProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulationApplication.SourceConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b07bcabc30b161a3b27df47d8e7cf734f9002a200932fd1c1777c3f3ef03939b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad67c7d83c9fcbd3cf4c7511d49a2bd7f2c52ed6ce1dc68063ded3b42c6bbb6b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5eddba1cd6f8159da95d199756aece7189ac992724326ee1649fe22981dd1e0(
    value: typing.Union[_IResolvable_da3f097b, CfnSimulationApplication.RobotSoftwareSuiteProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__003dd21a203873e85f6980fecd86a94b0531507d8242c4a61748ccddd022255b(
    value: typing.Union[_IResolvable_da3f097b, CfnSimulationApplication.SimulationSoftwareSuiteProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__068a8613a5e63c82ab19c78d5802a5b6611d12defd9ede2d2533997b03d365e9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69efbbc8b0b296d56da5d877f246f08f0fb859b0450a0b5284f1318fae1eca2c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c61e246fbb83f216937d12b47511a45dd9e3bbb9db8340e1bc7fc1b0134da507(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c52139e81e980013fe63c79055c9c5a430c7b60d4f73dab46a912bb62fccda4f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimulationApplication.RenderingEngineProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__351059f5bb1169ead5062e07e9d73fd8ac37f0cbad54a1d4e8e137cf716e9fae(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSimulationApplication.SourceConfigProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf0913d8e33389ea9f4a231680314b73532bf04cbe505a502315b25accf25846(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2863a3bc28feec06755c7b41ee081ad65e91ff48f9cf3a5d86d2f922abd3f95e(
    *,
    name: builtins.str,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c7cb9f4548e568c687370645ce34e3fd9ab505e3e7033e502d4e523d4d36e54(
    *,
    name: builtins.str,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42d44db48959e7b025183126f780f02ee10acdabda8e42593c0b8a1f0fe622a1(
    *,
    name: builtins.str,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4112adca6d32fda1641015d764412ce99d316d904ecd3983541c923ad04c55b8(
    *,
    architecture: builtins.str,
    s3_bucket: builtins.str,
    s3_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4fc5092e924ca6ac9045b6bf857cc7c5e8af28f105a1752b871bed705eac2ca(
    *,
    robot_software_suite: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulationApplication.RobotSoftwareSuiteProperty, typing.Dict[builtins.str, typing.Any]]],
    simulation_software_suite: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulationApplication.SimulationSoftwareSuiteProperty, typing.Dict[builtins.str, typing.Any]]],
    current_revision_id: typing.Optional[builtins.str] = None,
    environment: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    rendering_engine: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulationApplication.RenderingEngineProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimulationApplication.SourceConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b488a5e64a5298aa8517c15f71537daeb5f5871632b79431660409e31044cdbc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application: builtins.str,
    current_revision_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ead7db1870da4a55103971c097c2a0d658c0d64ba83064ca8e31b5e901ad912(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd075a23d16770c89bb7c07707cebfaee1999ac239256aecc881a91f2c392efc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9b594cec8275a90b1fc93b7ade9da7c6565f24e659e6aed511135526226f540(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4436c869d1e97db1310a07c8709c1c39527703571128932c8cdb4b5bea7f3ec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33d944589c147bd94eb24d591728491c11d414786b189bb1a955add8599bfacf(
    *,
    application: builtins.str,
    current_revision_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
