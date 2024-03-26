require 'rmagick'
require 'aws-sdk-s3'

# We need to set this environment variable to tell ImageMagick where the en- and de-coders are located.
# Without this set RMagick will fail to load any images.
ENV['MAGICK_CODER_MODULE_PATH'] = '/opt/coders'

S3_CLIENT = Aws::S3::Client.new

def lambda_handler(event:, context:)
  logger = configure_logging(context)
  destination_bucket = ENV['DESTINATION_BUCKET']
  maximum_size = (ENV['MAXIMUM_SIZE'] || 480).to_i
  result = resize_image(S3_CLIENT, event, destination_bucket, maximum_size, logger)

  {
    statusCode: 200,
    body: {
      result: result,
    }.to_json
  }
end

def configure_logging(context)
  # We configure the default logger to output JSON log lines.
  # We add the Lambda request ID to each log line so that we can correlate
  log_level = ENV.fetch('LOG_LEVEL',  'DEBUG')
  logger = Logger.new($stdout)
  logger.level = Logger.const_get(log_level.upcase)
  logger.formatter = proc do |severity, time, _progname, msg|
    JSON.dump({
      time: time.strftime('%Y-%m-%dT%H:%M:%S.%6N'),
      level: severity,
      message: msg,
      request_id: context.aws_request_id,
    })
  end
  logger
end

def resize_image(s3, event, destination_bucket, maximum_size, logger)
  s3_object_name = event.dig("Records", 0, "s3")
  s3_source_bucket = s3_object_name.dig("bucket", "name")
  s3_source_key = s3_object_name.dig("object", "key")

  logger.info("Resizing #{s3_source_key}")

  s3_object = s3.get_object(
    {
      bucket: s3_source_bucket,
      key: s3_source_key,
    })

  image = Magick::Image.from_blob(s3_object.body.read).first
  logger.info("Initial size: #{image.columns}x#{image.rows}")
  output_image = image.resize_to_fit(maximum_size, maximum_size)
  output_data = output_image.to_blob
  logger.info("Final size: #{output_image.columns}x#{output_image.rows}")

  result = s3.put_object(
    {
      bucket: destination_bucket,
      key: s3_source_key,
      body: output_data,
    })

  etag = result.etag
  logger.info("S3 Etag: #{etag}")

  {
    status: "ok",
    bucket: destination_bucket,
    key: s3_source_key,
    etag: etag,
  }
end
