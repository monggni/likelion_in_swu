#크롤링시 필요한 라이브러리 불러오기
from bs4 import BeautifulSoup #통에 정보를 담아주는 기능
import requests
import pandas as pd
from openpyxl import Workbook

#검색어 입력
search = input("검색할 키워드를 입력해주세요:")
#검색할 페이지 입력
page = int(input("크롤링할 페이지를 입력해주세요. ex)1(숫자만입력):")) # ex)1 =1페이지,2=2페이지...
print("크롤링할 페이지: ",page,"페이지")   
#start수를 1, 11, 21, 31 ...만들어 주는 함수
page_num = 0
number=1

if page == 1:
    page_num =1
elif page == 0:
    page_num =1
else:
    page_num = page+9*(page-1)
    
#url 생성
url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(page_num)
#print("생성url: ",url)

# ConnectionError방지
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/100.0.48496.75" }

#html불러오기
original_html = requests.get(url, headers=headers)
html = BeautifulSoup(original_html.text, "html.parser")

# 검색결과
articles = html.select("div.group_news > ul.list_news > li div.news_area > a")

# 검색된 기사의 갯수
print(len(articles),"개의 기사가 검색됨.")

#뉴스기사 제목 가져오기
news_title = []
num = []
for i in articles:
    news_title.append(i.attrs['title'])
    num.append(number)
    number+=1
#print(news_title)

wb = Workbook()
sheet = wb.active
sheet.title = "news_name"
col_names = ['번호', '제목']
for seq, name in enumerate(col_names):
    sheet.cell(row = 1, column =  seq+1, value=name)

#리스트를 데이터프레임으로 변환
df = pd.DataFrame({"번호":num, "제목" :news_title})

#df=pd.read_excel('news_title.xlsx')
news = pd.ExcelWriter('news_title.xlsx')
df.to_excel(news)
news.save()
print(df)


#https://www.delftstack.com/ko/howto/python-pandas/export-pandas-dataframe-to-excel-file/