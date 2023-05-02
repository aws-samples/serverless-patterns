import { Key } from "aws-cdk-lib/aws-kms";
import { Construct } from "constructs";

export class KeyConstruct extends Construct {
    private readonly _key: Key;

    constructor(scope: Construct, id: string) {
        super(scope, id);
        this._key = new Key(this, `Key`);
        this._key.addAlias(`alias/healthlake-key`);
    }

    get key(): Key {
        return this._key;
    }
}
