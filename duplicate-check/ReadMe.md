# 実行方法

## ディレクトリの情報ごと渡す場合

### Windows OS

```
dir /b | python main.py
```

### Mac OS

```
ls | python main.py
```

＊複数ディレクトリ・エラーを無視
```
find  /f/AppData/ /g/AppData/ /h/AppData/ /i/AppData/ -type f 2>/dev/null | python main.py
```