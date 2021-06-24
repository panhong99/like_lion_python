print("Talyor 스튜디오 입니다.")
print("야외 촬영 , 바디프로필 , 내부촬영 , 증명사진 , 웨딩촬영 등이 있습니다.")
print("각 촬영의 가격은 메뉴에 기재되어 있으니 메뉴를 읽어보시고 예약부탁드립니다.")
print("다른 손님과의 날짜가 겹칠 경우 고지를 해드리며 촬영가능한 날짜를 전송해드립니다.")
print("타 문의 사항은 글을 남겨주시면 빠른시일내에 피드백을 해드리겠습니다.")
print()

Menu = dict(zip([1,2,3,4,5] , ["증명사진" , "내부촬영" , "야외촬영" , "바디프로필" , "웨딩촬영"]))
Price = dict(zip(["증명사진" , "내부촬영" , "야외촬영" , "바디프로필" , "웨딩촬영"] , [20000 , 80000 , 200000 , 500000 , 800000]))
Option = dict(zip(["메이크업" , "헤어" , "의상대여"] , [30000 , 100000 , 150000]))
while True:
    Choice = int(input("어떤 촬영을 생각하고 오셨나요? : "))
    if Menu[Choice]:
        print(Menu[Choice] , "을 선택하셨습니다.")
        if Choice == 1:
            print(Menu[Choice] , "을 선택하셨습니다. 가격은 " , Price[Menu[Choice]] , "원 입니다.")
            print("증명사진은 따로 촬영장내에서 가능한 메이크업이나 헤어서비스가 제공되지 않습니다. 촬영장내 기본적인 드라이기와 헤어용품들은 있으니 참고하시길 바랍니다.")
            print("가급적 단정한 복장으로 상의는 흰티나 검은티를 추천드립니다.")
            print()
        elif Choice == 2:
            print(Menu[Choice] , "을 선택하셨습니다. 가격은 " , Price[Menu[Choice]] , "원 입니다.")
            print("내부촬영은 개인 촬영과 단체 촬영이 있습니다. 세부적으로 어떤 촬영을 원하시는지 선택해 주시길 바랍니다.")
            Subject = input("원하시는 촬영을 입력해주세요. : ")
            if Subject == "개인촬영":
                print("개인 촬영의 가격은 그대로이고 옵션을 원하신다면 선택해주시기 바랍니다.")
                print("옵션을 원하신다면 옵션을 선택해주시기 바랍니다.")
                Want = input("옵션을 선택하시겠습니까?? : ")
                if Want: 
                    print("옵션을 선택하셨고 추가가격은" , Option[Want] , "이며 총 지불해주셔야 하는 금액은" , Price[Menu[Choice]] + Option[Want] , "원 입니다. 꼭 금액을 확인해주시기 바랍니다.")
                else:
                    print("옵션선택은 없으시기 때문에 촬영은 기존의 선택하신대로 진행하도록 하겠습니다.")
            elif Subject == "단체촬영":
                print("단체촬영은 명수당 20000원이 추가가 됩니다.")
                Human_number = int(input(""))
                total_price_number2 = Price[Menu[Choice]] + (20000 * Human_number)
                print("총 촬영하시는 고객님은 " , Human_number , "분 이시고 총 가격은 " , total_price_number2 , "입니다." )
                print("옵션을 원하신다면 옵션을 선택해주시기 바랍니다.")
                Want = input("옵션을 선택하시겠습니까?? : ")
                if Want: 
                    print("옵션을 선택하셨고 추가가격은" , Option[Want] , "이며 총 지불해주셔야 하는 금액은" , total_price_number2 + Option[Want] , "원 입니다. 꼭 금액을 확인해주시기 바랍니다.")
                else:
                    print("옵션선택은 없으시기 때문에 촬영은 기존의 선택하신대로 진행하도록 하겠습니다.")
            print()
    break