# Outline
This is a simple script to merge and convert `.ts` files into a single `.mp4` file. \
This script depends on [ffmpeg](https://ffmpeg.org/).

# Setup
1. Go to the [ffmpeg website](https://ffmpeg.org/download.html) ([GitHub](https://github.com/BtbN/FFmpeg-Builds/releases) preffered)and download the latest version of ffmpeg for your operating system. \
    If you're on Windows 64-bit, you can download it [here](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl-shared.zip).
1. Extract the zip file to a folder of your choice.\
    For example, onto `C:\Program Files\`.
1. Add the `bin` folder to your PATH environment variable. \
   (If necessary, follow [this guide](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/).) \
   The directory name depends on your downloaded version. For example, `C:\Program Files\ffmpeg\bin`.
1. Open a command prompt and run `ffmpeg -version` to check if it's installed correctly.


- If looking like unsuccessful, try the following:
  - Close the environmental control panel (press "OK")
  - Restart terminal
  - Restart editor (VSCode for example)
  - Restart computer

# Usage
1. Clone this repository to your computer.
1. Open a command prompt and navigate to the root directory of this repository. (For example, `cd C:\Users\user\Documents\GitHub\merge-ts-as-mp4`)
1. Create a folder called `input` and put all your `.ts` files in there.
1. Type `python app.py` and press enter to run the script.
1. If the process is successful, you will find the output file in the `output` folder.

# Log example
![Log image 1](/docs/img/1.png)
![Log image 2](/docs/img/2.png)

```
C:\Users\pkmiya\OneDrive\MY_study\Chore\merge-ts-as-mp4>python3 app.py
START_OF_PROGRAM
1. Concatenating .ts files...
ffmpeg version N-112938-g12e25af7a8-20231210 Copyright (c) 2000-2023 the FFmpeg developers
  built with gcc 13.2.0 (crosstool-NG 1.25.0.232_c175b21)
  configuration: --prefix=/ffbuild/prefix --pkg-config-flags=--static --pkg-config=pkg-config --cross-prefix=x86_64-w64-mingw32- --arch=x86_64 --target-os=mingw32 --enable-gpl --enable-version3 --disable-debug --enable-shared --disable-static --disable-w32threads --enable-pthreads --enable-iconv --enable-libxml2 --enable-zlib --enable-libfreetype --enable-libfribidi --enable-gmp --enable-lzma --enable-fontconfig --enable-libharfbuzz --enable-libvorbis --enable-opencl --disable-libpulse --enable-libvmaf --disable-libxcb --disable-xlib --enable-amf --enable-libaom --enable-libaribb24 --enable-avisynth --enable-chromaprint --enable-libdav1d --enable-libdavs2 --disable-libfdk-aac --enable-ffnvcodec --enable-cuda-llvm --enable-frei0r --enable-libgme --enable-libkvazaar --enable-libaribcaption --enable-libass --enable-libbluray --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librist --enable-libssh --enable-libtheora --enable-libvpx --enable-libwebp 
--enable-lv2 --enable-libvpl --enable-openal --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenh264 --enable-libopenjpeg --enable-libopenmpt --enable-librav1e --enable-librubberband --enable-schannel --enable-sdl2 --enable-libsoxr --enable-libsrt --enable-libsvtav1 --enable-libtwolame --enable-libuavs3d --disable-libdrm --enable-vaapi --enable-libvidstab --enable-vulkan --enable-libshaderc --enable-libplacebo --enable-libx264 --enable-libx265 --enable-libxavs2 --enable-libxvid --enable-libzimg --enable-libzvbi --extra-cflags=-DLIBTWOLAME_STATIC --extra-cxxflags= --extra-ldflags=-pthread --extra-ldexeflags= --extra-libs=-lgomp --extra-version=20231210
  libavutil      58. 32.100 / 58. 32.100
  libavcodec     60. 35.100 / 60. 35.100
  libavformat    60. 18.100 / 60. 18.100
  libavdevice    60.  4.100 / 60.  4.100
  libavfilter     9. 14.100 /  9. 14.100
  libswscale      7.  6.100 /  7.  6.100
  libswresample   4. 13.100 /  4. 13.100
  libpostproc    57.  4.100 / 57.  4.100
Input #0, concat, from 'filelist.txt':
  Duration: N/A, start: 0.000000, bitrate: N/A
  Stream #0:0: Video: h264 (Main) ([27][0][0][0] / 0x001B), yuv420p(tv, bt709, progressive), 360x640 [SAR 1:1 DAR 9:16], 60 fps, 60 tbr, 90k tbn
  Stream #0:1(und): Audio: aac (LC) ([15][0][0][0] / 0x000F), 48000 Hz, stereo, fltp, 107 kb/s
Output #0, mpegts, to 'output.ts':
  Metadata:
    encoder         : Lavf60.18.100
  Stream #0:0: Video: h264 (Main) ([27][0][0][0] / 0x001B), yuv420p(tv, bt709, progressive), 360x640 [SAR 1:1 DAR 9:16], q=2-31, 60 fps, 60 tbr, 90k tbn
  Stream #0:1(und): Audio: aac (LC) ([15][0][0][0] / 0x000F), 48000 Hz, stereo, fltp, 107 kb/s
Stream mapping:
  Stream #0:0 -> #0:0 (copy)
  Stream #0:1 -> #0:1 (copy)
Press [q] to stop, [?] for help
[out#0/mpegts @ 0000024f9f73fa00] video:87225kB audio:8365kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 10.225758%
size=  105365kB time=00:11:54.55 bitrate=1208.0kbits/s speed= 733x
Done.
1. Converting .ts to .mp4...
ffmpeg version N-112938-g12e25af7a8-20231210 Copyright (c) 2000-2023 the FFmpeg developers
  built with gcc 13.2.0 (crosstool-NG 1.25.0.232_c175b21)
  configuration: --prefix=/ffbuild/prefix --pkg-config-flags=--static --pkg-config=pkg-config --cross-prefix=x86_64-w64-mingw32- --arch=x86_64 --target-os=mingw32 --enable-gpl --enable-version3 --disable-debug --enable-shared --disable-static --disable-w32threads --enable-pthreads --enable-iconv --enable-libxml2 --enable-zlib --enable-libfreetype --enable-libfribidi --enable-gmp --enable-lzma --enable-fontconfig --enable-libharfbuzz --enable-libvorbis --enable-opencl --disable-libpulse --enable-libvmaf --disable-libxcb --disable-xlib --enable-amf --enable-libaom --enable-libaribb24 --enable-avisynth --enable-chromaprint --enable-libdav1d --enable-libdavs2 --disable-libfdk-aac --enable-ffnvcodec --enable-cuda-llvm --enable-frei0r --enable-libgme --enable-libkvazaar --enable-libaribcaption --enable-libass --enable-libbluray --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librist --enable-libssh --enable-libtheora --enable-libvpx --enable-libwebp 
--enable-lv2 --enable-libvpl --enable-openal --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenh264 --enable-libopenjpeg --enable-libopenmpt --enable-librav1e --enable-librubberband --enable-schannel --enable-sdl2 --enable-libsoxr --enable-libsrt --enable-libsvtav1 --enable-libtwolame --enable-libuavs3d --disable-libdrm --enable-vaapi --enable-libvidstab --enable-vulkan --enable-libshaderc --enable-libplacebo --enable-libx264 --enable-libx265 --enable-libxavs2 --enable-libxvid --enable-libzimg --enable-libzvbi --extra-cflags=-DLIBTWOLAME_STATIC --extra-cxxflags= --extra-ldflags=-pthread --extra-ldexeflags= --extra-libs=-lgomp --extra-version=20231210
  libavutil      58. 32.100 / 58. 32.100
  libavcodec     60. 35.100 / 60. 35.100
  libavformat    60. 18.100 / 60. 18.100
  libavdevice    60.  4.100 / 60.  4.100
  libavfilter     9. 14.100 /  9. 14.100
  libswscale      7.  6.100 /  7.  6.100
  libswresample   4. 13.100 /  4. 13.100
  libpostproc    57.  4.100 / 57.  4.100
Input #0, mpegts, from 'output.ts':
  Duration: 00:11:54.58, start: 1.400000, bitrate: 1207 kb/s
  Program 1
    Metadata:
      service_name    : Service01
      service_provider: FFmpeg
  Stream #0:0[0x100]: Video: h264 (Main) ([27][0][0][0] / 0x001B), yuv420p(tv, bt709, progressive), 360x640 [SAR 1:1 DAR 9:16], 60 fps, 60 tbr, 90k tbn
  Stream #0:1[0x101](und): Audio: aac (LC) ([15][0][0][0] / 0x000F), 48000 Hz, stereo, fltp, 96 kb/s
Output #0, mp4, to './output\output.mp4':
  Metadata:
    encoder         : Lavf60.18.100
  Stream #0:0: Video: h264 (Main) (avc1 / 0x31637661), yuv420p(tv, bt709, progressive), 360x640 [SAR 1:1 DAR 9:16], q=2-31, 60 fps, 60 tbr, 90k tbn
  Stream #0:1(und): Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 96 kb/s
Stream mapping:
  Stream #0:0 -> #0:0 (copy)
  Stream #0:1 -> #0:1 (copy)
Press [q] to stop, [?] for help
[out#0/mp4 @ 000001ba532bd040] video:87225kB audio:8365kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.821726%
size=   96375kB time=00:11:54.55 bitrate=1104.9kbits/s speed=1.12e+03x
Done.
File saved as ./output\output.mp4.
File size: 98.69 MB
END_OF_PROGRAM
```