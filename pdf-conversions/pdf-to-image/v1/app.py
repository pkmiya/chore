import os
import fitz  # PyMuPDFのインポート

def convert_pdf_to_png(pdf_path, output_folder):
    # PDFファイルを開く
    doc = fitz.open(pdf_path)
    
    # 出力フォルダが存在しない場合は作成
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 各ページを処理
    for page_number in range(len(doc)):
        page = doc.load_page(page_number)  # ページを読み込む
        pix = page.get_pixmap()  # ピクセルマップを取得
        output_path = f"{output_folder}/page_{page_number + 1}.png"
        pix.save(output_path)  # 画像として保存

    doc.close()

# 使用例
pdf_path = 'input.pdf'
output_folder = './output'
convert_pdf_to_png(pdf_path, output_folder)

print("変換が完了しました。")
