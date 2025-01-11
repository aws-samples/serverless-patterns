package com.amazonaws.services.lambda.samples.events.das;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.zip.GZIPInputStream;
import javax.crypto.spec.SecretKeySpec;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.encryptionsdk.AwsCrypto;
import com.amazonaws.encryptionsdk.CommitmentPolicy;
import com.amazonaws.encryptionsdk.CryptoInputStream;
import com.amazonaws.encryptionsdk.jce.JceMasterKey;
import com.amazonaws.services.cloudwatch.model.ResourceNotFoundException;
import com.amazonaws.services.kms.AWSKMS;
import com.amazonaws.services.kms.AWSKMSClientBuilder;
import com.amazonaws.services.kms.model.DecryptRequest;
import com.amazonaws.services.kms.model.DecryptResult;
import com.amazonaws.util.Base64;
import com.amazonaws.util.IOUtils;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import com.amazonaws.services.secretsmanager.AWSSecretsManager;
import com.amazonaws.services.secretsmanager.AWSSecretsManagerClientBuilder;
import com.amazonaws.services.secretsmanager.model.DecryptionFailureException;
import com.amazonaws.services.secretsmanager.model.GetSecretValueRequest;
import com.amazonaws.services.secretsmanager.model.GetSecretValueResult;
import com.amazonaws.services.secretsmanager.model.InternalServiceErrorException;
import com.amazonaws.services.secretsmanager.model.InvalidParameterException;
import com.amazonaws.services.secretsmanager.model.InvalidRequestException;
import com.amazonaws.services.lambda.samples.events.das.models.aurorastreams.PostgresActivity;
import com.amazonaws.services.lambda.samples.events.das.models.aurorastreams.PostgresActivityRecords;;

/**
 * Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"). You may not
 * use this file except in compliance with the License. A copy of the License is
 * located at
 *
 * http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed on
 * an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 * 
 * This class provides a public method processPostgresActivity that takes the
 * content of an Aurora Database Activity Stream for Aurora Postgres Database.
 * In the future, similar methods will be provided for other databases that
 * support Database Activity Streams. This method needs two variables
 * aws-access-key-id and aws-secret-access-key to be stored in the Secrets
 * Manager in the same account as the Database Activity Stream. These need to be
 * the access key and the secret access key of the AWS user that created the
 * Aurora DAS. These are read from the Secrets Manager. Private methods are then
 * used to Base64 decode, decrypt and decompress the DAS message being streamed
 * onto the Kinesis Activity Stream.
 */
public class AuroraStreamsProcessor {

	final String AWS_ACCESS_KEY = "aws-access-key-id";
	final String AWS_SECRET_KEY = "aws-secret-access-key";
	final String POSTGRES = "postgres";
	final String MYSQL = "mysql";
	final String INVALID_DATABASE_TYPE = "Invalid Database Type";
	String awsAccessKey;
	String awsSecretKey;
	String awsRegion;
	BasicAWSCredentials credentials;
	AWSStaticCredentialsProvider credentialsProvider;
	AwsCrypto crypto;
	AWSKMS kms;
	Gson gson;

	/**
	 * @param awsRegion - The AWS region in which the Database Activity Stream is
	 *                  created
	 */
	public AuroraStreamsProcessor(String awsRegion) {
		super();
		if (null == awsRegion) {
			awsRegion = "us-east-1";
		}
		try {
			this.awsAccessKey = this.getSecret(AWS_ACCESS_KEY, awsRegion);
			this.awsSecretKey = this.getSecret(AWS_SECRET_KEY, awsRegion);
			this.awsRegion = awsRegion;
			this.credentials = new BasicAWSCredentials(awsAccessKey, awsSecretKey);
			this.credentialsProvider = new AWSStaticCredentialsProvider(credentials);
			this.crypto = AwsCrypto.builder().withCommitmentPolicy(CommitmentPolicy.RequireEncryptAllowDecrypt).build();
			this.kms = AWSKMSClientBuilder.standard().withRegion(awsRegion).withCredentials(credentialsProvider)
					.build();
			this.gson = new GsonBuilder().serializeNulls().create();
		} catch (Exception e) {
			throw e;
		}
	}

	/**
	 * @return the awsRegion
	 */
	public String getAwsRegion() {
		return awsRegion;
	}

	/**
	 * @param awsRegion the awsRegion to set
	 */
	public void setAwsRegion(String awsRegion) {
		this.awsRegion = awsRegion;
	}

	/**
	 * @param bytes         - The encrypted byte array that contains the Aurora DAS
	 *                      message
	 * @param dbcResourceId - This is the portion of the name of the DAS Kinesis
	 *                      Stream starting with "cluster-". This is needed to match
	 *                      the context of the decryption algorithm with the
	 *                      encrypted message
	 * @param logger        - A reference to the lambda logger to log error messages
	 *                      if any (or for debugging)
	 * @return - An object of class PostgresActivityRecords that replicates the
	 *         structure of a DAS message containing details of a specific database
	 *         activity such as a table creation, row insertion, query etc.
	 */
	public PostgresActivityRecords processPostgresActivity(final ByteBuffer bytes, String dbcResourceId,
			LambdaLogger logger) {
		PostgresActivityRecords processedDatabaseActivity = null;
		try {
			final PostgresActivity activity = gson.fromJson(new String(bytes.array(), StandardCharsets.UTF_8),
					PostgresActivity.class);

			// Base64.Decode
			final byte[] decoded = Base64.decode(activity.getDatabaseActivityEvents());
			final byte[] decodedDataKey = Base64.decode(activity.getKey());

			Map<String, String> context = new HashMap<>();
			context.put("aws:rds:dbc-id", dbcResourceId);

			// Decrypt
			final DecryptRequest decryptRequest = new DecryptRequest()
					.withCiphertextBlob(ByteBuffer.wrap(decodedDataKey)).withEncryptionContext(context);
			final DecryptResult decryptResult = kms.decrypt(decryptRequest);
			final byte[] decrypted = decrypt(decoded, getByteArray(decryptResult.getPlaintext()));

			// GZip Decompress
			final byte[] decompressed = decompress(decrypted);

			// JSON $ActivityRecords
			String processedJson = new String(decompressed, StandardCharsets.UTF_8);
			processedDatabaseActivity = gson.fromJson(processedJson, PostgresActivityRecords.class);

		} catch (Exception e) {
			logger.log(e.getMessage());

		}
		return processedDatabaseActivity;
	}

	/**
	 * @param src - Compressed byte array that needs to be decompressed
	 * @return - Decompressed byte array
	 * @throws IOException
	 */
	private byte[] decompress(final byte[] src) throws IOException {
		ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream(src);
		GZIPInputStream gzipInputStream = new GZIPInputStream(byteArrayInputStream);
		return IOUtils.toByteArray(gzipInputStream);
	}

	/**
	 * @param decoded        - The encrypted byte array containing the Aurora DAS
	 *                       message
	 * @param decodedDataKey - The encrypted key used to encrypt the Aurora DAS
	 *                       message
	 * @return - The decrypted byte array
	 * @throws IOException
	 */
	private byte[] decrypt(final byte[] decoded, final byte[] decodedDataKey) throws IOException {
		// Create a JCE master key provider using the random key and an AES-GCM
		// encryption algorithm
		final JceMasterKey masterKey = JceMasterKey.getInstance(new SecretKeySpec(decodedDataKey, "AES"), "BC",
				"DataKey", "AES/GCM/NoPadding");
		try (final CryptoInputStream<JceMasterKey> decryptingStream = crypto.createDecryptingStream(masterKey,
				new ByteArrayInputStream(decoded)); final ByteArrayOutputStream out = new ByteArrayOutputStream()) {
			IOUtils.copy(decryptingStream, out);
			return out.toByteArray();
		}
	}

	private static byte[] getByteArray(final ByteBuffer b) {
		byte[] byteArray = new byte[b.remaining()];
		b.get(byteArray);
		return byteArray;
	}

	/**
	 * @param secretName - The key of the secret to retrieve from the AWS Parameter
	 *                   Store
	 * @param region     - The AWS region
	 * @return - The value of the secret
	 */
	private String getSecret(String secretName, String region) {

		String secretValue = "";

		// Create a Secrets Manager client
		AWSSecretsManager client = AWSSecretsManagerClientBuilder.standard().withRegion(region).build();

		// In this sample we only handle the specific exceptions for the
		// 'GetSecretValue' API.
		// See
		// https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
		// We rethrow the exception by default.

		//String secret, decodedBinarySecret;
		GetSecretValueRequest getSecretValueRequest = new GetSecretValueRequest().withSecretId(secretName);
		GetSecretValueResult getSecretValueResult = null;

		try {
			getSecretValueResult = client.getSecretValue(getSecretValueRequest);
		} catch (DecryptionFailureException e) {
			// Secrets Manager can't decrypt the protected secret text using the provided
			// KMS key.
			// Deal with the exception here, and/or rethrow at your discretion.
			throw e;
		} catch (InternalServiceErrorException e) {
			// An error occurred on the server side.
			// Deal with the exception here, and/or rethrow at your discretion.
			throw e;
		} catch (InvalidParameterException e) {
			// You provided an invalid value for a parameter.
			// Deal with the exception here, and/or rethrow at your discretion.
			throw e;
		} catch (InvalidRequestException e) {
			// You provided a parameter value that is not valid for the current state of the
			// resource.
			// Deal with the exception here, and/or rethrow at your discretion.
			throw e;
		} catch (ResourceNotFoundException e) {
			// We can't find the resource that you asked for.
			// Deal with the exception here, and/or rethrow at your discretion.
			throw e;
		}

		// Decrypts secret using the associated KMS CMK.
		// Depending on whether the secret is a string or binary, one of these fields
		// will be populated.
		String secretValueFromSecretsManager = "";
		if (getSecretValueResult.getSecretString() != null) {
			secretValueFromSecretsManager = getSecretValueResult.getSecretString();
		} else {
			secretValueFromSecretsManager = new String(Base64.decode(getSecretValueResult.getSecretBinary().array()));
		}
		secretValue = secretValueFromSecretsManager.substring(secretValueFromSecretsManager.indexOf(":") + 2,
				secretValueFromSecretsManager.length() - 2);
		return secretValue;

	}
}
