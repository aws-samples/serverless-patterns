export type IMediaLiveConfig = {

  inputCidr: string;
  streamName: string;
  codec: string;
  encodingProfile: string;
  inputType: string;
  channelClass: string;
  priUrl: string;
  secUrl: string;
  priLink: string;
  secLink: string;
  priFlow: string;
  secFlow: string;
  sourceEndBehavior: string;
}


export type IMediaPackageConfig = {
  ad_markers: string;
  cdn_authorization: boolean;
  hls_program_date_interval: number;
  ip_sg_input: string;
  stream_name: string;
  hls_segment_duration_seconds: number;
  hls_playlist_window_seconds: number;
  hls_max_video_bits_per_second: number;
  hls_min_video_bits_per_second: number;
  hls_stream_order: string;
  hls_include_I_frame:boolean;
  hls_audio_rendition_group:boolean;
  dash_period_triggers: string;
  dash_segment_duration_seconds: number;
  dash_manifest_window_seconds: number;
  dash_max_video_bits_per_second: number;
  dash_min_video_bits_per_second: number;
  dash_stream_order: string;
  cmaf_segment_duration_seconds: number;
  cmaf_program_date_interval:number;
  cmaf_manifest_window_seconds: number;
  cmaf_max_video_bits_per_second: number;
  cmaf_min_video_bits_per_second: number;
  cmaf_stream_order: string;
  cmaf_include_I_frame:boolean;
  cmaf_audio_rendition_group:boolean;
  cmaf_include_encoder_configuration_in_segments:boolean;
  mss_segment_duration_seconds: number;
  mss_manifest_window_seconds: number;
  mss_max_video_bits_per_second: number;
  mss_min_video_bits_per_second: number;
  mss_stream_order: string;
}
