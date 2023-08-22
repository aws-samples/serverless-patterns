import pytest
from aws_cdk import App
from app import CdklambdaStack  

@pytest.fixture
def app():
    return App()

def test_stack_construction(app):
    stack = CdklambdaStack(app, "TestStack")
    
    # Perform assertions to verify the resources in the stack
    assert len(stack.input_bucket.node.children) == 1
    assert len(stack.valid_bucket.node.children) == 1
    assert len(stack.invalid_bucket.node.children) == 1
    assert len(stack.node.find_all(lambda_.Function)) == 1
  

    # Deploy the stack to a mock environment and perform additional tests
    with pytest.raises(ValueError):
        stack.valid_bucket.add_lifecycle_rule(expiration=60)  # Example of testing resource behavior
    
    # Clean up by deleting the stack
    stack.node.try_remove()
