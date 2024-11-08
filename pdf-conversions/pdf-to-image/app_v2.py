import os

from pdf2image import convert_from_path


def convert_pdf_to_png(input_pdf, output_prefix):
    # PDFを画像に変換
    images = convert_from_path(input_pdf)

    # 画像を保存
    for i, image in enumerate(images):
        if len(images) > 1:
            image.save(f'{output_prefix}_{i+1}.png', 'PNG')
        else:
            image.save(f'{output_prefix}.png', 'PNG')
    
    print(f"Converted {len(images)} pages from {input_pdf} to PNG files.")

def main():
    input_folder = 'input'
    output_folder = 'output'

    # 出力フォルダが存在しない場合は作成
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 入力フォルダ内のすべてのPDFファイルを取得
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

    # 各PDFファイルをPNGに変換
    for pdf_file in pdf_files:
        input_pdf_path = os.path.join(input_folder, pdf_file)
        output_prefix = os.path.join(output_folder, os.path.splitext(pdf_file)[0])
        convert_pdf_to_png(input_pdf_path, output_prefix)

if __name__ == "__main__":
    main()
