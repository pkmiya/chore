import re
import sys
from collections import Counter

# 動画IDの正規表現パターン
pattern = re.compile(r'\b[a-zA-Z]+-[a-zA-Z]+-\d{7}\b')

# 動画IDを格納
ids = []

try:
    for line in sys.stdin:
        try:
            line = line.strip()

            # ID抽出
            matches = pattern.findall(line)
            if matches:
                ids.extend(matches)
        except UnicodeDecodeError:
            # マルチバイト文字エラーを無視
            continue
except Exception as e:
    print(f"エラー発生: {e}", file=sys.stderr)

# 重複をカウント
counter = Counter(ids)
duplicates = [video_id for video_id, count in counter.items() if count > 1]

# 出力
for dup in duplicates:
    print(dup)
