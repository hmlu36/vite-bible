import requests
from bs4 import BeautifulSoup
import json
import time
import os
import re

class BibleComScraper:
    def __init__(self, digit, version_id="CUNPSS-神"):
        """
        初始化爬蟲
        :param version_id: 聖經版本 ID (例如: CUNPSS-神, RCUV, NCV 等)
        """
        self.base_url = "https://www.bible.com/zh-TW/bible"
        self.digit = digit
        self.version_id = version_id
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
    def get_book_info(self):
        """取得書卷資訊"""
        return {
            "GEN": {"name": "創世記", "chapters": 50},
            "EXO": {"name": "出埃及記", "chapters": 40},
            "LEV": {"name": "利未記", "chapters": 27},
            "NUM": {"name": "民數記", "chapters": 36},
            "DEU": {"name": "申命記", "chapters": 34},
            "JOS": {"name": "約書亞記", "chapters": 24},
            "JDG": {"name": "士師記", "chapters": 21},
            "RUT": {"name": "路得記", "chapters": 4},
            "1SA": {"name": "撒母耳記上", "chapters": 31},
            "2SA": {"name": "撒母耳記下", "chapters": 24},
            "1KI": {"name": "列王紀上", "chapters": 22},
            "2KI": {"name": "列王紀下", "chapters": 25},
            "1CH": {"name": "歷代志上", "chapters": 29},
            "2CH": {"name": "歷代志下", "chapters": 36},
            "EZR": {"name": "以斯拉記", "chapters": 10},
            "NEH": {"name": "尼希米記", "chapters": 13},
            "EST": {"name": "以斯帖記", "chapters": 10},
            "JOB": {"name": "約伯記", "chapters": 42},
            "PSA": {"name": "詩篇", "chapters": 150},
            "PRO": {"name": "箴言", "chapters": 31},
            "ECC": {"name": "傳道書", "chapters": 12},
            "SNG": {"name": "雅歌", "chapters": 8},
            "ISA": {"name": "以賽亞書", "chapters": 66},
            "JER": {"name": "耶利米書", "chapters": 52},
            "LAM": {"name": "耶利米哀歌", "chapters": 5},
            "EZK": {"name": "以西結書", "chapters": 48},
            "DAN": {"name": "但以理書", "chapters": 12},
            "HOS": {"name": "何西阿書", "chapters": 14},
            "JOL": {"name": "約珥書", "chapters": 3},
            "AMO": {"name": "阿摩司書", "chapters": 9},
            "OBA": {"name": "俄巴底亞書", "chapters": 1},
            "JON": {"name": "約拿書", "chapters": 4},
            "MIC": {"name": "彌迦書", "chapters": 7},
            "NAM": {"name": "那鴻書", "chapters": 3},
            "HAB": {"name": "哈巴谷書", "chapters": 3},
            "ZEP": {"name": "西番雅書", "chapters": 3},
            "HAG": {"name": "哈該書", "chapters": 2},
            "ZEC": {"name": "撒迦利亞書", "chapters": 14},
            "MAL": {"name": "瑪拉基書", "chapters": 4},
            "MAT": {"name": "馬太福音", "chapters": 28},
            "MRK": {"name": "馬可福音", "chapters": 16},
            "LUK": {"name": "路加福音", "chapters": 24},
            "JHN": {"name": "約翰福音", "chapters": 21},
            "ACT": {"name": "使徒行傳", "chapters": 28},
            "ROM": {"name": "羅馬書", "chapters": 16},
            "1CO": {"name": "哥林多前書", "chapters": 16},
            "2CO": {"name": "哥林多後書", "chapters": 13},
            "GAL": {"name": "加拉太書", "chapters": 6},
            "EPH": {"name": "以弗所書", "chapters": 6},
            "PHP": {"name": "腓立比書", "chapters": 4},
            "COL": {"name": "歌羅西書", "chapters": 4},
            "1TH": {"name": "帖撒羅尼迦前書", "chapters": 5},
            "2TH": {"name": "帖撒羅尼迦後書", "chapters": 3},
            "1TI": {"name": "提摩太前書", "chapters": 6},
            "2TI": {"name": "提摩太後書", "chapters": 4},
            "TIT": {"name": "提多書", "chapters": 3},
            "PHM": {"name": "腓利門書", "chapters": 1},
            "HEB": {"name": "希伯來書", "chapters": 13},
            "JAS": {"name": "雅各書", "chapters": 5},
            "1PE": {"name": "彼得前書", "chapters": 5},
            "2PE": {"name": "彼得後書", "chapters": 3},
            "1JN": {"name": "約翰一書", "chapters": 5},
            "2JN": {"name": "約翰二書", "chapters": 1},
            "3JN": {"name": "約翰三書", "chapters": 1},
            "JUD": {"name": "猶大書", "chapters": 1},
            "REV": {"name": "啟示錄", "chapters": 22}
        }

    def fetch_chapter(self, book_abbr, chapter):
        """
        抓取特定章節
        :param book_abbr: 書卷縮寫 (如 GEN, MAT)
        :param chapter: 章節編號
        :return: 經文列表
        """
        url = f"{self.base_url}/{self.digit}/{book_abbr}.{chapter}.{self.version_id}"
        print(f"正在抓取：{url}")
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Bible.com 的經文通常在 class 包含 'verse' 的元素中
            verses = []
            verse_elements = soup.find_all('span', class_=re.compile('verse|content'))
            
            if not verse_elements:
                # 備用方案：尋找其他可能的結構
                verse_elements = soup.find_all('p', class_=re.compile('verse|scripture'))
            
            for verse in verse_elements:
                text = verse.get_text(strip=True)
                if text and len(text) > 3:  # 過濾太短的內容
                    # 移除節號
                    text = re.sub(r'^\d+\s*', '', text)
                    verses.append(text)
            
            time.sleep(1)  # 避免請求過快
            return verses
            
        except requests.RequestException as e:
            print(f"抓取失敗 {url}: {e}")
            return []

    def scrape_all(self, output_file="bible_data.json"):
        """
        抓取所有書卷並儲存
        :param output_file: 輸出檔案名稱
        """
        books = self.get_book_info()
        bible_data = {}
        
        for book_abbr, book_info in books.items():
            book_name = book_info["name"]
            total_chapters = book_info["chapters"]
            
            print(f"\n開始抓取 {book_name} (共 {total_chapters} 章)")
            
            for chapter in range(1, total_chapters + 1):
                verses = self.fetch_chapter(book_abbr, chapter)
                
                if verses:
                    key = f"{book_abbr}{chapter}"
                    bible_data[key] = {
                        "book": book_name,
                        "chapter": chapter,
                        "verses": verses
                    }
                    print(f"✓ {book_name} 第 {chapter} 章 ({len(verses)} 節)")
                else:
                    print(f"✗ {book_name} 第 {chapter} 章抓取失敗")
        
        # 儲存 JSON
        self.save_json(bible_data, output_file)
        print(f"\n完成！已儲存至 {output_file}")

    def save_json(self, data, filename):
        """儲存為 JSON 檔案"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(base_dir, filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


# 使用範例
if __name__ == "__main__":
    # 可選版本：CUNPSS-神(和合本神版)、RCUV(和合本修訂版)、NCV(新譯本) 等
    scraper = BibleComScraper(digit="1588", version_id="AMP")
    scraper.scrape_all("bible_amp.json")