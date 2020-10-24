'''
메뉴 3개, 조리기구 4개, 테이블 5개

a메뉴 조리20 식사40 = 60분 8000원
b메뉴 조리20 식사50 = 70분 15000원
c메뉴 조리30 식사60 = 90분 20000원

24시간, 최대매출 구성?
table : i, j, k, l, m
menu : a, b, c
cooker : w, x, y, z
'''
# menu
a = [20, 60, 0.8, "a"]  # 조리 20분, 테이블 60분, 가격 8000원
b = [20, 70, 1.5, "b"]
c = [30, 90, 2.0, "c"]
menu = [a, b, c]
menu_count = [0, 0, 0]  # 메뉴 주문 수 a, b, c


def random_menu():  # 메뉴 랜덤지정
    chosen_num = 0
    ran = 0
    import random
    for i in range(1):  # 1개출력
        chosen_num = random.randrange(3)  # 0, 1, 2
    ran = menu[chosen_num]
    return ran


# cooker
w = [0, 0, "w"]  # 0:조리시간, 1:메뉴
x = [0, 0, "x"]
y = [0, 0, "y"]
z = [0, 0, "z"]
cooker = [w, x, y, z]  # 가용 조리도구
cooking_cooker = [w, x, y, z]


def random_cooker():  # cooker 랜덤으로 mix
    empty = len(cooker)  # 빈 조리도구 수, 조리도구 랜덤 선택 횟수
    initial_length = len(cooker)
    ran = []  # return용
    chosen_num = 0  # 선택 된 조리도구 번호
    chosen = 0  # 선택 된 조리도구 이름
    while empty != 0:  # 빈 조리도구가 있다면
        import random
        for i in range(1):
            chosen_num = random.randrange(empty)  # 조리도구번호 선택
        # print(chosen_num)
        chosen = cooker[chosen_num]  # 번호와 조리도구 매칭
        del cooker[chosen_num]  # 가용 조리도구리스트에서 선택된 조리도구 제거
        ran.append(chosen)  # ran list에 추가
        # print("empty: {}".format(empty))
        # print(ran)
        empty -= 1
    aaa = 0
    while aaa <= (initial_length - 1):  # 가용 조리도구 리스트 원상태로 복구
        # print("empty_cooker_number : {}".format(empty_cooker_number))
        cooker.append(ran[aaa])
        aaa += 1
        # print("cooker = {}".format(cooker))
    return ran



def minus_cooker():
    if w[0] > 10:
        w[0] -= 10
    elif w[0] == 10:
        w[0] -= 10
        w[1] = 0
        cooker.append(w)

    if x[0] > 10:
        x[0] -= 10
    elif x[0] == 10:
        x[0] -= 10
        x[1] = 0
        cooker.append(x)

    if y[0] > 10:
        y[0] -= 10
    elif y[0] == 10:
        y[0] -= 10
        y[1] = 0
        cooker.append(y)

    if z[0] > 10:
        z[0] -= 10
    elif z[0] == 10:
        z[0] -= 10
        z[1] = 0
        cooker.append(z)


# table
i = [0, 0, "i", 0]  # 0:테이블시간(조리+식사), 1:메뉴, 3:가격
j = [0, 0, "j", 0]
k = [0, 0, "k", 0]
l = [0, 0, "l", 0]
m = [0, 0, "m", 0]
table = [i, j, k, l, m]  # 가용 테이블
eating_table = [i, j, k, l, m]


def random_table():  # 빈 조리도구 수 만큼 랜덤으로 선택
    empty = len(table)  # 빈 조리도구 수, 조리도구 랜덤 선택 횟수
    initial_length = len(table)
    ran = []  # return용
    chosen_num = 0  # 선택 된 조리도구 번호
    chosen = 0  # 선택 된 조리도구 이름
    while empty != 0:
        import random
        for i in range(1):
            chosen_num = random.randrange(empty)
        chosen = table[chosen_num]
        del table[chosen_num]
        ran.append(chosen)
        # print("empty: {}".format(empty))
        # print(ran)
        empty -= 1
    aaa = 0
    while aaa <= (initial_length - 1):
        table.append(ran[aaa])
        aaa += 1
    return ran



def minus_table():
    if i[0] > 10:
        i[0] -= 10
        i[3] = 0
    elif i[0] == 10:
        i[0] -= 10
        i[1] = 0
        table.append(i)

    if j[0] > 10:
        j[0] -= 10
        j[3] = 0
    elif j[0] == 10:
        j[0] -= 10
        j[1] = 0
        table.append(j)

    if k[0] > 10:
        k[0] -= 10
        k[3] = 0
    elif k[0] == 10:
        k[0] -= 10
        k[1] = 0
        table.append(k)

    if l[0] > 10:
        l[0] -= 10
        l[3] = 0
    elif l[0] == 10:
        l[0] -= 10
        l[1] = 0
        table.append(l)

    if m[0] > 10:
        m[0] -= 10
        m[3] = 0
    elif m[0] == 10:
        m[0] -= 10
        m[1] = 0
        table.append(m)


sales_record = []
cycle_number = 100000000  #반복 횟수 입력

for aaa in range(1, cycle_number + 1):

    sales = 0
    time = 0
    print("**********영업시작**********")
    print("반복 수: {}".format(aaa))
    while time <= 1500:
        #print("***time start""")  #1회 출력

        random_cooker()  # 랜덤
        random_table()

        while len(cooker) > 0 and len(table) > 0:  # 빈 테이블, 조리도구에 랜덤으로 배치
          if time >=1440:
            #print("**********주문 종료**********")  #1회 출력
            break
          random_menu()
          r_menu = random_menu()
          table[0][0] = r_menu[1]
          table[0][1] = r_menu[3]
          table[0][3] = r_menu[2]
          cooker[0][0] = r_menu[0]
          cooker[0][1] = r_menu[3]
          """
          print("len(cooker): {}".format(len(cooker)))
          print("len(table: {}".format(len(table)))
          print(cooking_cooker)
          print(eating_table)"""

          del cooker[0]
          del table[0]

        sales = sales + eating_table[0][3] + eating_table[1][3] + eating_table[2][3] + eating_table[3][3]
        minus_cooker()  # 시간 차감
        minus_table()
        """#1회 출력
        print("매출 = {}".format(sales))
        print(cooking_cooker)
        print(eating_table)

        print("빈 조리도구: {}".format(cooker))
        print("빈 테이블: {}.".format(table))"""

        time += 10
        #print("time = {} ~ {}".format(time - 10, time))  #1회 출력

    print("**********영업종료**********")
    print("총 매출: {} 만원".format(sales))
    sales_record.append(sales)
sales_record.sort()
print(sales_record)
print("반복 수: {}".format(cycle_number))
print("최대 매출: {}".format(sales_record[cycle_number - 1]))




