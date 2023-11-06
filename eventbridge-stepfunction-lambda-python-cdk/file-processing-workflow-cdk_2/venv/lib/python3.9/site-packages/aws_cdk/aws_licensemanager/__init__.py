'''
# AWS::LicenseManager Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_licensemanager as licensemanager
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for LicenseManager construct libraries](https://constructs.dev/search?q=licensemanager)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::LicenseManager resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LicenseManager.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::LicenseManager](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LicenseManager.html).

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
class CfnGrant(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_licensemanager.CfnGrant",
):
    '''Specifies a grant.

    A grant shares the use of license entitlements with specific AWS accounts . For more information, see `Granted licenses <https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html>`_ in the *AWS License Manager User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_licensemanager as licensemanager
        
        cfn_grant = licensemanager.CfnGrant(self, "MyCfnGrant",
            allowed_operations=["allowedOperations"],
            grant_name="grantName",
            home_region="homeRegion",
            license_arn="licenseArn",
            principals=["principals"],
            status="status"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        allowed_operations: typing.Optional[typing.Sequence[builtins.str]] = None,
        grant_name: typing.Optional[builtins.str] = None,
        home_region: typing.Optional[builtins.str] = None,
        license_arn: typing.Optional[builtins.str] = None,
        principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param allowed_operations: Allowed operations for the grant.
        :param grant_name: Grant name.
        :param home_region: Home Region of the grant.
        :param license_arn: License ARN.
        :param principals: The grant principals. You can specify one of the following as an Amazon Resource Name (ARN):. - An AWS account, which includes only the account specified. - An organizational unit (OU), which includes all accounts in the OU. - An organization, which will include all accounts across your organization.
        :param status: Granted license status.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8429ee81c009103dd15c76170dfb52e5ca38f72a8912b82d6e63e3f460c3022)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGrantProps(
            allowed_operations=allowed_operations,
            grant_name=grant_name,
            home_region=home_region,
            license_arn=license_arn,
            principals=principals,
            status=status,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06f3d843a99f00dd40b93f69a334bda31af66745c91ef0da13aef948b5e7cd3b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f21921653469c34829dafde09a61b6573c5caa1cd6413329ac50f150c61edce)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrGrantArn")
    def attr_grant_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the grant.

        :cloudformationAttribute: GrantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGrantArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVersion")
    def attr_version(self) -> builtins.str:
        '''The grant version.

        :cloudformationAttribute: Version
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersion"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="allowedOperations")
    def allowed_operations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Allowed operations for the grant.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOperations"))

    @allowed_operations.setter
    def allowed_operations(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0365c0a6e5122b9fa8e724dcae1d11a86ea3be7b9c43576ae3984046a8a866a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOperations", value)

    @builtins.property
    @jsii.member(jsii_name="grantName")
    def grant_name(self) -> typing.Optional[builtins.str]:
        '''Grant name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "grantName"))

    @grant_name.setter
    def grant_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f4a134c7bb2f22cd48211ed5100e65a75fc658d9d8f836ea5c12000691c0cb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grantName", value)

    @builtins.property
    @jsii.member(jsii_name="homeRegion")
    def home_region(self) -> typing.Optional[builtins.str]:
        '''Home Region of the grant.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeRegion"))

    @home_region.setter
    def home_region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5031789a0d9f35bd09ee7810379dcbe0da55436888a38e9623b68c7226da0990)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeRegion", value)

    @builtins.property
    @jsii.member(jsii_name="licenseArn")
    def license_arn(self) -> typing.Optional[builtins.str]:
        '''License ARN.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseArn"))

    @license_arn.setter
    def license_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9ad1871340fca01eaad30a6180a827f5d9f498e7a913dbc15898d39ace8e741)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseArn", value)

    @builtins.property
    @jsii.member(jsii_name="principals")
    def principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The grant principals.

        You can specify one of the following as an Amazon Resource Name (ARN):.
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "principals"))

    @principals.setter
    def principals(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c571a4cf4f9bf1814a1015ca4a37680ca14b1356d42232abd8a71042c1e07bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principals", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''Granted license status.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__979cc3eeb34a65f4beb72557bbf7486f2c8b526da9a872d958b13f140f65edb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_licensemanager.CfnGrantProps",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_operations": "allowedOperations",
        "grant_name": "grantName",
        "home_region": "homeRegion",
        "license_arn": "licenseArn",
        "principals": "principals",
        "status": "status",
    },
)
class CfnGrantProps:
    def __init__(
        self,
        *,
        allowed_operations: typing.Optional[typing.Sequence[builtins.str]] = None,
        grant_name: typing.Optional[builtins.str] = None,
        home_region: typing.Optional[builtins.str] = None,
        license_arn: typing.Optional[builtins.str] = None,
        principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnGrant``.

        :param allowed_operations: Allowed operations for the grant.
        :param grant_name: Grant name.
        :param home_region: Home Region of the grant.
        :param license_arn: License ARN.
        :param principals: The grant principals. You can specify one of the following as an Amazon Resource Name (ARN):. - An AWS account, which includes only the account specified. - An organizational unit (OU), which includes all accounts in the OU. - An organization, which will include all accounts across your organization.
        :param status: Granted license status.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_licensemanager as licensemanager
            
            cfn_grant_props = licensemanager.CfnGrantProps(
                allowed_operations=["allowedOperations"],
                grant_name="grantName",
                home_region="homeRegion",
                license_arn="licenseArn",
                principals=["principals"],
                status="status"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55c62319564e7f4daffb2869290c03b511d6440828cc8d89ddb4e628ea3e0f93)
            check_type(argname="argument allowed_operations", value=allowed_operations, expected_type=type_hints["allowed_operations"])
            check_type(argname="argument grant_name", value=grant_name, expected_type=type_hints["grant_name"])
            check_type(argname="argument home_region", value=home_region, expected_type=type_hints["home_region"])
            check_type(argname="argument license_arn", value=license_arn, expected_type=type_hints["license_arn"])
            check_type(argname="argument principals", value=principals, expected_type=type_hints["principals"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allowed_operations is not None:
            self._values["allowed_operations"] = allowed_operations
        if grant_name is not None:
            self._values["grant_name"] = grant_name
        if home_region is not None:
            self._values["home_region"] = home_region
        if license_arn is not None:
            self._values["license_arn"] = license_arn
        if principals is not None:
            self._values["principals"] = principals
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def allowed_operations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Allowed operations for the grant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-allowedoperations
        '''
        result = self._values.get("allowed_operations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def grant_name(self) -> typing.Optional[builtins.str]:
        '''Grant name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-grantname
        '''
        result = self._values.get("grant_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_region(self) -> typing.Optional[builtins.str]:
        '''Home Region of the grant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-homeregion
        '''
        result = self._values.get("home_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license_arn(self) -> typing.Optional[builtins.str]:
        '''License ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-licensearn
        '''
        result = self._values.get("license_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The grant principals. You can specify one of the following as an Amazon Resource Name (ARN):.

        - An AWS account, which includes only the account specified.
        - An organizational unit (OU), which includes all accounts in the OU.
        - An organization, which will include all accounts across your organization.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-principals
        '''
        result = self._values.get("principals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Granted license status.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-grant.html#cfn-licensemanager-grant-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGrantProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLicense(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense",
):
    '''Specifies a granted license.

    Granted licenses are licenses for products that your organization purchased from AWS Marketplace or directly from a seller who integrated their software with managed entitlements. For more information, see `Granted licenses <https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html>`_ in the *AWS License Manager User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_licensemanager as licensemanager
        
        cfn_license = licensemanager.CfnLicense(self, "MyCfnLicense",
            consumption_configuration=licensemanager.CfnLicense.ConsumptionConfigurationProperty(
                borrow_configuration=licensemanager.CfnLicense.BorrowConfigurationProperty(
                    allow_early_check_in=False,
                    max_time_to_live_in_minutes=123
                ),
                provisional_configuration=licensemanager.CfnLicense.ProvisionalConfigurationProperty(
                    max_time_to_live_in_minutes=123
                ),
                renew_type="renewType"
            ),
            entitlements=[licensemanager.CfnLicense.EntitlementProperty(
                name="name",
                unit="unit",
        
                # the properties below are optional
                allow_check_in=False,
                max_count=123,
                overage=False,
                value="value"
            )],
            home_region="homeRegion",
            issuer=licensemanager.CfnLicense.IssuerDataProperty(
                name="name",
        
                # the properties below are optional
                sign_key="signKey"
            ),
            license_name="licenseName",
            product_name="productName",
            validity=licensemanager.CfnLicense.ValidityDateFormatProperty(
                begin="begin",
                end="end"
            ),
        
            # the properties below are optional
            beneficiary="beneficiary",
            license_metadata=[licensemanager.CfnLicense.MetadataProperty(
                name="name",
                value="value"
            )],
            product_sku="productSku",
            status="status"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        consumption_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLicense.ConsumptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        entitlements: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLicense.EntitlementProperty", typing.Dict[builtins.str, typing.Any]]]]],
        home_region: builtins.str,
        issuer: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLicense.IssuerDataProperty", typing.Dict[builtins.str, typing.Any]]],
        license_name: builtins.str,
        product_name: builtins.str,
        validity: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLicense.ValidityDateFormatProperty", typing.Dict[builtins.str, typing.Any]]],
        beneficiary: typing.Optional[builtins.str] = None,
        license_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLicense.MetadataProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        product_sku: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param consumption_configuration: Configuration for consumption of the license.
        :param entitlements: License entitlements.
        :param home_region: Home Region of the license.
        :param issuer: License issuer.
        :param license_name: License name.
        :param product_name: Product name.
        :param validity: Date and time range during which the license is valid, in ISO8601-UTC format.
        :param beneficiary: License beneficiary.
        :param license_metadata: License metadata.
        :param product_sku: Product SKU.
        :param status: License status.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fa5716b8b0216bdd1da1f12239ad6038aa037294da7f4a1f0215f1b16622526)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLicenseProps(
            consumption_configuration=consumption_configuration,
            entitlements=entitlements,
            home_region=home_region,
            issuer=issuer,
            license_name=license_name,
            product_name=product_name,
            validity=validity,
            beneficiary=beneficiary,
            license_metadata=license_metadata,
            product_sku=product_sku,
            status=status,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9cd2d3dab3901b09367da6f6bc033c9f014286742aa8f85c2c7a6834c1b1512)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5b3e1a3ed6019a3b4d49c9c0479889cc544e9ecc5ed6f1e04e62407fc3377a9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLicenseArn")
    def attr_license_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the license.

        :cloudformationAttribute: LicenseArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLicenseArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVersion")
    def attr_version(self) -> builtins.str:
        '''The license version.

        :cloudformationAttribute: Version
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersion"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="consumptionConfiguration")
    def consumption_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnLicense.ConsumptionConfigurationProperty"]:
        '''Configuration for consumption of the license.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLicense.ConsumptionConfigurationProperty"], jsii.get(self, "consumptionConfiguration"))

    @consumption_configuration.setter
    def consumption_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnLicense.ConsumptionConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__284aa1e5a6876d4f451b6e5e8f93fdb375fc583828e7e8d36f280d50e762d790)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consumptionConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="entitlements")
    def entitlements(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLicense.EntitlementProperty"]]]:
        '''License entitlements.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLicense.EntitlementProperty"]]], jsii.get(self, "entitlements"))

    @entitlements.setter
    def entitlements(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLicense.EntitlementProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73e1a84fbc6ca70d5dacac620ef3f77aa87a4d9b60385a5f2899f10ab1aefd7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entitlements", value)

    @builtins.property
    @jsii.member(jsii_name="homeRegion")
    def home_region(self) -> builtins.str:
        '''Home Region of the license.'''
        return typing.cast(builtins.str, jsii.get(self, "homeRegion"))

    @home_region.setter
    def home_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__543ec2abfa87082c6465bd9aa1ff4096a9a5ba669d3147343b69c96ff2f90d67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeRegion", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnLicense.IssuerDataProperty"]:
        '''License issuer.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLicense.IssuerDataProperty"], jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnLicense.IssuerDataProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8b07f82f3d197d61c5edecbc56261a03ad65f4f99d1bb7a3c7b629126bb6ce9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="licenseName")
    def license_name(self) -> builtins.str:
        '''License name.'''
        return typing.cast(builtins.str, jsii.get(self, "licenseName"))

    @license_name.setter
    def license_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e97ac745c4faabd1c139a343ce905672f7e647741a9827bd7f203b40fb8f01c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseName", value)

    @builtins.property
    @jsii.member(jsii_name="productName")
    def product_name(self) -> builtins.str:
        '''Product name.'''
        return typing.cast(builtins.str, jsii.get(self, "productName"))

    @product_name.setter
    def product_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2a880e38bf22471203328b40fbe7cfbc719574af83c33d27bfb321c125d66fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productName", value)

    @builtins.property
    @jsii.member(jsii_name="validity")
    def validity(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnLicense.ValidityDateFormatProperty"]:
        '''Date and time range during which the license is valid, in ISO8601-UTC format.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLicense.ValidityDateFormatProperty"], jsii.get(self, "validity"))

    @validity.setter
    def validity(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnLicense.ValidityDateFormatProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14bfd7eea976b95153acfc2c36f571a86f5e204050b842561bf3f488085a466b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validity", value)

    @builtins.property
    @jsii.member(jsii_name="beneficiary")
    def beneficiary(self) -> typing.Optional[builtins.str]:
        '''License beneficiary.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "beneficiary"))

    @beneficiary.setter
    def beneficiary(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf9994475a7c52b73f7bc27dcb24ebe97709f2662d5138be4da7b3c42265936d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "beneficiary", value)

    @builtins.property
    @jsii.member(jsii_name="licenseMetadata")
    def license_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLicense.MetadataProperty"]]]]:
        '''License metadata.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLicense.MetadataProperty"]]]], jsii.get(self, "licenseMetadata"))

    @license_metadata.setter
    def license_metadata(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLicense.MetadataProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c94759710766169f67f670504ad6a0d56a36207b2a7008e6962da6595d9b62f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseMetadata", value)

    @builtins.property
    @jsii.member(jsii_name="productSku")
    def product_sku(self) -> typing.Optional[builtins.str]:
        '''Product SKU.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productSku"))

    @product_sku.setter
    def product_sku(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e5b8b4e9b80cb8b0305a292b6c390efd67f677abdb467395dc1e4b849b9c418)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productSku", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''License status.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3a0bb88a6f2431e141da5aa1e0e1d94957e1ec7a904c8a0b4f79254b7ef6f01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense.BorrowConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allow_early_check_in": "allowEarlyCheckIn",
            "max_time_to_live_in_minutes": "maxTimeToLiveInMinutes",
        },
    )
    class BorrowConfigurationProperty:
        def __init__(
            self,
            *,
            allow_early_check_in: typing.Union[builtins.bool, _IResolvable_da3f097b],
            max_time_to_live_in_minutes: jsii.Number,
        ) -> None:
            '''Details about a borrow configuration.

            :param allow_early_check_in: Indicates whether early check-ins are allowed.
            :param max_time_to_live_in_minutes: Maximum time for the borrow configuration, in minutes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-borrowconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                borrow_configuration_property = licensemanager.CfnLicense.BorrowConfigurationProperty(
                    allow_early_check_in=False,
                    max_time_to_live_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6e1d045a93aaf4354921dc5e95316f2bc7fa071c999fdf4edaa837886e37fb65)
                check_type(argname="argument allow_early_check_in", value=allow_early_check_in, expected_type=type_hints["allow_early_check_in"])
                check_type(argname="argument max_time_to_live_in_minutes", value=max_time_to_live_in_minutes, expected_type=type_hints["max_time_to_live_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allow_early_check_in": allow_early_check_in,
                "max_time_to_live_in_minutes": max_time_to_live_in_minutes,
            }

        @builtins.property
        def allow_early_check_in(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether early check-ins are allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-borrowconfiguration.html#cfn-licensemanager-license-borrowconfiguration-allowearlycheckin
            '''
            result = self._values.get("allow_early_check_in")
            assert result is not None, "Required property 'allow_early_check_in' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def max_time_to_live_in_minutes(self) -> jsii.Number:
            '''Maximum time for the borrow configuration, in minutes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-borrowconfiguration.html#cfn-licensemanager-license-borrowconfiguration-maxtimetoliveinminutes
            '''
            result = self._values.get("max_time_to_live_in_minutes")
            assert result is not None, "Required property 'max_time_to_live_in_minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BorrowConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense.ConsumptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "borrow_configuration": "borrowConfiguration",
            "provisional_configuration": "provisionalConfiguration",
            "renew_type": "renewType",
        },
    )
    class ConsumptionConfigurationProperty:
        def __init__(
            self,
            *,
            borrow_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLicense.BorrowConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            provisional_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLicense.ProvisionalConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            renew_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details about a consumption configuration.

            :param borrow_configuration: Details about a borrow configuration.
            :param provisional_configuration: Details about a provisional configuration.
            :param renew_type: Renewal frequency.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                consumption_configuration_property = licensemanager.CfnLicense.ConsumptionConfigurationProperty(
                    borrow_configuration=licensemanager.CfnLicense.BorrowConfigurationProperty(
                        allow_early_check_in=False,
                        max_time_to_live_in_minutes=123
                    ),
                    provisional_configuration=licensemanager.CfnLicense.ProvisionalConfigurationProperty(
                        max_time_to_live_in_minutes=123
                    ),
                    renew_type="renewType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d0339c6f5ae5d479d45a7126a63515791f5389a9bec49ee661b2ba68e30f11f)
                check_type(argname="argument borrow_configuration", value=borrow_configuration, expected_type=type_hints["borrow_configuration"])
                check_type(argname="argument provisional_configuration", value=provisional_configuration, expected_type=type_hints["provisional_configuration"])
                check_type(argname="argument renew_type", value=renew_type, expected_type=type_hints["renew_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if borrow_configuration is not None:
                self._values["borrow_configuration"] = borrow_configuration
            if provisional_configuration is not None:
                self._values["provisional_configuration"] = provisional_configuration
            if renew_type is not None:
                self._values["renew_type"] = renew_type

        @builtins.property
        def borrow_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLicense.BorrowConfigurationProperty"]]:
            '''Details about a borrow configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html#cfn-licensemanager-license-consumptionconfiguration-borrowconfiguration
            '''
            result = self._values.get("borrow_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLicense.BorrowConfigurationProperty"]], result)

        @builtins.property
        def provisional_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLicense.ProvisionalConfigurationProperty"]]:
            '''Details about a provisional configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html#cfn-licensemanager-license-consumptionconfiguration-provisionalconfiguration
            '''
            result = self._values.get("provisional_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLicense.ProvisionalConfigurationProperty"]], result)

        @builtins.property
        def renew_type(self) -> typing.Optional[builtins.str]:
            '''Renewal frequency.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-consumptionconfiguration.html#cfn-licensemanager-license-consumptionconfiguration-renewtype
            '''
            result = self._values.get("renew_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConsumptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense.EntitlementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "unit": "unit",
            "allow_check_in": "allowCheckIn",
            "max_count": "maxCount",
            "overage": "overage",
            "value": "value",
        },
    )
    class EntitlementProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            unit: builtins.str,
            allow_check_in: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            max_count: typing.Optional[jsii.Number] = None,
            overage: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a resource entitled for use with a license.

            :param name: Entitlement name.
            :param unit: Entitlement unit.
            :param allow_check_in: Indicates whether check-ins are allowed.
            :param max_count: Maximum entitlement count. Use if the unit is not None.
            :param overage: Indicates whether overages are allowed.
            :param value: Entitlement resource. Use only if the unit is None.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                entitlement_property = licensemanager.CfnLicense.EntitlementProperty(
                    name="name",
                    unit="unit",
                
                    # the properties below are optional
                    allow_check_in=False,
                    max_count=123,
                    overage=False,
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0310e9bff8887cfad57aaed42cce71c67a7406c6a2a5cad997c2f8c17282a0fc)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
                check_type(argname="argument allow_check_in", value=allow_check_in, expected_type=type_hints["allow_check_in"])
                check_type(argname="argument max_count", value=max_count, expected_type=type_hints["max_count"])
                check_type(argname="argument overage", value=overage, expected_type=type_hints["overage"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "unit": unit,
            }
            if allow_check_in is not None:
                self._values["allow_check_in"] = allow_check_in
            if max_count is not None:
                self._values["max_count"] = max_count
            if overage is not None:
                self._values["overage"] = overage
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> builtins.str:
            '''Entitlement name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def unit(self) -> builtins.str:
            '''Entitlement unit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allow_check_in(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether check-ins are allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-allowcheckin
            '''
            result = self._values.get("allow_check_in")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def max_count(self) -> typing.Optional[jsii.Number]:
            '''Maximum entitlement count.

            Use if the unit is not None.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-maxcount
            '''
            result = self._values.get("max_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def overage(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether overages are allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-overage
            '''
            result = self._values.get("overage")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''Entitlement resource.

            Use only if the unit is None.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-entitlement.html#cfn-licensemanager-license-entitlement-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntitlementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense.IssuerDataProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "sign_key": "signKey"},
    )
    class IssuerDataProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            sign_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details associated with the issuer of a license.

            :param name: Issuer name.
            :param sign_key: Asymmetric KMS key from AWS Key Management Service . The KMS key must have a key usage of sign and verify, and support the RSASSA-PSS SHA-256 signing algorithm.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-issuerdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                issuer_data_property = licensemanager.CfnLicense.IssuerDataProperty(
                    name="name",
                
                    # the properties below are optional
                    sign_key="signKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__14e6502acbee6acb56ae6f5303cd05a5e9e848984928eb8f7cdc300d203b0415)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument sign_key", value=sign_key, expected_type=type_hints["sign_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if sign_key is not None:
                self._values["sign_key"] = sign_key

        @builtins.property
        def name(self) -> builtins.str:
            '''Issuer name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-issuerdata.html#cfn-licensemanager-license-issuerdata-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sign_key(self) -> typing.Optional[builtins.str]:
            '''Asymmetric KMS key from AWS Key Management Service .

            The KMS key must have a key usage of sign and verify, and support the RSASSA-PSS SHA-256 signing algorithm.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-issuerdata.html#cfn-licensemanager-license-issuerdata-signkey
            '''
            result = self._values.get("sign_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IssuerDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense.MetadataProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class MetadataProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''Describes key/value pairs.

            :param name: The key name.
            :param value: The value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-metadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                metadata_property = licensemanager.CfnLicense.MetadataProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__43bd7660cdb11f18c2d3760a0a57df1cc7ec3d2ee1e8d2b9e99b3e66311ed38d)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The key name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-metadata.html#cfn-licensemanager-license-metadata-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-metadata.html#cfn-licensemanager-license-metadata-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense.ProvisionalConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"max_time_to_live_in_minutes": "maxTimeToLiveInMinutes"},
    )
    class ProvisionalConfigurationProperty:
        def __init__(self, *, max_time_to_live_in_minutes: jsii.Number) -> None:
            '''Details about a provisional configuration.

            :param max_time_to_live_in_minutes: Maximum time for the provisional configuration, in minutes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-provisionalconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                provisional_configuration_property = licensemanager.CfnLicense.ProvisionalConfigurationProperty(
                    max_time_to_live_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__826b706a8e797ace8542469b88edc36e5448545c11f738cff1a9e72cb776c46e)
                check_type(argname="argument max_time_to_live_in_minutes", value=max_time_to_live_in_minutes, expected_type=type_hints["max_time_to_live_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_time_to_live_in_minutes": max_time_to_live_in_minutes,
            }

        @builtins.property
        def max_time_to_live_in_minutes(self) -> jsii.Number:
            '''Maximum time for the provisional configuration, in minutes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-provisionalconfiguration.html#cfn-licensemanager-license-provisionalconfiguration-maxtimetoliveinminutes
            '''
            result = self._values.get("max_time_to_live_in_minutes")
            assert result is not None, "Required property 'max_time_to_live_in_minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisionalConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicense.ValidityDateFormatProperty",
        jsii_struct_bases=[],
        name_mapping={"begin": "begin", "end": "end"},
    )
    class ValidityDateFormatProperty:
        def __init__(self, *, begin: builtins.str, end: builtins.str) -> None:
            '''Date and time range during which the license is valid, in ISO8601-UTC format.

            :param begin: Start of the time range.
            :param end: End of the time range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-validitydateformat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_licensemanager as licensemanager
                
                validity_date_format_property = licensemanager.CfnLicense.ValidityDateFormatProperty(
                    begin="begin",
                    end="end"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__483b5b4e301dfddf60a6c6da8bdc4898ec615b5045a70ceeeefc10fe7320e97e)
                check_type(argname="argument begin", value=begin, expected_type=type_hints["begin"])
                check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "begin": begin,
                "end": end,
            }

        @builtins.property
        def begin(self) -> builtins.str:
            '''Start of the time range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-validitydateformat.html#cfn-licensemanager-license-validitydateformat-begin
            '''
            result = self._values.get("begin")
            assert result is not None, "Required property 'begin' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end(self) -> builtins.str:
            '''End of the time range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-licensemanager-license-validitydateformat.html#cfn-licensemanager-license-validitydateformat-end
            '''
            result = self._values.get("end")
            assert result is not None, "Required property 'end' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValidityDateFormatProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_licensemanager.CfnLicenseProps",
    jsii_struct_bases=[],
    name_mapping={
        "consumption_configuration": "consumptionConfiguration",
        "entitlements": "entitlements",
        "home_region": "homeRegion",
        "issuer": "issuer",
        "license_name": "licenseName",
        "product_name": "productName",
        "validity": "validity",
        "beneficiary": "beneficiary",
        "license_metadata": "licenseMetadata",
        "product_sku": "productSku",
        "status": "status",
    },
)
class CfnLicenseProps:
    def __init__(
        self,
        *,
        consumption_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.ConsumptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        entitlements: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.EntitlementProperty, typing.Dict[builtins.str, typing.Any]]]]],
        home_region: builtins.str,
        issuer: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.IssuerDataProperty, typing.Dict[builtins.str, typing.Any]]],
        license_name: builtins.str,
        product_name: builtins.str,
        validity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.ValidityDateFormatProperty, typing.Dict[builtins.str, typing.Any]]],
        beneficiary: typing.Optional[builtins.str] = None,
        license_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.MetadataProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        product_sku: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnLicense``.

        :param consumption_configuration: Configuration for consumption of the license.
        :param entitlements: License entitlements.
        :param home_region: Home Region of the license.
        :param issuer: License issuer.
        :param license_name: License name.
        :param product_name: Product name.
        :param validity: Date and time range during which the license is valid, in ISO8601-UTC format.
        :param beneficiary: License beneficiary.
        :param license_metadata: License metadata.
        :param product_sku: Product SKU.
        :param status: License status.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_licensemanager as licensemanager
            
            cfn_license_props = licensemanager.CfnLicenseProps(
                consumption_configuration=licensemanager.CfnLicense.ConsumptionConfigurationProperty(
                    borrow_configuration=licensemanager.CfnLicense.BorrowConfigurationProperty(
                        allow_early_check_in=False,
                        max_time_to_live_in_minutes=123
                    ),
                    provisional_configuration=licensemanager.CfnLicense.ProvisionalConfigurationProperty(
                        max_time_to_live_in_minutes=123
                    ),
                    renew_type="renewType"
                ),
                entitlements=[licensemanager.CfnLicense.EntitlementProperty(
                    name="name",
                    unit="unit",
            
                    # the properties below are optional
                    allow_check_in=False,
                    max_count=123,
                    overage=False,
                    value="value"
                )],
                home_region="homeRegion",
                issuer=licensemanager.CfnLicense.IssuerDataProperty(
                    name="name",
            
                    # the properties below are optional
                    sign_key="signKey"
                ),
                license_name="licenseName",
                product_name="productName",
                validity=licensemanager.CfnLicense.ValidityDateFormatProperty(
                    begin="begin",
                    end="end"
                ),
            
                # the properties below are optional
                beneficiary="beneficiary",
                license_metadata=[licensemanager.CfnLicense.MetadataProperty(
                    name="name",
                    value="value"
                )],
                product_sku="productSku",
                status="status"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1d549419287a5a545bf5eecdc65cd6b52387eb01953f3d4ff24a43da333c424)
            check_type(argname="argument consumption_configuration", value=consumption_configuration, expected_type=type_hints["consumption_configuration"])
            check_type(argname="argument entitlements", value=entitlements, expected_type=type_hints["entitlements"])
            check_type(argname="argument home_region", value=home_region, expected_type=type_hints["home_region"])
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument license_name", value=license_name, expected_type=type_hints["license_name"])
            check_type(argname="argument product_name", value=product_name, expected_type=type_hints["product_name"])
            check_type(argname="argument validity", value=validity, expected_type=type_hints["validity"])
            check_type(argname="argument beneficiary", value=beneficiary, expected_type=type_hints["beneficiary"])
            check_type(argname="argument license_metadata", value=license_metadata, expected_type=type_hints["license_metadata"])
            check_type(argname="argument product_sku", value=product_sku, expected_type=type_hints["product_sku"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "consumption_configuration": consumption_configuration,
            "entitlements": entitlements,
            "home_region": home_region,
            "issuer": issuer,
            "license_name": license_name,
            "product_name": product_name,
            "validity": validity,
        }
        if beneficiary is not None:
            self._values["beneficiary"] = beneficiary
        if license_metadata is not None:
            self._values["license_metadata"] = license_metadata
        if product_sku is not None:
            self._values["product_sku"] = product_sku
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def consumption_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnLicense.ConsumptionConfigurationProperty]:
        '''Configuration for consumption of the license.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-consumptionconfiguration
        '''
        result = self._values.get("consumption_configuration")
        assert result is not None, "Required property 'consumption_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnLicense.ConsumptionConfigurationProperty], result)

    @builtins.property
    def entitlements(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLicense.EntitlementProperty]]]:
        '''License entitlements.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-entitlements
        '''
        result = self._values.get("entitlements")
        assert result is not None, "Required property 'entitlements' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLicense.EntitlementProperty]]], result)

    @builtins.property
    def home_region(self) -> builtins.str:
        '''Home Region of the license.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-homeregion
        '''
        result = self._values.get("home_region")
        assert result is not None, "Required property 'home_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def issuer(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnLicense.IssuerDataProperty]:
        '''License issuer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-issuer
        '''
        result = self._values.get("issuer")
        assert result is not None, "Required property 'issuer' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnLicense.IssuerDataProperty], result)

    @builtins.property
    def license_name(self) -> builtins.str:
        '''License name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-licensename
        '''
        result = self._values.get("license_name")
        assert result is not None, "Required property 'license_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_name(self) -> builtins.str:
        '''Product name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-productname
        '''
        result = self._values.get("product_name")
        assert result is not None, "Required property 'product_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def validity(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnLicense.ValidityDateFormatProperty]:
        '''Date and time range during which the license is valid, in ISO8601-UTC format.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-validity
        '''
        result = self._values.get("validity")
        assert result is not None, "Required property 'validity' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnLicense.ValidityDateFormatProperty], result)

    @builtins.property
    def beneficiary(self) -> typing.Optional[builtins.str]:
        '''License beneficiary.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-beneficiary
        '''
        result = self._values.get("beneficiary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLicense.MetadataProperty]]]]:
        '''License metadata.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-licensemetadata
        '''
        result = self._values.get("license_metadata")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLicense.MetadataProperty]]]], result)

    @builtins.property
    def product_sku(self) -> typing.Optional[builtins.str]:
        '''Product SKU.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-productsku
        '''
        result = self._values.get("product_sku")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''License status.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-licensemanager-license.html#cfn-licensemanager-license-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLicenseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGrant",
    "CfnGrantProps",
    "CfnLicense",
    "CfnLicenseProps",
]

publication.publish()

def _typecheckingstub__e8429ee81c009103dd15c76170dfb52e5ca38f72a8912b82d6e63e3f460c3022(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    allowed_operations: typing.Optional[typing.Sequence[builtins.str]] = None,
    grant_name: typing.Optional[builtins.str] = None,
    home_region: typing.Optional[builtins.str] = None,
    license_arn: typing.Optional[builtins.str] = None,
    principals: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06f3d843a99f00dd40b93f69a334bda31af66745c91ef0da13aef948b5e7cd3b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f21921653469c34829dafde09a61b6573c5caa1cd6413329ac50f150c61edce(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0365c0a6e5122b9fa8e724dcae1d11a86ea3be7b9c43576ae3984046a8a866a2(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f4a134c7bb2f22cd48211ed5100e65a75fc658d9d8f836ea5c12000691c0cb2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5031789a0d9f35bd09ee7810379dcbe0da55436888a38e9623b68c7226da0990(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9ad1871340fca01eaad30a6180a827f5d9f498e7a913dbc15898d39ace8e741(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c571a4cf4f9bf1814a1015ca4a37680ca14b1356d42232abd8a71042c1e07bc(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__979cc3eeb34a65f4beb72557bbf7486f2c8b526da9a872d958b13f140f65edb0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55c62319564e7f4daffb2869290c03b511d6440828cc8d89ddb4e628ea3e0f93(
    *,
    allowed_operations: typing.Optional[typing.Sequence[builtins.str]] = None,
    grant_name: typing.Optional[builtins.str] = None,
    home_region: typing.Optional[builtins.str] = None,
    license_arn: typing.Optional[builtins.str] = None,
    principals: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fa5716b8b0216bdd1da1f12239ad6038aa037294da7f4a1f0215f1b16622526(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    consumption_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.ConsumptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    entitlements: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.EntitlementProperty, typing.Dict[builtins.str, typing.Any]]]]],
    home_region: builtins.str,
    issuer: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.IssuerDataProperty, typing.Dict[builtins.str, typing.Any]]],
    license_name: builtins.str,
    product_name: builtins.str,
    validity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.ValidityDateFormatProperty, typing.Dict[builtins.str, typing.Any]]],
    beneficiary: typing.Optional[builtins.str] = None,
    license_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.MetadataProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    product_sku: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9cd2d3dab3901b09367da6f6bc033c9f014286742aa8f85c2c7a6834c1b1512(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5b3e1a3ed6019a3b4d49c9c0479889cc544e9ecc5ed6f1e04e62407fc3377a9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__284aa1e5a6876d4f451b6e5e8f93fdb375fc583828e7e8d36f280d50e762d790(
    value: typing.Union[_IResolvable_da3f097b, CfnLicense.ConsumptionConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73e1a84fbc6ca70d5dacac620ef3f77aa87a4d9b60385a5f2899f10ab1aefd7d(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLicense.EntitlementProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__543ec2abfa87082c6465bd9aa1ff4096a9a5ba669d3147343b69c96ff2f90d67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8b07f82f3d197d61c5edecbc56261a03ad65f4f99d1bb7a3c7b629126bb6ce9(
    value: typing.Union[_IResolvable_da3f097b, CfnLicense.IssuerDataProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e97ac745c4faabd1c139a343ce905672f7e647741a9827bd7f203b40fb8f01c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2a880e38bf22471203328b40fbe7cfbc719574af83c33d27bfb321c125d66fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14bfd7eea976b95153acfc2c36f571a86f5e204050b842561bf3f488085a466b(
    value: typing.Union[_IResolvable_da3f097b, CfnLicense.ValidityDateFormatProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf9994475a7c52b73f7bc27dcb24ebe97709f2662d5138be4da7b3c42265936d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c94759710766169f67f670504ad6a0d56a36207b2a7008e6962da6595d9b62f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLicense.MetadataProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e5b8b4e9b80cb8b0305a292b6c390efd67f677abdb467395dc1e4b849b9c418(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3a0bb88a6f2431e141da5aa1e0e1d94957e1ec7a904c8a0b4f79254b7ef6f01(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e1d045a93aaf4354921dc5e95316f2bc7fa071c999fdf4edaa837886e37fb65(
    *,
    allow_early_check_in: typing.Union[builtins.bool, _IResolvable_da3f097b],
    max_time_to_live_in_minutes: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d0339c6f5ae5d479d45a7126a63515791f5389a9bec49ee661b2ba68e30f11f(
    *,
    borrow_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.BorrowConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    provisional_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.ProvisionalConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    renew_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0310e9bff8887cfad57aaed42cce71c67a7406c6a2a5cad997c2f8c17282a0fc(
    *,
    name: builtins.str,
    unit: builtins.str,
    allow_check_in: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    max_count: typing.Optional[jsii.Number] = None,
    overage: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14e6502acbee6acb56ae6f5303cd05a5e9e848984928eb8f7cdc300d203b0415(
    *,
    name: builtins.str,
    sign_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43bd7660cdb11f18c2d3760a0a57df1cc7ec3d2ee1e8d2b9e99b3e66311ed38d(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__826b706a8e797ace8542469b88edc36e5448545c11f738cff1a9e72cb776c46e(
    *,
    max_time_to_live_in_minutes: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__483b5b4e301dfddf60a6c6da8bdc4898ec615b5045a70ceeeefc10fe7320e97e(
    *,
    begin: builtins.str,
    end: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1d549419287a5a545bf5eecdc65cd6b52387eb01953f3d4ff24a43da333c424(
    *,
    consumption_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.ConsumptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    entitlements: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.EntitlementProperty, typing.Dict[builtins.str, typing.Any]]]]],
    home_region: builtins.str,
    issuer: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.IssuerDataProperty, typing.Dict[builtins.str, typing.Any]]],
    license_name: builtins.str,
    product_name: builtins.str,
    validity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.ValidityDateFormatProperty, typing.Dict[builtins.str, typing.Any]]],
    beneficiary: typing.Optional[builtins.str] = None,
    license_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLicense.MetadataProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    product_sku: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
