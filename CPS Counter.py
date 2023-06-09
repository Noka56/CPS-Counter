##########################################################################
#                             CPS Counter                                #
#                                                 Made by Noka_official  #
##########################################################################

# 库调用
from tkinter import *
from PIL import ImageTk
from PIL import Image as Img
import time

# Tkinter窗口初始化
rt = Tk()
rt.title('CPS Counter')
rt.geometry('650x520+300+200')
rt.resizable(0,0)

#图片路径
img_path = './IMG/'

# PIL读取封面图片
img_new = Img.open(img_path + 'k (0).png')
img_new = ImageTk.PhotoImage(img_new)

# Tkinter组件
pic = Label(rt, width=600, height=400, image=img_new)
pic.grid(row=1, column=0, columnspan=4)  # 背景图片

et = Entry(rt, font=('微软雅黑', 20),
           highlightcolor='sky blue', highlightthickness=1)
et.place(x=114514, y=114514)  # 输入框

cps = Label(rt, text='您的每秒点击鼠标次数:', font=('微软雅黑'))
cps.grid(row=2, column=1, columnspan=3)  # 点击次数标签

com = Label(rt, text='评价在测试完后显示', font=('微软雅黑'))
com.grid(row=3, column=1, columnspan=3)  # 评价标签

cvs = Canvas(width=215, height=22, bg='black')
cvs.grid(row=3, column=0)  # 进度条

#定义la_cng函数,用以切换语言
def la_cng():
    global en

    if en:
        txtcn(cps,'您的每秒点击鼠标次数:'+str(cs))
        txtcn(lan_cng,'English')
        if st:
            txtcn(com, '评价在测试完后显示')
            if txtcg:
                txtcn(bt,'点击')
                txtcn(cng,'测试已经开始')
            else:
                txtcn(bt,'开始')
                txtcn(cng,'更改次数(若输入内容非纯数字或大于215或为1,则自动替换为215)')
        else:
            if 0 <= cs and 4 >= cs:
                comment('树獭')
            elif cs > 4 and cs <= 6:
                comment('鸵鸟')
            elif cs > 6 and cs <= 10:
                comment('兔子')
            elif cs > 10 and cs <= 12:
                comment('猎豹')
            else:
                comment('鹰')
        en = False
    else:
        txtcn(cps,'Your CPS:'+str(cs))
        txtcn(lan_cng,'中文')
        if st:
            txtcn(com, 'Comment will be here')
            if txtcg:
                txtcn(bt,'Click!')
                txtcn(cng,'Already Start')
            else:
                txtcn(bt,'Start')
                txtcn(cng,'Change Clicking numbers(Must less than 215)')
        else:
            if 0 <= cs and 4 >= cs:
                comment('TOO slow')
            elif cs > 4 and cs <= 6:
                comment('Slow')
            elif cs > 6 and cs <= 10:
                comment('Medium')
            elif cs > 10 and cs <= 12:
                comment('Fast')
            else:
                comment('VERY fast')
        en = True

#文字切换
def txtcn(module,text):
    module.configure(text=text)
    module.text = text

# 定义cag函数,用以更换点击次数
def cag():
    et.grid(row=0, column=0, columnspan=4)
    cng.place(x=1919180, y=1919180)

# 定义Counter函数,用以计时
def counter():
    global time1, min1, h1
    time1 = time.localtime().tm_sec
    min1 = time.localtime().tm_min
    h1 = time.localtime().tm_hour

# 定义Comment函数,用以输出评论
def comment(text):
    com.configure(text=text)
    com.text = text

#定义lan_check函数,用以识别语种
def lan_check(module,cn,eng):
    global en

    if en:
        txtcn(module,eng)
    else:
        txtcn(module,cn)

# 定义Change函数,用以
# 1.切换图片
# 2.计算CPS
# 3.主控制
def change():
    # 定义全局变量
    global st, img_name, se, mi, add, e_num, cs, txtcg

    #内容语言切换初始化
    txtcg  = True

    # 重置进度条
    cvs.delete('all')

    # 图片索引切换
    img_name += 1

    # 获取输入框内值
    e_num = et.get()

    # 改变输入框与按钮位置
    et.place(x=114514, y=114514)
    cng.place(x=1919180, y=1919180)
    # 标签代替输入框
    txt = Label(rt, font=('微软雅黑', 20))
    txt.grid(row=0, column=0, columnspan=4)
    lan_check(txt,'测试已经开始','Already Start') #语言检测
    # 检测输入内容
    if e_num == '':
        e_num = 215  # 默认值
    else:
        if e_num.isdigit():
            pass
        else:
            e_num = 215

        e_num = int(e_num)

        if e_num > 215:  # 数字检测
            e_num = 215
        elif e_num == 1:
            e_num = 215
    if img_name < e_num + 1:
        if st:
            # 变量赋值
            conti = 1

            # 切换按钮文字
            lan_check(bt,'点击','Click!')

            # 进度条动效
            add += 215/e_num
            for i in range(100):
                cvs.create_rectangle(0, 0, str(add), 22, width=2, fill='gray')

            if img_name == 1:
                # 调用counter模块
                counter()
            elif img_name == e_num:
                # CPS计算
                time2 = time.localtime().tm_sec
                min2 = time.localtime().tm_min
                h2 = time.localtime().tm_hour
                se, mi, ho = min2-min1, time2-time1, h2-h1
                st = False
                cs = int((e_num/(ho * 360 + se * 60 + mi))*100) / 100

                # 输出CPS
                lan_check(cps,'您的每秒点击鼠标次数:'+str(cs),'Your cps:'+str(cs))

                # 评价输出
                if en:
                    if 0 <= cs and 4 >= cs:
                        comment('TOO slow')
                    elif cs > 4 and cs <= 6:
                        comment('Slow')
                    elif cs > 6 and cs <= 10:
                        comment('Medium')
                    elif cs > 10 and cs <= 12:
                        comment('Fast')
                    else:
                        comment('VERY fast')
                else:
                    if 0 <= cs and 4 >= cs:
                        comment('树獭')
                    elif cs > 4 and cs <= 6:
                        comment('鸵鸟')
                    elif cs > 6 and cs <= 10:
                        comment('兔子')
                    elif cs > 10 and cs <= 12:
                        comment('猎豹')
                    else:
                        comment('鹰')

            # 读取图片
            img1 = Img.open(img_path + 'k (' + str(img_name) + ').png')
            img1 = ImageTk.PhotoImage(img1)

            # 刷新图片
            pic.configure(image=img1)
            pic.Image = img1
    else:
        # 重置图片索引
        img_name = 1


# 变量初始赋值
txtcg = False
img_name = 0
c_num = 0
conti = 0
st = True
add = 0
en = False
cs = 0

# 按钮组件定义
bt = Button(rt, font=('微软雅黑'), text='开始', command=change)
bt.grid(row=2, column=0)  # 开始按钮

cng = Button(rt, text='更改次数(若输入内容非纯数字或大于215或为1,则自动替换为215)',
             font=('微软雅黑', 13), width=50, command=cag)
cng.grid(row=0, column=0, columnspan=3)  # 更改次数按钮

lan_cng = Button(rt, font=('微软雅黑',13),text=('English'),command=la_cng)
lan_cng.grid(row=0,column=3) # 语言切换按钮 

rt.mainloop()