# quiz_generator_gemini.py
import os
import google.generativeai as genai
from dotenv import load_dotenv
from data_loader import CompanyDataLoader

class QuizGenerator:
    """財務データからクイズを自動生成するクラス（Google Gemini使用）"""
    
    def __init__(self):
        """初期化: APIキーを読み込み、Geminiを設定"""
        load_dotenv()
        
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            raise ValueError("❌ GOOGLE_API_KEYが設定されていません。.envファイルを確認してください。")
        
        print("✅ Google Gemini APIキーを読み込みました")
        
        # Gemini APIを設定
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
        self.data_loader = CompanyDataLoader()
    
    def generate_quiz(self, company=None):
        """財務データからクイズを生成"""
        if company is None:
            company = self.data_loader.get_random_company()
        
        if not company:
            raise ValueError("❌ 企業データを取得できませんでした。")
        
        company_name = company['name']
        industry = company['industry']
        fiscal_period = company['fiscal_period']
        
        print(f"📊 {company_name}のクイズを生成します...")
        
        financial = company['financial_data']
        
        prompt = f"""
あなたは公認会計士として、新卒社員向けの財務分析クイズを作成してください。

【企業情報】
企業名: {company_name}
業界: {industry}
決算期: {fiscal_period}

【財務データ】
売上高: {financial['revenue']:,}百万円（前年比 {financial.get('revenue_growth', 0):+.1f}%）
営業利益: {financial['operating_profit']:,}百万円（前年比 {financial.get('operating_profit_growth', 0):+.1f}%）
純利益: {financial['net_income']:,}百万円
総資産: {financial['total_assets']:,}百万円
純資産: {financial['equity']:,}百万円
ROE: {financial['roe']}%
自己資本比率: {financial['equity_ratio']}%
営業利益率: {financial.get('operating_margin', 0)}%

【指示】
1. この財務データから読み取れる経営課題や特徴を1つ見つけてください
2. 新卒社員が考えるための問題文を作成してください（難易度: 中級）
3. 考えるヒントを1-2つ提供してください
4. 模範解答を150-200文字で書いてください
5. 詳しい解説を200-300文字で書いてください

【出力フォーマット】
問題文:
（ここに問題。100-150文字程度）

ヒント:
（ここにヒント。50-100文字程度）

模範解答:
（ここに解答。150-200文字程度）

解説:
（ここに解説。200-300文字程度。なぜその分析が重要か、経営への示唆も含める）
"""
        
        try:
            print("🤖 Google Gemini AIが問題を生成中...")
            
            response = self.model.generate_content(prompt)
            
            print("✅ 問題生成完了！")
            
            quiz_text = response.text
            quiz = self._parse_quiz(quiz_text)
            
            quiz['company'] = {
                'name': company_name,
                'industry': industry,
                'fiscal_period': fiscal_period,
                'financial_data': financial
            }
            
            return quiz
            
        except Exception as e:
            print(f"❌ エラーが発生しました: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def _parse_quiz(self, text):
        """出力をパース"""
        sections = {
            'question': '',
            'hint': '',
            'answer': '',
            'explanation': ''
        }
        
        current_section = None
        
        for line in text.split('\n'):
            line = line.strip()
            
            if '問題文:' in line or '問題：' in line or '【問題】' in line or '問題:' in line:
                current_section = 'question'
                continue
            elif 'ヒント:' in line or 'ヒント：' in line or '【ヒント】' in line:
                current_section = 'hint'
                continue
            elif '模範解答:' in line or '模範解答：' in line or '解答:' in line or '【解答】' in line or '【模範解答】' in line or '解答：' in line:
                current_section = 'answer'
                continue
            elif '解説:' in line or '解説：' in line or '【解説】' in line:
                current_section = 'explanation'
                continue
            
            if current_section and line:
                sections[current_section] += line + '\n'
        
        for key in sections:
            sections[key] = sections[key].strip()
        
        return sections
    
    def display_quiz(self, quiz):
        """クイズを見やすく表示"""
        if not quiz:
            print("❌ クイズが生成されませんでした。")
            return
        
        company = quiz['company']
        
        print("\n" + "="*70)
        print(f"📊 今日の財務分析クイズ（Powered by Google Gemini）")
        print("="*70)
        print(f"\n🏢 企業名: {company['name']}")
        print(f"🏭 業界: {company['industry']}")
        print(f"📅 決算期: {company['fiscal_period']}")
        print(f"\n💰 財務サマリー:")
        print(f"   売上高: {company['financial_data']['revenue']:,}百万円")
        print(f"   営業利益: {company['financial_data']['operating_profit']:,}百万円")
        print(f"   ROE: {company['financial_data']['roe']}%")
        print(f"   自己資本比率: {company['financial_data']['equity_ratio']}%")
        
        print("\n" + "-"*70)
        print("📝 問題")
        print("-"*70)
        print(quiz['question'])
        
        print("\n" + "-"*70)
        print("💡 ヒント")
        print("-"*70)
        print(quiz['hint'])
        
        print("\n" + "="*70)
        input("✋ 考えてから Enter を押すと解答が表示されます...")
        print("="*70)
        
        print("\n" + "-"*70)
        print("✅ 模範解答")
        print("-"*70)
        print(quiz['answer'])
        
        print("\n" + "-"*70)
        print("📚 解説")
        print("-"*70)
        print(quiz['explanation'])
        print("\n" + "="*70)

if __name__ == '__main__':
    try:
        print("🚀 財務分析クイズ生成システム（Powered by Google Gemini）")
        print("="*70)
        print("💰 完全無料！無制限！")
        print("="*70)
        
        generator = QuizGenerator()
        quiz = generator.generate_quiz()
        
        if quiz:
            generator.display_quiz(quiz)
            print("\n✅ クイズ生成完了！")
            print("\n🎉 AIが自動で問題を作成しました！")
        else:
            print("\n❌ クイズの生成に失敗しました。")
            
    except ValueError as e:
        print(f"\n❌ 設定エラー: {e}")
        print("\n💡 対処法:")
        print("1. .env ファイルが存在するか確認")
        print("2. GOOGLE_API_KEY が正しく設定されているか確認")
        print("3. APIキーが AIzaSy で始まっているか確認")
    except Exception as e:
        print(f"\n❌ 予期しないエラー: {e}")
        import traceback
        traceback.print_exc()