#내장된 라이브러리이기 때문에 별도 설치x
import smtplib 
#작성하고 싶은 Email 내용을 MIME타입으로 변환시킴
from email.message import EmailMessage
import imghdr
#정규표현식 사용
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  #gmail지정 포트번호

def sendEmail(addr):
    reg="^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다. ")
    else:
        print("유효한 이메일 주소가 아닙니다. ")


message = EmailMessage() #메시지 통 생성
message.set_content("코드라이언") #메일의 본문

#헤더부분 지정
message["Subject"] = "이것은 제목입니다. "
message["From"] = "####@gmail.com"
message["To"] = "####@gmail.com"

# open() - codelion.png / rb
#image = open("codelion.png","rb")
with open("codelion.png","rb") as image:
    image_file = image.read()

#파일명과 실제 파일 데이터
image_type = imghdr.what('codelion',image_file)
message.add_attachment(image_file,maintype='image', subtype=image_type)

#SMTP는 서버를 연결하는 함수(서버주소, 포트번호)
smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT) 
#print (smtp)
smtp.login("####@gmail.com", "####")

# 메일을 보내는 sendEmail 함수를 호출해서 실행해보기
sendEmail("####@gmail.com")
smtp.quit()