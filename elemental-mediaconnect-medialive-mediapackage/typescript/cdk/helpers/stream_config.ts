export type IMediaConnectConfig = {
  whitelistCidr: string;
  availabilityZone: {
    a: string;
    b: string;
  };
  ingestPort: number;
  minLatency: number;
};

export type IMediaLiveConfig = {

  stream_name: string;
  streamName: string;
  codec: string;
  encodingProfile: string;
  type: string;
  priUrl: string;
  secUrl: string;
}


export type IMediaPackageConfig = {

  ip_sg_input: string;
  stream_name: string;
  hls_segment_duration_seconds: number;
  hls_playlist_window_seconds: number;
  hls_max_video_bits_per_second: number;
  hls_min_video_bits_per_second: number;
  hls_stream_order: string;
  dash_segment_duration_seconds: number;
  dash_manifest_window_seconds: number;
  dash_max_video_bits_per_second: number;
  dash_min_video_bits_per_second: number;
  dash_stream_order: string;
  mss_segment_duration_seconds: number;
  mss_manifest_window_seconds: number;
  mss_max_video_bits_per_second: number;
  mss_min_video_bits_per_second: number;
  mss_stream_order: string;
}
