# 使用方法
# 1.安装python3.4以上版本，并配置环境变量（目前有装3.9遇到坑的，我个人用的3.7.6）
# 教程：https://www.runoob.com/python3/python3-install.html
# 2.安装依赖包
# 方法：在cmd中（win+R  输入cmd  回车）输入
# pip install pyperclip 回车
# pip install xlrd 回车
# pip install pyautogui==0.9.50 回车
# pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple 回车
# pip install pillow 回车
# 这几步如果哪步没成功，请自行百度 如 pip install opencv-python失败
# 3.把每一步要操作的图标、区域截图保存至本文件夹  png格式（注意如果同屏有多个相同图标，回默认找到最左上的一个，因此怎么截图，截多大的区域，是个学问，如输入框只截中间空白部分肯定是不行的，宗旨就是“唯一”）
# 4.在cmd.csv 配置每一步的指令，如指令类型1234  对应的内容填截图文件名（别用中文）
# 5.偏移量默认0即可 点击位置非图片定位位置时使用
# 6.查找位置图片在屏幕中的坐标因为基于mac开发我做了比例调整（positionCD.x/2） windows 可以对应调整

import pyautogui
import time
import pyperclip
import csv
from pynput.mouse import Button, Controller



#点击
def mouseClick(clickEvent,clickButton,positionImg,x,y,long=None):
    loopTime = 0
    while True:
        #查找位置图片在屏幕中的坐标
        positionCD = pyautogui.locateCenterOnScreen(positionImg,confidence=0.9)
        if positionCD is not None:
            print(positionCD)
            pyautogui.moveTo(positionCD.x/2+float(x),positionCD.y/2+float(y))
            loopTime = 0
            if long is None:
                pyautogui.click(positionCD.x/2+float(x),positionCD.y/2+float(y),clicks=clickEvent,interval=0.2,duration=0.2,button=clickButton)
            else:
                pyautogui.mouseDown()
                time.sleep(4)
                pyautogui.mouseUp()
            break
        print("未匹配到位置,正在重试")
        time.sleep(0.3)
        if loopTime>5:
            print("未匹配到位置,跳过")
            break
        loopTime = loopTime +1

#任务
def mainWork(cmdType,cmdValue,x,y):
    #1代表单击左键
    if cmdType == 1:
        mouseClick(1,"left",cmdValue,x,y)
        print("单击左键",cmdValue)
    #2代表双击左键
    elif cmdType == 2:
        mouseClick(2,"left",cmdValue,x,y)
        print("双击左键",cmdValue)
    #3代表右键
    elif cmdType == 3:
        mouseClick(1,"right",cmdValue,x,y)
        print("右键",cmdValue)
    #4代表输入
    elif cmdType == 4:
        pyperclip.copy(cmdValue)
        pyautogui.hotkey('ctrl','v')
        pyautogui.hotkey('command','v')
        time.sleep(0.5)
        print("输入:",cmdValue)
    #5代表等待
    elif cmdType == 5:
        time.sleep(int(cmdValue))
        print("等待",cmdValue,"秒")
    #6代表滚轮
    elif cmdType == 6:
        pyautogui.scroll(int(cmdValue))
        print("滚轮滑动",int(cmdValue),"距离")
    #7代表长按
    elif cmdType == 7:
        mouseClick(1,"left",cmdValue,x,y,1)
        print("长按",cmdValue,"5秒")

def dealCmd(cmd):
    for k in cmd:
        row = cmd[k]
        print(row)
        mainWork(int(row[0]),row[1],row[2],row[3])

if __name__ == '__main__':
    file = 'cmd.csv'

    f = open(file)
    f_csv = csv.reader(f)
    #跳过第一行的标题
    next(f_csv)
    cmdList = {}
    i = 0 
    isWhile = 0
    for row in f_csv:
        print(row)
        if int(row[0]) == 0:
            isWhile = 1
        cmdList[i] = row
        i = i+1
    dealCmd(cmdList)
    while isWhile == 1:
        dealCmd(cmdList)

    

