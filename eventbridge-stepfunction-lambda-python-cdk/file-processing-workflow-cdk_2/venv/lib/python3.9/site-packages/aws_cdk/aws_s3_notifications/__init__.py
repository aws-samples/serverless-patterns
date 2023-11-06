'''
# S3 Bucket Notifications Destinations

This module includes integration classes for using Topics, Queues or Lambdas
as S3 Notification Destinations.

## Examples

The following example shows how to send a notification to an SNS
topic when an object is created in an S3 bucket:

```python
import aws_cdk.aws_sns as sns


bucket = s3.Bucket(self, "Bucket")
topic = sns.Topic(self, "Topic")

bucket.add_event_notification(s3.EventType.OBJECT_CREATED_PUT, s3n.SnsDestination(topic))
```

The following example shows how to send a notification to an SQS queue
when an object is created in an S3 bucket:

```python
import aws_cdk.aws_sqs as sqs


bucket = s3.Bucket(self, "Bucket")
queue = sqs.Queue(self, "Queue")

bucket.add_event_notification(s3.EventType.OBJECT_CREATED_PUT, s3n.SqsDestination(queue))
```

The following example shows how to send a notification to a Lambda function when an object is created in an S3 bucket:

```python
import aws_cdk.aws_lambda as lambda_


bucket = s3.Bucket(self, "Bucket")
fn = lambda_.Function(self, "MyFunction",
    runtime=lambda_.Runtime.NODEJS_14_X,
    handler="index.handler",
    code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler"))
)

bucket.add_event_notification(s3.EventType.OBJECT_CREATED, s3n.LambdaDestination(fn))
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
from ..aws_lambda import IFunction as _IFunction_6adb0ab8
from ..aws_s3 import (
    BucketNotificationDestinationConfig as _BucketNotificationDestinationConfig_a4c4f83d,
    IBucket as _IBucket_42e086fd,
    IBucketNotificationDestination as _IBucketNotificationDestination_ae5ca51a,
)
from ..aws_sns import ITopic as _ITopic_9eca4852
from ..aws_sqs import IQueue as _IQueue_7ed6f679


@jsii.implements(_IBucketNotificationDestination_ae5ca51a)
class LambdaDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3_notifications.LambdaDestination",
):
    '''Use a Lambda function as a bucket notification destination.

    :exampleMetadata: infused

    Example::

        # my_lambda: lambda.Function
        
        bucket = s3.Bucket.from_bucket_attributes(self, "ImportedBucket",
            bucket_arn="arn:aws:s3:::my-bucket"
        )
        
        # now you can just call methods on the bucket
        bucket.add_event_notification(s3.EventType.OBJECT_CREATED, s3n.LambdaDestination(my_lambda),
            prefix="home/myusername/*"
        )
    '''

    def __init__(self, fn: _IFunction_6adb0ab8) -> None:
        '''
        :param fn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa31f009d508c5e9716ef8081ccf63abb6866ffbf349417ea81abf6f60c25acc)
            check_type(argname="argument fn", value=fn, expected_type=type_hints["fn"])
        jsii.create(self.__class__, self, [fn])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        bucket: _IBucket_42e086fd,
    ) -> _BucketNotificationDestinationConfig_a4c4f83d:
        '''Registers this resource to receive notifications for the specified bucket.

        This method will only be called once for each destination/bucket
        pair and the result will be cached, so there is no need to implement
        idempotency in each destination.

        :param _scope: -
        :param bucket: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72fb0e43c5d0bdebbc9b643b327c5cd42f851dbe4c4a6ac53bb2849787b3adec)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        return typing.cast(_BucketNotificationDestinationConfig_a4c4f83d, jsii.invoke(self, "bind", [_scope, bucket]))


@jsii.implements(_IBucketNotificationDestination_ae5ca51a)
class SnsDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3_notifications.SnsDestination",
):
    '''Use an SNS topic as a bucket notification destination.

    :exampleMetadata: infused

    Example::

        bucket = s3.Bucket(self, "MyBucket")
        topic = sns.Topic(self, "MyTopic")
        bucket.add_event_notification(s3.EventType.OBJECT_CREATED, s3n.SnsDestination(topic))
    '''

    def __init__(self, topic: _ITopic_9eca4852) -> None:
        '''
        :param topic: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88bc302a2eb7b4d1c7dc00b1564ab4c536d2626942f2cec60d543582b3f80f43)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        jsii.create(self.__class__, self, [topic])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        bucket: _IBucket_42e086fd,
    ) -> _BucketNotificationDestinationConfig_a4c4f83d:
        '''Registers this resource to receive notifications for the specified bucket.

        This method will only be called once for each destination/bucket
        pair and the result will be cached, so there is no need to implement
        idempotency in each destination.

        :param _scope: -
        :param bucket: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3553ece4b599ce7e526b55722477cb04771e1907840471521f08a9dbdea726a1)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        return typing.cast(_BucketNotificationDestinationConfig_a4c4f83d, jsii.invoke(self, "bind", [_scope, bucket]))


@jsii.implements(_IBucketNotificationDestination_ae5ca51a)
class SqsDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3_notifications.SqsDestination",
):
    '''Use an SQS queue as a bucket notification destination.

    :exampleMetadata: infused

    Example::

        # my_queue: sqs.Queue
        
        bucket = s3.Bucket(self, "MyBucket")
        bucket.add_event_notification(s3.EventType.OBJECT_REMOVED, s3n.SqsDestination(my_queue),
            prefix="foo/",
            suffix=".jpg"
        )
    '''

    def __init__(self, queue: _IQueue_7ed6f679) -> None:
        '''
        :param queue: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b615fa89f2fab6db113bd6376cf27eba6eb754a702e60b29024bc94c89bac4c6)
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
        jsii.create(self.__class__, self, [queue])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        bucket: _IBucket_42e086fd,
    ) -> _BucketNotificationDestinationConfig_a4c4f83d:
        '''Allows using SQS queues as destinations for bucket notifications.

        Use ``bucket.onEvent(event, queue)`` to subscribe.

        :param _scope: -
        :param bucket: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e60900d91c64bba2d0ee8f8b0ace07ff0ee2d07e518d7b03941ed5bb85044f8b)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        return typing.cast(_BucketNotificationDestinationConfig_a4c4f83d, jsii.invoke(self, "bind", [_scope, bucket]))


__all__ = [
    "LambdaDestination",
    "SnsDestination",
    "SqsDestination",
]

publication.publish()

def _typecheckingstub__aa31f009d508c5e9716ef8081ccf63abb6866ffbf349417ea81abf6f60c25acc(
    fn: _IFunction_6adb0ab8,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72fb0e43c5d0bdebbc9b643b327c5cd42f851dbe4c4a6ac53bb2849787b3adec(
    _scope: _constructs_77d1e7e8.Construct,
    bucket: _IBucket_42e086fd,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88bc302a2eb7b4d1c7dc00b1564ab4c536d2626942f2cec60d543582b3f80f43(
    topic: _ITopic_9eca4852,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3553ece4b599ce7e526b55722477cb04771e1907840471521f08a9dbdea726a1(
    _scope: _constructs_77d1e7e8.Construct,
    bucket: _IBucket_42e086fd,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b615fa89f2fab6db113bd6376cf27eba6eb754a702e60b29024bc94c89bac4c6(
    queue: _IQueue_7ed6f679,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e60900d91c64bba2d0ee8f8b0ace07ff0ee2d07e518d7b03941ed5bb85044f8b(
    _scope: _constructs_77d1e7e8.Construct,
    bucket: _IBucket_42e086fd,
) -> None:
    """Type checking stubs"""
    pass
