import requests
from bs4 import BeautifulSoup

# 定义要爬取的URL
url = "http://127.0.0.1:8000/index.html"

try:
    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功
    
    # 设置正确的编码，解决中文匹配问题
    response.encoding = response.apparent_encoding
    
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 找到所有的section
    sections = soup.find_all('div', class_='section')
    
    # 遍历sections，找到包含"技能专长"的section
    for section in sections:
        section_title = section.find('h2', class_='section-title')
        if section_title and '技能专长' in section_title.text:
            # 找到section下的p标签，获取技能内容
            skill_content = section.find('p').text.strip()
            print("=== 爬取结果 ===")
            print("网页URL:", url)
            print("技能专长:", skill_content)
            break
    else:
        print("未找到'技能专长'部分")
        
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
except Exception as e:
    print(f"解析失败: {e}")
