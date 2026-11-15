import data.etl_data
import toml
import sys
import re
import subprocess
import os


def update_param_overrides(s, key, v):
    pattern = rf'{key}="(.*?)"'
    replacement = f'{key}="{v}"'
    return re.sub(pattern, replacement, s)

# this might not be needed
def update_template(s, key, v):
    pattern = rf'{key}: "(.*?)"'
    replacement = f'{key}: "{v}"'
    return re.sub(pattern, replacement, s)

if __name__ == """__main__""":
    if(len(sys.argv) < 2):
        print("Please pass in transformation name")
        exit()

    transform_config = data.etl_data.getTransformationByName(sys.argv[1])
    job_name = transform_config.getTransformationName().split("_")[0].capitalize() + transform_config.getSourceTableArn().split("/")[1]

    with open('samconfig.toml', 'r') as file:
        config = toml.load(file)
    param_overrides = config['default']['deploy']['parameters']["parameter_overrides"]

    param_overrides = update_param_overrides(param_overrides, "TransformTaskName", transform_config.getTransformationName())
    param_overrides = update_param_overrides(param_overrides, "S3BucketName", transform_config.getS3BucketName())
    param_overrides = update_param_overrides(param_overrides, "SourceTableARN", transform_config.getSourceTableArn())
    param_overrides = update_param_overrides(param_overrides, "JobName", job_name)


    config['default']['deploy']['parameters']['parameter_overrides'] = param_overrides

    stack_name = transform_config.getSourceTableArn().split("/")[1] + "Stack"
    config['default']['deploy']['parameters']['stack_name'] = stack_name
    config['default']['deploy']['parameters']['s3_prefix'] = stack_name

    print(config)

    with open('samconfig.toml', 'w') as file:
            toml.dump(config, file)

    script_location = "glue_jobs/" + transform_config.getTransformationName() + ".py"

    with open("template.yml", 'r') as file:
        content = file.read()

    updated_content = update_template(content, "ScriptLocation", script_location)

    with open("template.yml", 'w') as file:
        file.write(updated_content)

    curr_dir = os.getcwd()
    os.chdir("./scripts")
    subprocess.run(["./batch-orchestration-script.sh"])
    subprocess.run(["./run-job.sh", job_name])

    os.chdir(curr_dir)