<?php

use Bref\Context\Context;
use Bref\Event\Http\HttpResponse;
use GuzzleHttp\Client;
use Symfony\Component\HttpFoundation\JsonResponse;

// Responsibilities are simplified into one file for demonstration purposes
// We would have have those methods in a Service class

function getParam(string $parameterPath): string
{
    // Set `withDecryption=true if you also want to retrieve SecureString SSMs
    $url = "http://localhost:2773/systemsmanager/parameters/get?name={$parameterPath}&withDecryption=true";

    try {
        $client = new Client();

        $response = $client->get($url, [
            'headers' => [
                'X-Aws-Parameters-Secrets-Token' => getenv('AWS_SESSION_TOKEN'),
            ]
        ]);

        $data = json_decode($response->getBody());
        return $data->Parameter->Value;
    } catch (\Exception $e) {
        error_log('Error getting parameter => ' . print_r($e, true));
    }
}

function getSecret(string $secretName): stdClass
{
    $url = "http://localhost:2773/secretsmanager/get?secretId={$secretName}";

    try {
        $client = new Client();

        $response = $client->get($url, [
            'headers' => [
                'X-Aws-Parameters-Secrets-Token' => getenv('AWS_SESSION_TOKEN'),
            ]
        ]);

        $data = json_decode($response->getBody());
        return json_decode($data->SecretString);
    } catch (\Exception $e) {
        error_log('Error getting secretsmanager => ' . print_r($e, true));
    }
}

return function ($request, Context $context) {
    $secret = getSecret(getenv('THE_SECRET_NAME'));
    $response = new JsonResponse([
        'status' => 'OK',
        getenv('THE_SSM_PARAM_PATH') => getParam(getenv('THE_SSM_PARAM_PATH')),
        getenv('THE_SECRET_NAME') => [
            'password' => $secret->password,
            'username' => $secret->username,
        ],
    ]);

    return (new HttpResponse($response->getContent(), $response->headers->all()))->toApiGatewayFormatV2();
};
