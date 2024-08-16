import os
import subprocess

import ffmpeg

# FFmpegとffprobeのパスを指定
ffmpeg_path = '/opt/homebrew/bin/ffmpeg'  # この部分を実際のパスに置き換えてください
ffprobe_path = '/opt/homebrew/bin/ffprobe'  # この部分を実際のパスに置き換えてください

# FFmpegとffprobeのパスを設定
ffmpeg._run.DEFAULT_FFMPEG_PATH = ffmpeg_path
ffmpeg._probe.DEFAULT_FFPROBE_PATH = ffprobe_path

def compress_video(input_file, output_file, target_size_mb=10, min_audio_bitrate=32000, max_audio_bitrate=256000, min_video_bitrate=100000):
    probe = ffmpeg.probe(input_file)
    duration = float(probe['streams'][0]['duration'])
    target_total_bitrate = (target_size_mb * 8 * 1024 * 1024) / duration
    
    # オーディオビットレートを計算（全体の10%を割り当て）
    audio_bitrate = max(min(0.1 * target_total_bitrate, max_audio_bitrate), min_audio_bitrate)
    
    # 残りをビデオに割り当て
    video_bitrate = max(target_total_bitrate - audio_bitrate, min_video_bitrate)
    
    i = ffmpeg.input(input_file)
    ffmpeg.output(i, output_file,
                  **{'c:v': 'libx264', 'b:v': video_bitrate, 'c:a': 'aac', 'b:a': audio_bitrate}
                 ).overwrite_output().run()
    
    print(f'圧縮完了: {output_file}')
    print(f'元のファイルサイズ: {os.path.getsize(input_file) / (1024 * 1024):.2f} MB')
    print(f'圧縮後のファイルサイズ: {os.path.getsize(output_file) / (1024 * 1024):.2f} MB')

# 使用例
input_file = 'input_video.MOV'
output_file = 'compressed_video.MOV'
target_size_mb = 900  # 目標ファイルサイズ（MB）

compress_video(input_file, output_file, target_size_mb)
