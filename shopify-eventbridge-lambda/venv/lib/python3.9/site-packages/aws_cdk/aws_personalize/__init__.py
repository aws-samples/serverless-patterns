'''
# AWS::Personalize Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_personalize as personalize
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Personalize construct libraries](https://constructs.dev/search?q=personalize)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Personalize resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Personalize.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Personalize](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Personalize.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnDataset(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_personalize.CfnDataset",
):
    '''Creates an empty dataset and adds it to the specified dataset group.

    Use `CreateDatasetImportJob <https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetImportJob.html>`_ to import your training data to a dataset.

    There are 5 types of datasets:

    - Item interactions
    - Items
    - Users
    - Action interactions (you can't use CloudFormation to create an Action interactions dataset)
    - Actions (you can't use CloudFormation to create an Actions dataset)

    Each dataset type has an associated schema with required field types. Only the ``Item interactions`` dataset is required in order to train a model (also referred to as creating a solution).

    A dataset can be in one of the following states:

    - CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED
    - DELETE PENDING > DELETE IN_PROGRESS

    To get the status of the dataset, call `DescribeDataset <https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataset.html>`_ .

    **Related APIs** - `CreateDatasetGroup <https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetGroup.html>`_

    - `ListDatasets <https://docs.aws.amazon.com/personalize/latest/dg/API_ListDatasets.html>`_
    - `DescribeDataset <https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataset.html>`_
    - `DeleteDataset <https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteDataset.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html
    :cloudformationResource: AWS::Personalize::Dataset
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_personalize as personalize
        
        # data_source: Any
        
        cfn_dataset = personalize.CfnDataset(self, "MyCfnDataset",
            dataset_group_arn="datasetGroupArn",
            dataset_type="datasetType",
            name="name",
            schema_arn="schemaArn",
        
            # the properties below are optional
            dataset_import_job=personalize.CfnDataset.DatasetImportJobProperty(
                dataset_arn="datasetArn",
                dataset_import_job_arn="datasetImportJobArn",
                data_source=data_source,
                job_name="jobName",
                role_arn="roleArn"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        dataset_group_arn: builtins.str,
        dataset_type: builtins.str,
        name: builtins.str,
        schema_arn: builtins.str,
        dataset_import_job: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.DatasetImportJobProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param dataset_group_arn: The Amazon Resource Name (ARN) of the dataset group.
        :param dataset_type: One of the following values:. - Interactions - Items - Users .. epigraph:: You can't use CloudFormation to create an Action Interactions or Actions dataset.
        :param name: The name of the dataset.
        :param schema_arn: The ARN of the associated schema.
        :param dataset_import_job: Describes a job that imports training data from a data source (Amazon S3 bucket) to an Amazon Personalize dataset. If you specify a dataset import job as part of a dataset, all dataset import job fields are required.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8515dadec60af65aa740f35c8bee6bc85dafa7634c6b2270232bfa824452ebce)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatasetProps(
            dataset_group_arn=dataset_group_arn,
            dataset_type=dataset_type,
            name=name,
            schema_arn=schema_arn,
            dataset_import_job=dataset_import_job,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccbc61bfda7b82706a4bcf79fd5c92ea9ecab41d2ce92088c0f4792b980823a1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f187d3b2924b81109808f7eaa45f19c8884e1e1dea57aa4de729b9205cf518d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDatasetArn")
    def attr_dataset_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the dataset.

        :cloudformationAttribute: DatasetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatasetArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="datasetGroupArn")
    def dataset_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the dataset group.'''
        return typing.cast(builtins.str, jsii.get(self, "datasetGroupArn"))

    @dataset_group_arn.setter
    def dataset_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92b16c3f5a79428072afbfa189b761a25212440d1c418c8aeb6b18a8e98c91ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="datasetType")
    def dataset_type(self) -> builtins.str:
        '''One of the following values:.'''
        return typing.cast(builtins.str, jsii.get(self, "datasetType"))

    @dataset_type.setter
    def dataset_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92562664ab00f1e9056f6606e2970466af3ea0874ff465dde6f00b6ff0a5e8af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the dataset.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf263591c9e23855d850751cd45cff2e048c43deb7e160e3bada974d92469338)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schemaArn")
    def schema_arn(self) -> builtins.str:
        '''The ARN of the associated schema.'''
        return typing.cast(builtins.str, jsii.get(self, "schemaArn"))

    @schema_arn.setter
    def schema_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__113b0bea00700cff01f2c19ac9225d2dc8fbdd0c5ddf4b14941a4f9cf60fb979)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaArn", value)

    @builtins.property
    @jsii.member(jsii_name="datasetImportJob")
    def dataset_import_job(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.DatasetImportJobProperty"]]:
        '''Describes a job that imports training data from a data source (Amazon S3 bucket) to an Amazon Personalize dataset.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.DatasetImportJobProperty"]], jsii.get(self, "datasetImportJob"))

    @dataset_import_job.setter
    def dataset_import_job(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.DatasetImportJobProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afd06f21a72ea38837a666025b223a4003de38fe4bd9ff9796a64ce7a35f855d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetImportJob", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_personalize.CfnDataset.DataSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"data_location": "dataLocation"},
    )
    class DataSourceProperty:
        def __init__(
            self,
            *,
            data_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the data source that contains the data to upload to a dataset, or the list of records to delete from Amazon Personalize.

            :param data_location: For dataset import jobs, the path to the Amazon S3 bucket where the data that you want to upload to your dataset is stored. For data deletion jobs, the path to the Amazon S3 bucket that stores the list of records to delete. For example: ``s3://bucket-name/folder-name/fileName.csv`` If your CSV files are in a folder in your Amazon S3 bucket and you want your import job or data deletion job to consider multiple files, you can specify the path to the folder. With a data deletion job, Amazon Personalize uses all files in the folder and any sub folder. Use the following syntax with a ``/`` after the folder name: ``s3://bucket-name/folder-name/``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_personalize as personalize
                
                data_source_property = personalize.CfnDataset.DataSourceProperty(
                    data_location="dataLocation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__83ea3d6dacd8545ca3b15725588aca74892b310d047ede8d4d6e0e1671a9a0f1)
                check_type(argname="argument data_location", value=data_location, expected_type=type_hints["data_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data_location is not None:
                self._values["data_location"] = data_location

        @builtins.property
        def data_location(self) -> typing.Optional[builtins.str]:
            '''For dataset import jobs, the path to the Amazon S3 bucket where the data that you want to upload to your dataset is stored.

            For data deletion jobs, the path to the Amazon S3 bucket that stores the list of records to delete.

            For example:

            ``s3://bucket-name/folder-name/fileName.csv``

            If your CSV files are in a folder in your Amazon S3 bucket and you want your import job or data deletion job to consider multiple files, you can specify the path to the folder. With a data deletion job, Amazon Personalize uses all files in the folder and any sub folder. Use the following syntax with a ``/`` after the folder name:

            ``s3://bucket-name/folder-name/``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasource.html#cfn-personalize-dataset-datasource-datalocation
            '''
            result = self._values.get("data_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_personalize.CfnDataset.DatasetImportJobProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dataset_arn": "datasetArn",
            "dataset_import_job_arn": "datasetImportJobArn",
            "data_source": "dataSource",
            "job_name": "jobName",
            "role_arn": "roleArn",
        },
    )
    class DatasetImportJobProperty:
        def __init__(
            self,
            *,
            dataset_arn: typing.Optional[builtins.str] = None,
            dataset_import_job_arn: typing.Optional[builtins.str] = None,
            data_source: typing.Any = None,
            job_name: typing.Optional[builtins.str] = None,
            role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a job that imports training data from a data source (Amazon S3 bucket) to an Amazon Personalize dataset.

            A dataset import job can be in one of the following states:

            - CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

            If you specify a dataset import job as part of a dataset, all dataset import job fields are required.

            :param dataset_arn: The Amazon Resource Name (ARN) of the dataset that receives the imported data.
            :param dataset_import_job_arn: The ARN of the dataset import job.
            :param data_source: The Amazon S3 bucket that contains the training data to import.
            :param job_name: The name of the import job.
            :param role_arn: The ARN of the IAM role that has permissions to read from the Amazon S3 data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_personalize as personalize
                
                # data_source: Any
                
                dataset_import_job_property = personalize.CfnDataset.DatasetImportJobProperty(
                    dataset_arn="datasetArn",
                    dataset_import_job_arn="datasetImportJobArn",
                    data_source=data_source,
                    job_name="jobName",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f52207436b51d5c04d39a2c4edfacf59c3bb268757202e992b324a790558d823)
                check_type(argname="argument dataset_arn", value=dataset_arn, expected_type=type_hints["dataset_arn"])
                check_type(argname="argument dataset_import_job_arn", value=dataset_import_job_arn, expected_type=type_hints["dataset_import_job_arn"])
                check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
                check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dataset_arn is not None:
                self._values["dataset_arn"] = dataset_arn
            if dataset_import_job_arn is not None:
                self._values["dataset_import_job_arn"] = dataset_import_job_arn
            if data_source is not None:
                self._values["data_source"] = data_source
            if job_name is not None:
                self._values["job_name"] = job_name
            if role_arn is not None:
                self._values["role_arn"] = role_arn

        @builtins.property
        def dataset_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the dataset that receives the imported data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html#cfn-personalize-dataset-datasetimportjob-datasetarn
            '''
            result = self._values.get("dataset_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dataset_import_job_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the dataset import job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html#cfn-personalize-dataset-datasetimportjob-datasetimportjobarn
            '''
            result = self._values.get("dataset_import_job_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_source(self) -> typing.Any:
            '''The Amazon S3 bucket that contains the training data to import.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html#cfn-personalize-dataset-datasetimportjob-datasource
            '''
            result = self._values.get("data_source")
            return typing.cast(typing.Any, result)

        @builtins.property
        def job_name(self) -> typing.Optional[builtins.str]:
            '''The name of the import job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html#cfn-personalize-dataset-datasetimportjob-jobname
            '''
            result = self._values.get("job_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the IAM role that has permissions to read from the Amazon S3 data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html#cfn-personalize-dataset-datasetimportjob-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetImportJobProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnDatasetGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_personalize.CfnDatasetGroup",
):
    '''A dataset group is a collection of related datasets (Item interactions, Users, Items, Actions, Action interactions).

    You create a dataset group by calling `CreateDatasetGroup <https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetGroup.html>`_ . You then create a dataset and add it to a dataset group by calling `CreateDataset <https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataset.html>`_ . The dataset group is used to create and train a solution by calling `CreateSolution <https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html>`_ . A dataset group can contain only one of each type of dataset.

    You can specify an AWS Key Management Service (KMS) key to encrypt the datasets in the group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html
    :cloudformationResource: AWS::Personalize::DatasetGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_personalize as personalize
        
        cfn_dataset_group = personalize.CfnDatasetGroup(self, "MyCfnDatasetGroup",
            name="name",
        
            # the properties below are optional
            domain="domain",
            kms_key_arn="kmsKeyArn",
            role_arn="roleArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the dataset group.
        :param domain: The domain of a Domain dataset group.
        :param kms_key_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key used to encrypt the datasets.
        :param role_arn: The ARN of the AWS Identity and Access Management (IAM) role that has permissions to access the AWS Key Management Service (KMS) key. Supplying an IAM role is only valid when also specifying a KMS key.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca6485605ba6ab1dd805c944eddbfe77e62953abd16f2d5983bbfb3aa72d0285)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatasetGroupProps(
            name=name, domain=domain, kms_key_arn=kms_key_arn, role_arn=role_arn
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53e4c19bb006c2768929356ecd14cfe304a8014a04d11f94be61d3d7527fd927)
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
            type_hints = typing.get_type_hints(_typecheckingstub__715d2c0638aa998bd8905e903ac3daddc69f97e4dc87de13912612d90dd4b49c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDatasetGroupArn")
    def attr_dataset_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the dataset group.

        :cloudformationAttribute: DatasetGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatasetGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the dataset group.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56caa4338c47e6943a1c02910a656652ca6d93232611938e41763e2a0bc31ac2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> typing.Optional[builtins.str]:
        '''The domain of a Domain dataset group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb5624d0d309971f069b8bfdb5a86b8b0ca0848a9e223a6aaf05bd1fabaee32f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key used to encrypt the datasets.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89e3e6b46a117bd75a2a13063e2789e29dcad2fec7bbde978197af2d45bb130f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the AWS Identity and Access Management (IAM) role that has permissions to access the AWS Key Management Service (KMS) key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__659a9057a0256ba90eedec4d65dd5e9b7f237704a3d6394737385f6717edb9f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_personalize.CfnDatasetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "domain": "domain",
        "kms_key_arn": "kmsKeyArn",
        "role_arn": "roleArn",
    },
)
class CfnDatasetGroupProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDatasetGroup``.

        :param name: The name of the dataset group.
        :param domain: The domain of a Domain dataset group.
        :param kms_key_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key used to encrypt the datasets.
        :param role_arn: The ARN of the AWS Identity and Access Management (IAM) role that has permissions to access the AWS Key Management Service (KMS) key. Supplying an IAM role is only valid when also specifying a KMS key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_personalize as personalize
            
            cfn_dataset_group_props = personalize.CfnDatasetGroupProps(
                name="name",
            
                # the properties below are optional
                domain="domain",
                kms_key_arn="kmsKeyArn",
                role_arn="roleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fdb6f95ecf2ddb96752e4bd6a7d092a5e469f7a7350a52b8a17e2840cb0ff7b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if domain is not None:
            self._values["domain"] = domain
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the dataset group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''The domain of a Domain dataset group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-domain
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key used to encrypt the datasets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the AWS Identity and Access Management (IAM) role that has permissions to access the AWS Key Management Service (KMS) key.

        Supplying an IAM role is only valid when also specifying a KMS key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html#cfn-personalize-datasetgroup-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatasetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_personalize.CfnDatasetProps",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_group_arn": "datasetGroupArn",
        "dataset_type": "datasetType",
        "name": "name",
        "schema_arn": "schemaArn",
        "dataset_import_job": "datasetImportJob",
    },
)
class CfnDatasetProps:
    def __init__(
        self,
        *,
        dataset_group_arn: builtins.str,
        dataset_type: builtins.str,
        name: builtins.str,
        schema_arn: builtins.str,
        dataset_import_job: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.DatasetImportJobProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataset``.

        :param dataset_group_arn: The Amazon Resource Name (ARN) of the dataset group.
        :param dataset_type: One of the following values:. - Interactions - Items - Users .. epigraph:: You can't use CloudFormation to create an Action Interactions or Actions dataset.
        :param name: The name of the dataset.
        :param schema_arn: The ARN of the associated schema.
        :param dataset_import_job: Describes a job that imports training data from a data source (Amazon S3 bucket) to an Amazon Personalize dataset. If you specify a dataset import job as part of a dataset, all dataset import job fields are required.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_personalize as personalize
            
            # data_source: Any
            
            cfn_dataset_props = personalize.CfnDatasetProps(
                dataset_group_arn="datasetGroupArn",
                dataset_type="datasetType",
                name="name",
                schema_arn="schemaArn",
            
                # the properties below are optional
                dataset_import_job=personalize.CfnDataset.DatasetImportJobProperty(
                    dataset_arn="datasetArn",
                    dataset_import_job_arn="datasetImportJobArn",
                    data_source=data_source,
                    job_name="jobName",
                    role_arn="roleArn"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7542a55fdef9680f9b0e715bef803a25c64a52b098e530b53b6964f1521e383)
            check_type(argname="argument dataset_group_arn", value=dataset_group_arn, expected_type=type_hints["dataset_group_arn"])
            check_type(argname="argument dataset_type", value=dataset_type, expected_type=type_hints["dataset_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema_arn", value=schema_arn, expected_type=type_hints["schema_arn"])
            check_type(argname="argument dataset_import_job", value=dataset_import_job, expected_type=type_hints["dataset_import_job"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_group_arn": dataset_group_arn,
            "dataset_type": dataset_type,
            "name": name,
            "schema_arn": schema_arn,
        }
        if dataset_import_job is not None:
            self._values["dataset_import_job"] = dataset_import_job

    @builtins.property
    def dataset_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the dataset group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-datasetgrouparn
        '''
        result = self._values.get("dataset_group_arn")
        assert result is not None, "Required property 'dataset_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_type(self) -> builtins.str:
        '''One of the following values:.

        - Interactions
        - Items
        - Users

        .. epigraph::

           You can't use CloudFormation to create an Action Interactions or Actions dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-datasettype
        '''
        result = self._values.get("dataset_type")
        assert result is not None, "Required property 'dataset_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema_arn(self) -> builtins.str:
        '''The ARN of the associated schema.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-schemaarn
        '''
        result = self._values.get("schema_arn")
        assert result is not None, "Required property 'schema_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_import_job(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataset.DatasetImportJobProperty]]:
        '''Describes a job that imports training data from a data source (Amazon S3 bucket) to an Amazon Personalize dataset.

        If you specify a dataset import job as part of a dataset, all dataset import job fields are required.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html#cfn-personalize-dataset-datasetimportjob
        '''
        result = self._values.get("dataset_import_job")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataset.DatasetImportJobProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatasetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSchema(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_personalize.CfnSchema",
):
    '''Creates an Amazon Personalize schema from the specified schema string.

    The schema you create must be in Avro JSON format.

    Amazon Personalize recognizes three schema variants. Each schema is associated with a dataset type and has a set of required field and keywords. If you are creating a schema for a dataset in a Domain dataset group, you provide the domain of the Domain dataset group. You specify a schema when you call `CreateDataset <https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDataset.html>`_ .

    For more information on schemas, see `Datasets and schemas <https://docs.aws.amazon.com/personalize/latest/dg/how-it-works-dataset-schema.html>`_ .

    **Related APIs** - `ListSchemas <https://docs.aws.amazon.com/personalize/latest/dg/API_ListSchemas.html>`_

    - `DescribeSchema <https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSchema.html>`_
    - `DeleteSchema <https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteSchema.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html
    :cloudformationResource: AWS::Personalize::Schema
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_personalize as personalize
        
        cfn_schema = personalize.CfnSchema(self, "MyCfnSchema",
            name="name",
            schema="schema",
        
            # the properties below are optional
            domain="domain"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        schema: builtins.str,
        domain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the schema.
        :param schema: The schema.
        :param domain: The domain of a schema that you created for a dataset in a Domain dataset group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3e6ed202aec99faa9e93f3070998170cf57a57c87cb52aa42c8c64b4f4b03d3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSchemaProps(name=name, schema=schema, domain=domain)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54a74a8f66268c6c8277034ca68e794b56a9921e785dfb1020072d7639c5b791)
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
            type_hints = typing.get_type_hints(_typecheckingstub__528eb1953ae0921ec54fd18f52ccf18bdd12d6c8c00f8f2f2d9076a53ecfa30e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrSchemaArn")
    def attr_schema_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the schema.

        :cloudformationAttribute: SchemaArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSchemaArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the schema.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d9c0b7475806153ead9a8c83a37e5b2ac603ee63a5f403a958b6e3ba9fb6250)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        '''The schema.'''
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40ebe60cce6584e9de09b70c4a40099a56d4dfb618d3261f5454c033a461b36a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> typing.Optional[builtins.str]:
        '''The domain of a schema that you created for a dataset in a Domain dataset group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd4dc7d475cc6aef4202a8b9c451fd060bb3acc449768ed082a56731ceaec724)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_personalize.CfnSchemaProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "schema": "schema", "domain": "domain"},
)
class CfnSchemaProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        schema: builtins.str,
        domain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSchema``.

        :param name: The name of the schema.
        :param schema: The schema.
        :param domain: The domain of a schema that you created for a dataset in a Domain dataset group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_personalize as personalize
            
            cfn_schema_props = personalize.CfnSchemaProps(
                name="name",
                schema="schema",
            
                # the properties below are optional
                domain="domain"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c373947e46fb78bb07b658e8d58f6d2395c21ab9e13566c02ecc431ceeabab95)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "schema": schema,
        }
        if domain is not None:
            self._values["domain"] = domain

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the schema.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html#cfn-personalize-schema-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> builtins.str:
        '''The schema.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html#cfn-personalize-schema-schema
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''The domain of a schema that you created for a dataset in a Domain dataset group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html#cfn-personalize-schema-domain
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSchemaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSolution(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_personalize.CfnSolution",
):
    '''.. epigraph::

   After you create a solution, you can’t change its configuration.

    By default, all new solutions use automatic training. With automatic training, you incur training costs while your solution is active. You can't stop automatic training for a solution. To avoid unnecessary costs, make sure to delete the solution when you are finished. For information about training costs, see `Amazon Personalize pricing <https://docs.aws.amazon.com/https://aws.amazon.com/personalize/pricing/>`_ .

    An object that provides information about a solution. A solution includes the custom recipe, customized parameters, and trained models (Solution Versions) that Amazon Personalize uses to generate recommendations.

    After you create a solution, you can’t change its configuration. If you need to make changes, you can `clone the solution <https://docs.aws.amazon.com/personalize/latest/dg/cloning-solution.html>`_ with the Amazon Personalize console or create a new one.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html
    :cloudformationResource: AWS::Personalize::Solution
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_personalize as personalize
        
        # auto_ml_config: Any
        # hpo_config: Any
        
        cfn_solution = personalize.CfnSolution(self, "MyCfnSolution",
            dataset_group_arn="datasetGroupArn",
            name="name",
        
            # the properties below are optional
            event_type="eventType",
            perform_auto_ml=False,
            perform_hpo=False,
            recipe_arn="recipeArn",
            solution_config=personalize.CfnSolution.SolutionConfigProperty(
                algorithm_hyper_parameters={
                    "algorithm_hyper_parameters_key": "algorithmHyperParameters"
                },
                auto_ml_config=auto_ml_config,
                event_value_threshold="eventValueThreshold",
                feature_transformation_parameters={
                    "feature_transformation_parameters_key": "featureTransformationParameters"
                },
                hpo_config=hpo_config
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        dataset_group_arn: builtins.str,
        name: builtins.str,
        event_type: typing.Optional[builtins.str] = None,
        perform_auto_ml: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        perform_hpo: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        recipe_arn: typing.Optional[builtins.str] = None,
        solution_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSolution.SolutionConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param dataset_group_arn: The Amazon Resource Name (ARN) of the dataset group that provides the training data.
        :param name: The name of the solution.
        :param event_type: The event type (for example, 'click' or 'like') that is used for training the model. If no ``eventType`` is provided, Amazon Personalize uses all interactions for training with equal weight regardless of type.
        :param perform_auto_ml: .. epigraph:: We don't recommend enabling automated machine learning. Instead, match your use case to the available Amazon Personalize recipes. For more information, see `Determining your use case. <https://docs.aws.amazon.com/personalize/latest/dg/determining-use-case.html>`_ When true, Amazon Personalize performs a search for the best USER_PERSONALIZATION recipe from the list specified in the solution configuration ( ``recipeArn`` must not be specified). When false (the default), Amazon Personalize uses ``recipeArn`` for training.
        :param perform_hpo: Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is ``false`` .
        :param recipe_arn: The ARN of the recipe used to create the solution. This is required when ``performAutoML`` is false.
        :param solution_config: Describes the configuration properties for the solution.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d1a4b804c91e293dd01c8eb3bb351f1bf260d574f5446a5af1fd4af67486158)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSolutionProps(
            dataset_group_arn=dataset_group_arn,
            name=name,
            event_type=event_type,
            perform_auto_ml=perform_auto_ml,
            perform_hpo=perform_hpo,
            recipe_arn=recipe_arn,
            solution_config=solution_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d44a743b0ace7fb666eb713a9beab48e9acfc9be8b3d7a56bae6cd7c5faf226)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f354150e3f053177a5c6b552dcf2265c7a01c866acd39c2566cdf312401e0bb8)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrSolutionArn")
    def attr_solution_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the solution.

        :cloudformationAttribute: SolutionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSolutionArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="datasetGroupArn")
    def dataset_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the dataset group that provides the training data.'''
        return typing.cast(builtins.str, jsii.get(self, "datasetGroupArn"))

    @dataset_group_arn.setter
    def dataset_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b78584a18c785386a033bdfce75e78af21265a76d5875e76386307283c5c2b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the solution.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2e53700461a0ab0e9361adae30023d1631f4c64e36d5b399fa6fd98a6fce024)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> typing.Optional[builtins.str]:
        '''The event type (for example, 'click' or 'like') that is used for training the model.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventType"))

    @event_type.setter
    def event_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9ae5589137c09511c50e2c78e78c9b87725daa5bcb39ab66a02ee6e3b779340)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventType", value)

    @builtins.property
    @jsii.member(jsii_name="performAutoMl")
    def perform_auto_ml(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''.. epigraph::

   We don't recommend enabling automated machine learning.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "performAutoMl"))

    @perform_auto_ml.setter
    def perform_auto_ml(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7718a36d374a6f4c0570601284b1537a39320cca5ec21282175c284739ff0baa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "performAutoMl", value)

    @builtins.property
    @jsii.member(jsii_name="performHpo")
    def perform_hpo(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to perform hyperparameter optimization (HPO) on the chosen recipe.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "performHpo"))

    @perform_hpo.setter
    def perform_hpo(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a842fa66bea7e72d79a5717b13f90eded16557305c4bfd04d9cb6dbbcbaaf256)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "performHpo", value)

    @builtins.property
    @jsii.member(jsii_name="recipeArn")
    def recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the recipe used to create the solution.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recipeArn"))

    @recipe_arn.setter
    def recipe_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dba5a30057f6e37bc39f31122891ddde19d3dbf87647f24617faa220ab0d1e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recipeArn", value)

    @builtins.property
    @jsii.member(jsii_name="solutionConfig")
    def solution_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSolution.SolutionConfigProperty"]]:
        '''Describes the configuration properties for the solution.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSolution.SolutionConfigProperty"]], jsii.get(self, "solutionConfig"))

    @solution_config.setter
    def solution_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSolution.SolutionConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e94786b77ef81c42aefe1283c359b1bdf642a0315a4f2aac948ab2421fb6de5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "solutionConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_personalize.CfnSolution.AlgorithmHyperParameterRangesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "categorical_hyper_parameter_ranges": "categoricalHyperParameterRanges",
            "continuous_hyper_parameter_ranges": "continuousHyperParameterRanges",
            "integer_hyper_parameter_ranges": "integerHyperParameterRanges",
        },
    )
    class AlgorithmHyperParameterRangesProperty:
        def __init__(
            self,
            *,
            categorical_hyper_parameter_ranges: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSolution.CategoricalHyperParameterRangeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            continuous_hyper_parameter_ranges: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSolution.ContinuousHyperParameterRangeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            integer_hyper_parameter_ranges: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSolution.IntegerHyperParameterRangeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Specifies the hyperparameters and their ranges.

            Hyperparameters can be categorical, continuous, or integer-valued.

            :param categorical_hyper_parameter_ranges: Provides the name and range of a categorical hyperparameter.
            :param continuous_hyper_parameter_ranges: Provides the name and range of a continuous hyperparameter.
            :param integer_hyper_parameter_ranges: Provides the name and range of an integer-valued hyperparameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-algorithmhyperparameterranges.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_personalize as personalize
                
                algorithm_hyper_parameter_ranges_property = personalize.CfnSolution.AlgorithmHyperParameterRangesProperty(
                    categorical_hyper_parameter_ranges=[personalize.CfnSolution.CategoricalHyperParameterRangeProperty(
                        name="name",
                        values=["values"]
                    )],
                    continuous_hyper_parameter_ranges=[personalize.CfnSolution.ContinuousHyperParameterRangeProperty(
                        max_value=123,
                        min_value=123,
                        name="name"
                    )],
                    integer_hyper_parameter_ranges=[personalize.CfnSolution.IntegerHyperParameterRangeProperty(
                        max_value=123,
                        min_value=123,
                        name="name"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__15aa81799eb7fe8f49da8dbe0c566b7e7bfa41a9a4975d794011295adc618136)
                check_type(argname="argument categorical_hyper_parameter_ranges", value=categorical_hyper_parameter_ranges, expected_type=type_hints["categorical_hyper_parameter_ranges"])
                check_type(argname="argument continuous_hyper_parameter_ranges", value=continuous_hyper_parameter_ranges, expected_type=type_hints["continuous_hyper_parameter_ranges"])
                check_type(argname="argument integer_hyper_parameter_ranges", value=integer_hyper_parameter_ranges, expected_type=type_hints["integer_hyper_parameter_ranges"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if categorical_hyper_parameter_ranges is not None:
                self._values["categorical_hyper_parameter_ranges"] = categorical_hyper_parameter_ranges
            if continuous_hyper_parameter_ranges is not None:
                self._values["continuous_hyper_parameter_ranges"] = continuous_hyper_parameter_ranges
            if integer_hyper_parameter_ranges is not None:
                self._values["integer_hyper_parameter_ranges"] = integer_hyper_parameter_ranges

        @builtins.property
        def categorical_hyper_parameter_ranges(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSolution.CategoricalHyperParameterRangeProperty"]]]]:
            '''Provides the name and range of a categorical hyperparameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-algorithmhyperparameterranges.html#cfn-personalize-solution-algorithmhyperparameterranges-categoricalhyperparameterranges
            '''
            result = self._values.get("categorical_hyper_parameter_ranges")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSolution.CategoricalHyperParameterRangeProperty"]]]], result)

        @builtins.property
        def continuous_hyper_parameter_ranges(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSolution.ContinuousHyperParameterRangeProperty"]]]]:
            '''Provides the name and range of a continuous hyperparameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-algorithmhyperparameterranges.html#cfn-personalize-solution-algorithmhyperparameterranges-continuoushyperparameterranges
            '''
            result = self._values.get("continuous_hyper_parameter_ranges")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSolution.ContinuousHyperParameterRangeProperty"]]]], result)

        @builtins.property
        def integer_hyper_parameter_ranges(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSolution.IntegerHyperParameterRangeProperty"]]]]:
            '''Provides the name and range of an integer-valued hyperparameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-algorithmhyperparameterranges.html#cfn-personalize-solution-algorithmhyperparameterranges-integerhyperparameterranges
            '''
            result = self._values.get("integer_hyper_parameter_ranges")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSolution.IntegerHyperParameterRangeProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlgorithmHyperParameterRangesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_personalize.CfnSolution.AutoMLConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"metric_name": "metricName", "recipe_list": "recipeList"},
    )
    class AutoMLConfigProperty:
        def __init__(
            self,
            *,
            metric_name: typing.Optional[builtins.str] = None,
            recipe_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''When the solution performs AutoML ( ``performAutoML`` is true in `CreateSolution <https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html>`_ ), Amazon Personalize determines which recipe, from the specified list, optimizes the given metric. Amazon Personalize then uses that recipe for the solution.

            :param metric_name: The metric to optimize.
            :param recipe_list: The list of candidate recipes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-automlconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_personalize as personalize
                
                auto_mLConfig_property = personalize.CfnSolution.AutoMLConfigProperty(
                    metric_name="metricName",
                    recipe_list=["recipeList"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c033e664b3885950e91b55570f2c19628ad8a543fac916ca84ea51125c1f1b74)
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument recipe_list", value=recipe_list, expected_type=type_hints["recipe_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if metric_name is not None:
                self._values["metric_name"] = metric_name
            if recipe_list is not None:
                self._values["recipe_list"] = recipe_list

        @builtins.property
        def metric_name(self) -> typing.Optional[builtins.str]:
            '''The metric to optimize.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-automlconfig.html#cfn-personalize-solution-automlconfig-metricname
            '''
            result = self._values.get("metric_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def recipe_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of candidate recipes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-automlconfig.html#cfn-personalize-solution-automlconfig-recipelist
            '''
            result = self._values.get("recipe_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoMLConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_personalize.CfnSolution.CategoricalHyperParameterRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class CategoricalHyperParameterRangeProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Provides the name and range of a categorical hyperparameter.

            :param name: The name of the hyperparameter.
            :param values: A list of the categories for the hyperparameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-categoricalhyperparameterrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_personalize as personalize
                
                categorical_hyper_parameter_range_property = personalize.CfnSolution.CategoricalHyperParameterRangeProperty(
                    name="name",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__93afbb50f74193e82bb9acf1ca20840f492539113221ba5a7cba5b1f7714eaf5)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the hyperparameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-categoricalhyperparameterrange.html#cfn-personalize-solution-categoricalhyperparameterrange-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of the categories for the hyperparameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-categoricalhyperparameterrange.html#cfn-personalize-solution-categoricalhyperparameterrange-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CategoricalHyperParameterRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_personalize.CfnSolution.ContinuousHyperParameterRangeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_value": "maxValue",
            "min_value": "minValue",
            "name": "name",
        },
    )
    class ContinuousHyperParameterRangeProperty:
        def __init__(
            self,
            *,
            max_value: typing.Optional[jsii.Number] = None,
            min_value: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides the name and range of a continuous hyperparameter.

            :param max_value: The maximum allowable value for the hyperparameter.
            :param min_value: The minimum allowable value for the hyperparameter.
            :param name: The name of the hyperparameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-continuoushyperparameterrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_personalize as personalize
                
                continuous_hyper_parameter_range_property = personalize.CfnSolution.ContinuousHyperParameterRangeProperty(
                    max_value=123,
                    min_value=123,
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6a30e88e7bd5d172a754260a999f068d3b0f1b48eee8a8d29b69aa45738ba378)
                check_type(argname="argument max_value", value=max_value, expected_type=type_hints["max_value"])
                check_type(argname="argument min_value", value=min_value, expected_type=type_hints["min_value"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_value is not None:
                self._values["max_value"] = max_value
            if min_value is not None:
                self._values["min_value"] = min_value
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def max_value(self) -> typing.Optional[jsii.Number]:
            '''The maximum allowable value for the hyperparameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-continuoushyperparameterrange.html#cfn-personalize-solution-continuoushyperparameterrange-maxvalue
            '''
            result = self._values.get("max_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_value(self) -> typing.Optional[jsii.Number]:
            '''The minimum allowable value for the hyperparameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-continuoushyperparameterrange.html#cfn-personalize-solution-continuoushyperparameterrange-minvalue
            '''
            result = self._values.get("min_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the hyperparameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-continuoushyperparameterrange.html#cfn-personalize-solution-continuoushyperparameterrange-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContinuousHyperParameterRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_personalize.CfnSolution.HpoConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "algorithm_hyper_parameter_ranges": "algorithmHyperParameterRanges",
            "hpo_objective": "hpoObjective",
            "hpo_resource_config": "hpoResourceConfig",
        },
    )
    class HpoConfigProperty:
        def __init__(
            self,
            *,
            algorithm_hyper_parameter_ranges: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSolution.AlgorithmHyperParameterRangesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            hpo_objective: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSolution.HpoObjectiveProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            hpo_resource_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSolution.HpoResourceConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes the properties for hyperparameter optimization (HPO).

            :param algorithm_hyper_parameter_ranges: The hyperparameters and their allowable ranges.
            :param hpo_objective: The metric to optimize during HPO. .. epigraph:: Amazon Personalize doesn't support configuring the ``hpoObjective`` at this time.
            :param hpo_resource_config: Describes the resource configuration for HPO.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_personalize as personalize
                
                hpo_config_property = personalize.CfnSolution.HpoConfigProperty(
                    algorithm_hyper_parameter_ranges=personalize.CfnSolution.AlgorithmHyperParameterRangesProperty(
                        categorical_hyper_parameter_ranges=[personalize.CfnSolution.CategoricalHyperParameterRangeProperty(
                            name="name",
                            values=["values"]
                        )],
                        continuous_hyper_parameter_ranges=[personalize.CfnSolution.ContinuousHyperParameterRangeProperty(
                            max_value=123,
                            min_value=123,
                            name="name"
                        )],
                        integer_hyper_parameter_ranges=[personalize.CfnSolution.IntegerHyperParameterRangeProperty(
                            max_value=123,
                            min_value=123,
                            name="name"
                        )]
                    ),
                    hpo_objective=personalize.CfnSolution.HpoObjectiveProperty(
                        metric_name="metricName",
                        metric_regex="metricRegex",
                        type="type"
                    ),
                    hpo_resource_config=personalize.CfnSolution.HpoResourceConfigProperty(
                        max_number_of_training_jobs="maxNumberOfTrainingJobs",
                        max_parallel_training_jobs="maxParallelTrainingJobs"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d546b87038e3787fe0d49823b75ac103ad949fb7fa3ca1047cc21fd739dfd3ab)
                check_type(argname="argument algorithm_hyper_parameter_ranges", value=algorithm_hyper_parameter_ranges, expected_type=type_hints["algorithm_hyper_parameter_ranges"])
                check_type(argname="argument hpo_objective", value=hpo_objective, expected_type=type_hints["hpo_objective"])
                check_type(argname="argument hpo_resource_config", value=hpo_resource_config, expected_type=type_hints["hpo_resource_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if algorithm_hyper_parameter_ranges is not None:
                self._values["algorithm_hyper_parameter_ranges"] = algorithm_hyper_parameter_ranges
            if hpo_objective is not None:
                self._values["hpo_objective"] = hpo_objective
            if hpo_resource_config is not None:
                self._values["hpo_resource_config"] = hpo_resource_config

        @builtins.property
        def algorithm_hyper_parameter_ranges(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSolution.AlgorithmHyperParameterRangesProperty"]]:
            '''The hyperparameters and their allowable ranges.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoconfig.html#cfn-personalize-solution-hpoconfig-algorithmhyperparameterranges
            '''
            result = self._values.get("algorithm_hyper_parameter_ranges")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSolution.AlgorithmHyperParameterRangesProperty"]], result)

        @builtins.property
        def hpo_objective(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSolution.HpoObjectiveProperty"]]:
            '''The metric to optimize during HPO.

            .. epigraph::

               Amazon Personalize doesn't support configuring the ``hpoObjective`` at this time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoconfig.html#cfn-personalize-solution-hpoconfig-hpoobjective
            '''
            result = self._values.get("hpo_objective")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSolution.HpoObjectiveProperty"]], result)

        @builtins.property
        def hpo_resource_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSolution.HpoResourceConfigProperty"]]:
            '''Describes the resource configuration for HPO.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoconfig.html#cfn-personalize-solution-hpoconfig-hporesourceconfig
            '''
            result = self._values.get("hpo_resource_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSolution.HpoResourceConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HpoConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_personalize.CfnSolution.HpoObjectiveProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "metric_regex": "metricRegex",
            "type": "type",
        },
    )
    class HpoObjectiveProperty:
        def __init__(
            self,
            *,
            metric_name: typing.Optional[builtins.str] = None,
            metric_regex: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The metric to optimize during hyperparameter optimization (HPO).

            .. epigraph::

               Amazon Personalize doesn't support configuring the ``hpoObjective`` at this time.

            :param metric_name: The name of the metric.
            :param metric_regex: A regular expression for finding the metric in the training job logs.
            :param type: The type of the metric. Valid values are ``Maximize`` and ``Minimize`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoobjective.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_personalize as personalize
                
                hpo_objective_property = personalize.CfnSolution.HpoObjectiveProperty(
                    metric_name="metricName",
                    metric_regex="metricRegex",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f61ae92876cdb3cdd9faf92392beb44b141ee83ce186cc3582f456289fa8be3f)
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument metric_regex", value=metric_regex, expected_type=type_hints["metric_regex"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if metric_name is not None:
                self._values["metric_name"] = metric_name
            if metric_regex is not None:
                self._values["metric_regex"] = metric_regex
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def metric_name(self) -> typing.Optional[builtins.str]:
            '''The name of the metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoobjective.html#cfn-personalize-solution-hpoobjective-metricname
            '''
            result = self._values.get("metric_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metric_regex(self) -> typing.Optional[builtins.str]:
            '''A regular expression for finding the metric in the training job logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoobjective.html#cfn-personalize-solution-hpoobjective-metricregex
            '''
            result = self._values.get("metric_regex")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of the metric.

            Valid values are ``Maximize`` and ``Minimize`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hpoobjective.html#cfn-personalize-solution-hpoobjective-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HpoObjectiveProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_personalize.CfnSolution.HpoResourceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_number_of_training_jobs": "maxNumberOfTrainingJobs",
            "max_parallel_training_jobs": "maxParallelTrainingJobs",
        },
    )
    class HpoResourceConfigProperty:
        def __init__(
            self,
            *,
            max_number_of_training_jobs: typing.Optional[builtins.str] = None,
            max_parallel_training_jobs: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the resource configuration for hyperparameter optimization (HPO).

            :param max_number_of_training_jobs: The maximum number of training jobs when you create a solution version. The maximum value for ``maxNumberOfTrainingJobs`` is ``40`` .
            :param max_parallel_training_jobs: The maximum number of parallel training jobs when you create a solution version. The maximum value for ``maxParallelTrainingJobs`` is ``10`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hporesourceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_personalize as personalize
                
                hpo_resource_config_property = personalize.CfnSolution.HpoResourceConfigProperty(
                    max_number_of_training_jobs="maxNumberOfTrainingJobs",
                    max_parallel_training_jobs="maxParallelTrainingJobs"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb5ea2ab036b9e69c00912a8b1f69134e89b7a87e8642af3aca2af0714247bdf)
                check_type(argname="argument max_number_of_training_jobs", value=max_number_of_training_jobs, expected_type=type_hints["max_number_of_training_jobs"])
                check_type(argname="argument max_parallel_training_jobs", value=max_parallel_training_jobs, expected_type=type_hints["max_parallel_training_jobs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_number_of_training_jobs is not None:
                self._values["max_number_of_training_jobs"] = max_number_of_training_jobs
            if max_parallel_training_jobs is not None:
                self._values["max_parallel_training_jobs"] = max_parallel_training_jobs

        @builtins.property
        def max_number_of_training_jobs(self) -> typing.Optional[builtins.str]:
            '''The maximum number of training jobs when you create a solution version.

            The maximum value for ``maxNumberOfTrainingJobs`` is ``40`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hporesourceconfig.html#cfn-personalize-solution-hporesourceconfig-maxnumberoftrainingjobs
            '''
            result = self._values.get("max_number_of_training_jobs")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_parallel_training_jobs(self) -> typing.Optional[builtins.str]:
            '''The maximum number of parallel training jobs when you create a solution version.

            The maximum value for ``maxParallelTrainingJobs`` is ``10`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-hporesourceconfig.html#cfn-personalize-solution-hporesourceconfig-maxparalleltrainingjobs
            '''
            result = self._values.get("max_parallel_training_jobs")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HpoResourceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_personalize.CfnSolution.IntegerHyperParameterRangeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_value": "maxValue",
            "min_value": "minValue",
            "name": "name",
        },
    )
    class IntegerHyperParameterRangeProperty:
        def __init__(
            self,
            *,
            max_value: typing.Optional[jsii.Number] = None,
            min_value: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides the name and range of an integer-valued hyperparameter.

            :param max_value: The maximum allowable value for the hyperparameter.
            :param min_value: The minimum allowable value for the hyperparameter.
            :param name: The name of the hyperparameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-integerhyperparameterrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_personalize as personalize
                
                integer_hyper_parameter_range_property = personalize.CfnSolution.IntegerHyperParameterRangeProperty(
                    max_value=123,
                    min_value=123,
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ab41d3c62be2abf54857b89fc5f04495187be9a0397f3c839f5dcbcbf5a236b5)
                check_type(argname="argument max_value", value=max_value, expected_type=type_hints["max_value"])
                check_type(argname="argument min_value", value=min_value, expected_type=type_hints["min_value"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_value is not None:
                self._values["max_value"] = max_value
            if min_value is not None:
                self._values["min_value"] = min_value
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def max_value(self) -> typing.Optional[jsii.Number]:
            '''The maximum allowable value for the hyperparameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-integerhyperparameterrange.html#cfn-personalize-solution-integerhyperparameterrange-maxvalue
            '''
            result = self._values.get("max_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_value(self) -> typing.Optional[jsii.Number]:
            '''The minimum allowable value for the hyperparameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-integerhyperparameterrange.html#cfn-personalize-solution-integerhyperparameterrange-minvalue
            '''
            result = self._values.get("min_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the hyperparameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-integerhyperparameterrange.html#cfn-personalize-solution-integerhyperparameterrange-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntegerHyperParameterRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_personalize.CfnSolution.SolutionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "algorithm_hyper_parameters": "algorithmHyperParameters",
            "auto_ml_config": "autoMlConfig",
            "event_value_threshold": "eventValueThreshold",
            "feature_transformation_parameters": "featureTransformationParameters",
            "hpo_config": "hpoConfig",
        },
    )
    class SolutionConfigProperty:
        def __init__(
            self,
            *,
            algorithm_hyper_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            auto_ml_config: typing.Any = None,
            event_value_threshold: typing.Optional[builtins.str] = None,
            feature_transformation_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            hpo_config: typing.Any = None,
        ) -> None:
            '''Describes the configuration properties for the solution.

            :param algorithm_hyper_parameters: Lists the algorithm hyperparameters and their values.
            :param auto_ml_config: The `AutoMLConfig <https://docs.aws.amazon.com/personalize/latest/dg/API_AutoMLConfig.html>`_ object containing a list of recipes to search when AutoML is performed.
            :param event_value_threshold: Only events with a value greater than or equal to this threshold are used for training a model.
            :param feature_transformation_parameters: Lists the feature transformation parameters.
            :param hpo_config: Describes the properties for hyperparameter optimization (HPO).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_personalize as personalize
                
                # auto_ml_config: Any
                # hpo_config: Any
                
                solution_config_property = personalize.CfnSolution.SolutionConfigProperty(
                    algorithm_hyper_parameters={
                        "algorithm_hyper_parameters_key": "algorithmHyperParameters"
                    },
                    auto_ml_config=auto_ml_config,
                    event_value_threshold="eventValueThreshold",
                    feature_transformation_parameters={
                        "feature_transformation_parameters_key": "featureTransformationParameters"
                    },
                    hpo_config=hpo_config
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ced9838e4439e4bc1ac0405cb84c759dc1da0cf5422f515a7b0d86711bcce840)
                check_type(argname="argument algorithm_hyper_parameters", value=algorithm_hyper_parameters, expected_type=type_hints["algorithm_hyper_parameters"])
                check_type(argname="argument auto_ml_config", value=auto_ml_config, expected_type=type_hints["auto_ml_config"])
                check_type(argname="argument event_value_threshold", value=event_value_threshold, expected_type=type_hints["event_value_threshold"])
                check_type(argname="argument feature_transformation_parameters", value=feature_transformation_parameters, expected_type=type_hints["feature_transformation_parameters"])
                check_type(argname="argument hpo_config", value=hpo_config, expected_type=type_hints["hpo_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if algorithm_hyper_parameters is not None:
                self._values["algorithm_hyper_parameters"] = algorithm_hyper_parameters
            if auto_ml_config is not None:
                self._values["auto_ml_config"] = auto_ml_config
            if event_value_threshold is not None:
                self._values["event_value_threshold"] = event_value_threshold
            if feature_transformation_parameters is not None:
                self._values["feature_transformation_parameters"] = feature_transformation_parameters
            if hpo_config is not None:
                self._values["hpo_config"] = hpo_config

        @builtins.property
        def algorithm_hyper_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Lists the algorithm hyperparameters and their values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html#cfn-personalize-solution-solutionconfig-algorithmhyperparameters
            '''
            result = self._values.get("algorithm_hyper_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def auto_ml_config(self) -> typing.Any:
            '''The `AutoMLConfig <https://docs.aws.amazon.com/personalize/latest/dg/API_AutoMLConfig.html>`_ object containing a list of recipes to search when AutoML is performed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html#cfn-personalize-solution-solutionconfig-automlconfig
            '''
            result = self._values.get("auto_ml_config")
            return typing.cast(typing.Any, result)

        @builtins.property
        def event_value_threshold(self) -> typing.Optional[builtins.str]:
            '''Only events with a value greater than or equal to this threshold are used for training a model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html#cfn-personalize-solution-solutionconfig-eventvaluethreshold
            '''
            result = self._values.get("event_value_threshold")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def feature_transformation_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Lists the feature transformation parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html#cfn-personalize-solution-solutionconfig-featuretransformationparameters
            '''
            result = self._values.get("feature_transformation_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def hpo_config(self) -> typing.Any:
            '''Describes the properties for hyperparameter optimization (HPO).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html#cfn-personalize-solution-solutionconfig-hpoconfig
            '''
            result = self._values.get("hpo_config")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SolutionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_personalize.CfnSolutionProps",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_group_arn": "datasetGroupArn",
        "name": "name",
        "event_type": "eventType",
        "perform_auto_ml": "performAutoMl",
        "perform_hpo": "performHpo",
        "recipe_arn": "recipeArn",
        "solution_config": "solutionConfig",
    },
)
class CfnSolutionProps:
    def __init__(
        self,
        *,
        dataset_group_arn: builtins.str,
        name: builtins.str,
        event_type: typing.Optional[builtins.str] = None,
        perform_auto_ml: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        perform_hpo: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        recipe_arn: typing.Optional[builtins.str] = None,
        solution_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSolution.SolutionConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSolution``.

        :param dataset_group_arn: The Amazon Resource Name (ARN) of the dataset group that provides the training data.
        :param name: The name of the solution.
        :param event_type: The event type (for example, 'click' or 'like') that is used for training the model. If no ``eventType`` is provided, Amazon Personalize uses all interactions for training with equal weight regardless of type.
        :param perform_auto_ml: .. epigraph:: We don't recommend enabling automated machine learning. Instead, match your use case to the available Amazon Personalize recipes. For more information, see `Determining your use case. <https://docs.aws.amazon.com/personalize/latest/dg/determining-use-case.html>`_ When true, Amazon Personalize performs a search for the best USER_PERSONALIZATION recipe from the list specified in the solution configuration ( ``recipeArn`` must not be specified). When false (the default), Amazon Personalize uses ``recipeArn`` for training.
        :param perform_hpo: Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is ``false`` .
        :param recipe_arn: The ARN of the recipe used to create the solution. This is required when ``performAutoML`` is false.
        :param solution_config: Describes the configuration properties for the solution.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_personalize as personalize
            
            # auto_ml_config: Any
            # hpo_config: Any
            
            cfn_solution_props = personalize.CfnSolutionProps(
                dataset_group_arn="datasetGroupArn",
                name="name",
            
                # the properties below are optional
                event_type="eventType",
                perform_auto_ml=False,
                perform_hpo=False,
                recipe_arn="recipeArn",
                solution_config=personalize.CfnSolution.SolutionConfigProperty(
                    algorithm_hyper_parameters={
                        "algorithm_hyper_parameters_key": "algorithmHyperParameters"
                    },
                    auto_ml_config=auto_ml_config,
                    event_value_threshold="eventValueThreshold",
                    feature_transformation_parameters={
                        "feature_transformation_parameters_key": "featureTransformationParameters"
                    },
                    hpo_config=hpo_config
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69d40d42ad451a741444334b0be64eab69d658504abd7f1a87ae1558ac9c0e2e)
            check_type(argname="argument dataset_group_arn", value=dataset_group_arn, expected_type=type_hints["dataset_group_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
            check_type(argname="argument perform_auto_ml", value=perform_auto_ml, expected_type=type_hints["perform_auto_ml"])
            check_type(argname="argument perform_hpo", value=perform_hpo, expected_type=type_hints["perform_hpo"])
            check_type(argname="argument recipe_arn", value=recipe_arn, expected_type=type_hints["recipe_arn"])
            check_type(argname="argument solution_config", value=solution_config, expected_type=type_hints["solution_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_group_arn": dataset_group_arn,
            "name": name,
        }
        if event_type is not None:
            self._values["event_type"] = event_type
        if perform_auto_ml is not None:
            self._values["perform_auto_ml"] = perform_auto_ml
        if perform_hpo is not None:
            self._values["perform_hpo"] = perform_hpo
        if recipe_arn is not None:
            self._values["recipe_arn"] = recipe_arn
        if solution_config is not None:
            self._values["solution_config"] = solution_config

    @builtins.property
    def dataset_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the dataset group that provides the training data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-datasetgrouparn
        '''
        result = self._values.get("dataset_group_arn")
        assert result is not None, "Required property 'dataset_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the solution.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_type(self) -> typing.Optional[builtins.str]:
        '''The event type (for example, 'click' or 'like') that is used for training the model.

        If no ``eventType`` is provided, Amazon Personalize uses all interactions for training with equal weight regardless of type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-eventtype
        '''
        result = self._values.get("event_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def perform_auto_ml(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''.. epigraph::

   We don't recommend enabling automated machine learning.

        Instead, match your use case to the available Amazon Personalize recipes. For more information, see `Determining your use case. <https://docs.aws.amazon.com/personalize/latest/dg/determining-use-case.html>`_

        When true, Amazon Personalize performs a search for the best USER_PERSONALIZATION recipe from the list specified in the solution configuration ( ``recipeArn`` must not be specified). When false (the default), Amazon Personalize uses ``recipeArn`` for training.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-performautoml
        '''
        result = self._values.get("perform_auto_ml")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def perform_hpo(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to perform hyperparameter optimization (HPO) on the chosen recipe.

        The default is ``false`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-performhpo
        '''
        result = self._values.get("perform_hpo")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the recipe used to create the solution.

        This is required when ``performAutoML`` is false.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-recipearn
        '''
        result = self._values.get("recipe_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def solution_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSolution.SolutionConfigProperty]]:
        '''Describes the configuration properties for the solution.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html#cfn-personalize-solution-solutionconfig
        '''
        result = self._values.get("solution_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSolution.SolutionConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSolutionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataset",
    "CfnDatasetGroup",
    "CfnDatasetGroupProps",
    "CfnDatasetProps",
    "CfnSchema",
    "CfnSchemaProps",
    "CfnSolution",
    "CfnSolutionProps",
]

publication.publish()

def _typecheckingstub__8515dadec60af65aa740f35c8bee6bc85dafa7634c6b2270232bfa824452ebce(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    dataset_group_arn: builtins.str,
    dataset_type: builtins.str,
    name: builtins.str,
    schema_arn: builtins.str,
    dataset_import_job: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.DatasetImportJobProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccbc61bfda7b82706a4bcf79fd5c92ea9ecab41d2ce92088c0f4792b980823a1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f187d3b2924b81109808f7eaa45f19c8884e1e1dea57aa4de729b9205cf518d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92b16c3f5a79428072afbfa189b761a25212440d1c418c8aeb6b18a8e98c91ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92562664ab00f1e9056f6606e2970466af3ea0874ff465dde6f00b6ff0a5e8af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf263591c9e23855d850751cd45cff2e048c43deb7e160e3bada974d92469338(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__113b0bea00700cff01f2c19ac9225d2dc8fbdd0c5ddf4b14941a4f9cf60fb979(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afd06f21a72ea38837a666025b223a4003de38fe4bd9ff9796a64ce7a35f855d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataset.DatasetImportJobProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83ea3d6dacd8545ca3b15725588aca74892b310d047ede8d4d6e0e1671a9a0f1(
    *,
    data_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f52207436b51d5c04d39a2c4edfacf59c3bb268757202e992b324a790558d823(
    *,
    dataset_arn: typing.Optional[builtins.str] = None,
    dataset_import_job_arn: typing.Optional[builtins.str] = None,
    data_source: typing.Any = None,
    job_name: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca6485605ba6ab1dd805c944eddbfe77e62953abd16f2d5983bbfb3aa72d0285(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    domain: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53e4c19bb006c2768929356ecd14cfe304a8014a04d11f94be61d3d7527fd927(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__715d2c0638aa998bd8905e903ac3daddc69f97e4dc87de13912612d90dd4b49c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56caa4338c47e6943a1c02910a656652ca6d93232611938e41763e2a0bc31ac2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb5624d0d309971f069b8bfdb5a86b8b0ca0848a9e223a6aaf05bd1fabaee32f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89e3e6b46a117bd75a2a13063e2789e29dcad2fec7bbde978197af2d45bb130f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__659a9057a0256ba90eedec4d65dd5e9b7f237704a3d6394737385f6717edb9f5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fdb6f95ecf2ddb96752e4bd6a7d092a5e469f7a7350a52b8a17e2840cb0ff7b(
    *,
    name: builtins.str,
    domain: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7542a55fdef9680f9b0e715bef803a25c64a52b098e530b53b6964f1521e383(
    *,
    dataset_group_arn: builtins.str,
    dataset_type: builtins.str,
    name: builtins.str,
    schema_arn: builtins.str,
    dataset_import_job: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.DatasetImportJobProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3e6ed202aec99faa9e93f3070998170cf57a57c87cb52aa42c8c64b4f4b03d3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    schema: builtins.str,
    domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54a74a8f66268c6c8277034ca68e794b56a9921e785dfb1020072d7639c5b791(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__528eb1953ae0921ec54fd18f52ccf18bdd12d6c8c00f8f2f2d9076a53ecfa30e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d9c0b7475806153ead9a8c83a37e5b2ac603ee63a5f403a958b6e3ba9fb6250(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40ebe60cce6584e9de09b70c4a40099a56d4dfb618d3261f5454c033a461b36a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd4dc7d475cc6aef4202a8b9c451fd060bb3acc449768ed082a56731ceaec724(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c373947e46fb78bb07b658e8d58f6d2395c21ab9e13566c02ecc431ceeabab95(
    *,
    name: builtins.str,
    schema: builtins.str,
    domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d1a4b804c91e293dd01c8eb3bb351f1bf260d574f5446a5af1fd4af67486158(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    dataset_group_arn: builtins.str,
    name: builtins.str,
    event_type: typing.Optional[builtins.str] = None,
    perform_auto_ml: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    perform_hpo: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    recipe_arn: typing.Optional[builtins.str] = None,
    solution_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSolution.SolutionConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d44a743b0ace7fb666eb713a9beab48e9acfc9be8b3d7a56bae6cd7c5faf226(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f354150e3f053177a5c6b552dcf2265c7a01c866acd39c2566cdf312401e0bb8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b78584a18c785386a033bdfce75e78af21265a76d5875e76386307283c5c2b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2e53700461a0ab0e9361adae30023d1631f4c64e36d5b399fa6fd98a6fce024(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9ae5589137c09511c50e2c78e78c9b87725daa5bcb39ab66a02ee6e3b779340(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7718a36d374a6f4c0570601284b1537a39320cca5ec21282175c284739ff0baa(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a842fa66bea7e72d79a5717b13f90eded16557305c4bfd04d9cb6dbbcbaaf256(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dba5a30057f6e37bc39f31122891ddde19d3dbf87647f24617faa220ab0d1e7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e94786b77ef81c42aefe1283c359b1bdf642a0315a4f2aac948ab2421fb6de5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSolution.SolutionConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15aa81799eb7fe8f49da8dbe0c566b7e7bfa41a9a4975d794011295adc618136(
    *,
    categorical_hyper_parameter_ranges: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSolution.CategoricalHyperParameterRangeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    continuous_hyper_parameter_ranges: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSolution.ContinuousHyperParameterRangeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    integer_hyper_parameter_ranges: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSolution.IntegerHyperParameterRangeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c033e664b3885950e91b55570f2c19628ad8a543fac916ca84ea51125c1f1b74(
    *,
    metric_name: typing.Optional[builtins.str] = None,
    recipe_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93afbb50f74193e82bb9acf1ca20840f492539113221ba5a7cba5b1f7714eaf5(
    *,
    name: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a30e88e7bd5d172a754260a999f068d3b0f1b48eee8a8d29b69aa45738ba378(
    *,
    max_value: typing.Optional[jsii.Number] = None,
    min_value: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d546b87038e3787fe0d49823b75ac103ad949fb7fa3ca1047cc21fd739dfd3ab(
    *,
    algorithm_hyper_parameter_ranges: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSolution.AlgorithmHyperParameterRangesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hpo_objective: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSolution.HpoObjectiveProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hpo_resource_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSolution.HpoResourceConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f61ae92876cdb3cdd9faf92392beb44b141ee83ce186cc3582f456289fa8be3f(
    *,
    metric_name: typing.Optional[builtins.str] = None,
    metric_regex: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb5ea2ab036b9e69c00912a8b1f69134e89b7a87e8642af3aca2af0714247bdf(
    *,
    max_number_of_training_jobs: typing.Optional[builtins.str] = None,
    max_parallel_training_jobs: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab41d3c62be2abf54857b89fc5f04495187be9a0397f3c839f5dcbcbf5a236b5(
    *,
    max_value: typing.Optional[jsii.Number] = None,
    min_value: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ced9838e4439e4bc1ac0405cb84c759dc1da0cf5422f515a7b0d86711bcce840(
    *,
    algorithm_hyper_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    auto_ml_config: typing.Any = None,
    event_value_threshold: typing.Optional[builtins.str] = None,
    feature_transformation_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    hpo_config: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69d40d42ad451a741444334b0be64eab69d658504abd7f1a87ae1558ac9c0e2e(
    *,
    dataset_group_arn: builtins.str,
    name: builtins.str,
    event_type: typing.Optional[builtins.str] = None,
    perform_auto_ml: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    perform_hpo: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    recipe_arn: typing.Optional[builtins.str] = None,
    solution_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSolution.SolutionConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
