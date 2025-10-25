# daily_quiz.py
"""
毎日の財務分析クイズを生成してSlackに投稿するメインスクリプト
"""
import time
from quiz_generator_gemini import QuizGenerator
from slack_notifier import SlackNotifier

def main():
    """メイン処理"""
    print("🚀 財務分析クイズ自動配信システム")
    print("="*70)
    
    try:
        # 1. クイズ生成
        print("\n📝 Step 1: AIがクイズを生成中...")
        generator = QuizGenerator()
        quiz = generator.generate_quiz()
        
        if not quiz:
            print("❌ クイズの生成に失敗しました")
            return
        
        print(f"✅ クイズ生成完了: {quiz['company']['name']}")
        
        # 2. Slackに投稿
        print("\n📤 Step 2: Slackに投稿中...")
        notifier = SlackNotifier()
        
        # 問題を投稿
        if notifier.send_quiz(quiz):
            print("✅ 問題をSlackに投稿しました")
        else:
            print("❌ 問題の投稿に失敗しました")
            return
        
        # 3秒待つ（見やすくするため）
        print("\n⏱️  3秒後に解答を投稿します...")
        time.sleep(3)
        
        # 解答を投稿
        if notifier.send_answer(quiz):
            print("✅ 解答をSlackに投稿しました")
        else:
            print("❌ 解答の投稿に失敗しました")
            return
        
        print("\n" + "="*70)
        print("🎉 完了！Slackを確認してください！")
        print("="*70)
        
        # サマリー表示
        print(f"\n📊 本日のクイズ:")
        print(f"   企業名: {quiz['company']['name']}")
        print(f"   業界: {quiz['company']['industry']}")
        print(f"   決算期: {quiz['company']['fiscal_period']}")
        
    except Exception as e:
        print(f"\n❌ エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()