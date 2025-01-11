package com.amazonaws.services.lambda.samples.events.das;

import java.util.UUID;

import software.amazon.awssdk.awscore.exception.AwsServiceException;
import software.amazon.awssdk.core.exception.SdkClientException;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.regions.providers.DefaultAwsRegionProviderChain;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;

public class AuroraStreamsS3Inserter {
	String s3Bucket;
	String s3Prefix;
	S3Client s3Client;
	
	/**
	 * @param s3Bucket
	 * @param s3Prefix
	 */
	public AuroraStreamsS3Inserter(String s3Bucket, String s3Prefix) {
		super();
		this.s3Bucket = s3Bucket;
		this.s3Prefix = s3Prefix;
		DefaultAwsRegionProviderChain defaultAwsRegionProviderChain = new DefaultAwsRegionProviderChain();
		Region region = defaultAwsRegionProviderChain.getRegion();
		s3Client = S3Client.builder().region(region).build();
	}
	/**
	 * @return the s3Bucket
	 */
	public String getS3Bucket() {
		return s3Bucket;
	}
	/**
	 * @param s3Bucket the s3Bucket to set
	 */
	public void setS3Bucket(String s3Bucket) {
		this.s3Bucket = s3Bucket;
	}
	/**
	 * @return the s3Prefix
	 */
	public String getS3Prefix() {
		return s3Prefix;
	}
	/**
	 * @param s3Prefix the s3Prefix to set
	 */
	public void setS3Prefix(String s3Prefix) {
		this.s3Prefix = s3Prefix;
	}
	/**
	 * @return the s3Client
	 */
	public S3Client getS3Client() {
		return s3Client;
	}
	/**
	 * @param s3Client the s3Client to set
	 */
	public void setS3Client(S3Client s3Client) {
		this.s3Client = s3Client;
	}
	
	public void insertIntoS3(String objectData) throws AwsServiceException, SdkClientException {
		try {
			String objectKey = UUID.randomUUID().toString();
			String s3ObjectKey = "";
			if ("".equals(s3Prefix)) {
				s3ObjectKey = objectKey;
			} else if (s3Prefix.endsWith("/")) {
				s3ObjectKey = s3Prefix + objectKey;
			} else {
				s3ObjectKey = s3Prefix + "/" + objectKey;
			}
			
			PutObjectRequest objectRequest = PutObjectRequest.builder()
					                                         .bucket(s3Bucket)
					                                         .key(s3ObjectKey)
					                                         .build();
			s3Client.putObject(objectRequest, RequestBody.fromString(objectData));
		} catch (AwsServiceException | SdkClientException e) {
			throw e;
		}
		
	}
}
