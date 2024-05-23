"""
# _No.1_html

A=int(input())

count=0 #サイコロを振るべき回数
distance=A-1 #ゴールまでのマス数

if distance/6 == 0:  #ゴールまでのマス数が6の倍数であれば6で割った商が答えになる。
    count=distance // 6
    print(count)
else:
    count=(distance // 6) + (distance % 6) #ゴールまでのマス数が6の倍数でないなら剰余を加算しなければならない。
    print(count)
"""



"""
# _No.2_html

#石をひっくり返す関数
def turn_over_stones(stones, position, stone):
    #それぞれの反対の色の石の情報を保存
    if stone == 'B':
        opposite = 'W'
    else:
        opposite = 'B'

    # positionの左側の石をひっくり返す
    if position > 0 and stones[position - 1] == opposite:
        i = position - 1
        while i >= 0 and stones[i] == opposite:
            i -= 1
        if i >= 0 and stones[i] == stone:
            for j in range(i + 1, position):
                stones[j] = stone

    # positionの右側の石をひっくり返す
    if position < len(stones) - 1 and stones[position + 1] == opposite:
        i = position + 1
        while i < len(stones) and stones[i] == opposite:
            i += 1
        if i < len(stones) and stones[i] == stone:
            for j in range(position + 1, i):
                stones[j] = stone

#標準入力
S = input()

# 初期状態
stones = ['B', 'W']  

#ターンによってbool値を切り替える。黒のターンはtrueにする
turn = True  

for choice in S:
    if turn:
        stone = 'B'
    else:
        stone = 'W'

    if choice == 'R':  # 右を選択
        stones.append(stone)
        position = len(stones) - 1 #石を置く位置
    else:  # 左を選択
        stones.insert(0, stone)
        position = 0

    # 石の位置に従って石をひっくり返す
    turn_over_stones(stones, position, stone)

    # 次に置く石の色を反転
    turn = not turn

print(stones.count('B'), stones.count('W'))
"""




"""
# _No.3_html

x=input()

x_list = list(x) 

x_list_sorted = sorted(x_list)

# 先頭に0が含まれていた場合に0以外の最小の数との入れ替えを行う。
for i in range(len(x_list_sorted)):
    if x_list_sorted[i] != '0':
        x_list_sorted[0], x_list_sorted[i] = x_list_sorted[i], x_list_sorted[0]
        break

#リストを文字列に直す。
min=''.join(x_list_sorted)
print(min)
"""