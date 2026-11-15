from constructs import Construct
import aws_cdk.aws_apigateway as apigateway


class UsagePlanConstruct(Construct):
    def __init__(self, scope: Construct, id: str, apigateway_construct, plan_name, plan_config ,**kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Map the period of the usage plan from the config to apigateway.Period.XXX
        period_enum = self.get_period_enum(plan_config['quota']['period'])

        # Create usage plan dynamically using the context data
        usage_plan = apigateway_construct.api.add_usage_plan(plan_name,
            name=plan_name,
            throttle=apigateway.ThrottleSettings(
                rate_limit=plan_config['throttle']['rate_limit'],
                burst_limit=plan_config['throttle']['burst_limit']
            ),
            quota=apigateway.QuotaSettings(
                limit=plan_config['quota']['limit'],
                period=period_enum
            )
        )

        # Create API key 
        api_key = apigateway.ApiKey(self, f"ApiKey-{plan_name}",
                                    api_key_name=f"ApiKey-{plan_name}")
        self.api_key_id = api_key.key_id
        usage_plan.add_api_key(api_key)

        # If method is configured in the context assign the API key to the relevant API method
        if plan_config['method']:
            def get_method(method_name):
                method_mapping = { # Change the method to fit your API
                    "GET": apigateway_construct.get_method,
                    "POST": apigateway_construct.put_method,
                    "DELETE": apigateway_construct.delete_method
                }
                return method_mapping.get(method_name.upper())
            usage_plan.add_api_stage(
            stage=apigateway_construct.api.deployment_stage,
            throttle=[apigateway.ThrottlingPerMethod(
                method=get_method(plan_config['method']),
                throttle=apigateway.ThrottleSettings(
                    rate_limit=100,
                    burst_limit=1
                ))]
            )

        


    @staticmethod
    def get_period_enum(period: str) -> apigateway.Period:
        period_mapping = {
            "DAY": apigateway.Period.DAY,
            "WEEK": apigateway.Period.WEEK,
            "MONTH": apigateway.Period.MONTH
        }
        return period_mapping.get(period.upper())

        