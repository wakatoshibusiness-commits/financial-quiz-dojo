# 📊 AI財務分析クイズ生成システム

新卒社員向けに、AIが自動的に財務分析の学習用クイズを生成するシステムです。

## 🎯 プロジェクトの背景

### 課題
- 新卒社員が財務諸表を読めるようになるまで時間がかかる
- 座学だけでは実践的なスキルが身につきにくい
- 毎日継続的に学習する仕組みが必要

### 解決策
実在企業の決算データを使い、AIが自動的に問題を生成。
毎日異なる企業の財務分析問題を配信することで、
継続的な学習習慣を形成します。

## ✨ 主な機能

- 🤖 **AI自動問題生成**: Google Gemini APIを使用し、財務データから自動で問題を生成
- 📊 **実在企業データ**: 上場企業の実際の決算データを使用（トヨタ、ソニー、ユニクロなど）
- 💡 **段階的学習**: 問題 → ヒント → 解答 → 解説の流れで理解を深化
- 🆓 **完全無料**: Google Gemini の無料枠を使用し、コスト0で運用可能

## 🛠️ 技術スタック

- **言語**: Python 3.13
- **AI**: Google Gemini API (gemini-2.5-flash)
- **開発環境**: Cursor AI Editor
- **その他**: 
  - python-dotenv（環境変数管理）
  - google-generativeai（AI API）

## 📁 プロジェクト構成
```
financial-quiz-dojo/
├── company_data.json          # 企業財務データ（3社分）
├── data_loader.py             # データ読み込み・管理
├── quiz_generator_gemini.py   # AI問題生成メイン
├── check_models.py            # 利用可能なAIモデル確認
├── .env                       # APIキー（.gitignoreで除外）
├── .gitignore                 # Git除外設定
└── README.md                  # このファイル
```

## 🚀 セットアップ方法

### 1. リポジトリのクローン
```bash
git clone https://github.com/wakatoshibusiness-commits/financial-quiz-dojo.git
cd financial-quiz-dojo
```

### 2. 必要なパッケージのインストール
```bash
pip install google-generativeai python-dotenv
```

### 3. 環境変数の設定
`.env` ファイルを作成し、Google Gemini APIキーを設定：
```
GOOGLE_API_KEY=your_api_key_here
```

**APIキーの取得方法:**
1. [Google AI Studio](https://aistudio.google.com/) にアクセス
2. Googleアカウントでログイン
3. 「Get API key」→「Create API key」
4. 生成されたキーをコピー

### 4. 実行
```bash
python quiz_generator_gemini.py
```

## 📸 実行例
```
🚀 財務分析クイズ生成システム（Powered by Google Gemini）
======================================================================
💰 完全無料！無制限！
======================================================================

📊 今日の財務分析クイズ

🏢 企業名: トヨタ自動車
🏭 業界: 自動車製造業
📅 決算期: 2024年3月期

💰 財務サマリー:
   売上高: 37,200,000百万円
   営業利益: 2,840,000百万円
   ROE: 12.0%
   自己資本比率: 45.0%

----------------------------------------------------------------------
📝 問題
----------------------------------------------------------------------
トヨタ自動車の営業利益率は7.6%となっています。
売上高37兆円という巨大な規模の中で、この利益率を
どのように評価すべきでしょうか...
```

## 💡 工夫した点

### 1. 完全無料運用
- Google Gemini の無料枠を活用（月1,500リクエスト）
- クレジットカード登録不要
- 実質無制限に使用可能

### 2. セキュリティ
- `.gitignore` でAPIキーを厳重に管理
- 環境変数（.env）で機密情報を分離
- GitHubに秘密情報を公開しない設計

### 3. 教育的な出力
- 単なる正解だけでなく、ヒントと詳しい解説を生成
- 公認会計士の視点を含む実践的な内容
- 新卒でも理解できる丁寧な説明

### 4. 拡張性
- 企業データは簡単に追加可能（JSONファイル編集のみ）
- Slack連携など、今後の拡張を想定した設計
- モジュール化された構造

## 🎓 このプロジェクトで学んだこと

- Python環境構築と基礎文法
- AI API（Google Gemini）の実践的な活用方法
- JSON形式でのデータ構造設計
- Gitによるバージョン管理
- GitHubでのコード公開・管理
- プロンプトエンジニアリングの基礎
- セキュリティ（APIキー管理）の重要性

## 🔜 今後の展開

- [ ] Slack Webhook による自動投稿機能
- [ ] GitHub Actions で毎日自動実行
- [ ] 企業データを20社以上に拡充
- [ ] 回答履歴の記録・分析機能
- [ ] 難易度別の問題生成
- [ ] Webダッシュボードの作成

## 🤝 使用技術・参考資料

- [Google Gemini API Documentation](https://ai.google.dev/)
- [Python dotenv](https://github.com/theskumar/python-dotenv)
- [IR BANK](https://irbank.net/) - 企業財務データ参照

## 📝 ライセンス

MIT License

## 👤 作成者

wakatoshibusiness-commits
- GitHub: [@wakatoshibusiness-commits](https://github.com/wakatoshibusiness-commits)

---

**このプロジェクトは、社内の新卒教育を改善したいという思いから生まれました。**
**AI技術を活用して、より効果的で継続的な学習環境を提供することを目指しています。**