while True:
    print("자판기 입니다.")
    pocket = 0
    while True:
        choose = int(input("금액을 입력해주세요 : "))
        money =  dict(zip([1,2,3,4,5,0] , [10000 , 5000 , 1000 , 500 , 100 , 0]))
        pocket += money[choose]
        if money[choose]:
            print("입력 금액은" , money[choose], "입니다.")
            print("누적금액은" , pocket , "입니다.")
        elif choose == 0:
            print("금액 입력이 완료되었습니다.")
            break  
    kip = [0] * 5
    while True:    
        choice = int(input("음료를 선택해주세요 : "))   
        if pocket == 0:
                print("종료.")
                break
        elif choice == 0:
                print("주문이 완료 되었습니다. 총 주문은 사이다" , kip[0] ,"개","콜라",kip[1],"개","생수",kip[2],"개","주스",kip[3],"개","커피",kip[4],"개 입니다.")
                break
        elif choice > 0:
            kip[choice-1] += kip[choice-1] + 1
    while True:
        drink = dict(zip([1,2,3,4,5] , ["사이다" , "콜라" , "생수" , "주스" , "커피"]))
        price = dict(zip(["사이다" , "콜라" , "생수" , "주스" , "커피"] , [1200 , 1100 , 700 , 1500, 1300]))
        order = price[drink[choice]]
        return_money = pocket - price[drink[choice]]
        sum = price[drink[choice]]
        up = 0
        total = 0 
        for i in range(kip):
            if i[up]:
                total += i[up] * price[drink[up+1]]
                up += 1
        만원 = 0
        오천원 = 0  
        천원 = 0
        오백원  = 0
        백원 = 0
        if drink[choice]: 
            print("선택하신 음료는" , drink[choice] , "이고 상품의 금액은" , sum, "입니다.")
            if price[drink[choice]] > pocket:
                print("돈이 부족합니다. 돈을 더 넣어주세요.")
                break
            else:
                print("잔돈은" , return_money , "입니다.")
                if return_money > 10000:
                    만원 += int(return_money / 10000)
                    return_money -= 만원 * 10000
                    오천원 += int(return_money / 5000)
                    return_money -= 오천원 * 5000
                    천원 += int(return_money / 1000)
                    return_money -= 천원 * 1000
                    오백원 += int(return_money/500)
                    return_money -= 오백원 * 500
                    백원 += int(return_money/100)
                elif return_money < 10000:
                    오천원 += int(return_money / 5000)
                    return_money -= 오천원 * 5000
                    천원 += int(return_money / 1000)
                    return_money -= 천원 * 1000
                    오백원 += int(return_money/500)
                    return_money -= 오백원 * 500
                    백원 += int(return_money/100)        
                    print("만원", 만원 ,"장" , "오천원" , 오천원 ,"장" , "천원" , 천원 , "장" , "오백원" , 오백원 , "개" , "백원" , 백원, "개")
                    break
    stop = int(input("추가 주문을 하시겠습니까?"))
    if stop == 0:
        print("감사합니다.")
        break
                    


my_dict = {"1" : 10 , "2" : 20 , "3" : 30}
for i in my_dict:
    print(i)
print()

for i in my_dict.keys():
    print(i)
print()

for i in my_dict.values():
    print(i)
print()

'''리스트를 조작하는 메서드(method)(메서드는 객체에 속한 함수를 뜻함)'''
a = [10,20,30]
a.append(500) #<= 리스트에 객체를 추가해주는 함수(항상 맨마지막 index로 추가됨)
print(a)

a = []
for i in range(10):
    a.append(i)
print(a)

a = []
for i in range(10):
    a.append((i+1)*10)
print(a)

a = []
for i in range(100):
    if i % 2 == 0:
        a.append(i)
print(a)

a = [10, 20, 30]
a.append([500 , 600])
print(a)

a = [10, 20, 30]
a.extend([500 , 600]) # <= append와 다르게 리스트의 크기를 늘려서 내용을 입력한다.
print(a)

a = [10, 20, 30]
a.insert(2, 500) # <= insert는 내가 원하는 위치에 엘리멘트를 추가할 수 있다.
print(a)         # 마지막 객체는 한칸 뒤로 밀려난다. 

a = [1,2,3]
a.insert(len(a) + 1 , (500))
print(a)

a = [10, 20, 30]
a.insert(1, [500 ,600])
print(a)

a = [10, 20, 30]
a[1:1] = [500 ,600]
print(a)

a = [10, 20, 30]
print(a.pop()) # <= pop함수는 리스트의 마지막 엘리먼트를 삭제 시켜준다.
print(a)       # <= a.pop(1) index값을 넣어주면 해당 인덱스의 값이 사라진다. 

a = [10, 20, 30]
del a[1] # <= pop함수는 리스트의 마지막 엘리먼트를 삭제 시켜준다.
print(a)       # <= a.pop(1) 

a = [10, 20, 30]
a.remove(20) # <= remove함수는 해당 내용과 일치되는 엘리먼트가 있을 경우 삭제해준다.
print(a)       # <= 내용과 일치되는것이 없다면 에러 도출

a = [10, 20, 30 , 20]
a.remove(20) # <= 삭제하고자 하는 엘리먼트가 중복되었을때는 선두를 삭제시켜준다.
print(a)     

'''스택은 Last in Firsr out (선입후출)이라는 구조를 갖는 자료구조이다.'''
'''또는 First in Last out 이런 구조도 가능하다.'''
'''========================스택 구조 설명======================================'''
a = []
a.append(10)
print(a)
a.append(20)
print(a)
a.append(30)
print(a)
a.append(40)
print(a)
a.pop()
print(a)
a.pop()
print(a)
a.pop()
print(a)
a.pop()
print(a)

a = []
for  i in range(4):
    i += 1
    a.append(i*10)
    print(a)
for i in range(4):
    print(a.pop())
'''========================================================================'''

'''큐 구조는 First in First out (선입선출)구조를 갖는 자료구조이다.'''
'''or LiLo'''
'''================================================================='''
a = []
a.append(10)
print(a)
a.append(20)
print(a)
a.append(30)
print(a)
a.append(40)
print(a)
a.pop(0)
print(a)
a.pop(0)
print(a)
a.pop(0)
print(a)
a.pop(0)
print(a)

a = []
for  i in range(4):
    i += 1
    a.append(i*10)
    print(a)
for i in range(4):
    print(a.pop(0))

'''==============================================================='''

a = [10,20,30,15,20,40]
print(a.index(20)) #<= index함수는 설정한 내용이 리스트내에서 인덱스 번호가 몇번인지 알려준다.

'''특정값에 있는 모든 index구하기'''
a = [10,20,30,40,20,50,20,30,60,70,20]
i = 0
result = []
while i < len(a):
    if 20 in a:
        x = a.index(20)
        result.append(x + i)        
        a.pop(x)
        i += 1
    else:
        break
print(result)

while 20 in a:
    idx = a.index(20)
    result.append(idx)
    a[idx] = "x"
print(a)
print(result)

for i in a:
    print(a.index(20))
    a.pop(a.index(20))
    if 20 in a:
        a.insert(a.index(20) , 0)
    else:
        break

b = []
for i in a:
    if i == 20:
        b.append(a.index(i))
        del a[a.index(i)]
        a.insert(0,1)
    else:
        continue
print(b)

result = []
while True:
    if 20 in a:
        result.append(a.index(20))
        a[a.index(20)] = "x"
    else:
        break

a = [10,20,30,40,20,50,20,30,60,70,20]

b = []
for i in range(len(a)):
    if i == a.index(20):
        b.append(i)
        a.pop(i)
        a.insert(i , 0)
print(b)

