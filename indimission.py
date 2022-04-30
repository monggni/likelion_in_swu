import random 

#딕셔너리 생성
total_dictionary ={"집밖에 나가는 것 자체가 스케줄?":"", "불금에는 북적대는 곳보단 집이지?":'',"휴대폰만 있어도 안 심심한가요?":'', 
"카톡, 문자 알림을 잘 확인하지 않나요?":'',"아무 생각이 없다. 왜냐하면 아무 생각이 없기 때문이다 라고 자주 느끼시나요?":'',
"당신은 배달앱 VIP인가요?":'', "친구와의 약속이 갑작스레 파토났을 때 아쉽다는 생각보다 오예!라는 생각이 더 자주 드나요?":''} 

def qna (name):
    #name = input("당신의 이름은?")
    print ( "=====안녕하세요" ,name, "님, 당신은 집순이 일까요?=====")
    num = int(input("=====모든 질문의 대답을 네, 아니오로 답변해주세요=====\n"  "받을 질문의 개수를 입력해주세요(최대 7개 가능): "))
    #print(num)

    sum = 0
    for i in range(0, num):
        total_list=list(total_dictionary.keys())  #딕셔너리의 키 값만 뽑아서 넣기
        print(total_list[i]) 
        answer = input("답변: ")

        if (answer=="네"):
            sum = sum +1

    percent1 = sum/num * 100
    return percent1

def your_type(percent):
    if (percent>75):
        print("당신은 집순이 입니다.")
    elif(percent>50):
        print("당신은 집을 조금 더 좋아하네요.")
    elif(percent>25):
        print("당신은 밖을 조금 더 좋아하네요.")
    else:
        print("당신은 바깥순이입니다.")

name = input("당신의 이름은?")
percent = qna(name) #반환값이 존재
your_type(percent) #반환값이 없기 때문에 호출만

