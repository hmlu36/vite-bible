import requests
from bs4 import BeautifulSoup
import json
import gzip
import os
import re

# 基本 URL
base_url = "https://biblics.com/zh-Hant/聖經/聖經當代譯本修訂版"

# 書卷和章節列表（需自行補充完整）
# 書卷和章節列表（需自行補充完整）
books = {
    "舊約全書": [
        "創世記", "出埃及記", "利未記", "民數記", "申命記", "約書亞記", "士師記", "路得記", 
        "撒母耳記上", "撒母耳記下", "列王紀上", "列王紀下", "歷代志上", "歷代志下", 
        "以斯拉記", "尼希米記", "以斯帖記", "約伯記", "詩篇", "箴言", "傳道書", "雅歌", 
        "以賽亞書", "耶利米書", "耶利米哀歌", "以西結書", "但以理書", "何西阿書", "約珥書", 
        "阿摩司書", "俄巴底亞書", "約拿書", "彌迦書", "那鴻書", "哈巴谷書", "西番雅書", 
        "哈該書", "撒迦利亞書", "瑪拉基書"
    ],
    "新約全書": [
        "馬太福音", "馬可福音", "路加福音", "約翰福音", "使徒行傳", "羅馬書", "哥林多前書", 
        "哥林多後書", "加拉太書", "以弗所書", "腓立比書", "歌羅西書", "帖撒羅尼迦前書", 
        "帖撒羅尼迦後書", "提摩太前書", "提摩太後書", "提多書", "腓利門書", "希伯來書", 
        "雅各書", "彼得前書", "彼得後書", "約翰一書", "約翰二書", "約翰三書", "猶大書", "啟示錄"
    ]
}

chapters = {
    "創世記": 50,
    "出埃及記": 40,
    "利未記": 27,
    "民數記": 36,
    "申命記": 34,
    "約書亞記": 24,
    "士師記": 21,
    "路得記": 4,
    "撒母耳記上": 31,
    "撒母耳記下": 24,
    "列王紀上": 22,
    "列王紀下": 25,
    "歷代志上": 29,
    "歷代志下": 36,
    "以斯拉記": 10,
    "尼希米記": 13,
    "以斯帖記": 10,
    "約伯記": 42,
    "詩篇": 150,
    "箴言": 31,
    "傳道書": 12,
    "雅歌": 8,
    "以賽亞書": 66,
    "耶利米書": 52,
    "耶利米哀歌": 5,
    "以西結書": 48,
    "但以理書": 12,
    "何西阿書": 14,
    "約珥書": 3,
    "阿摩司書": 9,
    "俄巴底亞書": 1,
    "約拿書": 4,
    "彌迦書": 7,
    "那鴻書": 3,
    "哈巴谷書": 3,
    "西番雅書": 3,
    "哈該書": 2,
    "撒迦利亞書": 14,
    "瑪拉基書": 4,
    "馬太福音": 28,
    "馬可福音": 16,
    "路加福音": 24,
    "約翰福音": 21,
    "使徒行傳": 28,
    "羅馬書": 16,
    "哥林多前書": 16,
    "哥林多後書": 13,
    "加拉太書": 6,
    "以弗所書": 6,
    "腓立比書": 4,
    "歌羅西書": 4,
    "帖撒羅尼迦前書": 5,
    "帖撒羅尼迦後書": 3,
    "提摩太前書": 6,
    "提摩太後書": 4,
    "提多書": 3,
    "腓利門書": 1,
    "希伯來書": 13,
    "雅各書": 5,
    "彼得前書": 5,
    "彼得後書": 3,
    "約翰一書": 5,
    "約翰二書": 1,
    "約翰三書": 1,
    "猶大書": 1,
    "啟示錄": 22
}


# 存儲結果
bible_data = []


# 存儲結果
def write_to_gz(data):
    """
    將每次抓取到的資料直接壓縮並寫入 JSON 文件。
    :param data: 要寫入的資料（字典格式）。
    """
    try:
        # 將資料轉換為 JSON 字符串
        json_data = json.dumps(data, ensure_ascii=False)
        
        # 使用 gzip 壓縮 JSON 字符串
        compressed_data = gzip.compress(json_data.encode('utf-8'))
        
        # 以二進制模式寫入壓縮檔案
        with open("bible_data.json.gz", 'wb') as file:
            file.write(compressed_data)
            
        print("資料已成功壓縮並寫入檔案。")
    except Exception as e:
        print(f"寫入 JSON 文件時出現錯誤: {e}")

def write_to_json(data):
    """
    將每次抓取到的資料直接寫入 JSON 文件。
    :param data: 要寫入的資料（字典格式）。
    """
    try:
        # 動態生成檔案路徑
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, "../src/data/bible_ccb.json")

        # 以追加模式打開文件
        with open(json_path, 'a', encoding='utf-8') as file:
            # 將資料轉換為 JSON 字符串並寫入文件
            json.dump(bible_data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"寫入 JSON 文件時出現錯誤: {e}")
import os
import json

def load_book_abbr():
    """
    從 ../src/data/books.json 讀取書卷縮寫對應表。
    :return: 書卷名稱與縮寫的對應字典。
    """
    try:
        # 動態生成檔案路徑
        base_dir = os.path.dirname(os.path.abspath(__file__))
        book_json_path = os.path.join(base_dir, "../src/data/books.json")

        # 確認檔案是否存在
        if not os.path.exists(book_json_path):
            raise FileNotFoundError(f"檔案不存在: {book_json_path}")

        # 讀取 JSON 檔案
        with open(book_json_path, 'r', encoding='utf-8') as file:
            book_data = json.load(file)

        # 確認 JSON 資料是否為有效格式
        if not isinstance(book_data, list):
            raise ValueError("JSON 格式錯誤，應為列表格式的資料。")

        # 建立書卷名稱與縮寫的對應字典
        return {item['name']: item['abbr'] for item in book_data}
    except FileNotFoundError as e:
        print(f"檔案未找到: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON 格式錯誤: {e}")
    except Exception as e:
        print(f"讀取書卷縮寫對應表時出現錯誤: {e}")
    return {}

# 加載書卷縮寫對應表
book_abbr_map = load_book_abbr()
print(book_abbr_map)

# 儲存結果的字典
bible_data = {}

# 爬取內容
for testament, book_list in books.items():
    for book in book_list:
        for chapter in range(1, chapters[book] + 1):
            url = f"{base_url}/{testament}/{book}/{chapter}"
            print(f"正在處理：{url}")
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # 提取章節內容（需根據網頁結構調整）
                content = soup.find('div', class_='chapter-content').text.strip()
                # 將內容拆分成段落並移除多餘的換行符
                paragraphs = content.split("\n")
                cleaned_paragraphs = []
                for p in paragraphs:
                    p = p.strip()  # 移除前後空白
                    if p:  # 確保段落非空
                        # 使用正則表達式移除段落前的標號（如 "1."、"2." 等）
                        p = re.sub(r"^\d+\.\s*", "", p)
                        cleaned_paragraphs.append(p)
                
                # 使用縮寫作為 key
                abbr = book_abbr_map.get(book, book)  # 如果找不到縮寫，使用原書卷名稱
                key = f"{abbr}{chapter}"
                bible_data[key] = cleaned_paragraphs
            else:
                print(f"無法訪問 {url}")
                
write_to_json(bible_data)

print("爬取完成，已保存至 bible_data.json")
