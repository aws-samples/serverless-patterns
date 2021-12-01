import { Sequelize, Options as SequelizeOptions, DataTypes } from 'sequelize';
import { Signer } from 'aws-sdk-js-v3-rds-signer';

const sequelizeConfig: SequelizeOptions = {
  host: process.env.PGHOST,
  dialect: 'postgres'
};

if (process.env.STAGE !== 'local') {
  sequelizeConfig.dialectOptions = {
    ssl: {
      rejectUnauthorized: true
    }
  };
}

const signer = new Signer({
  hostname: process.env.PGHOST,
  port: 5432,
  region: process.env.AWS_REGION,
  username: 'syscdk'
});

const sequelize = new Sequelize(process.env.PGDATABASE || '', process.env.PGUSER || '', process.env.PGPASSWORD || '', sequelizeConfig);

if (process.env.STAGE !== 'local' && !sequelize.hasHook('beforeConnect')) {
  sequelize.addHook('beforeConnect', async (config) => {
    // @ts-ignore
    config.password = await signer.getAuthToken();
  });
}

const Stadium = sequelize.define('Stadium', {
  name: {
    type: DataTypes.STRING,
    allowNull: false
  },
  capacity: {
    type: DataTypes.INTEGER,
    allowNull: false
  },
  location: {
    type: DataTypes.STRING,
    allowNull: false
  },
  surface: {
    type: DataTypes.STRING,
    allowNull: false
  },
  roof: {
    type: DataTypes.STRING,
    allowNull: false
  },
  team: {
    type: DataTypes.STRING,
    allowNull: false
  },
  yearOpened: {
    type: DataTypes.STRING,
    allowNull: false
  }
}, {
  tableName: 'stadiums'
});

export { Stadium, sequelize };