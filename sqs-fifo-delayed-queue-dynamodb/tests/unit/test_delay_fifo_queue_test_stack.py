import aws_cdk as core
import aws_cdk.assertions as assertions

from delay_fifo_queue_test.delay_fifo_queue_test_stack import DelayFifoQueueTestStack

# example tests. To run these tests, uncomment this file along with the example
# resource in delay_fifo_queue_test/delay_fifo_queue_test_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DelayFifoQueueTestStack(app, "delay-fifo-queue-test")
    template = assertions.Template.from_stack(stack)
