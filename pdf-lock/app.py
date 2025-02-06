import itertools
import sys

import pikepdf

#パスワードがかけられているPDFファイル
pdf_lock = r'locked.pdf'
#パスワード解除後のPDFファイル
pdf_nolock = r'unlocked.pdf'

#パスワードの確認に使用する文字
characters = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#パスワードの桁数の設定
count = 0

#総当たり開始
while True:
    count += 1
    for password in itertools.product(characters,repeat=count):
        try:
            #パスワードの文字を結合
            password = ''.join( password )

            pdf = pikepdf.open(pdf_lock, password=password)
            pdf_unlock = pikepdf.new()
            pdf_unlock.pages.extend(pdf.pages)
            pdf_unlock.save(pdf_nolock)
        except:
            print(password + ' は一致しませんでした')
        else:
            print('パスワードは' + password + 'でした。')
            #処理終了
            sys.exit()
