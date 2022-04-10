total_list = []  #리스트

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question, "답변" : ""}) #딕셔너리로 만든 뒤 리스트로 추가

for i in total_list:
    print(i["질문"])   #key형태로
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer
print(total_list)