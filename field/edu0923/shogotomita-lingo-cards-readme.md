# Lingo Cards

観光・日常会話向けの多言語フラッシュカード学習アプリです。間隔反復（SRS）で覚えます。

対応言語: ヘブライ語 / スペイン語 / フランス語 / 中国語（各言語 約1500枚。動詞活用・アスペクト形込み）

## 構成

- ビルド不要の静的サイト（Vanilla HTML / CSS / JS）
- カードデータ: `data/{lang}.json`
- 進捗: `localStorage`（端末ローカル）
- 音声: Web Speech API（未対応環境では無効化）
- 単語データ生成: `scripts/build_decks.py`（`scripts/vocab/`）

## ローカル起動

`file://` だと `fetch` が失敗することがあるため、静的サーバで開いてください。

```bash
# Python 3
python3 -m http.server 8080
```

ブラウザで http://localhost:8080 を開きます。

## 単語データの再生成

```bash
python3 scripts/build_decks.py
# 特定言語のみ: python3 scripts/build_decks.py spanish
```

`data/` と `docs/` に JSON を出力します。語彙を一新すると `cardId` が変わるため、**既存の学習進捗は無効**になります。設定画面の「進捗をクリア」でリセットできます。

## GitHub Pages

リポジトリを GitHub に push し、Settings → Pages でソースをデプロイブランチ（例: `main` / root）に設定します。ルートに `index.html` があるため、そのまま公開できます。

## 使い方

1. 言語を選ぶ
2. カテゴリを選ぶ（デフォルトは全選択）
3. 「学習を始める」→ カード表面をタップして答えを表示（活用カードは裏面に原形も表示）
4. 「忘れた / 覚えた」で評価（覚えたカードも間隔を空けて再出題）
5. 統計・設定から進捗確認やバックアップ（JSON エクスポート／インポート）

## 仕様

詳細は [docs/SPEC.md](docs/SPEC.md) を参照してください。
