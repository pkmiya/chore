import argparse

from pdf2image import convert_from_path


def convert_pdf_to_png(input_pdf, output_prefix):
    # PDFを画像に変換
    images = convert_from_path(input_pdf)

    # 画像を保存
    for i, image in enumerate(images):
        image.save(f'{output_prefix}_{i+1}.png', 'PNG')
    
    print(f"Converted {len(images)} pages from {input_pdf} to PNG files.")

def main():
    # コマンドライン引数のパーサーを設定
    parser = argparse.ArgumentParser(description='Convert PDF to PNG images.')
    parser.add_argument('input_pdf', help='Input PDF file path')
    parser.add_argument('output_prefix', help='Prefix for output PNG files')

    # 引数を解析
    args = parser.parse_args()

    # PDF to PNG 変換を実行
    convert_pdf_to_png(args.input_pdf, args.output_prefix)

if __name__ == "__main__":
    main()
