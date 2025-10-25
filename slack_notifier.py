# slack_notifier.py
import os
import requests
import json
from dotenv import load_dotenv

class SlackNotifier:
    """Slackに通知を送信するクラス"""
    
    def __init__(self):
        load_dotenv()
        self.webhook_url = os.getenv('SLACK_WEBHOOK_URL')
        
        if not self.webhook_url:
            raise ValueError("❌ SLACK_WEBHOOK_URLが設定されていません")
        
        print("✅ Slack Webhook URL読み込み完了")
    
    def format_quiz_message(self, quiz):
        """クイズをSlack用にフォーマット"""
        company = quiz['company']
        
        # Slackのブロック形式でリッチな表示
        blocks = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "📊 今日の財務分析クイズ",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*🏢 企業名:*\n{company['name']}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*🏭 業界:*\n{company['industry']}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*📅 決算期:*\n{company['fiscal_period']}"
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*💰 財務サマリー*"
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*売上高:*\n{company['financial_data']['revenue']:,}百万円"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*営業利益:*\n{company['financial_data']['operating_profit']:,}百万円"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*ROE:*\n{company['financial_data']['roe']}%"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*自己資本比率:*\n{company['financial_data']['equity_ratio']}%"
                    }
                ]
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*📝 問題*\n{quiz['question']}"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*💡 ヒント*\n{quiz['hint']}"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "考えてからスレッドで解答を見てください 👇"
                    }
                ]
            }
        ]
        
        return {"blocks": blocks}
    
    def format_answer_message(self, quiz):
        """解答をSlack用にフォーマット"""
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*✅ 模範解答*"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": quiz['answer']
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*📚 解説*"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": quiz['explanation']
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "🤖 Powered by Google Gemini AI"
                    }
                ]
            }
        ]
        
        return {"blocks": blocks}
    
    def send_quiz(self, quiz):
        """クイズをSlackに送信"""
        try:
            # 問題を送信
            message = self.format_quiz_message(quiz)
            response = requests.post(
                self.webhook_url,
                data=json.dumps(message),
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code == 200:
                print("✅ クイズをSlackに投稿しました")
                return True
            else:
                print(f"❌ 投稿失敗: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ エラー: {e}")
            return False
    
    def send_answer(self, quiz):
        """解答をSlackに送信（スレッドで）"""
        try:
            message = self.format_answer_message(quiz)
            response = requests.post(
                self.webhook_url,
                data=json.dumps(message),
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code == 200:
                print("✅ 解答をSlackに投稿しました")
                return True
            else:
                print(f"❌ 投稿失敗: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ エラー: {e}")
            return False

# テスト実行
if __name__ == '__main__':
    print("🧪 Slack通知テスト")
    print("="*70)
    
    # 簡単なテストメッセージ
    load_dotenv()
    webhook_url = os.getenv('SLACK_WEBHOOK_URL')
    
    if not webhook_url:
        print("❌ SLACK_WEBHOOK_URLが設定されていません")
        exit(1)
    
    test_message = {
        "text": "🎉 Slack連携テスト成功！財務分析クイズBotが正常に動作しています。"
    }
    
    response = requests.post(
        webhook_url,
        data=json.dumps(test_message),
        headers={'Content-Type': 'application/json'}
    )
    
    if response.status_code == 200:
        print("✅ テストメッセージ送信成功！Slackを確認してください。")
    else:
        print(f"❌ 送信失敗: {response.status_code}")