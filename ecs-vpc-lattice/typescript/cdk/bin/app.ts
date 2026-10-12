#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { EcsVpcLatticeStack } from '../lib/ecs-vpc-lattice-stack';

const app = new cdk.App();
new EcsVpcLatticeStack(app, 'EcsVpcLatticeBlueGreenStack');
