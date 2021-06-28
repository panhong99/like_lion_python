Menu = dict(zip([1,2,3,4,5] , ["증명사진" , "내부촬영" , "야외촬영" , "바디프로필" , "웨딩촬영"]))
Price = dict(zip(["증명사진" , "내부촬영" , "야외촬영" , "바디프로필" , "웨딩촬영"] , [20000 , 80000 , 200000 , 500000 , 800000]))
Option = dict(zip(["메이크업" , "헤어" , "의상대여"] , [30000 , 100000 , 150000]))

class Talyor_Studio:
    def __init__(self):
        print("Talyor 스튜디오 입니다.")
        print("야외 촬영 , 바디프로필 , 내부촬영 , 증명사진 , 웨딩촬영 등이 있습니다.")
        print("각 촬영의 가격은 메뉴에 기재되어 있으니 메뉴를 읽어보시고 예약부탁드립니다.")
        print("다른 손님과의 날짜가 겹칠 경우 고지를 해드리며 촬영가능한 날짜를 전송해드립니다.")
        print("타 문의 사항은 글을 남겨주시면 빠른시일내에 피드백을 해드리겠습니다.")
        print()
        
    def Choice(self , Choice):
        self.choice = Choice
        if Menu[Choice]:
            print(Menu[Choice] , "을 선택하셨습니다.")
            if Choice == 1:
                print(Menu[Choice] , "을 선택하셨습니다. 기본가격은 " , Price[Menu[Choice]] , "원 입니다.")
                print("증명사진은 따로 촬영장내에서 가능한 메이크업이나 헤어서비스가 제공되지 않습니다. 촬영장내 기본적인 드라이기와 헤어용품들은 있으니 참고하시길 바랍니다.")
                print("가급적 단정한 복장으로 상의는 흰티나 검은티를 추천드립니다.")
                print()
            elif Choice == 2:
                print(Menu[Choice] , "을 선택하셨습니다. 기본가격은 " , Price[Menu[Choice]] , "원 입니다.")
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
            elif Choice == 3:
                only_Subject3_Price = dict(zip(["서울"  , "인천 경기" , "충청" , "경상" , "호남" ,"제주"] , [0 , 10000 , 20000 , 30000 , 40000 , 50000]))
                print(Menu[Choice] , "을 선택하셨습니다. 기본가격은 " , Price[Menu[Choice]] , "원 입니다.")
                print("야외촬영은 날씨의 영향을 받을 수 있고 따로 날씨에 상관없이 고객님께서 촬영진행을 원하시면 따로 추가적 금액이 없이 촬영은 진행합니다.")
                print("야외촬영은 출장비가 추가가 될수가 있습니다. 가격표는 다음과 같습니다." , only_Subject3_Price )
                Place = input("지역이 어디인가요? :")
                total_price_number3 = Price[Menu[Choice]] + only_Subject3_Price[Place]
                if Place == "인천 경기":
                    print("인천경기로 출장시 가격추가는 " , only_Subject3_Price[Place] , "입니다." )
                elif Place == "충청":
                    print("충청으로 출장시 가격추가는 " , only_Subject3_Price[Place] , "입니다." )
                elif Place == "경상":
                    print("경상으로 출장시 가격추가는 " , only_Subject3_Price[Place] , "입니다." )
                elif Place == "호남":
                    print("호남으로 출장시 가격추가는 " , only_Subject3_Price[Place] , "입니다." )
                elif Place == "제주":
                    print("제주로 출장시 가격추가는 " , only_Subject3_Price[Place] , "입니다." )
                else:
                    print("서울은 따로 추가금액 있지않습니다!")
                print("야외촬영시 착용할 의상과 신발은 넉넉히 준비를 해오시기 바랍니다. 촬영이 원활하게 진행될시 추가로 컷을 더 가져갈 수 있기때문에 조금 번거롭더라도 준비를 해오시길 권장드립니다!!")
                print("야외촬영은 옵션을 추가하실시 메이크업팀이 같이 동행을 하게 됩니다. 옵션을 원하신다면 옵션을 선택해주세요.")
                Want = input("옵션을 선택하시겠습니까?? : ")
                if Want != "아니요": 
                    print("옵션을 선택하셨고 추가가격은" , Option[Want] , "이며 총 지불해주셔야 하는 금액은" , total_price_number3 + Option[Want] , "원 입니다. 꼭 금액을 확인해주시기 바랍니다.")
                elif Want == "아니요":
                    print("옵션선택은 없으시기 때문에 촬영은 기존의 선택하신대로 진행하도록 하겠습니다. 최종 결재금액은" , Price[Menu[Choice]] , "입니다.")
            elif Choice == 4:
                only_Subject4_Price = dict(zip([1,2,3] , ["보정본 추가" , "컨셉 변경" , "동반촬영"])) 
                Price_Table = dict(zip(["보정본 추가" , "컨셉 변경" , "동반촬영"] , [50000 , 20000 , 100000]))
                print(Menu[Choice] , "을 선택하셨습니다. 기본가격은 " , Price[Menu[Choice]] , "원 입니다.")
                print("바디프로필은 촬영하시는분이 어느정도의 몸을 완성해오시다면 편집으로 충분히 더 부각되고 선멸하게 근육의 조정이 가능합니다.")
                print("하지만 10년후에 가지게 될 몸을 포토샵을 만들어 달라고 요청하시는 것은 불가하니 촬영당일까지 열심히 운동을 하시고 충분히 자신감을 내비칠 수 있는 수준을 만들어 오시길 바랍니다.")
                print("프로필 촬영의 옵션을 알려드리겠습니다." , only_Subject4_Price , "입니다.")
                print("프로필 촬영은 헤어 , 메이크업 옵션과 프로필 촬영만의 옵션이 있습니다. 옵션 추가를 원하시면 옵션을 선택해주세요.")
                Want = input("헤어 메이크업 옵션을 선택하시겠습니까?? : ")
                Want2 = input("프로필 옵션은 선택하시겠습니까?")
                if Want != "아니요" and Want2 == "아니요":
                    print("옵션을 선택하셨고 추가가격은" , Option[Want] , "이며 총 지불해주셔야 하는 금액은" , Price[Menu[Choice]] + Option[Want] , "원 입니다. 꼭 금액을 확인해주시기 바랍니다.")
                elif Want == "아니요" and Want2 != "아니요":
                    total_price_number4 = Price[Menu[Choice]] + Price_Table[Want2]
                    print("옵션을 선택하셨고 추가가격은" , Price_Table[Want2] , "이며 총 지불해주셔야 하는 금액은" , total_price_number4 , "원 입니다. 꼭 금액을 확인해주시기 바랍니다.")
                elif Want != "아니요" and Want2 != "아니요":
                    total_price_number4 = Price[Menu[Choice]] + Price_Table[Want2]
                    print("기본 옵션과 프로필 옵션을 선택하셨고 추가가격은" , Option[Want] + Price_Table[Want2] , "이며 총 합금액은 " , total_price_number4 + Option[Want] , "입니다.")
            elif Choice == 5:
                Wadding_dress = dict(zip([1 , 2 , 3] , ["드레스 및 턱시도" , "한복" , "둘 다"]))
                Dress_Price = dict(zip(["드레스 및 턱시도" , "한복" , "둘 다"] , [300000 , 400000 , 700000]))
                print(Menu[Choice] , "을 선택하셨습니다. 기본가격은 " , Price[Menu[Choice]] , "원 입니다.")
                print("웨딩촬영의 경우 시간적으로 여유가 필요하므로 최소 2개월전에 예약을 부탁드립니다.")
                print("드레스와 턱시도는 촬영장에서 대여가 가능하며 신부메이크업과 헤어 또한 가능합니다. 신부메이크업과 헤어의 가격은 신랑님과 신부님 합쳐 500000원 입니다.")
                print("웨딩촬영 또한 보정본이 추가될시 추가금액이 들어가며 그에 따른 의상대여금액도 추가가 됩니다.")
                print("컨셉은 다음과 같이 있으며 컨셉 변경 및 보정추가 금액은 장당 50000원씩입니다." , Wadding_dress )
                Concept = int(input("어떤 컨셉을 하시겠어요?? : "))
                Total_Wadding_price = Price[Menu[Choice]] + Dress_Price[Wadding_dress[Concept]]
                Want_Hair_Makeup = input("헤어와 메이크업은 촬영장 내에서 받으실 건가요?? : ")
                if Want_Hair_Makeup == "네":
                    Total_Wadding_price + 500000
                elif Want_Hair_Makeup == "아니요":
                    None
                if Concept == "드레스 및 턱시도":
                    print(Wadding_dress[Concept] , "를 선택하셨습니다. 가격은" , Total_Wadding_price , "입니다!")
                elif Concept == "한복":
                    print(Wadding_dress[Concept] , "를 선택하셨습니다. 가격은" , Total_Wadding_price , "입니다!")
                elif Concept == "지유복장":
                    print("자유복장은 추가금액이 없습니다! 그리고 자유복장의 헤어 , 메이크업은 기존에 옵션에서 선택을 해주시기 바랍니다. 옵션 : " ,Option )
                elif Concept == "둘 다":
                    print("컨셉을 2가지 선택을 해주셨고 현재 이벤트 진행중이므로 최종금액에서 10%를 할인해드립니다! 그러므로 최종금액은 " , Total_Wadding_price - (Total_Wadding_price * 10), "입니다.")
                Fixed_pic = int(input("보정 장수는 몇장을 하시겠어요?? : "))
                if Fixed_pic != 0 :
                    Total_Wadding_price + (50000 * Fixed_pic)
                    print("최종 가격은 ",Total_Wadding_price + (50000 * Fixed_pic) , "입니다.")
                else:
                    print("보정 장수 추가는 선택하지 않으셨습니다. 최종 가격은" , Total_Wadding_price , "입니다.")

Client1 = Talyor_Studio()
Choice = int(input("어떤 촬영을 생각하고 오셨나요? : "))
Client1.Choice(Choice)

Client2 = Talyor_Studio()
Choice = int(input("어떤 촬영을 생각하고 오셨나요? : "))
Client2.Choice(Choice)

Client3 = Talyor_Studio()
Choice = int(input("어떤 촬영을 생각하고 오셨나요? : "))
Client3.Choice(Choice)

Client4 = Talyor_Studio()
Choice = int(input("어떤 촬영을 생각하고 오셨나요? : "))
Client4.Choice(Choice)

Client5 = Talyor_Studio()
Choice = int(input("어떤 촬영을 생각하고 오셨나요? : "))
Client5.Choice(Choice)