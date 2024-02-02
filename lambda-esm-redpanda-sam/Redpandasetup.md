## Setting up and Deploying Redpanda in an EKS Cluster

In this guide, we will go through the steps in order to deploy Redpanda in AWS using an EKS cluster.  Ensure that you have set up the prerequisites found here:

[Lambda Integration with Redpanda](README.md)

## Prerequisites

This guide also has the following prerequisites for setting up and deploying Redpanda in EKS.

* Eksctl
* jq
* Kubectl
* Helm

## Eksctl

Eksctl is needed for CLI deployment of EKS clusters. Install the latest eksctl for your platform from here:

https://eksctl.io/installation/

**** 

## jq

We will make use of jq to parse JSON output and to store the results in environment variables. If you are using Cloud9, jq will already be installed.  If you do not have jq installed, you can find the latest version of jq and installation instructions here:

https://jqlang.github.io/jq/download/

**** 

## Kubectl

Kubectl is a command line tool that is used to communicate with the Kubernetes API server. Install the latest kubectl for your platform from here:

https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html
 **** 

## Helm

Helm is used as the Kubernetes package manager for deploying Redpanda. Install the latest version of Helm for your platform from here:

https://helm.sh/docs/intro/install/
 **** 

## Setting up the Cluster

The Redpanda deployment documentation was used extensively in the creation of this guide.  You can view the Redpanda guide at the following location:

https://docs.redpanda.com/current/deploy/deployment-option/self-hosted/kubernetes/eks-guide/

In setting up and configuring our Redpanda cluster in AWS, we are using an Amazon EKS cluster as described in the guide linked above.
 
For the purposes of this guide, we are using a three node cluster (the minimum recommended by Redpanda) with c5d.large instances (the minimum sized instances that include the recommended NVMe class storage). Note that Redpanda recommends c5d.2xlarge instances for production. See the Redpanda requirements and recommendations here:

https://docs.redpanda.com/current/deploy/deployment-option/self-hosted/kubernetes/kubernetes-cluster-requirements/

Use the following command line to create the cluster, replacing <cluster-name> with the name you would like to use:

```
eksctl create cluster \
--name <cluster-name> \
--nodegroup-name nvme-workers \
--node-type c5d.large \
--nodes 3 \
--external-dns-access
```

This command will take some time to complete as the CloudFormation stacks are built and deployed. When it is successful, you should see a message indicating that the new cluster is ready.

You can verify your kubeconfig file is pointing to your EKS cluster with the following command:

```
kubectl get service
```

You should see the output includes a ClusterIP service with the name “kubernetes”.
 
## Set up and Install the CSI Driver

In the next step, we use helm to install the LVM CSI driver with the following commands:

```
helm repo add metal-stack [https://helm.metal-stack.io](https://helm.metal-stack.io/)
helm repo update
helm install csi-driver-lvm metal-stack/csi-driver-lvm \
  --namespace csi-driver-lvm \
  --create-namespace \
  --set lvm.devicePattern='/dev/nvme[1-9]n[0-9]'
```

We will need to create a local yaml file to create and apply the Storage class.  Create a local file called “csi-driver-lvm-striped-xfs.yaml” and save the following contents in the file:

```
apiVersion: [storage.k8s.io/v1](http://storage.k8s.io/v1)
kind: StorageClass
metadata:
  name: csi-driver-lvm-striped-xfs
provisioner: [lvm.csi.metal-stack.io](http://lvm.csi.metal-stack.io/)
reclaimPolicy: Retain
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
parameters:
  type: "striped"
  [csi.storage.k8s.io/fstype](http://csi.storage.k8s.io/fstype): xfs
```

Once the yaml template is created and saved, run the following command line to apply it to your cluster:

```
kubectl apply -f csi-driver-lvm-striped-xfs.yaml
```

You should see the following output:

```
[storageclass.storage.k8s.io/csi-driver-lvm-striped-xfs](http://storageclass.storage.k8s.io/csi-driver-lvm-striped-xfs) created
```

## Configuring Security Groups

Now we will configure our security groups.  First, get the ID of the security group associated to the nodes in your EKS cluster using the following command:

```
AWS_SECURITY_GROUP_ID=``aws eks describe-cluster --name <cluster-name> | jq -r '.cluster.resourcesVpcConfig.clusterSecurityGroupId'``
```

You can verify the value of this with the following command line:

```
echo $AWS_SECURITY_GROUP_ID
```

You should see output like the following (your security group ID will be different):

```
sg-07782247abd908c3b
```

Next, modify the security groups to allow external traffic to reach the node ports.  Note that in this example we are exposing the ports to all inbound IP addresses with the CIDR range of “192.168.0.0/16”, which is the CIDR range assigned to our EKS VPC. Use the following command to modify your security groups to allow the external traffic (which will come from Lambda) to reach the node ports exposed on the Kubernetes worker nodes in the cluster:

```
aws ec2 authorize-security-group-ingress \
  --group-id ${AWS_SECURITY_GROUP_ID} \
  --ip-permissions '[
  {
    "IpProtocol": "tcp",
    "FromPort": 30081,
    "ToPort": 30081,
    "IpRanges": [{"CidrIp": "192.168.0.0/16"}]
  },
  {
    "IpProtocol": "tcp",
    "FromPort": 30082,
    "ToPort": 30082,
    "IpRanges": [{"CidrIp": "192.168.0.0/16"}]
  },
  {
    "IpProtocol": "tcp",
    "FromPort": 31644,
    "ToPort": 31644,
    "IpRanges": [{"CidrIp": "192.168.0.0/16"}]
  },
  {
    "IpProtocol": "tcp",
    "FromPort": 31092,
    "ToPort": 31092,
    "IpRanges": [{"CidrIp": "192.168.0.0/16"}]
  }
  ]'
```

You should see output that includes “Return": true", along with the modified security group rules after executing the command.
 
## Deploy cert-manager

cert-manager adds certificates and certificate issuers as resource types in Kubernetes clusters, and simplifies the process of obtaining, renewing and using those certificates. It will be used to generate the self signed certificates in our Redpanda deployment. You can read more about cert-manager here:

https://cert-manager.io/docs/

The following commands will install cert-manager using Helm:

```
helm repo add jetstack [https://charts.jetstack.io](https://charts.jetstack.io/)
helm repo update
helm install cert-manager jetstack/cert-manager \
  --set installCRDs=true \
  --namespace cert-manager \
  --create-namespace
```

Verify in the output that cert-manager is successfully deployed.

## Deploy Redpanda

The following steps will be used to deploy Redpanda and the Redpanda Console. It will be deployed with SASL SCRAM 256 authentication enabled and use a self-signed certificate for TLS.

There are multiple changes you will need to make to these commands before using them:

1. Change the “export DOMAIN” line to your preferred domain, as it will be used to advertise to external clients and will be the domain included in the self-signed certificates that will be generated.  Save this domain name in a separate text file (along with your security group ID from earlier) for later when SAM is used to deploy the remaining architecture.
2. Change the “secretpassword” password to a secure password as it is the superuser that will be able to fully administer your Redpanda deployment.
3. Choose the namespace to use for your Redpanda deployment.

Once you have made the desired changes to the following commands, execute them on the command line:

```
helm repo add redpanda [https://charts.redpanda.com](https://charts.redpanda.com/)
export DOMAIN=customredpandadomain.local && \
helm install redpanda redpanda/redpanda \
  --namespace <namespace> --create-namespace \
  --set auth.sasl.enabled=true \
  --set "auth.sasl.users[0].name=superuser" \
  --set "auth.sasl.users[0].password=<secretpassword>" \
  --set external.domain=${DOMAIN} \
  --set "storage.persistentVolume.storageClass=csi-driver-lvm-striped-xfs" \
  --wait \
  --timeout 1h
```

After a few minutes, you should see output that includes the message “Congratulations on installing redpanda!”, along with information on your cluster as well as a number of sample commands that you can use.
 
## Creating a User

Now that we have set up and deployed the Redpanda cluster, we will need to create a user.  To create the user, determine a username and password you would like to use, and use the following command to create the user:

```
kubectl --namespace <namespace> exec -ti redpanda-0 -c redpanda -- \
rpk acl user create <username> \
-p <password>
```

You should see the following output confirming successful creation of the user:

```
Created user "<username>".
```

Save the user name and password in a separate text file for later when SAM is used to deploy the remaining architecture.

## Creating a Topic

Next, we will use the superuser to grant the newly created user permission to execute all operations for a topic called twitch-chat. Feel free to use the topic name of your choice:

```
kubectl exec --namespace <namespace> -c redpanda redpanda-0 -- \
  rpk acl create --allow-principal User:<username> \
  --operation all \
  --topic twitch-chat \
  -X user=superuser -X pass=secretpassword -X sasl.mechanism=SCRAM-SHA-512
```

You should then see output similar to the following:

```
PRINCIPAL                     HOST  RESOURCE-TYPE  RESOURCE-NAME  RESOURCE-PATTERN-TYPE  OPERATION  PERMISSION  ERROR
User:redpanda-twitch-account  *     TOPIC          twitch-chat    LITERAL                ALL        ALLOW
```

In the following steps, we are going to use the newly created user account to create the topic, produce messages to the topic, and consumer messages to the topic.
 
First, we will create an alias to simplify the usage of the rpk commands that will be used to work with the Redpanda deployment.  Use the following command to configure the alias:

```
alias internal-rpk="kubectl --namespace <namespace> exec -i -t redpanda-0 -c redpanda -- rpk -X user=redpanda-twitch-account -X pass=changethispassword -X sasl.mechanism=SCRAM-SHA-256"
```

Next, create the topic “twitch-chat” with the following command:

```
internal-rpk topic create twitch-chat
```

You should see the following output after executing the above command:

```
TOPIC        STATUS
twitch-chat  OK
```

View the details of the topic just created by executing the following command:

```
internal-rpk topic describe twitch-chat
```

## Produce and Consume Messages

Now use the following command to interactively produce messages to the topic:

```
internal-rpk topic produce twitch-chat
```

Type in some text and press enter to publish the message.  After publishing several messages, use ctrl+C to end the publishing command.
 
The output should look something like the following:

```
hello world
Produced to partition 0 at offset 0 with timestamp 1702851801374.
hello world 2
Produced to partition 0 at offset 1 with timestamp 1702851806788.
hello world 3
Produced to partition 0 at offset 2 with timestamp 1702851810335.
hello world 4
Produced to partition 0 at offset 3 with timestamp 1702851813904.
^Ccommand terminated with exit code 130
```

Next, use the following command to consume one message from the topic:

```
internal-rpk topic consume twitch-chat --num 1
```

The output should look similar to the following:

```
{
  "topic": "twitch-chat",
  "value": "hello world",
  "timestamp": 1702851801374,
  "partition": 0,
  "offset": 0
}
```
## Accessing the Redpanda Console

Having verified that you can produce and consume messages, next we will access the Redpanda Console by port forwarding to our localhost.  This can be done using the following command:

```
kubectl --namespace <namespace> port-forward svc/redpanda-console 8080:8080
```

**Note:** If you are using Cloud9, you will need to use the following alternate command to do the port forwarding:

```
kubectl --namespace <namespace> port-forward --address 0.0.0.0 svc/redpanda-console 8080:8080
```

You will also need to allow traffic on port 8080 coming from your IP address to your localhost.  If you are using Cloud9 as described in this guide, you will need to edit the security group of your Cloud9 instance to allow port 8080 inbound with a source of “My IP”.

Do not allow full public access to port 8080, as the Redpanda Community Edition license does not enable authentication on the Redpanda Console.

Once you are able to access the Redpanda Console, you can view information about your brokers, IP addresses and IDs, as well as information on your topics.  You can view the messages produced to your topics, and produce additional messages to topics using the web interface.

## Expand the Permissions for the Created Redpanda Account

Now that the cluster is configured, we need to expand the permissions of the account that we created so that this account can be used to configure the AWS Lambda trigger. The account needs permissions such as creating new consumer groups. 

Steps:

1. Access the Redpanda console as described in previous steps.
2. Click on “Security” on the left margin.
3. Click on the username that you created in previous steps, our example uses “redpanda-twitch-account”.
4. A dialog titled “Edit ACL” will appear.  For the sake of this demo, click on “Allow all operations”.  Note that for production use, you will want to limit these permissions.
5. Click on “OK”.

## Configuring External Access

In order to allow our Lambda function to communicate with the cluster, we will need to take several steps to set up external access:

* Export the external certificate that was generated during the prior steps from the Redpanda cluster, and store it in AWS Secrets Manager
* Set up a username/password secret in AWS Secrets Manager
* Configure DNS to resolve the advertised external node names

We will dive deeper on these steps in the following sections. 

## Exporting the External Certificate

Switch back to the terminal you have been using to deploy and configure the cluster. Use the following command to export the external cert to the filename ca.crt:

```
kubectl get secret -n <namespace> redpanda-external-cert -o go-template='{{ index .data "ca.crt" | base64decode }}' > ca.crt
```

1. Copy the contents of the ca.crt file to your clipboard, and navigate to AWS Secrets Manager in the AWS console.  In Secrets Manager, click on “Store a new secret”.
2. Choose the Secret type “Other type of secret”.
3. Under “Key/value pairs”, click on “Plaintext”.  Paste the contents of your clipboard into the text field under “Plaintext”.  Then edit the text to match the following format:

```
{"certificate":"-----BEGIN CERTIFICATE-----
MIIBmjCCAUCgAwIBAgIQaMsCXPhoH7iVe8ewDJYYHTAKBggqhkjOPQQDAjAtMSsw
KQYDVQQDEyJyZWRwYW5kYS1leHRlcm5hbC1yb290LWNlcnRpZmljYXRlMB4XDTIz
MTIyMjE3NTM0M1oXDTI4MTIyMDE3NTM0M1owLTErMCkGA1UEAxMicmVkcGFuZGEt
ZXh0ZXJuYWwtcm9vdC1jZXJ0aWZpY2F0ZTBZMBMGByqGSM49AgEGCCqGSM49AwEH
A0IABNBbuTdNixU0y9CTa2nAo/x2KNHXBymhi8D+OJhvNcZgLFa1giQisekl1dA4
LRGs9pSziVa9oI75W1kl3SwnQT2jQjBAMA4GA1UdDwEB/wQEAwICpDAPBgNVHRMB
Af8EBTADAQH/MB0GA1UdDgQWBBSnPZZ1T/sKyuKlUwtFIy7/9kyC5zAKBggqhkjO
PQQDAgNIADBFAiBYm5Otwq8twAqrMemxQPXgATLvn9dzbvPSYv90JvFqXAIhAM+8
h23GH9rZM3K5zaeCg4dgn6Dd6UVGKLXKTlyn1AwC
-----END CERTIFICATE-----"
}
```

Matching this format is critical for the Lambda trigger integration to work correctly with our Redpanda cluster.

4. Click on “Next”.
5. Give your secret an easily identifiable name, such as “redpandarootcert”.  Accept the other defaults and click “Next”.
6. Click on “Next”, and then “Store” at the bottom of the next page.
7. You may need to click on the refresh button for your newly created secret to appear in the list.  Once it does appear, click on the secret name. 
8. Click on the copy button next to “Secret ARN” and save this in your notes for when we deploy using SAM.

## Save the Internal IPs of the Nodes

We need to know which IP addresses refers to the nodes, so run the following command in your terminal to get the information:

```
kubectl get pod --namespace <namespace>  \
-o=custom-columns=NODE:.spec.nodeName,NAME:.[metadata.name](http://metadata.name/) -l \
[app.kubernetes.io/component=redpanda-statefulset](http://app.kubernetes.io/component=redpanda-statefulset)
```

Save the output of this command this in your notes for use when deploying with SAM.

## Collecting Information Before Using SAM
 
We need to collect a few pieces of information before deploying our template.

* The VPC ID of the VPC created by eksctl.
* The subnet IDs of the public subnets created by eksctl.

Steps:

1. Navigate to the AWS Console and go to the VPC service.
2. Find the VPC created by our EKS cluster - the VPC name should have “eksctl” in the name.  Copy the VPC ID to your notes.  It should look something like “vpc-02bd59e133e36991d”.
3. Click on “Subnets” on the left margin.  Find the two subnets with “Public” and “eksctl” in the name, and copy the subnet IDs to your notes.  They should look something like “subnet-0d7fed3e19322e837”.

## Conclusion

With the Redpanda cluster now configured in EKS, we are ready to return to setting up the Lambda integration with Redpanda.

[Lambda Integration with Redpanda](README.md)

* * *
* * *
