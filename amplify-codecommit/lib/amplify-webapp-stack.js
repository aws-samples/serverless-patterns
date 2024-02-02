const {Construct} = require('constructs');
const {Stack} = require('aws-cdk-lib');
const {AmplifyWebAppConstruct} = require('./amplify-webapp-construct.js');

class AmplifyWebAppStack extends Stack {
    /**
     *
     * @param {Construct} scope
     * @param {string} id
     * @param {Object} props
     */
    constructor(scope, id, props) {
        super(scope, id, props);

        new AmplifyWebAppConstruct(this, 'AmplifyWebAppConstruct', props);
    }
}

module.exports = {AmplifyWebAppStack}