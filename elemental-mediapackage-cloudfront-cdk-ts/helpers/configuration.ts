import { IMediaPackageConfig } from "./stream_config";

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

