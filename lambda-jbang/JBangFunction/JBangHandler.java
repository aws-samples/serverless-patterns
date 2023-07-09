//usr/bin/env jbang "$0" "$@" ; exit $?
//JAVA 17
//DEPS com.amazonaws:aws-lambda-java-core:1.2.2
//DEPS com.amazonaws:aws-lambda-java-events:3.11.1
//SOURCES model/Person.java

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyResponseEvent;
import java.util.Map;
import model.Person;

public class JBangHandler implements RequestHandler<Person, APIGatewayProxyResponseEvent> {
    @Override
    public APIGatewayProxyResponseEvent handleRequest(Person person, Context context) {
        context.getLogger().log("Request received: " + person + "\n");

        return new APIGatewayProxyResponseEvent()
                .withStatusCode(200)
                .withHeaders(Map.of("Content-Type", "text/plain"))
                .withBody("Hello " + person.name() + "!");
    }
}
