# data_loader.py
import json
import random

class CompanyDataLoader:
    """企業データを読み込むクラス"""
    
    def __init__(self, json_path='company_data.json'):
        """
        初期化
        json_path: JSONファイルのパス
        """
        self.json_path = json_path
        self.companies = self._load_data()
    
    def _load_data(self):
        """JSONファイルを読み込む"""
        try:
            with open(self.json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                companies = data['companies']
                print(f"✅ データの読み込みが完了しました。{len(companies)}社のデータを読み込みました。")
                return companies
        except FileNotFoundError:
            print(f"❌ エラー: {self.json_path} が見つかりません")
            return []
        except json.JSONDecodeError as e:
            print(f"❌ エラー: {self.json_path} のJSON形式が間違っています")
            print(f"   詳細: {e}")
            return []
        except Exception as e:
            print(f"❌ 予期しないエラー: {e}")
            return []
    
    def get_random_company(self):
        """ランダムに1社取得"""
        if not self.companies:
            return None
        company = random.choice(self.companies)
        print(f"🎲 ランダムに選ばれた企業: {company['name']}")
        return company
    
    def get_company_by_code(self, code):
        """証券コードで企業を検索"""
        for company in self.companies:
            if company['code'] == code:
                print(f"🔍 企業コード '{code}' で見つかりました: {company['name']}")
                return company
        print(f"❌ 企業コード '{code}' の企業が見つかりませんでした。")
        return None
    
    def get_all_companies(self):
        """全企業を取得"""
        return self.companies
    
    def display_company_info(self, company):
        """企業情報を見やすく表示"""
        if not company:
            print("❌ 企業データがありません")
            return
        
        print("\n" + "="*50)
        print(f"🏢 企業名: {company['name']}")
        print(f"🔢 企業コード: {company['code']}")
        print(f"🏭 業界: {company['industry']}")
        
        financial = company['financial_data']
        print(f"💰 売上高: {financial['revenue']:,}百万円")
        print(f"📈 営業利益: {financial['operating_profit']:,}百万円")
        print(f"💵 純利益: {financial['net_income']:,}百万円")
        print(f"📊 ROE: {financial['roe']}%")
        print(f"🏦 自己資本比率: {financial['equity_ratio']}%")
        print("="*50)

# このファイルを直接実行した時だけ動く部分
if __name__ == '__main__':
    print("🎯 企業データローダーのテスト開始")
    print("-" * 40)
    
    # データローダーを作成
    loader = CompanyDataLoader()
    
    if not loader.get_all_companies():
        print("❌ データが読み込めませんでした")
        exit(1)
    
    # 1️⃣ 全企業データの取得
    print("\n1️⃣ 全企業データの取得:")
    all_companies = loader.get_all_companies()
    print(f"📊 全{len(all_companies)}社のデータを取得しました。")
    for company in all_companies:
        print(f"   - {company['name']} ({company['code']})")
    
    # 2️⃣ ランダムに1社取得
    print("\n2️⃣ ランダムに1社取得:")
    company = loader.get_random_company()
    if company:
        loader.display_company_info(company)
    
    # 3️⃣ 証券コードで検索
    print("\n3️⃣ 証券コードで検索:")
    toyota = loader.get_company_by_code('7203')
    if toyota:
        loader.display_company_info(toyota)
    
    # 4️⃣ 存在しないコードで検索
    print("\n4️⃣ 存在しないコードで検索:")
    loader.get_company_by_code('9999')
    
    print("\n✅ テスト完了！")


