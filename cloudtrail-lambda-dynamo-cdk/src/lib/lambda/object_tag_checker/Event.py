class Event:
    def __init__(self, object_arn, bucket_name, is_compliant, object_key):
        self.object_arn = object_arn
        self.bucket_name = bucket_name
        self.is_compliant = is_compliant
        self.object_key = object_key
        self.tags = None

    def validate_compliance(self, required_keys):
        result = self.tags.difference(required_keys)
        if result:
            return result
