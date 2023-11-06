'''
# AWS::ACMPCA Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_acmpca as acmpca
```

## Certificate Authority

This package contains a `CertificateAuthority` class.
At the moment, you cannot create new Authorities using it,
but you can import existing ones using the `fromCertificateAuthorityArn` static method:

```python
certificate_authority = acmpca.CertificateAuthority.from_certificate_authority_arn(self, "CA", "arn:aws:acm-pca:us-east-1:123456789012:certificate-authority/023077d8-2bfa-4eb0-8f22-05c96deade77")
```

## Low-level `Cfn*` classes

You can always use the low-level classes
(starting with `Cfn*`) to create resources like the Certificate Authority:

```python
cfn_certificate_authority = acmpca.CfnCertificateAuthority(self, "CA",
    type="ROOT",
    key_algorithm="RSA_2048",
    signing_algorithm="SHA256WITHRSA",
    subject=acmpca.CfnCertificateAuthority.SubjectProperty(
        country="US",
        organization="string",
        organizational_unit="string",
        distinguished_name_qualifier="string",
        state="string",
        common_name="123",
        serial_number="string",
        locality="string",
        title="string",
        surname="string",
        given_name="string",
        initials="DG",
        pseudonym="string",
        generation_qualifier="DBG"
    )
)
```

If you need to pass the higher-level `ICertificateAuthority` somewhere,
you can get it from the lower-level `CfnCertificateAuthority` using the same `fromCertificateAuthorityArn` method:

```python
# cfn_certificate_authority: acmpca.CfnCertificateAuthority


certificate_authority = acmpca.CertificateAuthority.from_certificate_authority_arn(self, "CertificateAuthority", cfn_certificate_authority.attr_arn)
```
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
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


class CertificateAuthority(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_acmpca.CertificateAuthority",
):
    '''Defines a Certificate for ACMPCA.

    :resource: AWS::ACMPCA::CertificateAuthority
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_acmpca as acmpca
        
        # vpc: ec2.Vpc
        
        cluster = msk.Cluster(self, "Cluster",
            cluster_name="myCluster",
            kafka_version=msk.KafkaVersion.V2_8_1,
            vpc=vpc,
            encryption_in_transit=msk.EncryptionInTransitConfig(
                client_broker=msk.ClientBrokerEncryption.TLS
            ),
            client_authentication=msk.ClientAuthentication.tls(
                certificate_authorities=[
                    acmpca.CertificateAuthority.from_certificate_authority_arn(self, "CertificateAuthority", "arn:aws:acm-pca:us-west-2:1234567890:certificate-authority/11111111-1111-1111-1111-111111111111")
                ]
            )
        )
    '''

    @jsii.member(jsii_name="fromCertificateAuthorityArn")
    @builtins.classmethod
    def from_certificate_authority_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        certificate_authority_arn: builtins.str,
    ) -> "ICertificateAuthority":
        '''Import an existing Certificate given an ARN.

        :param scope: -
        :param id: -
        :param certificate_authority_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1395360f89634b836bfd8f83f0cbc2f4dbb936a9ba23c531cd8ffe3998f45c2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument certificate_authority_arn", value=certificate_authority_arn, expected_type=type_hints["certificate_authority_arn"])
        return typing.cast("ICertificateAuthority", jsii.sinvoke(cls, "fromCertificateAuthorityArn", [scope, id, certificate_authority_arn]))


@jsii.implements(_IInspectable_c2943556)
class CfnCertificate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificate",
):
    '''The ``AWS::ACMPCA::Certificate`` resource is used to issue a certificate using your private certificate authority.

    For more information, see the `IssueCertificate <https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html>`_ action.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_acmpca as acmpca
        
        cfn_certificate = acmpca.CfnCertificate(self, "MyCfnCertificate",
            certificate_authority_arn="certificateAuthorityArn",
            certificate_signing_request="certificateSigningRequest",
            signing_algorithm="signingAlgorithm",
            validity=acmpca.CfnCertificate.ValidityProperty(
                type="type",
                value=123
            ),
        
            # the properties below are optional
            api_passthrough=acmpca.CfnCertificate.ApiPassthroughProperty(
                extensions=acmpca.CfnCertificate.ExtensionsProperty(
                    certificate_policies=[acmpca.CfnCertificate.PolicyInformationProperty(
                        cert_policy_id="certPolicyId",
        
                        # the properties below are optional
                        policy_qualifiers=[acmpca.CfnCertificate.PolicyQualifierInfoProperty(
                            policy_qualifier_id="policyQualifierId",
                            qualifier=acmpca.CfnCertificate.QualifierProperty(
                                cps_uri="cpsUri"
                            )
                        )]
                    )],
                    custom_extensions=[acmpca.CfnCertificate.CustomExtensionProperty(
                        object_identifier="objectIdentifier",
                        value="value",
        
                        # the properties below are optional
                        critical=False
                    )],
                    extended_key_usage=[acmpca.CfnCertificate.ExtendedKeyUsageProperty(
                        extended_key_usage_object_identifier="extendedKeyUsageObjectIdentifier",
                        extended_key_usage_type="extendedKeyUsageType"
                    )],
                    key_usage=acmpca.CfnCertificate.KeyUsageProperty(
                        crl_sign=False,
                        data_encipherment=False,
                        decipher_only=False,
                        digital_signature=False,
                        encipher_only=False,
                        key_agreement=False,
                        key_cert_sign=False,
                        key_encipherment=False,
                        non_repudiation=False
                    ),
                    subject_alternative_names=[acmpca.CfnCertificate.GeneralNameProperty(
                        directory_name=acmpca.CfnCertificate.SubjectProperty(
                            common_name="commonName",
                            country="country",
                            custom_attributes=[acmpca.CfnCertificate.CustomAttributeProperty(
                                object_identifier="objectIdentifier",
                                value="value"
                            )],
                            distinguished_name_qualifier="distinguishedNameQualifier",
                            generation_qualifier="generationQualifier",
                            given_name="givenName",
                            initials="initials",
                            locality="locality",
                            organization="organization",
                            organizational_unit="organizationalUnit",
                            pseudonym="pseudonym",
                            serial_number="serialNumber",
                            state="state",
                            surname="surname",
                            title="title"
                        ),
                        dns_name="dnsName",
                        edi_party_name=acmpca.CfnCertificate.EdiPartyNameProperty(
                            name_assigner="nameAssigner",
                            party_name="partyName"
                        ),
                        ip_address="ipAddress",
                        other_name=acmpca.CfnCertificate.OtherNameProperty(
                            type_id="typeId",
                            value="value"
                        ),
                        registered_id="registeredId",
                        rfc822_name="rfc822Name",
                        uniform_resource_identifier="uniformResourceIdentifier"
                    )]
                ),
                subject=acmpca.CfnCertificate.SubjectProperty(
                    common_name="commonName",
                    country="country",
                    custom_attributes=[acmpca.CfnCertificate.CustomAttributeProperty(
                        object_identifier="objectIdentifier",
                        value="value"
                    )],
                    distinguished_name_qualifier="distinguishedNameQualifier",
                    generation_qualifier="generationQualifier",
                    given_name="givenName",
                    initials="initials",
                    locality="locality",
                    organization="organization",
                    organizational_unit="organizationalUnit",
                    pseudonym="pseudonym",
                    serial_number="serialNumber",
                    state="state",
                    surname="surname",
                    title="title"
                )
            ),
            template_arn="templateArn",
            validity_not_before=acmpca.CfnCertificate.ValidityProperty(
                type="type",
                value=123
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        certificate_authority_arn: builtins.str,
        certificate_signing_request: builtins.str,
        signing_algorithm: builtins.str,
        validity: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.ValidityProperty", typing.Dict[builtins.str, typing.Any]]],
        api_passthrough: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.ApiPassthroughProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        template_arn: typing.Optional[builtins.str] = None,
        validity_not_before: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.ValidityProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param certificate_authority_arn: The Amazon Resource Name (ARN) for the private CA issues the certificate.
        :param certificate_signing_request: The certificate signing request (CSR) for the certificate.
        :param signing_algorithm: The name of the algorithm that will be used to sign the certificate to be issued. This parameter should not be confused with the ``SigningAlgorithm`` parameter used to sign a CSR in the ``CreateCertificateAuthority`` action. .. epigraph:: The specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key.
        :param validity: The period of time during which the certificate will be valid.
        :param api_passthrough: Specifies X.509 certificate information to be included in the issued certificate. An ``APIPassthrough`` or ``APICSRPassthrough`` template variant must be selected, or else this parameter is ignored.
        :param template_arn: Specifies a custom configuration template to use when issuing a certificate. If this parameter is not provided, AWS Private CA defaults to the ``EndEntityCertificate/V1`` template. For more information about AWS Private CA templates, see `Using Templates <https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html>`_ .
        :param validity_not_before: Information describing the start of the validity period of the certificate. This parameter sets the “Not Before" date for the certificate. By default, when issuing a certificate, AWS Private CA sets the "Not Before" date to the issuance time minus 60 minutes. This compensates for clock inconsistencies across computer systems. The ``ValidityNotBefore`` parameter can be used to customize the “Not Before” value. Unlike the ``Validity`` parameter, the ``ValidityNotBefore`` parameter is optional. The ``ValidityNotBefore`` value is expressed as an explicit date and time, using the ``Validity`` type value ``ABSOLUTE`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c63a1f66d359048e3b7f539f55f0320982cfa96588aa92aa5a52d4f490ff7c7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCertificateProps(
            certificate_authority_arn=certificate_authority_arn,
            certificate_signing_request=certificate_signing_request,
            signing_algorithm=signing_algorithm,
            validity=validity,
            api_passthrough=api_passthrough,
            template_arn=template_arn,
            validity_not_before=validity_not_before,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae245fe6e4335d443fbf3d06674c0a246856a567c69eac96b60daf71940d2ba9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ced20980ce5020a1c27b089ee9acf9c670389a6dca8d4db4d86c9ffbf01c1a1)
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
        '''The Amazon Resource Name (ARN) of the issued certificate.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCertificate")
    def attr_certificate(self) -> builtins.str:
        '''The issued Base64 PEM-encoded certificate.

        :cloudformationAttribute: Certificate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCertificate"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the private CA issues the certificate.'''
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthorityArn"))

    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__929f46388471884d412a93caaec6152169738bcde7736082806fa61355f38450)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthorityArn", value)

    @builtins.property
    @jsii.member(jsii_name="certificateSigningRequest")
    def certificate_signing_request(self) -> builtins.str:
        '''The certificate signing request (CSR) for the certificate.'''
        return typing.cast(builtins.str, jsii.get(self, "certificateSigningRequest"))

    @certificate_signing_request.setter
    def certificate_signing_request(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16a09377d92f4e276678c2c81de91b48247f6567816f2a450052d3564b74e969)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateSigningRequest", value)

    @builtins.property
    @jsii.member(jsii_name="signingAlgorithm")
    def signing_algorithm(self) -> builtins.str:
        '''The name of the algorithm that will be used to sign the certificate to be issued.'''
        return typing.cast(builtins.str, jsii.get(self, "signingAlgorithm"))

    @signing_algorithm.setter
    def signing_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__643e9821d5b63922252de6f66c05ac417883bee41b28c13cf3db8cd2632e14e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signingAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="validity")
    def validity(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCertificate.ValidityProperty"]:
        '''The period of time during which the certificate will be valid.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCertificate.ValidityProperty"], jsii.get(self, "validity"))

    @validity.setter
    def validity(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCertificate.ValidityProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b0f98fada0460f1013060888886a3c2a49f08cade3f294d7b78ab8077353d28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validity", value)

    @builtins.property
    @jsii.member(jsii_name="apiPassthrough")
    def api_passthrough(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.ApiPassthroughProperty"]]:
        '''Specifies X.509 certificate information to be included in the issued certificate. An ``APIPassthrough`` or ``APICSRPassthrough`` template variant must be selected, or else this parameter is ignored.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.ApiPassthroughProperty"]], jsii.get(self, "apiPassthrough"))

    @api_passthrough.setter
    def api_passthrough(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.ApiPassthroughProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07edd7fc55218dbdda428adf3aa29d974595465ca0c1084ed6f98a79f08d4841)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiPassthrough", value)

    @builtins.property
    @jsii.member(jsii_name="templateArn")
    def template_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies a custom configuration template to use when issuing a certificate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateArn"))

    @template_arn.setter
    def template_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20f419f7a37472cedd9954e752bfa553241909264a1db9544a8edce9404b9552)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateArn", value)

    @builtins.property
    @jsii.member(jsii_name="validityNotBefore")
    def validity_not_before(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.ValidityProperty"]]:
        '''Information describing the start of the validity period of the certificate.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.ValidityProperty"]], jsii.get(self, "validityNotBefore"))

    @validity_not_before.setter
    def validity_not_before(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.ValidityProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce4f5fb71e1d9798d96fd2e8524ac910685f8e895b03a85141518face166fd7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validityNotBefore", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificate.ApiPassthroughProperty",
        jsii_struct_bases=[],
        name_mapping={"extensions": "extensions", "subject": "subject"},
    )
    class ApiPassthroughProperty:
        def __init__(
            self,
            *,
            extensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.ExtensionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            subject: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.SubjectProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains X.509 certificate information to be placed in an issued certificate. An ``APIPassthrough`` or ``APICSRPassthrough`` template variant must be selected, or else this parameter is ignored.

            If conflicting or duplicate certificate information is supplied from other sources, AWS Private CA applies `order of operation rules <https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html#template-order-of-operations>`_ to determine what information is used.

            :param extensions: Specifies X.509 extension information for a certificate.
            :param subject: Contains information about the certificate subject. The Subject field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The Subject must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-apipassthrough.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                api_passthrough_property = acmpca.CfnCertificate.ApiPassthroughProperty(
                    extensions=acmpca.CfnCertificate.ExtensionsProperty(
                        certificate_policies=[acmpca.CfnCertificate.PolicyInformationProperty(
                            cert_policy_id="certPolicyId",
                
                            # the properties below are optional
                            policy_qualifiers=[acmpca.CfnCertificate.PolicyQualifierInfoProperty(
                                policy_qualifier_id="policyQualifierId",
                                qualifier=acmpca.CfnCertificate.QualifierProperty(
                                    cps_uri="cpsUri"
                                )
                            )]
                        )],
                        custom_extensions=[acmpca.CfnCertificate.CustomExtensionProperty(
                            object_identifier="objectIdentifier",
                            value="value",
                
                            # the properties below are optional
                            critical=False
                        )],
                        extended_key_usage=[acmpca.CfnCertificate.ExtendedKeyUsageProperty(
                            extended_key_usage_object_identifier="extendedKeyUsageObjectIdentifier",
                            extended_key_usage_type="extendedKeyUsageType"
                        )],
                        key_usage=acmpca.CfnCertificate.KeyUsageProperty(
                            crl_sign=False,
                            data_encipherment=False,
                            decipher_only=False,
                            digital_signature=False,
                            encipher_only=False,
                            key_agreement=False,
                            key_cert_sign=False,
                            key_encipherment=False,
                            non_repudiation=False
                        ),
                        subject_alternative_names=[acmpca.CfnCertificate.GeneralNameProperty(
                            directory_name=acmpca.CfnCertificate.SubjectProperty(
                                common_name="commonName",
                                country="country",
                                custom_attributes=[acmpca.CfnCertificate.CustomAttributeProperty(
                                    object_identifier="objectIdentifier",
                                    value="value"
                                )],
                                distinguished_name_qualifier="distinguishedNameQualifier",
                                generation_qualifier="generationQualifier",
                                given_name="givenName",
                                initials="initials",
                                locality="locality",
                                organization="organization",
                                organizational_unit="organizationalUnit",
                                pseudonym="pseudonym",
                                serial_number="serialNumber",
                                state="state",
                                surname="surname",
                                title="title"
                            ),
                            dns_name="dnsName",
                            edi_party_name=acmpca.CfnCertificate.EdiPartyNameProperty(
                                name_assigner="nameAssigner",
                                party_name="partyName"
                            ),
                            ip_address="ipAddress",
                            other_name=acmpca.CfnCertificate.OtherNameProperty(
                                type_id="typeId",
                                value="value"
                            ),
                            registered_id="registeredId",
                            rfc822_name="rfc822Name",
                            uniform_resource_identifier="uniformResourceIdentifier"
                        )]
                    ),
                    subject=acmpca.CfnCertificate.SubjectProperty(
                        common_name="commonName",
                        country="country",
                        custom_attributes=[acmpca.CfnCertificate.CustomAttributeProperty(
                            object_identifier="objectIdentifier",
                            value="value"
                        )],
                        distinguished_name_qualifier="distinguishedNameQualifier",
                        generation_qualifier="generationQualifier",
                        given_name="givenName",
                        initials="initials",
                        locality="locality",
                        organization="organization",
                        organizational_unit="organizationalUnit",
                        pseudonym="pseudonym",
                        serial_number="serialNumber",
                        state="state",
                        surname="surname",
                        title="title"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3c063a4aa0db8588e572959a6949f00a9e649d71349c0f01000aee85a36d5959)
                check_type(argname="argument extensions", value=extensions, expected_type=type_hints["extensions"])
                check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if extensions is not None:
                self._values["extensions"] = extensions
            if subject is not None:
                self._values["subject"] = subject

        @builtins.property
        def extensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.ExtensionsProperty"]]:
            '''Specifies X.509 extension information for a certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-apipassthrough.html#cfn-acmpca-certificate-apipassthrough-extensions
            '''
            result = self._values.get("extensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.ExtensionsProperty"]], result)

        @builtins.property
        def subject(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.SubjectProperty"]]:
            '''Contains information about the certificate subject.

            The Subject field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The Subject must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-apipassthrough.html#cfn-acmpca-certificate-apipassthrough-subject
            '''
            result = self._values.get("subject")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.SubjectProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiPassthroughProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificate.CustomAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"object_identifier": "objectIdentifier", "value": "value"},
    )
    class CustomAttributeProperty:
        def __init__(
            self,
            *,
            object_identifier: builtins.str,
            value: builtins.str,
        ) -> None:
            '''Defines the X.500 relative distinguished name (RDN).

            :param object_identifier: Specifies the object identifier (OID) of the attribute type of the relative distinguished name (RDN).
            :param value: Specifies the attribute value of relative distinguished name (RDN).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-customattribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                custom_attribute_property = acmpca.CfnCertificate.CustomAttributeProperty(
                    object_identifier="objectIdentifier",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__98994bee25a07a794a889c37c3d7fad1758f74e523835472e78fee9b53895d92)
                check_type(argname="argument object_identifier", value=object_identifier, expected_type=type_hints["object_identifier"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object_identifier": object_identifier,
                "value": value,
            }

        @builtins.property
        def object_identifier(self) -> builtins.str:
            '''Specifies the object identifier (OID) of the attribute type of the relative distinguished name (RDN).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-customattribute.html#cfn-acmpca-certificate-customattribute-objectidentifier
            '''
            result = self._values.get("object_identifier")
            assert result is not None, "Required property 'object_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''Specifies the attribute value of relative distinguished name (RDN).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-customattribute.html#cfn-acmpca-certificate-customattribute-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificate.CustomExtensionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "object_identifier": "objectIdentifier",
            "value": "value",
            "critical": "critical",
        },
    )
    class CustomExtensionProperty:
        def __init__(
            self,
            *,
            object_identifier: builtins.str,
            value: builtins.str,
            critical: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specifies the X.509 extension information for a certificate.

            Extensions present in ``CustomExtensions`` follow the ``ApiPassthrough`` `template rules <https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html#template-order-of-operations>`_ .

            :param object_identifier: Specifies the object identifier (OID) of the X.509 extension. For more information, see the `Global OID reference database. <https://docs.aws.amazon.com/https://oidref.com/2.5.29>`_.
            :param value: Specifies the base64-encoded value of the X.509 extension.
            :param critical: Specifies the critical flag of the X.509 extension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-customextension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                custom_extension_property = acmpca.CfnCertificate.CustomExtensionProperty(
                    object_identifier="objectIdentifier",
                    value="value",
                
                    # the properties below are optional
                    critical=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__51c3c7eafba7b9c58470900a599324795cc525bc9a07c9dca8f8225ffa1776cc)
                check_type(argname="argument object_identifier", value=object_identifier, expected_type=type_hints["object_identifier"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument critical", value=critical, expected_type=type_hints["critical"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object_identifier": object_identifier,
                "value": value,
            }
            if critical is not None:
                self._values["critical"] = critical

        @builtins.property
        def object_identifier(self) -> builtins.str:
            '''Specifies the object identifier (OID) of the X.509 extension. For more information, see the `Global OID reference database. <https://docs.aws.amazon.com/https://oidref.com/2.5.29>`_.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-customextension.html#cfn-acmpca-certificate-customextension-objectidentifier
            '''
            result = self._values.get("object_identifier")
            assert result is not None, "Required property 'object_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''Specifies the base64-encoded value of the X.509 extension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-customextension.html#cfn-acmpca-certificate-customextension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def critical(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies the critical flag of the X.509 extension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-customextension.html#cfn-acmpca-certificate-customextension-critical
            '''
            result = self._values.get("critical")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomExtensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificate.EdiPartyNameProperty",
        jsii_struct_bases=[],
        name_mapping={"name_assigner": "nameAssigner", "party_name": "partyName"},
    )
    class EdiPartyNameProperty:
        def __init__(
            self,
            *,
            name_assigner: builtins.str,
            party_name: builtins.str,
        ) -> None:
            '''Describes an Electronic Data Interchange (EDI) entity as described in as defined in `Subject Alternative Name <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc5280>`_ in RFC 5280.

            :param name_assigner: Specifies the name assigner.
            :param party_name: Specifies the party name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-edipartyname.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                edi_party_name_property = acmpca.CfnCertificate.EdiPartyNameProperty(
                    name_assigner="nameAssigner",
                    party_name="partyName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0061c1a7a051fd8dd8ea03b1a7705465837ca64fe8e1aaee6033e7ba0e78499f)
                check_type(argname="argument name_assigner", value=name_assigner, expected_type=type_hints["name_assigner"])
                check_type(argname="argument party_name", value=party_name, expected_type=type_hints["party_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name_assigner": name_assigner,
                "party_name": party_name,
            }

        @builtins.property
        def name_assigner(self) -> builtins.str:
            '''Specifies the name assigner.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-edipartyname.html#cfn-acmpca-certificate-edipartyname-nameassigner
            '''
            result = self._values.get("name_assigner")
            assert result is not None, "Required property 'name_assigner' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def party_name(self) -> builtins.str:
            '''Specifies the party name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-edipartyname.html#cfn-acmpca-certificate-edipartyname-partyname
            '''
            result = self._values.get("party_name")
            assert result is not None, "Required property 'party_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EdiPartyNameProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificate.ExtendedKeyUsageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "extended_key_usage_object_identifier": "extendedKeyUsageObjectIdentifier",
            "extended_key_usage_type": "extendedKeyUsageType",
        },
    )
    class ExtendedKeyUsageProperty:
        def __init__(
            self,
            *,
            extended_key_usage_object_identifier: typing.Optional[builtins.str] = None,
            extended_key_usage_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies additional purposes for which the certified public key may be used other than basic purposes indicated in the ``KeyUsage`` extension.

            :param extended_key_usage_object_identifier: Specifies a custom ``ExtendedKeyUsage`` with an object identifier (OID).
            :param extended_key_usage_type: Specifies a standard ``ExtendedKeyUsage`` as defined as in `RFC 5280 <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extendedkeyusage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                extended_key_usage_property = acmpca.CfnCertificate.ExtendedKeyUsageProperty(
                    extended_key_usage_object_identifier="extendedKeyUsageObjectIdentifier",
                    extended_key_usage_type="extendedKeyUsageType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f2060402888ad8f292021f28746d894182b12eb1844683d776ca901ec58edf19)
                check_type(argname="argument extended_key_usage_object_identifier", value=extended_key_usage_object_identifier, expected_type=type_hints["extended_key_usage_object_identifier"])
                check_type(argname="argument extended_key_usage_type", value=extended_key_usage_type, expected_type=type_hints["extended_key_usage_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if extended_key_usage_object_identifier is not None:
                self._values["extended_key_usage_object_identifier"] = extended_key_usage_object_identifier
            if extended_key_usage_type is not None:
                self._values["extended_key_usage_type"] = extended_key_usage_type

        @builtins.property
        def extended_key_usage_object_identifier(self) -> typing.Optional[builtins.str]:
            '''Specifies a custom ``ExtendedKeyUsage`` with an object identifier (OID).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extendedkeyusage.html#cfn-acmpca-certificate-extendedkeyusage-extendedkeyusageobjectidentifier
            '''
            result = self._values.get("extended_key_usage_object_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def extended_key_usage_type(self) -> typing.Optional[builtins.str]:
            '''Specifies a standard ``ExtendedKeyUsage`` as defined as in `RFC 5280 <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extendedkeyusage.html#cfn-acmpca-certificate-extendedkeyusage-extendedkeyusagetype
            '''
            result = self._values.get("extended_key_usage_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExtendedKeyUsageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificate.ExtensionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_policies": "certificatePolicies",
            "custom_extensions": "customExtensions",
            "extended_key_usage": "extendedKeyUsage",
            "key_usage": "keyUsage",
            "subject_alternative_names": "subjectAlternativeNames",
        },
    )
    class ExtensionsProperty:
        def __init__(
            self,
            *,
            certificate_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.PolicyInformationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            custom_extensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.CustomExtensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            extended_key_usage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.ExtendedKeyUsageProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            key_usage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.KeyUsageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            subject_alternative_names: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.GeneralNameProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Contains X.509 extension information for a certificate.

            :param certificate_policies: Contains a sequence of one or more policy information terms, each of which consists of an object identifier (OID) and optional qualifiers. For more information, see NIST's definition of `Object Identifier (OID) <https://docs.aws.amazon.com/https://csrc.nist.gov/glossary/term/Object_Identifier>`_ . In an end-entity certificate, these terms indicate the policy under which the certificate was issued and the purposes for which it may be used. In a CA certificate, these terms limit the set of policies for certification paths that include this certificate.
            :param custom_extensions: Contains a sequence of one or more X.509 extensions, each of which consists of an object identifier (OID), a base64-encoded value, and the critical flag. For more information, see the `Global OID reference database. <https://docs.aws.amazon.com/https://oidref.com/2.5.29>`_.
            :param extended_key_usage: Specifies additional purposes for which the certified public key may be used other than basic purposes indicated in the ``KeyUsage`` extension.
            :param key_usage: Defines one or more purposes for which the key contained in the certificate can be used. Default value for each option is false.
            :param subject_alternative_names: The subject alternative name extension allows identities to be bound to the subject of the certificate. These identities may be included in addition to or in place of the identity in the subject field of the certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                extensions_property = acmpca.CfnCertificate.ExtensionsProperty(
                    certificate_policies=[acmpca.CfnCertificate.PolicyInformationProperty(
                        cert_policy_id="certPolicyId",
                
                        # the properties below are optional
                        policy_qualifiers=[acmpca.CfnCertificate.PolicyQualifierInfoProperty(
                            policy_qualifier_id="policyQualifierId",
                            qualifier=acmpca.CfnCertificate.QualifierProperty(
                                cps_uri="cpsUri"
                            )
                        )]
                    )],
                    custom_extensions=[acmpca.CfnCertificate.CustomExtensionProperty(
                        object_identifier="objectIdentifier",
                        value="value",
                
                        # the properties below are optional
                        critical=False
                    )],
                    extended_key_usage=[acmpca.CfnCertificate.ExtendedKeyUsageProperty(
                        extended_key_usage_object_identifier="extendedKeyUsageObjectIdentifier",
                        extended_key_usage_type="extendedKeyUsageType"
                    )],
                    key_usage=acmpca.CfnCertificate.KeyUsageProperty(
                        crl_sign=False,
                        data_encipherment=False,
                        decipher_only=False,
                        digital_signature=False,
                        encipher_only=False,
                        key_agreement=False,
                        key_cert_sign=False,
                        key_encipherment=False,
                        non_repudiation=False
                    ),
                    subject_alternative_names=[acmpca.CfnCertificate.GeneralNameProperty(
                        directory_name=acmpca.CfnCertificate.SubjectProperty(
                            common_name="commonName",
                            country="country",
                            custom_attributes=[acmpca.CfnCertificate.CustomAttributeProperty(
                                object_identifier="objectIdentifier",
                                value="value"
                            )],
                            distinguished_name_qualifier="distinguishedNameQualifier",
                            generation_qualifier="generationQualifier",
                            given_name="givenName",
                            initials="initials",
                            locality="locality",
                            organization="organization",
                            organizational_unit="organizationalUnit",
                            pseudonym="pseudonym",
                            serial_number="serialNumber",
                            state="state",
                            surname="surname",
                            title="title"
                        ),
                        dns_name="dnsName",
                        edi_party_name=acmpca.CfnCertificate.EdiPartyNameProperty(
                            name_assigner="nameAssigner",
                            party_name="partyName"
                        ),
                        ip_address="ipAddress",
                        other_name=acmpca.CfnCertificate.OtherNameProperty(
                            type_id="typeId",
                            value="value"
                        ),
                        registered_id="registeredId",
                        rfc822_name="rfc822Name",
                        uniform_resource_identifier="uniformResourceIdentifier"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f542a5e2932abd07f7c4fac088c4ae0b0560522e990c6e4ad85dbfe915c5854b)
                check_type(argname="argument certificate_policies", value=certificate_policies, expected_type=type_hints["certificate_policies"])
                check_type(argname="argument custom_extensions", value=custom_extensions, expected_type=type_hints["custom_extensions"])
                check_type(argname="argument extended_key_usage", value=extended_key_usage, expected_type=type_hints["extended_key_usage"])
                check_type(argname="argument key_usage", value=key_usage, expected_type=type_hints["key_usage"])
                check_type(argname="argument subject_alternative_names", value=subject_alternative_names, expected_type=type_hints["subject_alternative_names"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if certificate_policies is not None:
                self._values["certificate_policies"] = certificate_policies
            if custom_extensions is not None:
                self._values["custom_extensions"] = custom_extensions
            if extended_key_usage is not None:
                self._values["extended_key_usage"] = extended_key_usage
            if key_usage is not None:
                self._values["key_usage"] = key_usage
            if subject_alternative_names is not None:
                self._values["subject_alternative_names"] = subject_alternative_names

        @builtins.property
        def certificate_policies(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificate.PolicyInformationProperty"]]]]:
            '''Contains a sequence of one or more policy information terms, each of which consists of an object identifier (OID) and optional qualifiers.

            For more information, see NIST's definition of `Object Identifier (OID) <https://docs.aws.amazon.com/https://csrc.nist.gov/glossary/term/Object_Identifier>`_ .

            In an end-entity certificate, these terms indicate the policy under which the certificate was issued and the purposes for which it may be used. In a CA certificate, these terms limit the set of policies for certification paths that include this certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html#cfn-acmpca-certificate-extensions-certificatepolicies
            '''
            result = self._values.get("certificate_policies")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificate.PolicyInformationProperty"]]]], result)

        @builtins.property
        def custom_extensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificate.CustomExtensionProperty"]]]]:
            '''Contains a sequence of one or more X.509 extensions, each of which consists of an object identifier (OID), a base64-encoded value, and the critical flag. For more information, see the `Global OID reference database. <https://docs.aws.amazon.com/https://oidref.com/2.5.29>`_.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html#cfn-acmpca-certificate-extensions-customextensions
            '''
            result = self._values.get("custom_extensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificate.CustomExtensionProperty"]]]], result)

        @builtins.property
        def extended_key_usage(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificate.ExtendedKeyUsageProperty"]]]]:
            '''Specifies additional purposes for which the certified public key may be used other than basic purposes indicated in the ``KeyUsage`` extension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html#cfn-acmpca-certificate-extensions-extendedkeyusage
            '''
            result = self._values.get("extended_key_usage")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificate.ExtendedKeyUsageProperty"]]]], result)

        @builtins.property
        def key_usage(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.KeyUsageProperty"]]:
            '''Defines one or more purposes for which the key contained in the certificate can be used.

            Default value for each option is false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html#cfn-acmpca-certificate-extensions-keyusage
            '''
            result = self._values.get("key_usage")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.KeyUsageProperty"]], result)

        @builtins.property
        def subject_alternative_names(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificate.GeneralNameProperty"]]]]:
            '''The subject alternative name extension allows identities to be bound to the subject of the certificate.

            These identities may be included in addition to or in place of the identity in the subject field of the certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html#cfn-acmpca-certificate-extensions-subjectalternativenames
            '''
            result = self._values.get("subject_alternative_names")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificate.GeneralNameProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExtensionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificate.GeneralNameProperty",
        jsii_struct_bases=[],
        name_mapping={
            "directory_name": "directoryName",
            "dns_name": "dnsName",
            "edi_party_name": "ediPartyName",
            "ip_address": "ipAddress",
            "other_name": "otherName",
            "registered_id": "registeredId",
            "rfc822_name": "rfc822Name",
            "uniform_resource_identifier": "uniformResourceIdentifier",
        },
    )
    class GeneralNameProperty:
        def __init__(
            self,
            *,
            directory_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.SubjectProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dns_name: typing.Optional[builtins.str] = None,
            edi_party_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.EdiPartyNameProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ip_address: typing.Optional[builtins.str] = None,
            other_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.OtherNameProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            registered_id: typing.Optional[builtins.str] = None,
            rfc822_name: typing.Optional[builtins.str] = None,
            uniform_resource_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an ASN.1 X.400 ``GeneralName`` as defined in `RFC 5280 <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc5280>`_ . Only one of the following naming options should be provided. Providing more than one option results in an ``InvalidArgsException`` error.

            :param directory_name: Contains information about the certificate subject. The certificate can be one issued by your private certificate authority (CA) or it can be your private CA certificate. The Subject field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The Subject must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate. The DN must be unique for each entity, but your private CA can issue more than one certificate with the same DN to the same entity.
            :param dns_name: Represents ``GeneralName`` as a DNS name.
            :param edi_party_name: Represents ``GeneralName`` as an ``EdiPartyName`` object.
            :param ip_address: Represents ``GeneralName`` as an IPv4 or IPv6 address.
            :param other_name: Represents ``GeneralName`` using an ``OtherName`` object.
            :param registered_id: Represents ``GeneralName`` as an object identifier (OID).
            :param rfc822_name: Represents ``GeneralName`` as an `RFC 822 <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc822>`_ email address.
            :param uniform_resource_identifier: Represents ``GeneralName`` as a URI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                general_name_property = acmpca.CfnCertificate.GeneralNameProperty(
                    directory_name=acmpca.CfnCertificate.SubjectProperty(
                        common_name="commonName",
                        country="country",
                        custom_attributes=[acmpca.CfnCertificate.CustomAttributeProperty(
                            object_identifier="objectIdentifier",
                            value="value"
                        )],
                        distinguished_name_qualifier="distinguishedNameQualifier",
                        generation_qualifier="generationQualifier",
                        given_name="givenName",
                        initials="initials",
                        locality="locality",
                        organization="organization",
                        organizational_unit="organizationalUnit",
                        pseudonym="pseudonym",
                        serial_number="serialNumber",
                        state="state",
                        surname="surname",
                        title="title"
                    ),
                    dns_name="dnsName",
                    edi_party_name=acmpca.CfnCertificate.EdiPartyNameProperty(
                        name_assigner="nameAssigner",
                        party_name="partyName"
                    ),
                    ip_address="ipAddress",
                    other_name=acmpca.CfnCertificate.OtherNameProperty(
                        type_id="typeId",
                        value="value"
                    ),
                    registered_id="registeredId",
                    rfc822_name="rfc822Name",
                    uniform_resource_identifier="uniformResourceIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__430fe7518ff7ed70184671ff079a80b537708dad686da415fe31db2f83f9a991)
                check_type(argname="argument directory_name", value=directory_name, expected_type=type_hints["directory_name"])
                check_type(argname="argument dns_name", value=dns_name, expected_type=type_hints["dns_name"])
                check_type(argname="argument edi_party_name", value=edi_party_name, expected_type=type_hints["edi_party_name"])
                check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
                check_type(argname="argument other_name", value=other_name, expected_type=type_hints["other_name"])
                check_type(argname="argument registered_id", value=registered_id, expected_type=type_hints["registered_id"])
                check_type(argname="argument rfc822_name", value=rfc822_name, expected_type=type_hints["rfc822_name"])
                check_type(argname="argument uniform_resource_identifier", value=uniform_resource_identifier, expected_type=type_hints["uniform_resource_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if directory_name is not None:
                self._values["directory_name"] = directory_name
            if dns_name is not None:
                self._values["dns_name"] = dns_name
            if edi_party_name is not None:
                self._values["edi_party_name"] = edi_party_name
            if ip_address is not None:
                self._values["ip_address"] = ip_address
            if other_name is not None:
                self._values["other_name"] = other_name
            if registered_id is not None:
                self._values["registered_id"] = registered_id
            if rfc822_name is not None:
                self._values["rfc822_name"] = rfc822_name
            if uniform_resource_identifier is not None:
                self._values["uniform_resource_identifier"] = uniform_resource_identifier

        @builtins.property
        def directory_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.SubjectProperty"]]:
            '''Contains information about the certificate subject.

            The certificate can be one issued by your private certificate authority (CA) or it can be your private CA certificate. The Subject field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The Subject must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate. The DN must be unique for each entity, but your private CA can issue more than one certificate with the same DN to the same entity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-directoryname
            '''
            result = self._values.get("directory_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.SubjectProperty"]], result)

        @builtins.property
        def dns_name(self) -> typing.Optional[builtins.str]:
            '''Represents ``GeneralName`` as a DNS name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-dnsname
            '''
            result = self._values.get("dns_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def edi_party_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.EdiPartyNameProperty"]]:
            '''Represents ``GeneralName`` as an ``EdiPartyName`` object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-edipartyname
            '''
            result = self._values.get("edi_party_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.EdiPartyNameProperty"]], result)

        @builtins.property
        def ip_address(self) -> typing.Optional[builtins.str]:
            '''Represents ``GeneralName`` as an IPv4 or IPv6 address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-ipaddress
            '''
            result = self._values.get("ip_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def other_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.OtherNameProperty"]]:
            '''Represents ``GeneralName`` using an ``OtherName`` object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-othername
            '''
            result = self._values.get("other_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificate.OtherNameProperty"]], result)

        @builtins.property
        def registered_id(self) -> typing.Optional[builtins.str]:
            '''Represents ``GeneralName`` as an object identifier (OID).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-registeredid
            '''
            result = self._values.get("registered_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rfc822_name(self) -> typing.Optional[builtins.str]:
            '''Represents ``GeneralName`` as an `RFC 822 <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc822>`_ email address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-rfc822name
            '''
            result = self._values.get("rfc822_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def uniform_resource_identifier(self) -> typing.Optional[builtins.str]:
            '''Represents ``GeneralName`` as a URI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-uniformresourceidentifier
            '''
            result = self._values.get("uniform_resource_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeneralNameProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificate.KeyUsageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "crl_sign": "crlSign",
            "data_encipherment": "dataEncipherment",
            "decipher_only": "decipherOnly",
            "digital_signature": "digitalSignature",
            "encipher_only": "encipherOnly",
            "key_agreement": "keyAgreement",
            "key_cert_sign": "keyCertSign",
            "key_encipherment": "keyEncipherment",
            "non_repudiation": "nonRepudiation",
        },
    )
    class KeyUsageProperty:
        def __init__(
            self,
            *,
            crl_sign: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            data_encipherment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            decipher_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            digital_signature: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            encipher_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            key_agreement: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            key_cert_sign: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            key_encipherment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            non_repudiation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Defines one or more purposes for which the key contained in the certificate can be used.

            Default value for each option is false.

            :param crl_sign: Key can be used to sign CRLs. Default: - false
            :param data_encipherment: Key can be used to decipher data. Default: - false
            :param decipher_only: Key can be used only to decipher data. Default: - false
            :param digital_signature: Key can be used for digital signing. Default: - false
            :param encipher_only: Key can be used only to encipher data. Default: - false
            :param key_agreement: Key can be used in a key-agreement protocol. Default: - false
            :param key_cert_sign: Key can be used to sign certificates. Default: - false
            :param key_encipherment: Key can be used to encipher data. Default: - false
            :param non_repudiation: Key can be used for non-repudiation. Default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                key_usage_property = acmpca.CfnCertificate.KeyUsageProperty(
                    crl_sign=False,
                    data_encipherment=False,
                    decipher_only=False,
                    digital_signature=False,
                    encipher_only=False,
                    key_agreement=False,
                    key_cert_sign=False,
                    key_encipherment=False,
                    non_repudiation=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f50230a7e5fd5786670a469e1db1bb8ceadc1d39e95454db10bc795348abf38c)
                check_type(argname="argument crl_sign", value=crl_sign, expected_type=type_hints["crl_sign"])
                check_type(argname="argument data_encipherment", value=data_encipherment, expected_type=type_hints["data_encipherment"])
                check_type(argname="argument decipher_only", value=decipher_only, expected_type=type_hints["decipher_only"])
                check_type(argname="argument digital_signature", value=digital_signature, expected_type=type_hints["digital_signature"])
                check_type(argname="argument encipher_only", value=encipher_only, expected_type=type_hints["encipher_only"])
                check_type(argname="argument key_agreement", value=key_agreement, expected_type=type_hints["key_agreement"])
                check_type(argname="argument key_cert_sign", value=key_cert_sign, expected_type=type_hints["key_cert_sign"])
                check_type(argname="argument key_encipherment", value=key_encipherment, expected_type=type_hints["key_encipherment"])
                check_type(argname="argument non_repudiation", value=non_repudiation, expected_type=type_hints["non_repudiation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if crl_sign is not None:
                self._values["crl_sign"] = crl_sign
            if data_encipherment is not None:
                self._values["data_encipherment"] = data_encipherment
            if decipher_only is not None:
                self._values["decipher_only"] = decipher_only
            if digital_signature is not None:
                self._values["digital_signature"] = digital_signature
            if encipher_only is not None:
                self._values["encipher_only"] = encipher_only
            if key_agreement is not None:
                self._values["key_agreement"] = key_agreement
            if key_cert_sign is not None:
                self._values["key_cert_sign"] = key_cert_sign
            if key_encipherment is not None:
                self._values["key_encipherment"] = key_encipherment
            if non_repudiation is not None:
                self._values["non_repudiation"] = non_repudiation

        @builtins.property
        def crl_sign(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used to sign CRLs.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-crlsign
            '''
            result = self._values.get("crl_sign")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def data_encipherment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used to decipher data.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-dataencipherment
            '''
            result = self._values.get("data_encipherment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def decipher_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used only to decipher data.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-decipheronly
            '''
            result = self._values.get("decipher_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def digital_signature(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used for digital signing.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-digitalsignature
            '''
            result = self._values.get("digital_signature")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def encipher_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used only to encipher data.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-encipheronly
            '''
            result = self._values.get("encipher_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def key_agreement(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used in a key-agreement protocol.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-keyagreement
            '''
            result = self._values.get("key_agreement")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def key_cert_sign(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used to sign certificates.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-keycertsign
            '''
            result = self._values.get("key_cert_sign")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def key_encipherment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used to encipher data.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-keyencipherment
            '''
            result = self._values.get("key_encipherment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def non_repudiation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used for non-repudiation.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-nonrepudiation
            '''
            result = self._values.get("non_repudiation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyUsageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificate.OtherNameProperty",
        jsii_struct_bases=[],
        name_mapping={"type_id": "typeId", "value": "value"},
    )
    class OtherNameProperty:
        def __init__(self, *, type_id: builtins.str, value: builtins.str) -> None:
            '''Defines a custom ASN.1 X.400 ``GeneralName`` using an object identifier (OID) and value. The OID must satisfy the regular expression shown below. For more information, see NIST's definition of `Object Identifier (OID) <https://docs.aws.amazon.com/https://csrc.nist.gov/glossary/term/Object_Identifier>`_ .

            :param type_id: Specifies an OID.
            :param value: Specifies an OID value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-othername.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                other_name_property = acmpca.CfnCertificate.OtherNameProperty(
                    type_id="typeId",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__620191e18964b334afd3f451ecad5f454c321164e05b6bdb1f75897c2ea3f73f)
                check_type(argname="argument type_id", value=type_id, expected_type=type_hints["type_id"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type_id": type_id,
                "value": value,
            }

        @builtins.property
        def type_id(self) -> builtins.str:
            '''Specifies an OID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-othername.html#cfn-acmpca-certificate-othername-typeid
            '''
            result = self._values.get("type_id")
            assert result is not None, "Required property 'type_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''Specifies an OID value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-othername.html#cfn-acmpca-certificate-othername-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OtherNameProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificate.PolicyInformationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cert_policy_id": "certPolicyId",
            "policy_qualifiers": "policyQualifiers",
        },
    )
    class PolicyInformationProperty:
        def __init__(
            self,
            *,
            cert_policy_id: builtins.str,
            policy_qualifiers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.PolicyQualifierInfoProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Defines the X.509 ``CertificatePolicies`` extension.

            :param cert_policy_id: Specifies the object identifier (OID) of the certificate policy under which the certificate was issued. For more information, see NIST's definition of `Object Identifier (OID) <https://docs.aws.amazon.com/https://csrc.nist.gov/glossary/term/Object_Identifier>`_ .
            :param policy_qualifiers: Modifies the given ``CertPolicyId`` with a qualifier. AWS Private CA supports the certification practice statement (CPS) qualifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyinformation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                policy_information_property = acmpca.CfnCertificate.PolicyInformationProperty(
                    cert_policy_id="certPolicyId",
                
                    # the properties below are optional
                    policy_qualifiers=[acmpca.CfnCertificate.PolicyQualifierInfoProperty(
                        policy_qualifier_id="policyQualifierId",
                        qualifier=acmpca.CfnCertificate.QualifierProperty(
                            cps_uri="cpsUri"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d0fa8861568fe4db83bd309e3f4d649fe7756fe2dd1ed1ee0ef9fbd24abf8d32)
                check_type(argname="argument cert_policy_id", value=cert_policy_id, expected_type=type_hints["cert_policy_id"])
                check_type(argname="argument policy_qualifiers", value=policy_qualifiers, expected_type=type_hints["policy_qualifiers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cert_policy_id": cert_policy_id,
            }
            if policy_qualifiers is not None:
                self._values["policy_qualifiers"] = policy_qualifiers

        @builtins.property
        def cert_policy_id(self) -> builtins.str:
            '''Specifies the object identifier (OID) of the certificate policy under which the certificate was issued.

            For more information, see NIST's definition of `Object Identifier (OID) <https://docs.aws.amazon.com/https://csrc.nist.gov/glossary/term/Object_Identifier>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyinformation.html#cfn-acmpca-certificate-policyinformation-certpolicyid
            '''
            result = self._values.get("cert_policy_id")
            assert result is not None, "Required property 'cert_policy_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def policy_qualifiers(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificate.PolicyQualifierInfoProperty"]]]]:
            '''Modifies the given ``CertPolicyId`` with a qualifier.

            AWS Private CA supports the certification practice statement (CPS) qualifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyinformation.html#cfn-acmpca-certificate-policyinformation-policyqualifiers
            '''
            result = self._values.get("policy_qualifiers")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificate.PolicyQualifierInfoProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyInformationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificate.PolicyQualifierInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "policy_qualifier_id": "policyQualifierId",
            "qualifier": "qualifier",
        },
    )
    class PolicyQualifierInfoProperty:
        def __init__(
            self,
            *,
            policy_qualifier_id: builtins.str,
            qualifier: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.QualifierProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Modifies the ``CertPolicyId`` of a ``PolicyInformation`` object with a qualifier.

            AWS Private CA supports the certification practice statement (CPS) qualifier.

            :param policy_qualifier_id: Identifies the qualifier modifying a ``CertPolicyId`` .
            :param qualifier: Defines the qualifier type. AWS Private CA supports the use of a URI for a CPS qualifier in this field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyqualifierinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                policy_qualifier_info_property = acmpca.CfnCertificate.PolicyQualifierInfoProperty(
                    policy_qualifier_id="policyQualifierId",
                    qualifier=acmpca.CfnCertificate.QualifierProperty(
                        cps_uri="cpsUri"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b0e7f8f4f896a22f7904c707eeac3e27d496db6421b2ec5f4494b75be75f9670)
                check_type(argname="argument policy_qualifier_id", value=policy_qualifier_id, expected_type=type_hints["policy_qualifier_id"])
                check_type(argname="argument qualifier", value=qualifier, expected_type=type_hints["qualifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "policy_qualifier_id": policy_qualifier_id,
                "qualifier": qualifier,
            }

        @builtins.property
        def policy_qualifier_id(self) -> builtins.str:
            '''Identifies the qualifier modifying a ``CertPolicyId`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyqualifierinfo.html#cfn-acmpca-certificate-policyqualifierinfo-policyqualifierid
            '''
            result = self._values.get("policy_qualifier_id")
            assert result is not None, "Required property 'policy_qualifier_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def qualifier(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCertificate.QualifierProperty"]:
            '''Defines the qualifier type.

            AWS Private CA supports the use of a URI for a CPS qualifier in this field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyqualifierinfo.html#cfn-acmpca-certificate-policyqualifierinfo-qualifier
            '''
            result = self._values.get("qualifier")
            assert result is not None, "Required property 'qualifier' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCertificate.QualifierProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyQualifierInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificate.QualifierProperty",
        jsii_struct_bases=[],
        name_mapping={"cps_uri": "cpsUri"},
    )
    class QualifierProperty:
        def __init__(self, *, cps_uri: builtins.str) -> None:
            '''Defines a ``PolicyInformation`` qualifier.

            AWS Private CA supports the `certification practice statement (CPS) qualifier <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.4>`_ defined in RFC 5280.

            :param cps_uri: Contains a pointer to a certification practice statement (CPS) published by the CA.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-qualifier.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                qualifier_property = acmpca.CfnCertificate.QualifierProperty(
                    cps_uri="cpsUri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__48eb999ea7bed23111f3eabf8a679cdc5d044a7c3764f62d64d132c1815c3ec4)
                check_type(argname="argument cps_uri", value=cps_uri, expected_type=type_hints["cps_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cps_uri": cps_uri,
            }

        @builtins.property
        def cps_uri(self) -> builtins.str:
            '''Contains a pointer to a certification practice statement (CPS) published by the CA.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-qualifier.html#cfn-acmpca-certificate-qualifier-cpsuri
            '''
            result = self._values.get("cps_uri")
            assert result is not None, "Required property 'cps_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QualifierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificate.SubjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "common_name": "commonName",
            "country": "country",
            "custom_attributes": "customAttributes",
            "distinguished_name_qualifier": "distinguishedNameQualifier",
            "generation_qualifier": "generationQualifier",
            "given_name": "givenName",
            "initials": "initials",
            "locality": "locality",
            "organization": "organization",
            "organizational_unit": "organizationalUnit",
            "pseudonym": "pseudonym",
            "serial_number": "serialNumber",
            "state": "state",
            "surname": "surname",
            "title": "title",
        },
    )
    class SubjectProperty:
        def __init__(
            self,
            *,
            common_name: typing.Optional[builtins.str] = None,
            country: typing.Optional[builtins.str] = None,
            custom_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.CustomAttributeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            distinguished_name_qualifier: typing.Optional[builtins.str] = None,
            generation_qualifier: typing.Optional[builtins.str] = None,
            given_name: typing.Optional[builtins.str] = None,
            initials: typing.Optional[builtins.str] = None,
            locality: typing.Optional[builtins.str] = None,
            organization: typing.Optional[builtins.str] = None,
            organizational_unit: typing.Optional[builtins.str] = None,
            pseudonym: typing.Optional[builtins.str] = None,
            serial_number: typing.Optional[builtins.str] = None,
            state: typing.Optional[builtins.str] = None,
            surname: typing.Optional[builtins.str] = None,
            title: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about the certificate subject.

            The ``Subject`` field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The ``Subject`` must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate.

            :param common_name: For CA and end-entity certificates in a private PKI, the common name (CN) can be any string within the length limit. Note: In publicly trusted certificates, the common name must be a fully qualified domain name (FQDN) associated with the certificate subject.
            :param country: Two-digit code that specifies the country in which the certificate subject located.
            :param custom_attributes: Contains a sequence of one or more X.500 relative distinguished names (RDNs), each of which consists of an object identifier (OID) and a value. For more information, see NIST’s definition of `Object Identifier (OID) <https://docs.aws.amazon.com/https://csrc.nist.gov/glossary/term/Object_Identifier>`_ . .. epigraph:: Custom attributes cannot be used in combination with standard attributes.
            :param distinguished_name_qualifier: Disambiguating information for the certificate subject.
            :param generation_qualifier: Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.
            :param given_name: First name.
            :param initials: Concatenation that typically contains the first letter of the *GivenName* , the first letter of the middle name if one exists, and the first letter of the *Surname* .
            :param locality: The locality (such as a city or town) in which the certificate subject is located.
            :param organization: Legal name of the organization with which the certificate subject is affiliated.
            :param organizational_unit: A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.
            :param pseudonym: Typically a shortened version of a longer *GivenName* . For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.
            :param serial_number: The certificate serial number.
            :param state: State in which the subject of the certificate is located.
            :param surname: Family name. In the US and the UK, for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.
            :param title: A title such as Mr. or Ms., which is pre-pended to the name to refer formally to the certificate subject.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                subject_property = acmpca.CfnCertificate.SubjectProperty(
                    common_name="commonName",
                    country="country",
                    custom_attributes=[acmpca.CfnCertificate.CustomAttributeProperty(
                        object_identifier="objectIdentifier",
                        value="value"
                    )],
                    distinguished_name_qualifier="distinguishedNameQualifier",
                    generation_qualifier="generationQualifier",
                    given_name="givenName",
                    initials="initials",
                    locality="locality",
                    organization="organization",
                    organizational_unit="organizationalUnit",
                    pseudonym="pseudonym",
                    serial_number="serialNumber",
                    state="state",
                    surname="surname",
                    title="title"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d2b7efde7b9d2e6233f33ab24f10ede12022114a34cf3d75ff1d1bf6b8283a93)
                check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
                check_type(argname="argument country", value=country, expected_type=type_hints["country"])
                check_type(argname="argument custom_attributes", value=custom_attributes, expected_type=type_hints["custom_attributes"])
                check_type(argname="argument distinguished_name_qualifier", value=distinguished_name_qualifier, expected_type=type_hints["distinguished_name_qualifier"])
                check_type(argname="argument generation_qualifier", value=generation_qualifier, expected_type=type_hints["generation_qualifier"])
                check_type(argname="argument given_name", value=given_name, expected_type=type_hints["given_name"])
                check_type(argname="argument initials", value=initials, expected_type=type_hints["initials"])
                check_type(argname="argument locality", value=locality, expected_type=type_hints["locality"])
                check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
                check_type(argname="argument organizational_unit", value=organizational_unit, expected_type=type_hints["organizational_unit"])
                check_type(argname="argument pseudonym", value=pseudonym, expected_type=type_hints["pseudonym"])
                check_type(argname="argument serial_number", value=serial_number, expected_type=type_hints["serial_number"])
                check_type(argname="argument state", value=state, expected_type=type_hints["state"])
                check_type(argname="argument surname", value=surname, expected_type=type_hints["surname"])
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if common_name is not None:
                self._values["common_name"] = common_name
            if country is not None:
                self._values["country"] = country
            if custom_attributes is not None:
                self._values["custom_attributes"] = custom_attributes
            if distinguished_name_qualifier is not None:
                self._values["distinguished_name_qualifier"] = distinguished_name_qualifier
            if generation_qualifier is not None:
                self._values["generation_qualifier"] = generation_qualifier
            if given_name is not None:
                self._values["given_name"] = given_name
            if initials is not None:
                self._values["initials"] = initials
            if locality is not None:
                self._values["locality"] = locality
            if organization is not None:
                self._values["organization"] = organization
            if organizational_unit is not None:
                self._values["organizational_unit"] = organizational_unit
            if pseudonym is not None:
                self._values["pseudonym"] = pseudonym
            if serial_number is not None:
                self._values["serial_number"] = serial_number
            if state is not None:
                self._values["state"] = state
            if surname is not None:
                self._values["surname"] = surname
            if title is not None:
                self._values["title"] = title

        @builtins.property
        def common_name(self) -> typing.Optional[builtins.str]:
            '''For CA and end-entity certificates in a private PKI, the common name (CN) can be any string within the length limit.

            Note: In publicly trusted certificates, the common name must be a fully qualified domain name (FQDN) associated with the certificate subject.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-commonname
            '''
            result = self._values.get("common_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def country(self) -> typing.Optional[builtins.str]:
            '''Two-digit code that specifies the country in which the certificate subject located.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-country
            '''
            result = self._values.get("country")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificate.CustomAttributeProperty"]]]]:
            '''Contains a sequence of one or more X.500 relative distinguished names (RDNs), each of which consists of an object identifier (OID) and a value. For more information, see NIST’s definition of `Object Identifier (OID) <https://docs.aws.amazon.com/https://csrc.nist.gov/glossary/term/Object_Identifier>`_ .

            .. epigraph::

               Custom attributes cannot be used in combination with standard attributes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-customattributes
            '''
            result = self._values.get("custom_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificate.CustomAttributeProperty"]]]], result)

        @builtins.property
        def distinguished_name_qualifier(self) -> typing.Optional[builtins.str]:
            '''Disambiguating information for the certificate subject.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-distinguishednamequalifier
            '''
            result = self._values.get("distinguished_name_qualifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def generation_qualifier(self) -> typing.Optional[builtins.str]:
            '''Typically a qualifier appended to the name of an individual.

            Examples include Jr. for junior, Sr. for senior, and III for third.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-generationqualifier
            '''
            result = self._values.get("generation_qualifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def given_name(self) -> typing.Optional[builtins.str]:
            '''First name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-givenname
            '''
            result = self._values.get("given_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def initials(self) -> typing.Optional[builtins.str]:
            '''Concatenation that typically contains the first letter of the *GivenName* , the first letter of the middle name if one exists, and the first letter of the *Surname* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-initials
            '''
            result = self._values.get("initials")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def locality(self) -> typing.Optional[builtins.str]:
            '''The locality (such as a city or town) in which the certificate subject is located.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-locality
            '''
            result = self._values.get("locality")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organization(self) -> typing.Optional[builtins.str]:
            '''Legal name of the organization with which the certificate subject is affiliated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-organization
            '''
            result = self._values.get("organization")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organizational_unit(self) -> typing.Optional[builtins.str]:
            '''A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-organizationalunit
            '''
            result = self._values.get("organizational_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pseudonym(self) -> typing.Optional[builtins.str]:
            '''Typically a shortened version of a longer *GivenName* .

            For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-pseudonym
            '''
            result = self._values.get("pseudonym")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def serial_number(self) -> typing.Optional[builtins.str]:
            '''The certificate serial number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-serialnumber
            '''
            result = self._values.get("serial_number")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''State in which the subject of the certificate is located.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def surname(self) -> typing.Optional[builtins.str]:
            '''Family name.

            In the US and the UK, for example, the surname of an individual is ordered last. In Asian cultures the surname is typically ordered first.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-surname
            '''
            result = self._values.get("surname")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def title(self) -> typing.Optional[builtins.str]:
            '''A title such as Mr.

            or Ms., which is pre-pended to the name to refer formally to the certificate subject.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificate.ValidityProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class ValidityProperty:
        def __init__(self, *, type: builtins.str, value: jsii.Number) -> None:
            '''Length of time for which the certificate issued by your private certificate authority (CA), or by the private CA itself, is valid in days, months, or years.

            You can issue a certificate by calling the ``IssueCertificate`` operation.

            :param type: Specifies whether the ``Value`` parameter represents days, months, or years.
            :param value: A long integer interpreted according to the value of ``Type`` , below.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-validity.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                validity_property = acmpca.CfnCertificate.ValidityProperty(
                    type="type",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__843e728892e8512a7c481feaede4179f4288a992c2488e36dd55acf5618446bd)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''Specifies whether the ``Value`` parameter represents days, months, or years.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-validity.html#cfn-acmpca-certificate-validity-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''A long integer interpreted according to the value of ``Type`` , below.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-validity.html#cfn-acmpca-certificate-validity-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValidityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCertificateAuthority(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthority",
):
    '''Use the ``AWS::ACMPCA::CertificateAuthority`` resource to create a private CA.

    Once the CA exists, you can use the ``AWS::ACMPCA::Certificate`` resource to issue a new CA certificate. Alternatively, you can issue a CA certificate using an on-premises CA, and then use the ``AWS::ACMPCA::CertificateAuthorityActivation`` resource to import the new CA certificate and activate the CA.
    .. epigraph::

       Before removing a ``AWS::ACMPCA::CertificateAuthority`` resource from the CloudFormation stack, disable the affected CA. Otherwise, the action will fail. You can disable the CA by removing its associated ``AWS::ACMPCA::CertificateAuthorityActivation`` resource from CloudFormation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html
    :exampleMetadata: infused

    Example::

        cfn_certificate_authority = acmpca.CfnCertificateAuthority(self, "CA",
            type="ROOT",
            key_algorithm="RSA_2048",
            signing_algorithm="SHA256WITHRSA",
            subject=acmpca.CfnCertificateAuthority.SubjectProperty(
                country="US",
                organization="string",
                organizational_unit="string",
                distinguished_name_qualifier="string",
                state="string",
                common_name="123",
                serial_number="string",
                locality="string",
                title="string",
                surname="string",
                given_name="string",
                initials="DG",
                pseudonym="string",
                generation_qualifier="DBG"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        key_algorithm: builtins.str,
        signing_algorithm: builtins.str,
        subject: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificateAuthority.SubjectProperty", typing.Dict[builtins.str, typing.Any]]],
        type: builtins.str,
        csr_extensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificateAuthority.CsrExtensionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        key_storage_security_standard: typing.Optional[builtins.str] = None,
        revocation_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificateAuthority.RevocationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        usage_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param key_algorithm: Type of the public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate. When you create a subordinate CA, you must use a key algorithm supported by the parent CA.
        :param signing_algorithm: Name of the algorithm your private CA uses to sign certificate requests. This parameter should not be confused with the ``SigningAlgorithm`` parameter used to sign certificates when they are issued.
        :param subject: Structure that contains X.500 distinguished name information for your private CA.
        :param type: Type of your private CA.
        :param csr_extensions: Specifies information to be added to the extension section of the certificate signing request (CSR).
        :param key_storage_security_standard: Specifies a cryptographic key management compliance standard used for handling CA keys. Default: FIPS_140_2_LEVEL_3_OR_HIGHER .. epigraph:: Some AWS Regions do not support the default. When creating a CA in these Regions, you must provide ``FIPS_140_2_LEVEL_2_OR_HIGHER`` as the argument for ``KeyStorageSecurityStandard`` . Failure to do this results in an ``InvalidArgsException`` with the message, "A certificate authority cannot be created in this region with the specified security standard." For information about security standard support in various Regions, see `Storage and security compliance of AWS Private CA private keys <https://docs.aws.amazon.com/privateca/latest/userguide/data-protection.html#private-keys>`_ .
        :param revocation_configuration: Certificate revocation information used by the `CreateCertificateAuthority <https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html>`_ and `UpdateCertificateAuthority <https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html>`_ actions. Your private certificate authority (CA) can configure Online Certificate Status Protocol (OCSP) support and/or maintain a certificate revocation list (CRL). OCSP returns validation information about certificates as requested by clients, and a CRL contains an updated list of certificates revoked by your CA. For more information, see `RevokeCertificate <https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html>`_ in the *AWS Private CA API Reference* and `Setting up a certificate revocation method <https://docs.aws.amazon.com/privateca/latest/userguide/revocation-setup.html>`_ in the *AWS Private CA User Guide* . .. epigraph:: The following requirements apply to revocation configurations. - A configuration disabling CRLs or OCSP must contain only the ``Enabled=False`` parameter, and will fail if other parameters such as ``CustomCname`` or ``ExpirationInDays`` are included. - In a CRL configuration, the ``S3BucketName`` parameter must conform to the `Amazon S3 bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html>`_ . - A configuration containing a custom Canonical Name (CNAME) parameter for CRLs or OCSP must conform to `RFC2396 <https://docs.aws.amazon.com/https://www.ietf.org/rfc/rfc2396.txt>`_ restrictions on the use of special characters in a CNAME. - In a CRL or OCSP configuration, the value of a CNAME parameter must not include a protocol prefix such as "http://" or "https://".
        :param tags: Key-value pairs that will be attached to the new private CA. You can associate up to 50 tags with a private CA. For information using tags with IAM to manage permissions, see `Controlling Access Using IAM Tags <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html>`_ .
        :param usage_mode: Specifies whether the CA issues general-purpose certificates that typically require a revocation mechanism, or short-lived certificates that may optionally omit revocation because they expire quickly. Short-lived certificate validity is limited to seven days. The default value is GENERAL_PURPOSE.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6947ebcc03e9e02f9fc5dee73eaa3cd88dd10713851f61d2ce61f6210abfb16)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCertificateAuthorityProps(
            key_algorithm=key_algorithm,
            signing_algorithm=signing_algorithm,
            subject=subject,
            type=type,
            csr_extensions=csr_extensions,
            key_storage_security_standard=key_storage_security_standard,
            revocation_configuration=revocation_configuration,
            tags=tags,
            usage_mode=usage_mode,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97a6fe8ac6bf6021d6476713901b5d434081cdc009d802a3f665c0611673e27e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__20898061f346ffdc7eeb4ea9b7e48dcc46ae909c1b748cd318e50ca8408327e8)
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
        '''The Amazon Resource Name (ARN) for the private CA that issued the certificate.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCertificateSigningRequest")
    def attr_certificate_signing_request(self) -> builtins.str:
        '''The Base64 PEM-encoded certificate signing request (CSR) for your certificate authority certificate.

        :cloudformationAttribute: CertificateSigningRequest
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCertificateSigningRequest"))

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
    @jsii.member(jsii_name="keyAlgorithm")
    def key_algorithm(self) -> builtins.str:
        '''Type of the public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate.'''
        return typing.cast(builtins.str, jsii.get(self, "keyAlgorithm"))

    @key_algorithm.setter
    def key_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7e6c5981edef9a3b3627b2003de2630869e19cd61c48d608bfd86a7f219e472)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="signingAlgorithm")
    def signing_algorithm(self) -> builtins.str:
        '''Name of the algorithm your private CA uses to sign certificate requests.'''
        return typing.cast(builtins.str, jsii.get(self, "signingAlgorithm"))

    @signing_algorithm.setter
    def signing_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7e2832fbc61e46c30f08119509dacf6b15d90881721ef6f70b6331442b62041)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signingAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.SubjectProperty"]:
        '''Structure that contains X.500 distinguished name information for your private CA.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.SubjectProperty"], jsii.get(self, "subject"))

    @subject.setter
    def subject(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.SubjectProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65bb497527ac064e6e2dac08377e39c6239f7e846ca18078132927a75d6471bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subject", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''Type of your private CA.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77017d7803db08d3adb6df13436c6f61e9248dba04cb27f3ad2c009449c54235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="csrExtensions")
    def csr_extensions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.CsrExtensionsProperty"]]:
        '''Specifies information to be added to the extension section of the certificate signing request (CSR).'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.CsrExtensionsProperty"]], jsii.get(self, "csrExtensions"))

    @csr_extensions.setter
    def csr_extensions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.CsrExtensionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__672400fc9d101cb3557ef2b74a3ed2c3389e8f619013c4b2a84263707b9ad5d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csrExtensions", value)

    @builtins.property
    @jsii.member(jsii_name="keyStorageSecurityStandard")
    def key_storage_security_standard(self) -> typing.Optional[builtins.str]:
        '''Specifies a cryptographic key management compliance standard used for handling CA keys.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyStorageSecurityStandard"))

    @key_storage_security_standard.setter
    def key_storage_security_standard(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be8e4d5ae1e7416c87aef05e06dfd53984f27b32f1d6ac821bb176da70ccf89f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyStorageSecurityStandard", value)

    @builtins.property
    @jsii.member(jsii_name="revocationConfiguration")
    def revocation_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.RevocationConfigurationProperty"]]:
        '''Certificate revocation information used by the `CreateCertificateAuthority <https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html>`_ and `UpdateCertificateAuthority <https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html>`_ actions. Your private certificate authority (CA) can configure Online Certificate Status Protocol (OCSP) support and/or maintain a certificate revocation list (CRL). OCSP returns validation information about certificates as requested by clients, and a CRL contains an updated list of certificates revoked by your CA. For more information, see `RevokeCertificate <https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html>`_ in the *AWS Private CA API Reference* and `Setting up a certificate revocation method <https://docs.aws.amazon.com/privateca/latest/userguide/revocation-setup.html>`_ in the *AWS Private CA User Guide* .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.RevocationConfigurationProperty"]], jsii.get(self, "revocationConfiguration"))

    @revocation_configuration.setter
    def revocation_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.RevocationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__203567ece18e0659c536811874601c021c570afc77b0834d25d2e06ac2849f57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revocationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that will be attached to the new private CA.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01bad6d3cb4db9f6f71a433aa44c7435297b8f644c8fdcbe06a0550035a76fa5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="usageMode")
    def usage_mode(self) -> typing.Optional[builtins.str]:
        '''Specifies whether the CA issues general-purpose certificates that typically require a revocation mechanism, or short-lived certificates that may optionally omit revocation because they expire quickly.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usageMode"))

    @usage_mode.setter
    def usage_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d183c3c1616f42e791fb50dd3640b6710dbdb67c4b67d83635a3687f5abb9d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usageMode", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthority.AccessDescriptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_location": "accessLocation",
            "access_method": "accessMethod",
        },
    )
    class AccessDescriptionProperty:
        def __init__(
            self,
            *,
            access_location: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificateAuthority.GeneralNameProperty", typing.Dict[builtins.str, typing.Any]]],
            access_method: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificateAuthority.AccessMethodProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Provides access information used by the ``authorityInfoAccess`` and ``subjectInfoAccess`` extensions described in `RFC 5280 <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc5280>`_ .

            :param access_location: The location of ``AccessDescription`` information.
            :param access_method: The type and format of ``AccessDescription`` information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessdescription.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                access_description_property = acmpca.CfnCertificateAuthority.AccessDescriptionProperty(
                    access_location=acmpca.CfnCertificateAuthority.GeneralNameProperty(
                        directory_name=acmpca.CfnCertificateAuthority.SubjectProperty(
                            common_name="commonName",
                            country="country",
                            custom_attributes=[acmpca.CfnCertificateAuthority.CustomAttributeProperty(
                                object_identifier="objectIdentifier",
                                value="value"
                            )],
                            distinguished_name_qualifier="distinguishedNameQualifier",
                            generation_qualifier="generationQualifier",
                            given_name="givenName",
                            initials="initials",
                            locality="locality",
                            organization="organization",
                            organizational_unit="organizationalUnit",
                            pseudonym="pseudonym",
                            serial_number="serialNumber",
                            state="state",
                            surname="surname",
                            title="title"
                        ),
                        dns_name="dnsName",
                        edi_party_name=acmpca.CfnCertificateAuthority.EdiPartyNameProperty(
                            name_assigner="nameAssigner",
                            party_name="partyName"
                        ),
                        ip_address="ipAddress",
                        other_name=acmpca.CfnCertificateAuthority.OtherNameProperty(
                            type_id="typeId",
                            value="value"
                        ),
                        registered_id="registeredId",
                        rfc822_name="rfc822Name",
                        uniform_resource_identifier="uniformResourceIdentifier"
                    ),
                    access_method=acmpca.CfnCertificateAuthority.AccessMethodProperty(
                        access_method_type="accessMethodType",
                        custom_object_identifier="customObjectIdentifier"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__44464105e0a77464936471a53d0b7f113a7a84bceeeb9b081b7a817472f3c88c)
                check_type(argname="argument access_location", value=access_location, expected_type=type_hints["access_location"])
                check_type(argname="argument access_method", value=access_method, expected_type=type_hints["access_method"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "access_location": access_location,
                "access_method": access_method,
            }

        @builtins.property
        def access_location(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.GeneralNameProperty"]:
            '''The location of ``AccessDescription`` information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessdescription.html#cfn-acmpca-certificateauthority-accessdescription-accesslocation
            '''
            result = self._values.get("access_location")
            assert result is not None, "Required property 'access_location' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.GeneralNameProperty"], result)

        @builtins.property
        def access_method(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.AccessMethodProperty"]:
            '''The type and format of ``AccessDescription`` information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessdescription.html#cfn-acmpca-certificateauthority-accessdescription-accessmethod
            '''
            result = self._values.get("access_method")
            assert result is not None, "Required property 'access_method' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.AccessMethodProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessDescriptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthority.AccessMethodProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_method_type": "accessMethodType",
            "custom_object_identifier": "customObjectIdentifier",
        },
    )
    class AccessMethodProperty:
        def __init__(
            self,
            *,
            access_method_type: typing.Optional[builtins.str] = None,
            custom_object_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the type and format of extension access.

            Only one of ``CustomObjectIdentifier`` or ``AccessMethodType`` may be provided. Providing both results in ``InvalidArgsException`` .

            :param access_method_type: Specifies the ``AccessMethod`` .
            :param custom_object_identifier: An object identifier (OID) specifying the ``AccessMethod`` . The OID must satisfy the regular expression shown below. For more information, see NIST's definition of `Object Identifier (OID) <https://docs.aws.amazon.com/https://csrc.nist.gov/glossary/term/Object_Identifier>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessmethod.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                access_method_property = acmpca.CfnCertificateAuthority.AccessMethodProperty(
                    access_method_type="accessMethodType",
                    custom_object_identifier="customObjectIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a665d65bdd95c9f57ee7ca3fee24e377b63436ab67f86d6e09696910c191d3e2)
                check_type(argname="argument access_method_type", value=access_method_type, expected_type=type_hints["access_method_type"])
                check_type(argname="argument custom_object_identifier", value=custom_object_identifier, expected_type=type_hints["custom_object_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_method_type is not None:
                self._values["access_method_type"] = access_method_type
            if custom_object_identifier is not None:
                self._values["custom_object_identifier"] = custom_object_identifier

        @builtins.property
        def access_method_type(self) -> typing.Optional[builtins.str]:
            '''Specifies the ``AccessMethod`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessmethod.html#cfn-acmpca-certificateauthority-accessmethod-accessmethodtype
            '''
            result = self._values.get("access_method_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_object_identifier(self) -> typing.Optional[builtins.str]:
            '''An object identifier (OID) specifying the ``AccessMethod`` .

            The OID must satisfy the regular expression shown below. For more information, see NIST's definition of `Object Identifier (OID) <https://docs.aws.amazon.com/https://csrc.nist.gov/glossary/term/Object_Identifier>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessmethod.html#cfn-acmpca-certificateauthority-accessmethod-customobjectidentifier
            '''
            result = self._values.get("custom_object_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessMethodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthority.CrlConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_cname": "customCname",
            "enabled": "enabled",
            "expiration_in_days": "expirationInDays",
            "s3_bucket_name": "s3BucketName",
            "s3_object_acl": "s3ObjectAcl",
        },
    )
    class CrlConfigurationProperty:
        def __init__(
            self,
            *,
            custom_cname: typing.Optional[builtins.str] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            expiration_in_days: typing.Optional[jsii.Number] = None,
            s3_bucket_name: typing.Optional[builtins.str] = None,
            s3_object_acl: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains configuration information for a certificate revocation list (CRL).

            Your private certificate authority (CA) creates base CRLs. Delta CRLs are not supported. You can enable CRLs for your new or an existing private CA by setting the *Enabled* parameter to ``true`` . Your private CA writes CRLs to an S3 bucket that you specify in the *S3BucketName* parameter. You can hide the name of your bucket by specifying a value for the *CustomCname* parameter. Your private CA copies the CNAME or the S3 bucket name to the *CRL Distribution Points* extension of each certificate it issues. Your S3 bucket policy must give write permission to AWS Private CA.

            AWS Private CA assets that are stored in Amazon S3 can be protected with encryption. For more information, see `Encrypting Your CRLs <https://docs.aws.amazon.com/privateca/latest/userguide/PcaCreateCa.html#crl-encryption>`_ .

            Your private CA uses the value in the *ExpirationInDays* parameter to calculate the *nextUpdate* field in the CRL. The CRL is refreshed prior to a certificate's expiration date or when a certificate is revoked. When a certificate is revoked, it appears in the CRL until the certificate expires, and then in one additional CRL after expiration, and it always appears in the audit report.

            A CRL is typically updated approximately 30 minutes after a certificate is revoked. If for any reason a CRL update fails, AWS Private CA makes further attempts every 15 minutes.

            CRLs contain the following fields:

            - *Version* : The current version number defined in RFC 5280 is V2. The integer value is 0x1.
            - *Signature Algorithm* : The name of the algorithm used to sign the CRL.
            - *Issuer* : The X.500 distinguished name of your private CA that issued the CRL.
            - *Last Update* : The issue date and time of this CRL.
            - *Next Update* : The day and time by which the next CRL will be issued.
            - *Revoked Certificates* : List of revoked certificates. Each list item contains the following information.
            - *Serial Number* : The serial number, in hexadecimal format, of the revoked certificate.
            - *Revocation Date* : Date and time the certificate was revoked.
            - *CRL Entry Extensions* : Optional extensions for the CRL entry.
            - *X509v3 CRL Reason Code* : Reason the certificate was revoked.
            - *CRL Extensions* : Optional extensions for the CRL.
            - *X509v3 Authority Key Identifier* : Identifies the public key associated with the private key used to sign the certificate.
            - *X509v3 CRL Number:* : Decimal sequence number for the CRL.
            - *Signature Algorithm* : Algorithm used by your private CA to sign the CRL.
            - *Signature Value* : Signature computed over the CRL.

            Certificate revocation lists created by AWS Private CA are DER-encoded. You can use the following OpenSSL command to list a CRL.

            ``openssl crl -inform DER -text -in *crl_path* -noout``

            For more information, see `Planning a certificate revocation list (CRL) <https://docs.aws.amazon.com/privateca/latest/userguide/crl-planning.html>`_ in the *AWS Private Certificate Authority User Guide*

            :param custom_cname: Name inserted into the certificate *CRL Distribution Points* extension that enables the use of an alias for the CRL distribution point. Use this value if you don't want the name of your S3 bucket to be public. .. epigraph:: The content of a Canonical Name (CNAME) record must conform to `RFC2396 <https://docs.aws.amazon.com/https://www.ietf.org/rfc/rfc2396.txt>`_ restrictions on the use of special characters in URIs. Additionally, the value of the CNAME must not include a protocol prefix such as "http://" or "https://".
            :param enabled: Boolean value that specifies whether certificate revocation lists (CRLs) are enabled. You can use this value to enable certificate revocation for a new CA when you call the ``CreateCertificateAuthority`` operation or for an existing CA when you call the ``UpdateCertificateAuthority`` operation.
            :param expiration_in_days: Validity period of the CRL in days.
            :param s3_bucket_name: Name of the S3 bucket that contains the CRL. If you do not provide a value for the *CustomCname* argument, the name of your S3 bucket is placed into the *CRL Distribution Points* extension of the issued certificate. You can change the name of your bucket by calling the `UpdateCertificateAuthority <https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html>`_ operation. You must specify a `bucket policy <https://docs.aws.amazon.com/privateca/latest/userguide/PcaCreateCa.html#s3-policies>`_ that allows AWS Private CA to write the CRL to your bucket. .. epigraph:: The ``S3BucketName`` parameter must conform to the `S3 bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html>`_ .
            :param s3_object_acl: Determines whether the CRL will be publicly readable or privately held in the CRL Amazon S3 bucket. If you choose PUBLIC_READ, the CRL will be accessible over the public internet. If you choose BUCKET_OWNER_FULL_CONTROL, only the owner of the CRL S3 bucket can access the CRL, and your PKI clients may need an alternative method of access. If no value is specified, the default is PUBLIC_READ. *Note:* This default can cause CA creation to fail in some circumstances. If you have have enabled the Block Public Access (BPA) feature in your S3 account, then you must specify the value of this parameter as ``BUCKET_OWNER_FULL_CONTROL`` , and not doing so results in an error. If you have disabled BPA in S3, then you can specify either ``BUCKET_OWNER_FULL_CONTROL`` or ``PUBLIC_READ`` as the value. For more information, see `Blocking public access to the S3 bucket <https://docs.aws.amazon.com/privateca/latest/userguide/PcaCreateCa.html#s3-bpa>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                crl_configuration_property = acmpca.CfnCertificateAuthority.CrlConfigurationProperty(
                    custom_cname="customCname",
                    enabled=False,
                    expiration_in_days=123,
                    s3_bucket_name="s3BucketName",
                    s3_object_acl="s3ObjectAcl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__de72782a3b3117c1f101c2c6c2fad457863e581a5bdcd67a1280a825dc55ea17)
                check_type(argname="argument custom_cname", value=custom_cname, expected_type=type_hints["custom_cname"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument expiration_in_days", value=expiration_in_days, expected_type=type_hints["expiration_in_days"])
                check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
                check_type(argname="argument s3_object_acl", value=s3_object_acl, expected_type=type_hints["s3_object_acl"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_cname is not None:
                self._values["custom_cname"] = custom_cname
            if enabled is not None:
                self._values["enabled"] = enabled
            if expiration_in_days is not None:
                self._values["expiration_in_days"] = expiration_in_days
            if s3_bucket_name is not None:
                self._values["s3_bucket_name"] = s3_bucket_name
            if s3_object_acl is not None:
                self._values["s3_object_acl"] = s3_object_acl

        @builtins.property
        def custom_cname(self) -> typing.Optional[builtins.str]:
            '''Name inserted into the certificate *CRL Distribution Points* extension that enables the use of an alias for the CRL distribution point.

            Use this value if you don't want the name of your S3 bucket to be public.
            .. epigraph::

               The content of a Canonical Name (CNAME) record must conform to `RFC2396 <https://docs.aws.amazon.com/https://www.ietf.org/rfc/rfc2396.txt>`_ restrictions on the use of special characters in URIs. Additionally, the value of the CNAME must not include a protocol prefix such as "http://" or "https://".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html#cfn-acmpca-certificateauthority-crlconfiguration-customcname
            '''
            result = self._values.get("custom_cname")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Boolean value that specifies whether certificate revocation lists (CRLs) are enabled.

            You can use this value to enable certificate revocation for a new CA when you call the ``CreateCertificateAuthority`` operation or for an existing CA when you call the ``UpdateCertificateAuthority`` operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html#cfn-acmpca-certificateauthority-crlconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def expiration_in_days(self) -> typing.Optional[jsii.Number]:
            '''Validity period of the CRL in days.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html#cfn-acmpca-certificateauthority-crlconfiguration-expirationindays
            '''
            result = self._values.get("expiration_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def s3_bucket_name(self) -> typing.Optional[builtins.str]:
            '''Name of the S3 bucket that contains the CRL.

            If you do not provide a value for the *CustomCname* argument, the name of your S3 bucket is placed into the *CRL Distribution Points* extension of the issued certificate. You can change the name of your bucket by calling the `UpdateCertificateAuthority <https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html>`_ operation. You must specify a `bucket policy <https://docs.aws.amazon.com/privateca/latest/userguide/PcaCreateCa.html#s3-policies>`_ that allows AWS Private CA to write the CRL to your bucket.
            .. epigraph::

               The ``S3BucketName`` parameter must conform to the `S3 bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html#cfn-acmpca-certificateauthority-crlconfiguration-s3bucketname
            '''
            result = self._values.get("s3_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_object_acl(self) -> typing.Optional[builtins.str]:
            '''Determines whether the CRL will be publicly readable or privately held in the CRL Amazon S3 bucket.

            If you choose PUBLIC_READ, the CRL will be accessible over the public internet. If you choose BUCKET_OWNER_FULL_CONTROL, only the owner of the CRL S3 bucket can access the CRL, and your PKI clients may need an alternative method of access.

            If no value is specified, the default is PUBLIC_READ.

            *Note:* This default can cause CA creation to fail in some circumstances. If you have have enabled the Block Public Access (BPA) feature in your S3 account, then you must specify the value of this parameter as ``BUCKET_OWNER_FULL_CONTROL`` , and not doing so results in an error. If you have disabled BPA in S3, then you can specify either ``BUCKET_OWNER_FULL_CONTROL`` or ``PUBLIC_READ`` as the value.

            For more information, see `Blocking public access to the S3 bucket <https://docs.aws.amazon.com/privateca/latest/userguide/PcaCreateCa.html#s3-bpa>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html#cfn-acmpca-certificateauthority-crlconfiguration-s3objectacl
            '''
            result = self._values.get("s3_object_acl")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CrlConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthority.CsrExtensionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "key_usage": "keyUsage",
            "subject_information_access": "subjectInformationAccess",
        },
    )
    class CsrExtensionsProperty:
        def __init__(
            self,
            *,
            key_usage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificateAuthority.KeyUsageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            subject_information_access: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificateAuthority.AccessDescriptionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Describes the certificate extensions to be added to the certificate signing request (CSR).

            :param key_usage: Indicates the purpose of the certificate and of the key contained in the certificate.
            :param subject_information_access: For CA certificates, provides a path to additional information pertaining to the CA, such as revocation and policy. For more information, see `Subject Information Access <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.2.2>`_ in RFC 5280.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-csrextensions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                csr_extensions_property = acmpca.CfnCertificateAuthority.CsrExtensionsProperty(
                    key_usage=acmpca.CfnCertificateAuthority.KeyUsageProperty(
                        crl_sign=False,
                        data_encipherment=False,
                        decipher_only=False,
                        digital_signature=False,
                        encipher_only=False,
                        key_agreement=False,
                        key_cert_sign=False,
                        key_encipherment=False,
                        non_repudiation=False
                    ),
                    subject_information_access=[acmpca.CfnCertificateAuthority.AccessDescriptionProperty(
                        access_location=acmpca.CfnCertificateAuthority.GeneralNameProperty(
                            directory_name=acmpca.CfnCertificateAuthority.SubjectProperty(
                                common_name="commonName",
                                country="country",
                                custom_attributes=[acmpca.CfnCertificateAuthority.CustomAttributeProperty(
                                    object_identifier="objectIdentifier",
                                    value="value"
                                )],
                                distinguished_name_qualifier="distinguishedNameQualifier",
                                generation_qualifier="generationQualifier",
                                given_name="givenName",
                                initials="initials",
                                locality="locality",
                                organization="organization",
                                organizational_unit="organizationalUnit",
                                pseudonym="pseudonym",
                                serial_number="serialNumber",
                                state="state",
                                surname="surname",
                                title="title"
                            ),
                            dns_name="dnsName",
                            edi_party_name=acmpca.CfnCertificateAuthority.EdiPartyNameProperty(
                                name_assigner="nameAssigner",
                                party_name="partyName"
                            ),
                            ip_address="ipAddress",
                            other_name=acmpca.CfnCertificateAuthority.OtherNameProperty(
                                type_id="typeId",
                                value="value"
                            ),
                            registered_id="registeredId",
                            rfc822_name="rfc822Name",
                            uniform_resource_identifier="uniformResourceIdentifier"
                        ),
                        access_method=acmpca.CfnCertificateAuthority.AccessMethodProperty(
                            access_method_type="accessMethodType",
                            custom_object_identifier="customObjectIdentifier"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fad5bc7b7fbc7061150ae02b07b6566cf328ba6ffd556e6c6ea3738e4c89711a)
                check_type(argname="argument key_usage", value=key_usage, expected_type=type_hints["key_usage"])
                check_type(argname="argument subject_information_access", value=subject_information_access, expected_type=type_hints["subject_information_access"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key_usage is not None:
                self._values["key_usage"] = key_usage
            if subject_information_access is not None:
                self._values["subject_information_access"] = subject_information_access

        @builtins.property
        def key_usage(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.KeyUsageProperty"]]:
            '''Indicates the purpose of the certificate and of the key contained in the certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-csrextensions.html#cfn-acmpca-certificateauthority-csrextensions-keyusage
            '''
            result = self._values.get("key_usage")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.KeyUsageProperty"]], result)

        @builtins.property
        def subject_information_access(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.AccessDescriptionProperty"]]]]:
            '''For CA certificates, provides a path to additional information pertaining to the CA, such as revocation and policy.

            For more information, see `Subject Information Access <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.2.2>`_ in RFC 5280.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-csrextensions.html#cfn-acmpca-certificateauthority-csrextensions-subjectinformationaccess
            '''
            result = self._values.get("subject_information_access")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.AccessDescriptionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CsrExtensionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthority.CustomAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"object_identifier": "objectIdentifier", "value": "value"},
    )
    class CustomAttributeProperty:
        def __init__(
            self,
            *,
            object_identifier: builtins.str,
            value: builtins.str,
        ) -> None:
            '''Defines the X.500 relative distinguished name (RDN).

            :param object_identifier: Specifies the object identifier (OID) of the attribute type of the relative distinguished name (RDN).
            :param value: Specifies the attribute value of relative distinguished name (RDN).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-customattribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                custom_attribute_property = acmpca.CfnCertificateAuthority.CustomAttributeProperty(
                    object_identifier="objectIdentifier",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0caab149cb10c9e2e41c808164411855ca5f9298e171e0db7a1a0913ea642d2)
                check_type(argname="argument object_identifier", value=object_identifier, expected_type=type_hints["object_identifier"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object_identifier": object_identifier,
                "value": value,
            }

        @builtins.property
        def object_identifier(self) -> builtins.str:
            '''Specifies the object identifier (OID) of the attribute type of the relative distinguished name (RDN).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-customattribute.html#cfn-acmpca-certificateauthority-customattribute-objectidentifier
            '''
            result = self._values.get("object_identifier")
            assert result is not None, "Required property 'object_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''Specifies the attribute value of relative distinguished name (RDN).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-customattribute.html#cfn-acmpca-certificateauthority-customattribute-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthority.EdiPartyNameProperty",
        jsii_struct_bases=[],
        name_mapping={"name_assigner": "nameAssigner", "party_name": "partyName"},
    )
    class EdiPartyNameProperty:
        def __init__(
            self,
            *,
            name_assigner: builtins.str,
            party_name: builtins.str,
        ) -> None:
            '''Describes an Electronic Data Interchange (EDI) entity as described in as defined in `Subject Alternative Name <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc5280>`_ in RFC 5280.

            :param name_assigner: Specifies the name assigner.
            :param party_name: Specifies the party name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-edipartyname.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                edi_party_name_property = acmpca.CfnCertificateAuthority.EdiPartyNameProperty(
                    name_assigner="nameAssigner",
                    party_name="partyName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e187a86a6b5c31d0b8c99e998eea3f8683787066dcfd319750892c59195bf6e8)
                check_type(argname="argument name_assigner", value=name_assigner, expected_type=type_hints["name_assigner"])
                check_type(argname="argument party_name", value=party_name, expected_type=type_hints["party_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name_assigner": name_assigner,
                "party_name": party_name,
            }

        @builtins.property
        def name_assigner(self) -> builtins.str:
            '''Specifies the name assigner.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-edipartyname.html#cfn-acmpca-certificateauthority-edipartyname-nameassigner
            '''
            result = self._values.get("name_assigner")
            assert result is not None, "Required property 'name_assigner' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def party_name(self) -> builtins.str:
            '''Specifies the party name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-edipartyname.html#cfn-acmpca-certificateauthority-edipartyname-partyname
            '''
            result = self._values.get("party_name")
            assert result is not None, "Required property 'party_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EdiPartyNameProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthority.GeneralNameProperty",
        jsii_struct_bases=[],
        name_mapping={
            "directory_name": "directoryName",
            "dns_name": "dnsName",
            "edi_party_name": "ediPartyName",
            "ip_address": "ipAddress",
            "other_name": "otherName",
            "registered_id": "registeredId",
            "rfc822_name": "rfc822Name",
            "uniform_resource_identifier": "uniformResourceIdentifier",
        },
    )
    class GeneralNameProperty:
        def __init__(
            self,
            *,
            directory_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificateAuthority.SubjectProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dns_name: typing.Optional[builtins.str] = None,
            edi_party_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificateAuthority.EdiPartyNameProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ip_address: typing.Optional[builtins.str] = None,
            other_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificateAuthority.OtherNameProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            registered_id: typing.Optional[builtins.str] = None,
            rfc822_name: typing.Optional[builtins.str] = None,
            uniform_resource_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an ASN.1 X.400 ``GeneralName`` as defined in `RFC 5280 <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc5280>`_ . Only one of the following naming options should be provided. Providing more than one option results in an ``InvalidArgsException`` error.

            :param directory_name: Contains information about the certificate subject. The certificate can be one issued by your private certificate authority (CA) or it can be your private CA certificate. The Subject field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The Subject must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate. The DN must be unique for each entity, but your private CA can issue more than one certificate with the same DN to the same entity.
            :param dns_name: Represents ``GeneralName`` as a DNS name.
            :param edi_party_name: Represents ``GeneralName`` as an ``EdiPartyName`` object.
            :param ip_address: Represents ``GeneralName`` as an IPv4 or IPv6 address.
            :param other_name: Represents ``GeneralName`` using an ``OtherName`` object.
            :param registered_id: Represents ``GeneralName`` as an object identifier (OID).
            :param rfc822_name: Represents ``GeneralName`` as an `RFC 822 <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc822>`_ email address.
            :param uniform_resource_identifier: Represents ``GeneralName`` as a URI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                general_name_property = acmpca.CfnCertificateAuthority.GeneralNameProperty(
                    directory_name=acmpca.CfnCertificateAuthority.SubjectProperty(
                        common_name="commonName",
                        country="country",
                        custom_attributes=[acmpca.CfnCertificateAuthority.CustomAttributeProperty(
                            object_identifier="objectIdentifier",
                            value="value"
                        )],
                        distinguished_name_qualifier="distinguishedNameQualifier",
                        generation_qualifier="generationQualifier",
                        given_name="givenName",
                        initials="initials",
                        locality="locality",
                        organization="organization",
                        organizational_unit="organizationalUnit",
                        pseudonym="pseudonym",
                        serial_number="serialNumber",
                        state="state",
                        surname="surname",
                        title="title"
                    ),
                    dns_name="dnsName",
                    edi_party_name=acmpca.CfnCertificateAuthority.EdiPartyNameProperty(
                        name_assigner="nameAssigner",
                        party_name="partyName"
                    ),
                    ip_address="ipAddress",
                    other_name=acmpca.CfnCertificateAuthority.OtherNameProperty(
                        type_id="typeId",
                        value="value"
                    ),
                    registered_id="registeredId",
                    rfc822_name="rfc822Name",
                    uniform_resource_identifier="uniformResourceIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9350b2847a089516fb8a320d9014174879fc12ab6024b5f5abe53240af563f91)
                check_type(argname="argument directory_name", value=directory_name, expected_type=type_hints["directory_name"])
                check_type(argname="argument dns_name", value=dns_name, expected_type=type_hints["dns_name"])
                check_type(argname="argument edi_party_name", value=edi_party_name, expected_type=type_hints["edi_party_name"])
                check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
                check_type(argname="argument other_name", value=other_name, expected_type=type_hints["other_name"])
                check_type(argname="argument registered_id", value=registered_id, expected_type=type_hints["registered_id"])
                check_type(argname="argument rfc822_name", value=rfc822_name, expected_type=type_hints["rfc822_name"])
                check_type(argname="argument uniform_resource_identifier", value=uniform_resource_identifier, expected_type=type_hints["uniform_resource_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if directory_name is not None:
                self._values["directory_name"] = directory_name
            if dns_name is not None:
                self._values["dns_name"] = dns_name
            if edi_party_name is not None:
                self._values["edi_party_name"] = edi_party_name
            if ip_address is not None:
                self._values["ip_address"] = ip_address
            if other_name is not None:
                self._values["other_name"] = other_name
            if registered_id is not None:
                self._values["registered_id"] = registered_id
            if rfc822_name is not None:
                self._values["rfc822_name"] = rfc822_name
            if uniform_resource_identifier is not None:
                self._values["uniform_resource_identifier"] = uniform_resource_identifier

        @builtins.property
        def directory_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.SubjectProperty"]]:
            '''Contains information about the certificate subject.

            The certificate can be one issued by your private certificate authority (CA) or it can be your private CA certificate. The Subject field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The Subject must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate. The DN must be unique for each entity, but your private CA can issue more than one certificate with the same DN to the same entity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-directoryname
            '''
            result = self._values.get("directory_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.SubjectProperty"]], result)

        @builtins.property
        def dns_name(self) -> typing.Optional[builtins.str]:
            '''Represents ``GeneralName`` as a DNS name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-dnsname
            '''
            result = self._values.get("dns_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def edi_party_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.EdiPartyNameProperty"]]:
            '''Represents ``GeneralName`` as an ``EdiPartyName`` object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-edipartyname
            '''
            result = self._values.get("edi_party_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.EdiPartyNameProperty"]], result)

        @builtins.property
        def ip_address(self) -> typing.Optional[builtins.str]:
            '''Represents ``GeneralName`` as an IPv4 or IPv6 address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-ipaddress
            '''
            result = self._values.get("ip_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def other_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.OtherNameProperty"]]:
            '''Represents ``GeneralName`` using an ``OtherName`` object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-othername
            '''
            result = self._values.get("other_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.OtherNameProperty"]], result)

        @builtins.property
        def registered_id(self) -> typing.Optional[builtins.str]:
            '''Represents ``GeneralName`` as an object identifier (OID).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-registeredid
            '''
            result = self._values.get("registered_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rfc822_name(self) -> typing.Optional[builtins.str]:
            '''Represents ``GeneralName`` as an `RFC 822 <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc822>`_ email address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-rfc822name
            '''
            result = self._values.get("rfc822_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def uniform_resource_identifier(self) -> typing.Optional[builtins.str]:
            '''Represents ``GeneralName`` as a URI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-uniformresourceidentifier
            '''
            result = self._values.get("uniform_resource_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeneralNameProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthority.KeyUsageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "crl_sign": "crlSign",
            "data_encipherment": "dataEncipherment",
            "decipher_only": "decipherOnly",
            "digital_signature": "digitalSignature",
            "encipher_only": "encipherOnly",
            "key_agreement": "keyAgreement",
            "key_cert_sign": "keyCertSign",
            "key_encipherment": "keyEncipherment",
            "non_repudiation": "nonRepudiation",
        },
    )
    class KeyUsageProperty:
        def __init__(
            self,
            *,
            crl_sign: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            data_encipherment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            decipher_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            digital_signature: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            encipher_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            key_agreement: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            key_cert_sign: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            key_encipherment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            non_repudiation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Defines one or more purposes for which the key contained in the certificate can be used.

            Default value for each option is false.

            :param crl_sign: Key can be used to sign CRLs. Default: - false
            :param data_encipherment: Key can be used to decipher data. Default: - false
            :param decipher_only: Key can be used only to decipher data. Default: - false
            :param digital_signature: Key can be used for digital signing. Default: - false
            :param encipher_only: Key can be used only to encipher data. Default: - false
            :param key_agreement: Key can be used in a key-agreement protocol. Default: - false
            :param key_cert_sign: Key can be used to sign certificates. Default: - false
            :param key_encipherment: Key can be used to encipher data. Default: - false
            :param non_repudiation: Key can be used for non-repudiation. Default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                key_usage_property = acmpca.CfnCertificateAuthority.KeyUsageProperty(
                    crl_sign=False,
                    data_encipherment=False,
                    decipher_only=False,
                    digital_signature=False,
                    encipher_only=False,
                    key_agreement=False,
                    key_cert_sign=False,
                    key_encipherment=False,
                    non_repudiation=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f8dd4df3844e389720f6addec59149d792d65195686e07b6e154c3a6d3da26e6)
                check_type(argname="argument crl_sign", value=crl_sign, expected_type=type_hints["crl_sign"])
                check_type(argname="argument data_encipherment", value=data_encipherment, expected_type=type_hints["data_encipherment"])
                check_type(argname="argument decipher_only", value=decipher_only, expected_type=type_hints["decipher_only"])
                check_type(argname="argument digital_signature", value=digital_signature, expected_type=type_hints["digital_signature"])
                check_type(argname="argument encipher_only", value=encipher_only, expected_type=type_hints["encipher_only"])
                check_type(argname="argument key_agreement", value=key_agreement, expected_type=type_hints["key_agreement"])
                check_type(argname="argument key_cert_sign", value=key_cert_sign, expected_type=type_hints["key_cert_sign"])
                check_type(argname="argument key_encipherment", value=key_encipherment, expected_type=type_hints["key_encipherment"])
                check_type(argname="argument non_repudiation", value=non_repudiation, expected_type=type_hints["non_repudiation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if crl_sign is not None:
                self._values["crl_sign"] = crl_sign
            if data_encipherment is not None:
                self._values["data_encipherment"] = data_encipherment
            if decipher_only is not None:
                self._values["decipher_only"] = decipher_only
            if digital_signature is not None:
                self._values["digital_signature"] = digital_signature
            if encipher_only is not None:
                self._values["encipher_only"] = encipher_only
            if key_agreement is not None:
                self._values["key_agreement"] = key_agreement
            if key_cert_sign is not None:
                self._values["key_cert_sign"] = key_cert_sign
            if key_encipherment is not None:
                self._values["key_encipherment"] = key_encipherment
            if non_repudiation is not None:
                self._values["non_repudiation"] = non_repudiation

        @builtins.property
        def crl_sign(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used to sign CRLs.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-crlsign
            '''
            result = self._values.get("crl_sign")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def data_encipherment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used to decipher data.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-dataencipherment
            '''
            result = self._values.get("data_encipherment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def decipher_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used only to decipher data.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-decipheronly
            '''
            result = self._values.get("decipher_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def digital_signature(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used for digital signing.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-digitalsignature
            '''
            result = self._values.get("digital_signature")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def encipher_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used only to encipher data.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-encipheronly
            '''
            result = self._values.get("encipher_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def key_agreement(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used in a key-agreement protocol.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-keyagreement
            '''
            result = self._values.get("key_agreement")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def key_cert_sign(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used to sign certificates.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-keycertsign
            '''
            result = self._values.get("key_cert_sign")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def key_encipherment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used to encipher data.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-keyencipherment
            '''
            result = self._values.get("key_encipherment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def non_repudiation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Key can be used for non-repudiation.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-nonrepudiation
            '''
            result = self._values.get("non_repudiation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyUsageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthority.OcspConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "ocsp_custom_cname": "ocspCustomCname"},
    )
    class OcspConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            ocsp_custom_cname: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information to enable and configure Online Certificate Status Protocol (OCSP) for validating certificate revocation status.

            :param enabled: Flag enabling use of the Online Certificate Status Protocol (OCSP) for validating certificate revocation status.
            :param ocsp_custom_cname: By default, AWS Private CA injects an Amazon domain into certificates being validated by the Online Certificate Status Protocol (OCSP). A customer can alternatively use this object to define a CNAME specifying a customized OCSP domain. .. epigraph:: The content of a Canonical Name (CNAME) record must conform to `RFC2396 <https://docs.aws.amazon.com/https://www.ietf.org/rfc/rfc2396.txt>`_ restrictions on the use of special characters in URIs. Additionally, the value of the CNAME must not include a protocol prefix such as "http://" or "https://".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-ocspconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                ocsp_configuration_property = acmpca.CfnCertificateAuthority.OcspConfigurationProperty(
                    enabled=False,
                    ocsp_custom_cname="ocspCustomCname"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__db2a6b0f215dcb411b988d99d6a91fb7c758aefe4260650026b58ba7b1cddde5)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument ocsp_custom_cname", value=ocsp_custom_cname, expected_type=type_hints["ocsp_custom_cname"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if ocsp_custom_cname is not None:
                self._values["ocsp_custom_cname"] = ocsp_custom_cname

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Flag enabling use of the Online Certificate Status Protocol (OCSP) for validating certificate revocation status.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-ocspconfiguration.html#cfn-acmpca-certificateauthority-ocspconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def ocsp_custom_cname(self) -> typing.Optional[builtins.str]:
            '''By default, AWS Private CA injects an Amazon domain into certificates being validated by the Online Certificate Status Protocol (OCSP).

            A customer can alternatively use this object to define a CNAME specifying a customized OCSP domain.
            .. epigraph::

               The content of a Canonical Name (CNAME) record must conform to `RFC2396 <https://docs.aws.amazon.com/https://www.ietf.org/rfc/rfc2396.txt>`_ restrictions on the use of special characters in URIs. Additionally, the value of the CNAME must not include a protocol prefix such as "http://" or "https://".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-ocspconfiguration.html#cfn-acmpca-certificateauthority-ocspconfiguration-ocspcustomcname
            '''
            result = self._values.get("ocsp_custom_cname")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OcspConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthority.OtherNameProperty",
        jsii_struct_bases=[],
        name_mapping={"type_id": "typeId", "value": "value"},
    )
    class OtherNameProperty:
        def __init__(self, *, type_id: builtins.str, value: builtins.str) -> None:
            '''Defines a custom ASN.1 X.400 ``GeneralName`` using an object identifier (OID) and value. The OID must satisfy the regular expression shown below. For more information, see NIST's definition of `Object Identifier (OID) <https://docs.aws.amazon.com/https://csrc.nist.gov/glossary/term/Object_Identifier>`_ .

            :param type_id: Specifies an OID.
            :param value: Specifies an OID value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-othername.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                other_name_property = acmpca.CfnCertificateAuthority.OtherNameProperty(
                    type_id="typeId",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__798f8d72c7f9ddb26ba8e82b9a6c8b81465d40f828b01a11ac8c09bfb53381ff)
                check_type(argname="argument type_id", value=type_id, expected_type=type_hints["type_id"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type_id": type_id,
                "value": value,
            }

        @builtins.property
        def type_id(self) -> builtins.str:
            '''Specifies an OID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-othername.html#cfn-acmpca-certificateauthority-othername-typeid
            '''
            result = self._values.get("type_id")
            assert result is not None, "Required property 'type_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''Specifies an OID value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-othername.html#cfn-acmpca-certificateauthority-othername-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OtherNameProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthority.RevocationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "crl_configuration": "crlConfiguration",
            "ocsp_configuration": "ocspConfiguration",
        },
    )
    class RevocationConfigurationProperty:
        def __init__(
            self,
            *,
            crl_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificateAuthority.CrlConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ocsp_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificateAuthority.OcspConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Certificate revocation information used by the `CreateCertificateAuthority <https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html>`_ and `UpdateCertificateAuthority <https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html>`_ actions. Your private certificate authority (CA) can configure Online Certificate Status Protocol (OCSP) support and/or maintain a certificate revocation list (CRL). OCSP returns validation information about certificates as requested by clients, and a CRL contains an updated list of certificates revoked by your CA. For more information, see `RevokeCertificate <https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html>`_ in the *AWS Private CA API Reference* and `Setting up a certificate revocation method <https://docs.aws.amazon.com/privateca/latest/userguide/revocation-setup.html>`_ in the *AWS Private CA User Guide* .

            .. epigraph::

               The following requirements apply to revocation configurations.

               - A configuration disabling CRLs or OCSP must contain only the ``Enabled=False`` parameter, and will fail if other parameters such as ``CustomCname`` or ``ExpirationInDays`` are included.
               - In a CRL configuration, the ``S3BucketName`` parameter must conform to the `Amazon S3 bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html>`_ .
               - A configuration containing a custom Canonical Name (CNAME) parameter for CRLs or OCSP must conform to `RFC2396 <https://docs.aws.amazon.com/https://www.ietf.org/rfc/rfc2396.txt>`_ restrictions on the use of special characters in a CNAME.
               - In a CRL or OCSP configuration, the value of a CNAME parameter must not include a protocol prefix such as "http://" or "https://".

            :param crl_configuration: Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.
            :param ocsp_configuration: Configuration of Online Certificate Status Protocol (OCSP) support, if any, maintained by your private CA.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-revocationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                revocation_configuration_property = acmpca.CfnCertificateAuthority.RevocationConfigurationProperty(
                    crl_configuration=acmpca.CfnCertificateAuthority.CrlConfigurationProperty(
                        custom_cname="customCname",
                        enabled=False,
                        expiration_in_days=123,
                        s3_bucket_name="s3BucketName",
                        s3_object_acl="s3ObjectAcl"
                    ),
                    ocsp_configuration=acmpca.CfnCertificateAuthority.OcspConfigurationProperty(
                        enabled=False,
                        ocsp_custom_cname="ocspCustomCname"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3b8bd7c76f7f0154f73285d0a3cebdc5be93c7168017624ee216b2e39d0a3ec0)
                check_type(argname="argument crl_configuration", value=crl_configuration, expected_type=type_hints["crl_configuration"])
                check_type(argname="argument ocsp_configuration", value=ocsp_configuration, expected_type=type_hints["ocsp_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if crl_configuration is not None:
                self._values["crl_configuration"] = crl_configuration
            if ocsp_configuration is not None:
                self._values["ocsp_configuration"] = ocsp_configuration

        @builtins.property
        def crl_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.CrlConfigurationProperty"]]:
            '''Configuration of the certificate revocation list (CRL), if any, maintained by your private CA.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-revocationconfiguration.html#cfn-acmpca-certificateauthority-revocationconfiguration-crlconfiguration
            '''
            result = self._values.get("crl_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.CrlConfigurationProperty"]], result)

        @builtins.property
        def ocsp_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.OcspConfigurationProperty"]]:
            '''Configuration of Online Certificate Status Protocol (OCSP) support, if any, maintained by your private CA.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-revocationconfiguration.html#cfn-acmpca-certificateauthority-revocationconfiguration-ocspconfiguration
            '''
            result = self._values.get("ocsp_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.OcspConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RevocationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthority.SubjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "common_name": "commonName",
            "country": "country",
            "custom_attributes": "customAttributes",
            "distinguished_name_qualifier": "distinguishedNameQualifier",
            "generation_qualifier": "generationQualifier",
            "given_name": "givenName",
            "initials": "initials",
            "locality": "locality",
            "organization": "organization",
            "organizational_unit": "organizationalUnit",
            "pseudonym": "pseudonym",
            "serial_number": "serialNumber",
            "state": "state",
            "surname": "surname",
            "title": "title",
        },
    )
    class SubjectProperty:
        def __init__(
            self,
            *,
            common_name: typing.Optional[builtins.str] = None,
            country: typing.Optional[builtins.str] = None,
            custom_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificateAuthority.CustomAttributeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            distinguished_name_qualifier: typing.Optional[builtins.str] = None,
            generation_qualifier: typing.Optional[builtins.str] = None,
            given_name: typing.Optional[builtins.str] = None,
            initials: typing.Optional[builtins.str] = None,
            locality: typing.Optional[builtins.str] = None,
            organization: typing.Optional[builtins.str] = None,
            organizational_unit: typing.Optional[builtins.str] = None,
            pseudonym: typing.Optional[builtins.str] = None,
            serial_number: typing.Optional[builtins.str] = None,
            state: typing.Optional[builtins.str] = None,
            surname: typing.Optional[builtins.str] = None,
            title: typing.Optional[builtins.str] = None,
        ) -> None:
            '''ASN1 subject for the certificate authority.

            :param common_name: Fully qualified domain name (FQDN) associated with the certificate subject.
            :param country: Two-digit code that specifies the country in which the certificate subject located.
            :param custom_attributes: Contains a sequence of one or more X.500 relative distinguished names (RDNs), each of which consists of an object identifier (OID) and a value. For more information, see NIST’s definition of `Object Identifier (OID) <https://docs.aws.amazon.com/https://csrc.nist.gov/glossary/term/Object_Identifier>`_ . .. epigraph:: Custom attributes cannot be used in combination with standard attributes.
            :param distinguished_name_qualifier: Disambiguating information for the certificate subject.
            :param generation_qualifier: Typically a qualifier appended to the name of an individual. Examples include Jr. for junior, Sr. for senior, and III for third.
            :param given_name: First name.
            :param initials: Concatenation that typically contains the first letter of the GivenName, the first letter of the middle name if one exists, and the first letter of the SurName.
            :param locality: The locality (such as a city or town) in which the certificate subject is located.
            :param organization: Legal name of the organization with which the certificate subject is affiliated.
            :param organizational_unit: A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.
            :param pseudonym: Typically a shortened version of a longer GivenName. For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.
            :param serial_number: The certificate serial number.
            :param state: State in which the subject of the certificate is located.
            :param surname: Family name.
            :param title: A personal title such as Mr.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_acmpca as acmpca
                
                subject_property = acmpca.CfnCertificateAuthority.SubjectProperty(
                    common_name="commonName",
                    country="country",
                    custom_attributes=[acmpca.CfnCertificateAuthority.CustomAttributeProperty(
                        object_identifier="objectIdentifier",
                        value="value"
                    )],
                    distinguished_name_qualifier="distinguishedNameQualifier",
                    generation_qualifier="generationQualifier",
                    given_name="givenName",
                    initials="initials",
                    locality="locality",
                    organization="organization",
                    organizational_unit="organizationalUnit",
                    pseudonym="pseudonym",
                    serial_number="serialNumber",
                    state="state",
                    surname="surname",
                    title="title"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2fe22c69366f0a777e4079f3471779342ff021a43565fd6a2cc33bd8cb705970)
                check_type(argname="argument common_name", value=common_name, expected_type=type_hints["common_name"])
                check_type(argname="argument country", value=country, expected_type=type_hints["country"])
                check_type(argname="argument custom_attributes", value=custom_attributes, expected_type=type_hints["custom_attributes"])
                check_type(argname="argument distinguished_name_qualifier", value=distinguished_name_qualifier, expected_type=type_hints["distinguished_name_qualifier"])
                check_type(argname="argument generation_qualifier", value=generation_qualifier, expected_type=type_hints["generation_qualifier"])
                check_type(argname="argument given_name", value=given_name, expected_type=type_hints["given_name"])
                check_type(argname="argument initials", value=initials, expected_type=type_hints["initials"])
                check_type(argname="argument locality", value=locality, expected_type=type_hints["locality"])
                check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
                check_type(argname="argument organizational_unit", value=organizational_unit, expected_type=type_hints["organizational_unit"])
                check_type(argname="argument pseudonym", value=pseudonym, expected_type=type_hints["pseudonym"])
                check_type(argname="argument serial_number", value=serial_number, expected_type=type_hints["serial_number"])
                check_type(argname="argument state", value=state, expected_type=type_hints["state"])
                check_type(argname="argument surname", value=surname, expected_type=type_hints["surname"])
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if common_name is not None:
                self._values["common_name"] = common_name
            if country is not None:
                self._values["country"] = country
            if custom_attributes is not None:
                self._values["custom_attributes"] = custom_attributes
            if distinguished_name_qualifier is not None:
                self._values["distinguished_name_qualifier"] = distinguished_name_qualifier
            if generation_qualifier is not None:
                self._values["generation_qualifier"] = generation_qualifier
            if given_name is not None:
                self._values["given_name"] = given_name
            if initials is not None:
                self._values["initials"] = initials
            if locality is not None:
                self._values["locality"] = locality
            if organization is not None:
                self._values["organization"] = organization
            if organizational_unit is not None:
                self._values["organizational_unit"] = organizational_unit
            if pseudonym is not None:
                self._values["pseudonym"] = pseudonym
            if serial_number is not None:
                self._values["serial_number"] = serial_number
            if state is not None:
                self._values["state"] = state
            if surname is not None:
                self._values["surname"] = surname
            if title is not None:
                self._values["title"] = title

        @builtins.property
        def common_name(self) -> typing.Optional[builtins.str]:
            '''Fully qualified domain name (FQDN) associated with the certificate subject.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-commonname
            '''
            result = self._values.get("common_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def country(self) -> typing.Optional[builtins.str]:
            '''Two-digit code that specifies the country in which the certificate subject located.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-country
            '''
            result = self._values.get("country")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.CustomAttributeProperty"]]]]:
            '''Contains a sequence of one or more X.500 relative distinguished names (RDNs), each of which consists of an object identifier (OID) and a value. For more information, see NIST’s definition of `Object Identifier (OID) <https://docs.aws.amazon.com/https://csrc.nist.gov/glossary/term/Object_Identifier>`_ .

            .. epigraph::

               Custom attributes cannot be used in combination with standard attributes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-customattributes
            '''
            result = self._values.get("custom_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificateAuthority.CustomAttributeProperty"]]]], result)

        @builtins.property
        def distinguished_name_qualifier(self) -> typing.Optional[builtins.str]:
            '''Disambiguating information for the certificate subject.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-distinguishednamequalifier
            '''
            result = self._values.get("distinguished_name_qualifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def generation_qualifier(self) -> typing.Optional[builtins.str]:
            '''Typically a qualifier appended to the name of an individual.

            Examples include Jr. for junior, Sr. for senior, and III for third.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-generationqualifier
            '''
            result = self._values.get("generation_qualifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def given_name(self) -> typing.Optional[builtins.str]:
            '''First name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-givenname
            '''
            result = self._values.get("given_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def initials(self) -> typing.Optional[builtins.str]:
            '''Concatenation that typically contains the first letter of the GivenName, the first letter of the middle name if one exists, and the first letter of the SurName.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-initials
            '''
            result = self._values.get("initials")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def locality(self) -> typing.Optional[builtins.str]:
            '''The locality (such as a city or town) in which the certificate subject is located.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-locality
            '''
            result = self._values.get("locality")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organization(self) -> typing.Optional[builtins.str]:
            '''Legal name of the organization with which the certificate subject is affiliated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-organization
            '''
            result = self._values.get("organization")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organizational_unit(self) -> typing.Optional[builtins.str]:
            '''A subdivision or unit of the organization (such as sales or finance) with which the certificate subject is affiliated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-organizationalunit
            '''
            result = self._values.get("organizational_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pseudonym(self) -> typing.Optional[builtins.str]:
            '''Typically a shortened version of a longer GivenName.

            For example, Jonathan is often shortened to John. Elizabeth is often shortened to Beth, Liz, or Eliza.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-pseudonym
            '''
            result = self._values.get("pseudonym")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def serial_number(self) -> typing.Optional[builtins.str]:
            '''The certificate serial number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-serialnumber
            '''
            result = self._values.get("serial_number")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''State in which the subject of the certificate is located.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def surname(self) -> typing.Optional[builtins.str]:
            '''Family name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-surname
            '''
            result = self._values.get("surname")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def title(self) -> typing.Optional[builtins.str]:
            '''A personal title such as Mr.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnCertificateAuthorityActivation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthorityActivation",
):
    '''The ``AWS::ACMPCA::CertificateAuthorityActivation`` resource creates and installs a CA certificate on a CA.

    If no status is specified, the ``AWS::ACMPCA::CertificateAuthorityActivation`` resource status defaults to ACTIVE. Once the CA has a CA certificate installed, you can use the resource to toggle the CA status field between ``ACTIVE`` and ``DISABLED`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_acmpca as acmpca
        
        cfn_certificate_authority_activation = acmpca.CfnCertificateAuthorityActivation(self, "MyCfnCertificateAuthorityActivation",
            certificate="certificate",
            certificate_authority_arn="certificateAuthorityArn",
        
            # the properties below are optional
            certificate_chain="certificateChain",
            status="status"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        certificate: builtins.str,
        certificate_authority_arn: builtins.str,
        certificate_chain: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param certificate: The Base64 PEM-encoded certificate authority certificate.
        :param certificate_authority_arn: The Amazon Resource Name (ARN) of your private CA.
        :param certificate_chain: The Base64 PEM-encoded certificate chain that chains up to the root CA certificate that you used to sign your private CA certificate.
        :param status: Status of your private CA.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e91763a1b089310141664991133bb321cced18cd10da038baa589bcc1474a665)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCertificateAuthorityActivationProps(
            certificate=certificate,
            certificate_authority_arn=certificate_authority_arn,
            certificate_chain=certificate_chain,
            status=status,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aa9f665899e699513e4e5b43f65abecdf25087e15d590d69d34112ce8a940fd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__affce5b20bcb3ac9dadff19bff87a0c6ab15d608153cfb9a691b56aeaecfb1a2)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCompleteCertificateChain")
    def attr_complete_certificate_chain(self) -> builtins.str:
        '''The complete Base64 PEM-encoded certificate chain, including the certificate authority certificate.

        :cloudformationAttribute: CompleteCertificateChain
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCompleteCertificateChain"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        '''The Base64 PEM-encoded certificate authority certificate.'''
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b279179f6b525656e5ee2f3b4d595cb75d494cf246f2e92a8469589c5395bfdd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of your private CA.'''
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthorityArn"))

    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43dd6c4689519828c2c042c80ee0ae6a9d3b03512aaac4693b2c9abdf2799b92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthorityArn", value)

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> typing.Optional[builtins.str]:
        '''The Base64 PEM-encoded certificate chain that chains up to the root CA certificate that you used to sign your private CA certificate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87c41ac4f9f42cd4127fcc9a6dfc22f017ed7eeba7dd94714974f3af2143dce1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''Status of your private CA.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bb84ac3ee8ec3f7d2297504aaca248c351bd9fd6b388a9a80a5c547a8b217eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthorityActivationProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate": "certificate",
        "certificate_authority_arn": "certificateAuthorityArn",
        "certificate_chain": "certificateChain",
        "status": "status",
    },
)
class CfnCertificateAuthorityActivationProps:
    def __init__(
        self,
        *,
        certificate: builtins.str,
        certificate_authority_arn: builtins.str,
        certificate_chain: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCertificateAuthorityActivation``.

        :param certificate: The Base64 PEM-encoded certificate authority certificate.
        :param certificate_authority_arn: The Amazon Resource Name (ARN) of your private CA.
        :param certificate_chain: The Base64 PEM-encoded certificate chain that chains up to the root CA certificate that you used to sign your private CA certificate.
        :param status: Status of your private CA.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_acmpca as acmpca
            
            cfn_certificate_authority_activation_props = acmpca.CfnCertificateAuthorityActivationProps(
                certificate="certificate",
                certificate_authority_arn="certificateAuthorityArn",
            
                # the properties below are optional
                certificate_chain="certificateChain",
                status="status"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b63918960d16b9d2632b9277b07b10494327c3d038ba9f5522225f20dfed02d)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument certificate_authority_arn", value=certificate_authority_arn, expected_type=type_hints["certificate_authority_arn"])
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate": certificate,
            "certificate_authority_arn": certificate_authority_arn,
        }
        if certificate_chain is not None:
            self._values["certificate_chain"] = certificate_chain
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def certificate(self) -> builtins.str:
        '''The Base64 PEM-encoded certificate authority certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-certificate
        '''
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_authority_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of your private CA.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-certificateauthorityarn
        '''
        result = self._values.get("certificate_authority_arn")
        assert result is not None, "Required property 'certificate_authority_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_chain(self) -> typing.Optional[builtins.str]:
        '''The Base64 PEM-encoded certificate chain that chains up to the root CA certificate that you used to sign your private CA certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-certificatechain
        '''
        result = self._values.get("certificate_chain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Status of your private CA.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCertificateAuthorityActivationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateAuthorityProps",
    jsii_struct_bases=[],
    name_mapping={
        "key_algorithm": "keyAlgorithm",
        "signing_algorithm": "signingAlgorithm",
        "subject": "subject",
        "type": "type",
        "csr_extensions": "csrExtensions",
        "key_storage_security_standard": "keyStorageSecurityStandard",
        "revocation_configuration": "revocationConfiguration",
        "tags": "tags",
        "usage_mode": "usageMode",
    },
)
class CfnCertificateAuthorityProps:
    def __init__(
        self,
        *,
        key_algorithm: builtins.str,
        signing_algorithm: builtins.str,
        subject: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.SubjectProperty, typing.Dict[builtins.str, typing.Any]]],
        type: builtins.str,
        csr_extensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.CsrExtensionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        key_storage_security_standard: typing.Optional[builtins.str] = None,
        revocation_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.RevocationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        usage_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCertificateAuthority``.

        :param key_algorithm: Type of the public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate. When you create a subordinate CA, you must use a key algorithm supported by the parent CA.
        :param signing_algorithm: Name of the algorithm your private CA uses to sign certificate requests. This parameter should not be confused with the ``SigningAlgorithm`` parameter used to sign certificates when they are issued.
        :param subject: Structure that contains X.500 distinguished name information for your private CA.
        :param type: Type of your private CA.
        :param csr_extensions: Specifies information to be added to the extension section of the certificate signing request (CSR).
        :param key_storage_security_standard: Specifies a cryptographic key management compliance standard used for handling CA keys. Default: FIPS_140_2_LEVEL_3_OR_HIGHER .. epigraph:: Some AWS Regions do not support the default. When creating a CA in these Regions, you must provide ``FIPS_140_2_LEVEL_2_OR_HIGHER`` as the argument for ``KeyStorageSecurityStandard`` . Failure to do this results in an ``InvalidArgsException`` with the message, "A certificate authority cannot be created in this region with the specified security standard." For information about security standard support in various Regions, see `Storage and security compliance of AWS Private CA private keys <https://docs.aws.amazon.com/privateca/latest/userguide/data-protection.html#private-keys>`_ .
        :param revocation_configuration: Certificate revocation information used by the `CreateCertificateAuthority <https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html>`_ and `UpdateCertificateAuthority <https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html>`_ actions. Your private certificate authority (CA) can configure Online Certificate Status Protocol (OCSP) support and/or maintain a certificate revocation list (CRL). OCSP returns validation information about certificates as requested by clients, and a CRL contains an updated list of certificates revoked by your CA. For more information, see `RevokeCertificate <https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html>`_ in the *AWS Private CA API Reference* and `Setting up a certificate revocation method <https://docs.aws.amazon.com/privateca/latest/userguide/revocation-setup.html>`_ in the *AWS Private CA User Guide* . .. epigraph:: The following requirements apply to revocation configurations. - A configuration disabling CRLs or OCSP must contain only the ``Enabled=False`` parameter, and will fail if other parameters such as ``CustomCname`` or ``ExpirationInDays`` are included. - In a CRL configuration, the ``S3BucketName`` parameter must conform to the `Amazon S3 bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html>`_ . - A configuration containing a custom Canonical Name (CNAME) parameter for CRLs or OCSP must conform to `RFC2396 <https://docs.aws.amazon.com/https://www.ietf.org/rfc/rfc2396.txt>`_ restrictions on the use of special characters in a CNAME. - In a CRL or OCSP configuration, the value of a CNAME parameter must not include a protocol prefix such as "http://" or "https://".
        :param tags: Key-value pairs that will be attached to the new private CA. You can associate up to 50 tags with a private CA. For information using tags with IAM to manage permissions, see `Controlling Access Using IAM Tags <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html>`_ .
        :param usage_mode: Specifies whether the CA issues general-purpose certificates that typically require a revocation mechanism, or short-lived certificates that may optionally omit revocation because they expire quickly. Short-lived certificate validity is limited to seven days. The default value is GENERAL_PURPOSE.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html
        :exampleMetadata: infused

        Example::

            cfn_certificate_authority = acmpca.CfnCertificateAuthority(self, "CA",
                type="ROOT",
                key_algorithm="RSA_2048",
                signing_algorithm="SHA256WITHRSA",
                subject=acmpca.CfnCertificateAuthority.SubjectProperty(
                    country="US",
                    organization="string",
                    organizational_unit="string",
                    distinguished_name_qualifier="string",
                    state="string",
                    common_name="123",
                    serial_number="string",
                    locality="string",
                    title="string",
                    surname="string",
                    given_name="string",
                    initials="DG",
                    pseudonym="string",
                    generation_qualifier="DBG"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__052831322c2ba10fea8b5f47de894be5f1f8c54474bf38a71f380e37f9733c87)
            check_type(argname="argument key_algorithm", value=key_algorithm, expected_type=type_hints["key_algorithm"])
            check_type(argname="argument signing_algorithm", value=signing_algorithm, expected_type=type_hints["signing_algorithm"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument csr_extensions", value=csr_extensions, expected_type=type_hints["csr_extensions"])
            check_type(argname="argument key_storage_security_standard", value=key_storage_security_standard, expected_type=type_hints["key_storage_security_standard"])
            check_type(argname="argument revocation_configuration", value=revocation_configuration, expected_type=type_hints["revocation_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument usage_mode", value=usage_mode, expected_type=type_hints["usage_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_algorithm": key_algorithm,
            "signing_algorithm": signing_algorithm,
            "subject": subject,
            "type": type,
        }
        if csr_extensions is not None:
            self._values["csr_extensions"] = csr_extensions
        if key_storage_security_standard is not None:
            self._values["key_storage_security_standard"] = key_storage_security_standard
        if revocation_configuration is not None:
            self._values["revocation_configuration"] = revocation_configuration
        if tags is not None:
            self._values["tags"] = tags
        if usage_mode is not None:
            self._values["usage_mode"] = usage_mode

    @builtins.property
    def key_algorithm(self) -> builtins.str:
        '''Type of the public key algorithm and size, in bits, of the key pair that your CA creates when it issues a certificate.

        When you create a subordinate CA, you must use a key algorithm supported by the parent CA.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-keyalgorithm
        '''
        result = self._values.get("key_algorithm")
        assert result is not None, "Required property 'key_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signing_algorithm(self) -> builtins.str:
        '''Name of the algorithm your private CA uses to sign certificate requests.

        This parameter should not be confused with the ``SigningAlgorithm`` parameter used to sign certificates when they are issued.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-signingalgorithm
        '''
        result = self._values.get("signing_algorithm")
        assert result is not None, "Required property 'signing_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subject(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCertificateAuthority.SubjectProperty]:
        '''Structure that contains X.500 distinguished name information for your private CA.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-subject
        '''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCertificateAuthority.SubjectProperty], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of your private CA.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def csr_extensions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCertificateAuthority.CsrExtensionsProperty]]:
        '''Specifies information to be added to the extension section of the certificate signing request (CSR).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-csrextensions
        '''
        result = self._values.get("csr_extensions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCertificateAuthority.CsrExtensionsProperty]], result)

    @builtins.property
    def key_storage_security_standard(self) -> typing.Optional[builtins.str]:
        '''Specifies a cryptographic key management compliance standard used for handling CA keys.

        Default: FIPS_140_2_LEVEL_3_OR_HIGHER
        .. epigraph::

           Some AWS Regions do not support the default. When creating a CA in these Regions, you must provide ``FIPS_140_2_LEVEL_2_OR_HIGHER`` as the argument for ``KeyStorageSecurityStandard`` . Failure to do this results in an ``InvalidArgsException`` with the message, "A certificate authority cannot be created in this region with the specified security standard."

           For information about security standard support in various Regions, see `Storage and security compliance of AWS Private CA private keys <https://docs.aws.amazon.com/privateca/latest/userguide/data-protection.html#private-keys>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-keystoragesecuritystandard
        '''
        result = self._values.get("key_storage_security_standard")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revocation_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCertificateAuthority.RevocationConfigurationProperty]]:
        '''Certificate revocation information used by the `CreateCertificateAuthority <https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html>`_ and `UpdateCertificateAuthority <https://docs.aws.amazon.com/privateca/latest/APIReference/API_UpdateCertificateAuthority.html>`_ actions. Your private certificate authority (CA) can configure Online Certificate Status Protocol (OCSP) support and/or maintain a certificate revocation list (CRL). OCSP returns validation information about certificates as requested by clients, and a CRL contains an updated list of certificates revoked by your CA. For more information, see `RevokeCertificate <https://docs.aws.amazon.com/privateca/latest/APIReference/API_RevokeCertificate.html>`_ in the *AWS Private CA API Reference* and `Setting up a certificate revocation method <https://docs.aws.amazon.com/privateca/latest/userguide/revocation-setup.html>`_ in the *AWS Private CA User Guide* .

        .. epigraph::

           The following requirements apply to revocation configurations.

           - A configuration disabling CRLs or OCSP must contain only the ``Enabled=False`` parameter, and will fail if other parameters such as ``CustomCname`` or ``ExpirationInDays`` are included.
           - In a CRL configuration, the ``S3BucketName`` parameter must conform to the `Amazon S3 bucket naming rules <https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html>`_ .
           - A configuration containing a custom Canonical Name (CNAME) parameter for CRLs or OCSP must conform to `RFC2396 <https://docs.aws.amazon.com/https://www.ietf.org/rfc/rfc2396.txt>`_ restrictions on the use of special characters in a CNAME.
           - In a CRL or OCSP configuration, the value of a CNAME parameter must not include a protocol prefix such as "http://" or "https://".

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-revocationconfiguration
        '''
        result = self._values.get("revocation_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCertificateAuthority.RevocationConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that will be attached to the new private CA.

        You can associate up to 50 tags with a private CA. For information using tags with IAM to manage permissions, see `Controlling Access Using IAM Tags <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def usage_mode(self) -> typing.Optional[builtins.str]:
        '''Specifies whether the CA issues general-purpose certificates that typically require a revocation mechanism, or short-lived certificates that may optionally omit revocation because they expire quickly.

        Short-lived certificate validity is limited to seven days.

        The default value is GENERAL_PURPOSE.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-usagemode
        '''
        result = self._values.get("usage_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCertificateAuthorityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_acmpca.CfnCertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_authority_arn": "certificateAuthorityArn",
        "certificate_signing_request": "certificateSigningRequest",
        "signing_algorithm": "signingAlgorithm",
        "validity": "validity",
        "api_passthrough": "apiPassthrough",
        "template_arn": "templateArn",
        "validity_not_before": "validityNotBefore",
    },
)
class CfnCertificateProps:
    def __init__(
        self,
        *,
        certificate_authority_arn: builtins.str,
        certificate_signing_request: builtins.str,
        signing_algorithm: builtins.str,
        validity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.ValidityProperty, typing.Dict[builtins.str, typing.Any]]],
        api_passthrough: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.ApiPassthroughProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        template_arn: typing.Optional[builtins.str] = None,
        validity_not_before: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.ValidityProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCertificate``.

        :param certificate_authority_arn: The Amazon Resource Name (ARN) for the private CA issues the certificate.
        :param certificate_signing_request: The certificate signing request (CSR) for the certificate.
        :param signing_algorithm: The name of the algorithm that will be used to sign the certificate to be issued. This parameter should not be confused with the ``SigningAlgorithm`` parameter used to sign a CSR in the ``CreateCertificateAuthority`` action. .. epigraph:: The specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key.
        :param validity: The period of time during which the certificate will be valid.
        :param api_passthrough: Specifies X.509 certificate information to be included in the issued certificate. An ``APIPassthrough`` or ``APICSRPassthrough`` template variant must be selected, or else this parameter is ignored.
        :param template_arn: Specifies a custom configuration template to use when issuing a certificate. If this parameter is not provided, AWS Private CA defaults to the ``EndEntityCertificate/V1`` template. For more information about AWS Private CA templates, see `Using Templates <https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html>`_ .
        :param validity_not_before: Information describing the start of the validity period of the certificate. This parameter sets the “Not Before" date for the certificate. By default, when issuing a certificate, AWS Private CA sets the "Not Before" date to the issuance time minus 60 minutes. This compensates for clock inconsistencies across computer systems. The ``ValidityNotBefore`` parameter can be used to customize the “Not Before” value. Unlike the ``Validity`` parameter, the ``ValidityNotBefore`` parameter is optional. The ``ValidityNotBefore`` value is expressed as an explicit date and time, using the ``Validity`` type value ``ABSOLUTE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_acmpca as acmpca
            
            cfn_certificate_props = acmpca.CfnCertificateProps(
                certificate_authority_arn="certificateAuthorityArn",
                certificate_signing_request="certificateSigningRequest",
                signing_algorithm="signingAlgorithm",
                validity=acmpca.CfnCertificate.ValidityProperty(
                    type="type",
                    value=123
                ),
            
                # the properties below are optional
                api_passthrough=acmpca.CfnCertificate.ApiPassthroughProperty(
                    extensions=acmpca.CfnCertificate.ExtensionsProperty(
                        certificate_policies=[acmpca.CfnCertificate.PolicyInformationProperty(
                            cert_policy_id="certPolicyId",
            
                            # the properties below are optional
                            policy_qualifiers=[acmpca.CfnCertificate.PolicyQualifierInfoProperty(
                                policy_qualifier_id="policyQualifierId",
                                qualifier=acmpca.CfnCertificate.QualifierProperty(
                                    cps_uri="cpsUri"
                                )
                            )]
                        )],
                        custom_extensions=[acmpca.CfnCertificate.CustomExtensionProperty(
                            object_identifier="objectIdentifier",
                            value="value",
            
                            # the properties below are optional
                            critical=False
                        )],
                        extended_key_usage=[acmpca.CfnCertificate.ExtendedKeyUsageProperty(
                            extended_key_usage_object_identifier="extendedKeyUsageObjectIdentifier",
                            extended_key_usage_type="extendedKeyUsageType"
                        )],
                        key_usage=acmpca.CfnCertificate.KeyUsageProperty(
                            crl_sign=False,
                            data_encipherment=False,
                            decipher_only=False,
                            digital_signature=False,
                            encipher_only=False,
                            key_agreement=False,
                            key_cert_sign=False,
                            key_encipherment=False,
                            non_repudiation=False
                        ),
                        subject_alternative_names=[acmpca.CfnCertificate.GeneralNameProperty(
                            directory_name=acmpca.CfnCertificate.SubjectProperty(
                                common_name="commonName",
                                country="country",
                                custom_attributes=[acmpca.CfnCertificate.CustomAttributeProperty(
                                    object_identifier="objectIdentifier",
                                    value="value"
                                )],
                                distinguished_name_qualifier="distinguishedNameQualifier",
                                generation_qualifier="generationQualifier",
                                given_name="givenName",
                                initials="initials",
                                locality="locality",
                                organization="organization",
                                organizational_unit="organizationalUnit",
                                pseudonym="pseudonym",
                                serial_number="serialNumber",
                                state="state",
                                surname="surname",
                                title="title"
                            ),
                            dns_name="dnsName",
                            edi_party_name=acmpca.CfnCertificate.EdiPartyNameProperty(
                                name_assigner="nameAssigner",
                                party_name="partyName"
                            ),
                            ip_address="ipAddress",
                            other_name=acmpca.CfnCertificate.OtherNameProperty(
                                type_id="typeId",
                                value="value"
                            ),
                            registered_id="registeredId",
                            rfc822_name="rfc822Name",
                            uniform_resource_identifier="uniformResourceIdentifier"
                        )]
                    ),
                    subject=acmpca.CfnCertificate.SubjectProperty(
                        common_name="commonName",
                        country="country",
                        custom_attributes=[acmpca.CfnCertificate.CustomAttributeProperty(
                            object_identifier="objectIdentifier",
                            value="value"
                        )],
                        distinguished_name_qualifier="distinguishedNameQualifier",
                        generation_qualifier="generationQualifier",
                        given_name="givenName",
                        initials="initials",
                        locality="locality",
                        organization="organization",
                        organizational_unit="organizationalUnit",
                        pseudonym="pseudonym",
                        serial_number="serialNumber",
                        state="state",
                        surname="surname",
                        title="title"
                    )
                ),
                template_arn="templateArn",
                validity_not_before=acmpca.CfnCertificate.ValidityProperty(
                    type="type",
                    value=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acca39b375eaa0ca77d761ffe82a05a53633d418331265d827cb5959406a431b)
            check_type(argname="argument certificate_authority_arn", value=certificate_authority_arn, expected_type=type_hints["certificate_authority_arn"])
            check_type(argname="argument certificate_signing_request", value=certificate_signing_request, expected_type=type_hints["certificate_signing_request"])
            check_type(argname="argument signing_algorithm", value=signing_algorithm, expected_type=type_hints["signing_algorithm"])
            check_type(argname="argument validity", value=validity, expected_type=type_hints["validity"])
            check_type(argname="argument api_passthrough", value=api_passthrough, expected_type=type_hints["api_passthrough"])
            check_type(argname="argument template_arn", value=template_arn, expected_type=type_hints["template_arn"])
            check_type(argname="argument validity_not_before", value=validity_not_before, expected_type=type_hints["validity_not_before"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_authority_arn": certificate_authority_arn,
            "certificate_signing_request": certificate_signing_request,
            "signing_algorithm": signing_algorithm,
            "validity": validity,
        }
        if api_passthrough is not None:
            self._values["api_passthrough"] = api_passthrough
        if template_arn is not None:
            self._values["template_arn"] = template_arn
        if validity_not_before is not None:
            self._values["validity_not_before"] = validity_not_before

    @builtins.property
    def certificate_authority_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the private CA issues the certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-certificateauthorityarn
        '''
        result = self._values.get("certificate_authority_arn")
        assert result is not None, "Required property 'certificate_authority_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_signing_request(self) -> builtins.str:
        '''The certificate signing request (CSR) for the certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-certificatesigningrequest
        '''
        result = self._values.get("certificate_signing_request")
        assert result is not None, "Required property 'certificate_signing_request' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signing_algorithm(self) -> builtins.str:
        '''The name of the algorithm that will be used to sign the certificate to be issued.

        This parameter should not be confused with the ``SigningAlgorithm`` parameter used to sign a CSR in the ``CreateCertificateAuthority`` action.
        .. epigraph::

           The specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-signingalgorithm
        '''
        result = self._values.get("signing_algorithm")
        assert result is not None, "Required property 'signing_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def validity(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCertificate.ValidityProperty]:
        '''The period of time during which the certificate will be valid.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-validity
        '''
        result = self._values.get("validity")
        assert result is not None, "Required property 'validity' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCertificate.ValidityProperty], result)

    @builtins.property
    def api_passthrough(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCertificate.ApiPassthroughProperty]]:
        '''Specifies X.509 certificate information to be included in the issued certificate. An ``APIPassthrough`` or ``APICSRPassthrough`` template variant must be selected, or else this parameter is ignored.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-apipassthrough
        '''
        result = self._values.get("api_passthrough")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCertificate.ApiPassthroughProperty]], result)

    @builtins.property
    def template_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies a custom configuration template to use when issuing a certificate.

        If this parameter is not provided, AWS Private CA defaults to the ``EndEntityCertificate/V1`` template. For more information about AWS Private CA templates, see `Using Templates <https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-templatearn
        '''
        result = self._values.get("template_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validity_not_before(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCertificate.ValidityProperty]]:
        '''Information describing the start of the validity period of the certificate.

        This parameter sets the “Not Before" date for the certificate.

        By default, when issuing a certificate, AWS Private CA sets the "Not Before" date to the issuance time minus 60 minutes. This compensates for clock inconsistencies across computer systems. The ``ValidityNotBefore`` parameter can be used to customize the “Not Before” value.

        Unlike the ``Validity`` parameter, the ``ValidityNotBefore`` parameter is optional.

        The ``ValidityNotBefore`` value is expressed as an explicit date and time, using the ``Validity`` type value ``ABSOLUTE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-validitynotbefore
        '''
        result = self._values.get("validity_not_before")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCertificate.ValidityProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPermission(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_acmpca.CfnPermission",
):
    '''Grants permissions to the AWS Certificate Manager ( ACM ) service principal ( ``acm.amazonaws.com`` ) to perform `IssueCertificate <https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html>`_ , `GetCertificate <https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificate.html>`_ , and `ListPermissions <https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListPermissions.html>`_ actions on a CA. These actions are needed for the ACM principal to renew private PKI certificates requested through ACM and residing in the same AWS account as the CA.

    **About permissions** - If the private CA and the certificates it issues reside in the same account, you can use ``AWS::ACMPCA::Permission`` to grant permissions for ACM to carry out automatic certificate renewals.

    - For automatic certificate renewal to succeed, the ACM service principal needs permissions to create, retrieve, and list permissions.
    - If the private CA and the ACM certificates reside in different accounts, then permissions cannot be used to enable automatic renewals. Instead, the ACM certificate owner must set up a resource-based policy to enable cross-account issuance and renewals. For more information, see `Using a Resource Based Policy with AWS Private CA <https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html>`_ .

    .. epigraph::

       To update an ``AWS::ACMPCA::Permission`` resource, you must first delete the existing permission resource from the CloudFormation stack and then create a new permission resource with updated properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_acmpca as acmpca
        
        cfn_permission = acmpca.CfnPermission(self, "MyCfnPermission",
            actions=["actions"],
            certificate_authority_arn="certificateAuthorityArn",
            principal="principal",
        
            # the properties below are optional
            source_account="sourceAccount"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        actions: typing.Sequence[builtins.str],
        certificate_authority_arn: builtins.str,
        principal: builtins.str,
        source_account: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param actions: The private CA actions that can be performed by the designated AWS service. Supported actions are ``IssueCertificate`` , ``GetCertificate`` , and ``ListPermissions`` .
        :param certificate_authority_arn: The Amazon Resource Number (ARN) of the private CA from which the permission was issued.
        :param principal: The AWS service or entity that holds the permission. At this time, the only valid principal is ``acm.amazonaws.com`` .
        :param source_account: The ID of the account that assigned the permission.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7403df10c7598bb11bc4b6722147156ca094291bc6367ca41ea832274c8ba866)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPermissionProps(
            actions=actions,
            certificate_authority_arn=certificate_authority_arn,
            principal=principal,
            source_account=source_account,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__736cd0bbd63ec99b393fc6cfb13ed07576415246aa33c0d3f8bef76d76c571f2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a942124043a22313212f4489fd8a8d5fd3886ab1ae46cfa306ee2b3024cf78f)
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
    @jsii.member(jsii_name="actions")
    def actions(self) -> typing.List[builtins.str]:
        '''The private CA actions that can be performed by the designated AWS service.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "actions"))

    @actions.setter
    def actions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d66768d9ebbeae3804aef733e92b2f439fa97176bd7c8fe4678fdb5bcb1a203c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actions", value)

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> builtins.str:
        '''The Amazon Resource Number (ARN) of the private CA from which the permission was issued.'''
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthorityArn"))

    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cedc10edb2bf740d73d914ce4705a9a6c80297d3e34901af9a5206b3fe6d131)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthorityArn", value)

    @builtins.property
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        '''The AWS service or entity that holds the permission.'''
        return typing.cast(builtins.str, jsii.get(self, "principal"))

    @principal.setter
    def principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15c3392ebc670af42af684ca42dddcffe29ad37af007e2788604447f884ea595)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)

    @builtins.property
    @jsii.member(jsii_name="sourceAccount")
    def source_account(self) -> typing.Optional[builtins.str]:
        '''The ID of the account that assigned the permission.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceAccount"))

    @source_account.setter
    def source_account(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__336a294e18ad34a8379580ec71e5c0dca499ba44efb4e2cad4bf5190ba57b1fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceAccount", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_acmpca.CfnPermissionProps",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "certificate_authority_arn": "certificateAuthorityArn",
        "principal": "principal",
        "source_account": "sourceAccount",
    },
)
class CfnPermissionProps:
    def __init__(
        self,
        *,
        actions: typing.Sequence[builtins.str],
        certificate_authority_arn: builtins.str,
        principal: builtins.str,
        source_account: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPermission``.

        :param actions: The private CA actions that can be performed by the designated AWS service. Supported actions are ``IssueCertificate`` , ``GetCertificate`` , and ``ListPermissions`` .
        :param certificate_authority_arn: The Amazon Resource Number (ARN) of the private CA from which the permission was issued.
        :param principal: The AWS service or entity that holds the permission. At this time, the only valid principal is ``acm.amazonaws.com`` .
        :param source_account: The ID of the account that assigned the permission.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_acmpca as acmpca
            
            cfn_permission_props = acmpca.CfnPermissionProps(
                actions=["actions"],
                certificate_authority_arn="certificateAuthorityArn",
                principal="principal",
            
                # the properties below are optional
                source_account="sourceAccount"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e4f8a50d06c841025fd393d8e235b3e62339c693e4dbb7a9ab17b5554c6a581)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument certificate_authority_arn", value=certificate_authority_arn, expected_type=type_hints["certificate_authority_arn"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument source_account", value=source_account, expected_type=type_hints["source_account"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "certificate_authority_arn": certificate_authority_arn,
            "principal": principal,
        }
        if source_account is not None:
            self._values["source_account"] = source_account

    @builtins.property
    def actions(self) -> typing.List[builtins.str]:
        '''The private CA actions that can be performed by the designated AWS service.

        Supported actions are ``IssueCertificate`` , ``GetCertificate`` , and ``ListPermissions`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-actions
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def certificate_authority_arn(self) -> builtins.str:
        '''The Amazon Resource Number (ARN) of the private CA from which the permission was issued.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-certificateauthorityarn
        '''
        result = self._values.get("certificate_authority_arn")
        assert result is not None, "Required property 'certificate_authority_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal(self) -> builtins.str:
        '''The AWS service or entity that holds the permission.

        At this time, the only valid principal is ``acm.amazonaws.com`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-principal
        '''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_account(self) -> typing.Optional[builtins.str]:
        '''The ID of the account that assigned the permission.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-sourceaccount
        '''
        result = self._values.get("source_account")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPermissionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_acmpca.ICertificateAuthority")
class ICertificateAuthority(_IResource_c80c4260, typing_extensions.Protocol):
    '''Interface which all CertificateAuthority based class must implement.'''

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> builtins.str:
        '''The Amazon Resource Name of the Certificate.

        :attribute: true
        '''
        ...


class _ICertificateAuthorityProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Interface which all CertificateAuthority based class must implement.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_acmpca.ICertificateAuthority"

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> builtins.str:
        '''The Amazon Resource Name of the Certificate.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthorityArn"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICertificateAuthority).__jsii_proxy_class__ = lambda : _ICertificateAuthorityProxy


__all__ = [
    "CertificateAuthority",
    "CfnCertificate",
    "CfnCertificateAuthority",
    "CfnCertificateAuthorityActivation",
    "CfnCertificateAuthorityActivationProps",
    "CfnCertificateAuthorityProps",
    "CfnCertificateProps",
    "CfnPermission",
    "CfnPermissionProps",
    "ICertificateAuthority",
]

publication.publish()

def _typecheckingstub__e1395360f89634b836bfd8f83f0cbc2f4dbb936a9ba23c531cd8ffe3998f45c2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    certificate_authority_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c63a1f66d359048e3b7f539f55f0320982cfa96588aa92aa5a52d4f490ff7c7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    certificate_authority_arn: builtins.str,
    certificate_signing_request: builtins.str,
    signing_algorithm: builtins.str,
    validity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.ValidityProperty, typing.Dict[builtins.str, typing.Any]]],
    api_passthrough: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.ApiPassthroughProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_arn: typing.Optional[builtins.str] = None,
    validity_not_before: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.ValidityProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae245fe6e4335d443fbf3d06674c0a246856a567c69eac96b60daf71940d2ba9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ced20980ce5020a1c27b089ee9acf9c670389a6dca8d4db4d86c9ffbf01c1a1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__929f46388471884d412a93caaec6152169738bcde7736082806fa61355f38450(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16a09377d92f4e276678c2c81de91b48247f6567816f2a450052d3564b74e969(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__643e9821d5b63922252de6f66c05ac417883bee41b28c13cf3db8cd2632e14e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b0f98fada0460f1013060888886a3c2a49f08cade3f294d7b78ab8077353d28(
    value: typing.Union[_IResolvable_da3f097b, CfnCertificate.ValidityProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07edd7fc55218dbdda428adf3aa29d974595465ca0c1084ed6f98a79f08d4841(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCertificate.ApiPassthroughProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20f419f7a37472cedd9954e752bfa553241909264a1db9544a8edce9404b9552(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce4f5fb71e1d9798d96fd2e8524ac910685f8e895b03a85141518face166fd7e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCertificate.ValidityProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c063a4aa0db8588e572959a6949f00a9e649d71349c0f01000aee85a36d5959(
    *,
    extensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.ExtensionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    subject: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.SubjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98994bee25a07a794a889c37c3d7fad1758f74e523835472e78fee9b53895d92(
    *,
    object_identifier: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51c3c7eafba7b9c58470900a599324795cc525bc9a07c9dca8f8225ffa1776cc(
    *,
    object_identifier: builtins.str,
    value: builtins.str,
    critical: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0061c1a7a051fd8dd8ea03b1a7705465837ca64fe8e1aaee6033e7ba0e78499f(
    *,
    name_assigner: builtins.str,
    party_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2060402888ad8f292021f28746d894182b12eb1844683d776ca901ec58edf19(
    *,
    extended_key_usage_object_identifier: typing.Optional[builtins.str] = None,
    extended_key_usage_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f542a5e2932abd07f7c4fac088c4ae0b0560522e990c6e4ad85dbfe915c5854b(
    *,
    certificate_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.PolicyInformationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    custom_extensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.CustomExtensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    extended_key_usage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.ExtendedKeyUsageProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    key_usage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.KeyUsageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    subject_alternative_names: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.GeneralNameProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__430fe7518ff7ed70184671ff079a80b537708dad686da415fe31db2f83f9a991(
    *,
    directory_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.SubjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dns_name: typing.Optional[builtins.str] = None,
    edi_party_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.EdiPartyNameProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ip_address: typing.Optional[builtins.str] = None,
    other_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.OtherNameProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    registered_id: typing.Optional[builtins.str] = None,
    rfc822_name: typing.Optional[builtins.str] = None,
    uniform_resource_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f50230a7e5fd5786670a469e1db1bb8ceadc1d39e95454db10bc795348abf38c(
    *,
    crl_sign: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    data_encipherment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    decipher_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    digital_signature: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    encipher_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    key_agreement: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    key_cert_sign: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    key_encipherment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    non_repudiation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__620191e18964b334afd3f451ecad5f454c321164e05b6bdb1f75897c2ea3f73f(
    *,
    type_id: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0fa8861568fe4db83bd309e3f4d649fe7756fe2dd1ed1ee0ef9fbd24abf8d32(
    *,
    cert_policy_id: builtins.str,
    policy_qualifiers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.PolicyQualifierInfoProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0e7f8f4f896a22f7904c707eeac3e27d496db6421b2ec5f4494b75be75f9670(
    *,
    policy_qualifier_id: builtins.str,
    qualifier: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.QualifierProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48eb999ea7bed23111f3eabf8a679cdc5d044a7c3764f62d64d132c1815c3ec4(
    *,
    cps_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2b7efde7b9d2e6233f33ab24f10ede12022114a34cf3d75ff1d1bf6b8283a93(
    *,
    common_name: typing.Optional[builtins.str] = None,
    country: typing.Optional[builtins.str] = None,
    custom_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.CustomAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    distinguished_name_qualifier: typing.Optional[builtins.str] = None,
    generation_qualifier: typing.Optional[builtins.str] = None,
    given_name: typing.Optional[builtins.str] = None,
    initials: typing.Optional[builtins.str] = None,
    locality: typing.Optional[builtins.str] = None,
    organization: typing.Optional[builtins.str] = None,
    organizational_unit: typing.Optional[builtins.str] = None,
    pseudonym: typing.Optional[builtins.str] = None,
    serial_number: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    surname: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__843e728892e8512a7c481feaede4179f4288a992c2488e36dd55acf5618446bd(
    *,
    type: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6947ebcc03e9e02f9fc5dee73eaa3cd88dd10713851f61d2ce61f6210abfb16(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    key_algorithm: builtins.str,
    signing_algorithm: builtins.str,
    subject: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.SubjectProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
    csr_extensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.CsrExtensionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    key_storage_security_standard: typing.Optional[builtins.str] = None,
    revocation_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.RevocationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    usage_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97a6fe8ac6bf6021d6476713901b5d434081cdc009d802a3f665c0611673e27e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20898061f346ffdc7eeb4ea9b7e48dcc46ae909c1b748cd318e50ca8408327e8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7e6c5981edef9a3b3627b2003de2630869e19cd61c48d608bfd86a7f219e472(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7e2832fbc61e46c30f08119509dacf6b15d90881721ef6f70b6331442b62041(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65bb497527ac064e6e2dac08377e39c6239f7e846ca18078132927a75d6471bb(
    value: typing.Union[_IResolvable_da3f097b, CfnCertificateAuthority.SubjectProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77017d7803db08d3adb6df13436c6f61e9248dba04cb27f3ad2c009449c54235(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__672400fc9d101cb3557ef2b74a3ed2c3389e8f619013c4b2a84263707b9ad5d3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCertificateAuthority.CsrExtensionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be8e4d5ae1e7416c87aef05e06dfd53984f27b32f1d6ac821bb176da70ccf89f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__203567ece18e0659c536811874601c021c570afc77b0834d25d2e06ac2849f57(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCertificateAuthority.RevocationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01bad6d3cb4db9f6f71a433aa44c7435297b8f644c8fdcbe06a0550035a76fa5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d183c3c1616f42e791fb50dd3640b6710dbdb67c4b67d83635a3687f5abb9d0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44464105e0a77464936471a53d0b7f113a7a84bceeeb9b081b7a817472f3c88c(
    *,
    access_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.GeneralNameProperty, typing.Dict[builtins.str, typing.Any]]],
    access_method: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.AccessMethodProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a665d65bdd95c9f57ee7ca3fee24e377b63436ab67f86d6e09696910c191d3e2(
    *,
    access_method_type: typing.Optional[builtins.str] = None,
    custom_object_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de72782a3b3117c1f101c2c6c2fad457863e581a5bdcd67a1280a825dc55ea17(
    *,
    custom_cname: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    expiration_in_days: typing.Optional[jsii.Number] = None,
    s3_bucket_name: typing.Optional[builtins.str] = None,
    s3_object_acl: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fad5bc7b7fbc7061150ae02b07b6566cf328ba6ffd556e6c6ea3738e4c89711a(
    *,
    key_usage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.KeyUsageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    subject_information_access: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.AccessDescriptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0caab149cb10c9e2e41c808164411855ca5f9298e171e0db7a1a0913ea642d2(
    *,
    object_identifier: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e187a86a6b5c31d0b8c99e998eea3f8683787066dcfd319750892c59195bf6e8(
    *,
    name_assigner: builtins.str,
    party_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9350b2847a089516fb8a320d9014174879fc12ab6024b5f5abe53240af563f91(
    *,
    directory_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.SubjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dns_name: typing.Optional[builtins.str] = None,
    edi_party_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.EdiPartyNameProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ip_address: typing.Optional[builtins.str] = None,
    other_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.OtherNameProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    registered_id: typing.Optional[builtins.str] = None,
    rfc822_name: typing.Optional[builtins.str] = None,
    uniform_resource_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8dd4df3844e389720f6addec59149d792d65195686e07b6e154c3a6d3da26e6(
    *,
    crl_sign: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    data_encipherment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    decipher_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    digital_signature: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    encipher_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    key_agreement: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    key_cert_sign: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    key_encipherment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    non_repudiation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db2a6b0f215dcb411b988d99d6a91fb7c758aefe4260650026b58ba7b1cddde5(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ocsp_custom_cname: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__798f8d72c7f9ddb26ba8e82b9a6c8b81465d40f828b01a11ac8c09bfb53381ff(
    *,
    type_id: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b8bd7c76f7f0154f73285d0a3cebdc5be93c7168017624ee216b2e39d0a3ec0(
    *,
    crl_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.CrlConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ocsp_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.OcspConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fe22c69366f0a777e4079f3471779342ff021a43565fd6a2cc33bd8cb705970(
    *,
    common_name: typing.Optional[builtins.str] = None,
    country: typing.Optional[builtins.str] = None,
    custom_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.CustomAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    distinguished_name_qualifier: typing.Optional[builtins.str] = None,
    generation_qualifier: typing.Optional[builtins.str] = None,
    given_name: typing.Optional[builtins.str] = None,
    initials: typing.Optional[builtins.str] = None,
    locality: typing.Optional[builtins.str] = None,
    organization: typing.Optional[builtins.str] = None,
    organizational_unit: typing.Optional[builtins.str] = None,
    pseudonym: typing.Optional[builtins.str] = None,
    serial_number: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    surname: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e91763a1b089310141664991133bb321cced18cd10da038baa589bcc1474a665(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    certificate: builtins.str,
    certificate_authority_arn: builtins.str,
    certificate_chain: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aa9f665899e699513e4e5b43f65abecdf25087e15d590d69d34112ce8a940fd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__affce5b20bcb3ac9dadff19bff87a0c6ab15d608153cfb9a691b56aeaecfb1a2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b279179f6b525656e5ee2f3b4d595cb75d494cf246f2e92a8469589c5395bfdd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43dd6c4689519828c2c042c80ee0ae6a9d3b03512aaac4693b2c9abdf2799b92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87c41ac4f9f42cd4127fcc9a6dfc22f017ed7eeba7dd94714974f3af2143dce1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bb84ac3ee8ec3f7d2297504aaca248c351bd9fd6b388a9a80a5c547a8b217eb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b63918960d16b9d2632b9277b07b10494327c3d038ba9f5522225f20dfed02d(
    *,
    certificate: builtins.str,
    certificate_authority_arn: builtins.str,
    certificate_chain: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__052831322c2ba10fea8b5f47de894be5f1f8c54474bf38a71f380e37f9733c87(
    *,
    key_algorithm: builtins.str,
    signing_algorithm: builtins.str,
    subject: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.SubjectProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
    csr_extensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.CsrExtensionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    key_storage_security_standard: typing.Optional[builtins.str] = None,
    revocation_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificateAuthority.RevocationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    usage_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acca39b375eaa0ca77d761ffe82a05a53633d418331265d827cb5959406a431b(
    *,
    certificate_authority_arn: builtins.str,
    certificate_signing_request: builtins.str,
    signing_algorithm: builtins.str,
    validity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.ValidityProperty, typing.Dict[builtins.str, typing.Any]]],
    api_passthrough: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.ApiPassthroughProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_arn: typing.Optional[builtins.str] = None,
    validity_not_before: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.ValidityProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7403df10c7598bb11bc4b6722147156ca094291bc6367ca41ea832274c8ba866(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    actions: typing.Sequence[builtins.str],
    certificate_authority_arn: builtins.str,
    principal: builtins.str,
    source_account: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__736cd0bbd63ec99b393fc6cfb13ed07576415246aa33c0d3f8bef76d76c571f2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a942124043a22313212f4489fd8a8d5fd3886ab1ae46cfa306ee2b3024cf78f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d66768d9ebbeae3804aef733e92b2f439fa97176bd7c8fe4678fdb5bcb1a203c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cedc10edb2bf740d73d914ce4705a9a6c80297d3e34901af9a5206b3fe6d131(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15c3392ebc670af42af684ca42dddcffe29ad37af007e2788604447f884ea595(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__336a294e18ad34a8379580ec71e5c0dca499ba44efb4e2cad4bf5190ba57b1fd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e4f8a50d06c841025fd393d8e235b3e62339c693e4dbb7a9ab17b5554c6a581(
    *,
    actions: typing.Sequence[builtins.str],
    certificate_authority_arn: builtins.str,
    principal: builtins.str,
    source_account: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
