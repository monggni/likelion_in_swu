from this import d
import time


cake_dictionary = {"딸기케이크": 6000, "초코케이크":5000, "치즈케이크":4000} #디저트 딕셔너리 생성
coffee_dictionary = {"아메리카노" :4000, "카페라떼":4500, "바닐라라떼":5500, "카푸치노":5000} #음료 딕셔너리 생성
  #총 합계?
total1 = 0
total2 = 0
cake_list = []   #케이크 주문 리스트
coffee_list = []  #커피 주문 리스트

#메뉴판 출력
print("\n카페에 오신 것을 환영합니다. (주문 중단 :'q'입력)\n")
print (cake_dictionary)
print (coffee_dictionary)


while True:
    cake = input("\n디저트를 입력해주세요 : ")
    #cakelist = cake.items()

    if (cake == "q"):
        break
  
    else:
        cake_list.append(cake)
        print("케이크가 추가되었습니다. ")

    coffee = input("\n커피를 입력해주세요 : ")
    #coffeelist = coffee.items()

    if (coffee == "q"):
        break
  
    else:
        coffee_list.append(coffee)
        print("커피가 추가되었습니다. ")

#print(cake_list)

#while 메뉴 삭제하는 기능
set_cake = set(cake_list)
set_coffee = set(coffee_list)

while True:
    #케이크 삭제
    print(set_cake, "\n")

    cake = input("삭제할 케이크를 선택하세요. : ")

    if(cake == "q"):
        break
    else:
        set_cake = set_cake - set([cake])

    print(set_cake, "\n")

    #커피 삭제
    print(set_coffee, "\n")

    coffee = input("삭제할 커피를 선택하세요. : ")

    if(coffee == "q"):
        break
    else:
        set_coffee = set_coffee - set([coffee])
        
    print(set_coffee, "\n")


#최종 장바구니
print("\n=============주문서=============\n")
print (time.strftime('%Y년 %m월 %d일 %H시 %M분 %S초', time.localtime(time.time())))

print("주문내역\n", set_cake | set_coffee)

#########
for i in list(set_cake): #리스트 명시
    total1 = total1 + cake_dictionary[i]

for j in list(set_coffee): #리스트 명시
    total2 = total2 + coffee_dictionary[j]


print ("►►►►►►►►► 총 주문하신 금액은 " , total1+total2 ,"입니다. ◅◅◅◅◅◅◅◅◅ ")
print("⁑⁑⁑⁑⁑⁑⁑⁑⁑⁑⁑⁑⁑⁑⁑ 이용해주셔서 감사합니다. ⁑⁑⁑⁑⁑⁑⁑⁑⁑⁑⁑⁑⁑⁑⁑")


    


