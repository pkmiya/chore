import os
import subprocess

file_list = "filelist.txt"
preprocess_file = "output.ts"
output_folder = "./output"
output_file = os.path.join(output_folder, "output.mp4")

def create_output_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def concatenate_ts_files(input_folder, num_files=None):
    # ファイルリストを作成
    ts_files = [f for f in sorted(os.listdir(input_folder)) if f.endswith('.ts')]
    
    # 指定された数のファイルのみを選択
    if num_files is not None:
        ts_files = ts_files[:num_files]

    # ファイルリストをテキストファイルに書き込み
    with open(file_list, 'w') as f:
        for filename in ts_files:
            f.write("file '{}/{}'\n".format(input_folder, filename))

    # ffmpegを使用してファイルを結合
    subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', file_list, '-c', 'copy', preprocess_file])
    
    # filelist.txtを削除
    os.remove(file_list)

def convert_ts_to_mp4(ts_file, output_path):
    # ffmpegを使用して.tsファイルを.mp4に変換
    subprocess.run(['ffmpeg', '-i', ts_file, '-codec', 'copy', output_path])
    
    # output.tsを削除
    os.remove(ts_file)

def main():
    print("START_OF_PROGRAM")
    
    # '/output' フォルダの作成
    create_output_folder(output_folder)

    print("1. Concatenating .ts files...")
    # './input'フォルダ内の全ての.tsファイルを結合
    concatenate_ts_files('./input') # 必要があれば，num_files=でファイル数を指定
    print("Done.")
    
    print("2. Converting .ts to .mp4...")
    # 結合された.tsファイルを.mp4に変換
    convert_ts_to_mp4(preprocess_file, output_file)
    print("Done.")
    
    print(f"File saved as {output_file}.")
    print(f"File size: {os.path.getsize(output_file) / 1000000:.2f} MB")
    print("END_OF_PROGRAM")

main()