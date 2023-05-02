import { GoFunction } from "@aws-cdk/aws-lambda-go-alpha";
import * as cdk from "aws-cdk-lib";
import { Duration, Fn, Tags } from "aws-cdk-lib";
import { Construct } from "constructs";
import * as path from "path";
import { IFunction } from "aws-cdk-lib/aws-lambda";
import { addHealthlakeToFunc } from "./function-utils";
import { CfnFHIRDatastore } from "aws-cdk-lib/aws-healthlake";
import { Key } from "aws-cdk-lib/aws-kms";

export class FunctionsConstruct extends Construct {
    private _patientHydrator: IFunction;
    private _patientPublisher: IFunction;
    private readonly _storeId: string;

    constructor(scope: Construct, id: string, hl: CfnFHIRDatastore, key: Key) {
        super(scope, id);

        const version = new Date().toISOString();
        this._storeId = hl.attrDatastoreId;
        this.buildPatientHydrator(hl, key);
        this.buildPatientPublisher();

        Tags.of(this._patientHydrator).add("version", version);
        Tags.of(this._patientPublisher).add("version", version);
    }

    buildPatientHydrator = (hl: CfnFHIRDatastore, key: Key) => {
        this._patientHydrator = new GoFunction(
            this,
            `PatientHydratorFunction`,
            {
                entry: path.join(__dirname, `../src/patient-hydrator`),
                functionName: `healthlake-cdc-patient-hydrator`,
                timeout: Duration.seconds(30),
                environment: {
                    HL_STORE_ID: this._storeId,
                },
            }
        );

        addHealthlakeToFunc(
            this,
            "PatientHydratorFunction",
            this._patientHydrator,
            hl,
            key
        );
    };

    buildPatientPublisher = () => {
        this._patientPublisher = new GoFunction(
            this,
            `PatientPublisherFunction`,
            {
                entry: path.join(__dirname, `../src/patient-publisher`),
                functionName: `healthlake-cdc-patient-publisher`,
                timeout: Duration.seconds(30),
                environment: {},
            }
        );
    };

    get patientHydrator(): IFunction {
        return this._patientHydrator;
    }

    get patientPublisher(): IFunction {
        return this._patientPublisher;
    }
}
