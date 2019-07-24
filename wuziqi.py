#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:unflypig
# datetime:2019/6/27 0027 19:42
# software: PyCharm
SIZE = 10#设置棋盘大小
run_flag = True#循环运行标志位
qipan_array = []

#初始化棋盘函数
def init_board(size):
    global qipan_array
    qipan_array = [['+']*SIZE]
    for i in range(size + 1):
        qipan_array += [['+']*size]
    return 0
#检测输入坐标是否合法,若合法则返回坐标
def coordinate_legal(str):
    import re
    xy_str = re.match('\d,\d', str)
    if xy_str:
        #合法返回坐标
        x, y = xy_str.group().split(",")
        return int(x), int(y)
    else:
        #非法返回False
        return False
#刷新棋盘函数
def refresh_board(size):
    for i in range(size):
        for j in range(size):
            print(qipan_array[i][j], end="")
        print()
    return 0
#在用户输入的坐标设置棋子
def set_chessmen(x, y, user_name):
    global  qipan_array
    if qipan_array[x][y] != '+':
        #该坐标已落子
        xy_str = input("该坐标已存在棋子!\n请重新输入您要落子的坐标，格式为x,y:")
    if user_name == "black":
        user_symble = "●"
    elif user_name == "white":
        user_symble = "○"
    qipan_array[x][y] = user_symble
    return True
#判断是否获胜(是否有连续相同5个棋子)
def judge_win(user_name):
    global  SIZE
    global qipan_array
    if user_name == "black":
        user_symble = "●"
    elif user_name == "white":
        user_symble = "○"
    #判断每个横行是否有连续五个子
    for row in range(0,SIZE):
        col = 0#列索引
        counter = 0#用于计数连续的棋子
        while col < SIZE and counter < 5:
            if(qipan_array[row][col] == user_symble):
                #发现棋子
                counter += 1#棋子计数加1
            elif(qipan_array[row][col] != user_symble):
                #该位置未发现对应棋子
                counter = 0#连续棋子个数清零
            col += 1#下一列
        if counter == 5:#发现5个连续相同的棋子
            return True
    #判断每个竖列是否有连续五个子
    for col in range(0,SIZE):
        row = 0#列索引
        counter = 0#用于计数连续的棋子
        while row < SIZE and counter < 5:
            if(qipan_array[row][col] == user_symble):
                #发现棋子
                counter += 1#棋子计数加1
            elif(qipan_array[row][col] != user_symble):
                #该位置未发现对应棋子
                counter = 0#连续棋子个数清零
            row += 1#下一列
        if counter == 5:#发现5个连续相同的棋子
            return True
    #检测每个/方向是否有5个连续相同棋子
    counter = 0
    for y in range(SIZE):
        x = 0
        #横纵坐标必须在合法范围内
        while(x < SIZE and x >= 0) and (y < SIZE and y >= 0):
            if counter == 5:
                return True
            if (str(qipan_array[x][y]) == str(user_symble)):
                counter += 1
                x += 1
                y -= 1
            else:
                break
    #检测每个\方向是否有5个连续相同棋子
    counter = 0
    for y in range(SIZE):
        x = 0
        #横纵坐标必须在合法范围内
        while(x < SIZE and x >= 0) and (y < SIZE and y >= 0):
            if counter == 5:
                return True
            if (str(qipan_array[x][y]) == str(user_symble)):
                counter += 1
                x += 1
                y += 1
            else:
                break

init_board(SIZE)
xy_str = input("游戏开始，请黑方输入您要落子的坐标，格式为x,y:")
step_conter = 0#记录一共走了多少步
while run_flag and xy_str != "exit":
    if coordinate_legal(xy_str):
        #输入坐标合法
        x, y = coordinate_legal(xy_str)
        if qipan_array[x][y] != '+':
            #该坐标已落子
            xy_str = input("该坐标已存在棋子!\n请重新输入您要落子的坐标，格式为x,y:")
            continue
        #根据步数判断当前是黑子下还是白子下
        if ((step_conter % 2)  ==  0):
            chess_color = "white"
        else:
            chess_color = "black"
        #将用户输入的坐标改为“棋子”
        set_chessmen(x, y, chess_color)
        #刷新棋盘
        refresh_board(SIZE)
        if judge_win("white"):
            print("白方胜利!")
            break
        elif judge_win("black"):
            print("黑方胜利！")
            break
        else:
            #若当前无用户胜利则由另一方落子
            if ((step_conter % 2)  ==  0):
                xy_str = input("游戏继续，请白方输入您要落子的坐标，格式为x,y:")
            else:
                xy_str = input("游戏继续，请黑方输入您要落子的坐标，格式为x,y:")
        step_conter +=1
    else:
        #输入坐标非法
        xy_str = input("坐标输入错误，请输入正确的坐标，格式为x,y:")
print("游戏结束！")
