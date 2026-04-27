from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import LambdaFunction
from diagrams.aws.storage import ElasticFileSystemEFS, SimpleStorageServiceS3Bucket, S3AccessPoints
from diagrams.aws.network import Endpoint, Privatelink
from diagrams.onprem.client import Client

with Diagram(
    "S3 Files + Lambda Architecture",
    filename="serverless-patterns/s3files-lambda-sam/generated-diagrams/architecture",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr={"fontsize": "14", "bgcolor": "white", "pad": "0.5"}
):
    user = Client("Invoke")

    with Cluster("AWS Cloud"):
        with Cluster("VPC"):
            with Cluster("Private Subnet"):
                lambda_fn = LambdaFunction("S3FilesReaderFunction\n/mnt/s3data")
                mount_target = ElasticFileSystemEFS("S3 Files\nMount Target")

            with Cluster("VPC Endpoints"):
                s3_endpoint = Endpoint("S3 Gateway\nEndpoint")
                s3files_endpoint = Privatelink("S3 Files\nInterface Endpoint")

        with Cluster("S3 Files"):
            from diagrams.aws.storage import ElasticFileSystemEFS as EFS2
            fs = EFS2("S3 File System")
            ap = S3AccessPoints("Access Point\n/lambda")

        s3 = SimpleStorageServiceS3Bucket("S3 Bucket\nlambda/input/")

    user >> lambda_fn
    lambda_fn >> mount_target
    mount_target >> fs
    fs >> ap
    ap >> s3_endpoint
    s3_endpoint >> s3
    lambda_fn >> s3files_endpoint >> fs
