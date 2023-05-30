class Event:
    def __init__(self, resource_arn, event_id, event_source, resource_name, is_compliant):
        self.resource_arn = resource_arn
        self.event_id = event_id
        self.event_source = event_source
        self.resource_name = resource_name
        self.is_compliant = is_compliant
        self.service = self.event_source.split(".")[0]
        self.tags = None
        
    
    def validate_compliance(self, required_keys):
        result = self.tags.difference(required_keys)
        if result:
            return result