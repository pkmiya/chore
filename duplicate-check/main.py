import re
import sys
from collections import Counter

# 正規表現パターン: abc-def-1234567 形式
pattern = re.compile(r'\b[a-zA-Z]+-[a-zA-Z]+-\d{7}\b')

# 入力を読み込む（標準入力から改行区切り）
file_names = sys.stdin.read().splitlines()

# IDを抽出してカウント
ids = []
for name in file_names:
    matches = pattern.findall(name)
    ids.extend(matches)

# カウントして重複するものを抽出
counter = Counter(ids)
duplicates = [video_id for video_id, count in counter.items() if count > 1]

# 出力
for dup in duplicates:
    print(dup)
