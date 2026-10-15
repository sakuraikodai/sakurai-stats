# kodai-stats

数値のリストから算術平均を計算するPythonライブラリです。

## インストール

```bash
python -m pip install "git+https://github.com/sakuraikodai/kodai-stats.git"
```

## 使用例

```python
from kodai_stats import mean

print(mean([1, 2, 3]))
# 2.0
```

空のリストを渡すとValueErrorになります。

## 開発・テスト

```bash
poetry install
poetry run pytest
```

## 参考資料

ゼミ資料「Pythonライブラリの作り方」のDEMOをもとに作成しました。

## AI利用

コードと説明文の作成にChatGPTを使用しています。
