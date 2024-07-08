package com.myorg;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.aws_apigatewayv2_integrations.HttpStepFunctionsIntegration;
import software.amazon.awscdk.services.apigatewayv2.AddRoutesOptions;
import software.amazon.awscdk.services.apigatewayv2.HttpApi;
import software.amazon.awscdk.services.apigatewayv2.HttpIntegrationSubtype;
import software.amazon.awscdk.services.apigatewayv2.HttpMethod;
import software.amazon.awscdk.services.apigatewayv2.MappingValue;
import software.amazon.awscdk.services.apigatewayv2.ParameterMapping;
import software.amazon.awscdk.services.logs.LogGroup;
import software.amazon.awscdk.services.stepfunctions.DefinitionBody;
import software.amazon.awscdk.services.stepfunctions.LogLevel;
import software.amazon.awscdk.services.stepfunctions.LogOptions;
import software.amazon.awscdk.services.stepfunctions.Pass;
import software.amazon.awscdk.services.stepfunctions.StateMachine;
import software.amazon.awscdk.services.stepfunctions.StateMachineType;
import software.constructs.Construct;

import java.util.List;
import java.util.Map;

public class HttpApiGatewayStepFunctionsStack extends Stack {
    public HttpApiGatewayStepFunctionsStack(final Construct scope, final String id) {
        this(scope, id, null);
    }

    public HttpApiGatewayStepFunctionsStack(final Construct scope, final String id, final StackProps props) {
        super(scope, id, props);

        Pass startState = Pass.Builder.create(this, "StartState").build();

        DefinitionBody definitionBody = DefinitionBody.fromChainable(startState);

        LogGroup logGroup = LogGroup.Builder.create(this, "HttpExpressWorkflowLogGroup").build();

        StateMachine stepFunction = StateMachine.Builder.create(this, "HttpExpressWorkflow")
                .stateMachineName("HttpExpressWorkflowExample")
                .stateMachineType(StateMachineType.EXPRESS)
                .definitionBody(definitionBody)
                .logs(LogOptions.builder()
                        .destination(logGroup)
                        .level(LogLevel.ALL)
                        .build())
                .tracingEnabled(true)
                .build();

        HttpApi httpApi = HttpApi.Builder.create(this, "HttpApi")
                .createDefaultStage(true)
                .build();

        Map<String, MappingValue> requestParameters = Map.of(
                "Input", MappingValue.custom("$request.body"),
                "StateMachineArn", MappingValue.custom(stepFunction.getStateMachineArn())
        );

        HttpStepFunctionsIntegration integration = HttpStepFunctionsIntegration.Builder.create("StepFunctionIntegration")
                .stateMachine(stepFunction)
                .subtype(HttpIntegrationSubtype.STEPFUNCTIONS_START_SYNC_EXECUTION)
                .parameterMapping(ParameterMapping.fromObject(requestParameters))
                .build();

        httpApi.addRoutes(AddRoutesOptions.builder()
                        .integration(integration)
                        .methods(List.of(HttpMethod.POST))
                        .path("/execute")
                .build());

    }
}
