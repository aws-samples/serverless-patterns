import { IMediaConnectConfig, IMediaLiveConfig, IMediaPackageConfig } from "./stream_config";

export function loadMediaConnectConfig(): IMediaConnectConfig {
  let config = {} as IMediaConnectConfig;

  try {
    config = require("../config/media_connect.json");
  } catch (e) {
    console.error(`The 'media_connect.json' file could not be found.`);
    process.exit(1);
  }

  return config as IMediaConnectConfig;
}

export function loadMediaLiveConfig(): IMediaLiveConfig {
  let config = {} as IMediaLiveConfig;

  try {
    config = require("../config/media_live.json");
  } catch (e) {
    console.error(`The 'media_live.json' file could not be found.`);
    process.exit(1);
  }

  return config as IMediaLiveConfig;
}



export function loadMediaPackageConfig(): IMediaPackageConfig {
  let config = {} as IMediaPackageConfig;

  try {
    config = require("../config/media_package.json");
  } catch (e) {
    console.error(`The 'media_package.json' file could not be found.`);
    process.exit(1);
  }

  return config as IMediaPackageConfig;
}

