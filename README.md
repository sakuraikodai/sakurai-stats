# sakurai-stats

数値のリストから算術平均を計算するシンプルなPythonライブラリです。

尾山ゼミの2026年10月5日の課題として作成しました。

## インストール

GitHubから直接インストールできます。

```bash
python -m pip install "git+https://github.com/sakuraikodai/sakurai-stats.git"
```

## 使用例

```python
from sakurai_stats import mean

print(mean([1, 2, 3]))
# 2.0

print(mean([0.1, 0.2]))
# 0.15000000000000002
```

空のリストを渡した場合は `ValueError` が発生します。

## 開発・テスト

依存関係の管理にはPoetryを使用しています。

```bash
poetry install
poetry run pytest
```

以下の3つのケースをテストしています。

- 整数のリストの平均値
- 小数のリストの平均値
- 空のリストを渡した場合の例外処理

## 参考資料

- [尾山ゼミ 2026「10/5の課題」](https://github.com/OyamaZemi/2026/issues/31) — 課題の指示
- [尾山ゼミ 2026 Issue #30](https://github.com/OyamaZemi/2026/issues/30) — ライブラリ作成のDEMOに関する資料
- [尾山ゼミ Settingup「Python（Poetryを使う方法）」](https://github.com/OyamaZemi/Settingup/blob/master/docs/python-poetry.md) — Poetryによる開発環境の構築

## AI利用

ライブラリの実装、テストコードおよびREADMEの作成にChatGPTを使用しました。
