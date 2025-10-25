# check_models.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    print("❌ GOOGLE_API_KEY が設定されていません")
    exit(1)

genai.configure(api_key=api_key)

print("📋 利用可能なGeminiモデル一覧:")
print("="*60)

for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"✅ {model.name}")
        print(f"   説明: {model.display_name}")
        print()

print("="*60)
print("💡 上記のモデル名を quiz_generator_gemini.py で使えます")