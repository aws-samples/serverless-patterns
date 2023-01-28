import { RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib'
import { AttributeType, BillingMode, Table } from 'aws-cdk-lib/aws-dynamodb'
import { Construct } from 'constructs'

interface DatabaseStackProps extends StackProps {}

export class DatabaseStack extends Stack {
	public readonly productTable: Table
	constructor(scope: Construct, id: string, props: DatabaseStackProps) {
		super(scope, id, props)

		const productTable = new Table(this, 'ProductTable', {
			removalPolicy: RemovalPolicy.DESTROY,
			billingMode: BillingMode.PAY_PER_REQUEST,
			partitionKey: { name: 'id', type: AttributeType.STRING },
		})

		this.productTable = productTable
	}
}
