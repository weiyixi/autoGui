# autoGui
桌面自动化b站 自动发弹幕 + 一件三连
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
