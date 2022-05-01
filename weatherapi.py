import requests
import json

city = "Seoul"
apikey = "###############################"

lang = "kr"

#units - metric 단위 화씨에서 도씨로 변경

api = f"""http://api.openweathermap.org/data/2.5/\
weather?q={city}&appid={apikey}&lang={lang}&units=metric"""

#fstring을 사용하면 문자열 안에 우리가 원하는 변수를 넣을 수 있음(링크를 또 만들 필요 없이 변수만 넣어주면 됨)
#api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

print(api)
result = requests.get(api)
#print(result.text)

data = json.loads(result.text)

#print(type(result.text))
#print(type(data))

print(data["name"],"의 날씨입니다.")
#리스트 안에 딕셔너리, 첫번째 인덱스에 있는 딕셔너리 사용
print("날씨는 ",data["weather"][0]["main"],"입니다.") #######틀림
print("날씨는 ",data["weather"][0]["description"],"입니다.")

print("현재 온도는 ",data["main"]["temp"],"입니다.")
print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")

# 최저 기온 : main - temp_min
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
# 최고 기온 : main - temp_max
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
# 습도 : main - humidity
print("습도는 ",data["main"]["humidity"],"입니다.")
# 기압 : main - pressure
print("기압은 ",data["main"]["pressure"],"입니다.")
# 풍향 : wind - deg
print("풍향은 ",data["wind"]["deg"],"입니다.")
# 풍속 : wind - speed
print("풍속은 ",data["wind"]["speed"],"입니다.")