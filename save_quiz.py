# save_quiz.py
import json
import os
from datetime import datetime
from quiz_generator_gemini import QuizGenerator

def save_quiz_to_file(quiz, output_dir='output'):
    """生成したクイズをファイルに保存"""
    
    # outputディレクトリがなければ作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"📁 {output_dir} フォルダを作成しました")
    
    # ファイル名（日時 + 企業名）
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    company_name = quiz['company']['name'].replace('（', '').replace('）', '')
    filename = f"{output_dir}/quiz_{timestamp}_{company_name}.json"
    
    # JSONとして保存
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(quiz, f, ensure_ascii=False, indent=2)
    
    print(f"💾 問題を保存しました: {filename}")
    return filename

if __name__ == '__main__':
    print("🚀 AIクイズ生成 & 保存システム")
    print("="*70)
    
    generator = QuizGenerator()
    
    # 問題を3つ生成
    for i in range(3):
        print(f"\n📝 {i+1}問目を生成中...")
        quiz = generator.generate_quiz()
        
        if quiz:
            generator.display_quiz(quiz)
            save_quiz_to_file(quiz)
        
        print("\n" + "="*70)
    
    print("\n✅ 全て完了！outputフォルダに保存されました")