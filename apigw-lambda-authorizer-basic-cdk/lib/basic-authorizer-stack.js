const {Construct} = require('constructs');
const {Stack} = require('aws-cdk-lib');
const {BasicAuthorizerConstruct} = require('./basic-authorizer-construct');

class BasicAuthorizerStack extends Stack {
    /**
     *
     * @param {Construct} scope
     * @param {string} id
     * @param {Object} props
     */
    constructor(scope, id, props) {
        super(scope, id, props);

        new BasicAuthorizerConstruct(this, 'BasicAuthorizerConstruct', props);
    }
}

module.exports = {BasicAuthorizerStack}
