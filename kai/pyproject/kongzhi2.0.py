#!/usr/bin/env python
#  QAQ coding:utf-8 QAQ


import time
import os
import win32api
import sys
import poplib    #接收，读取邮件
import smtplib   #发送邮件
from email.header import decode_header  #编码解码
from email.mime.text import MIMEText    #设置邮件内容
import email


def get_sub(name):
        # 以发送为目的的登录，使用SMTP进行登录
        sent = smtplib.SMTP('smtp.sina.cn')  # 登录的邮箱的smtp服务器地址
        sent.login('13125179586@sina.cn', '2627932.kai')  # 所需要登录的邮箱名和邮箱密码

        # 设置发送邮件的内容，收件人，发件人，主题，内容等
        to = ['13125179586@sina.cn']  # 创建一个变量to，将需要发送的邮件人的地址赋值给他
        content = MIMEText('o:help \n a:shutdown \nb:reboot \nc:open the music '
                           '\nd:close the music \ne:open the browser'
                           '\nf:close the browser')  # 邮件内容
        content['Subject'] = name  # 邮件主题
        content['From'] = '13125179586@sina.cn'  # 发件人
        content['To'] = ','.join(to)  # 收件人，这里是读取变量to，获取收件人地址，
        sent.sendmail('13125179586@sina.cn', to, content.as_string())  # 实现邮件发送，发送人，接收人，邮件内容等
        sent.close()  # 关闭邮件

def popmail():
    # 读取邮件
    read = poplib.POP3('pop.sina.cn')  # 登录邮件的pop服务器地址
    read.user('13125179586@sina.cn')  # 登录邮件的用户名
    read.pass_('2627932.kai')  # 登录邮件的密码
    tongji = read.stat()  # 将获取到的返回值赋值给变量
    str = read.top(tongji[0], 0)  # 获取返回的内容的第0行
    str2 = []  # 创建一个空的列表，承载需要的内容
    for x in str[1]:  # 将获取到的内容，通过for循环，将其添加到str2
        str2.append(x)
        # try:                                  #解码，编码过程
        #     str2.append(x.decode('utf-8'))
        # except:
        #     try:
        #         str2.append(x.decode('gbk'))
        #     except:
        #         str2.append(x.decode('big5'))
    msg = email.message_from_string('\n'.join(str2))  # 将获取到的内容，进行重新编排
    biaoti = decode_header(msg['Subject'])  # 获取到邮件的主题
    jishu = tongji[0]           #获取邮箱邮件总数量
    biaoti = biaoti[0][0]       #获取邮件的主题名称
    if biaoti == "a":
        return 1,jishu
    elif biaoti == "b":
        return 2,jishu
    elif biaoti == "c":
        return 3,jishu
    elif biaoti == "d":
        return 4,jishu
    elif biaoti == "e":
        return 5,jishu
    elif biaoti == "f":
        return 6,jishu
    elif biaoti == "h":
        return 0,jishu
    else:
        return 10,jishu

def func(popl):

    if popl == 1:
        os.system('shutdown -r')
    if popl == 2:
        os.system('shutdown -s -t 20 -c "Will shut down your computer and 20 seconds, please be prepared!" -f')
    if popl == 3:
        win32api.ShellExecute(0, 'open', 'D:\Program Files (x86)\music\cloudmusic.exe', '', '', 1)
    if popl == 4:
        os.system('taskkill /F /IM cloudmusic.exe')
    if popl == 5:
        win32api.ShellExecute(0, 'open', 'https://www.douyu.com/', '', '', 1)
    if popl == 6:
        os.system('taskkill /F /IM chrome.exe')
    else:
        pass

if __name__ == '__main__':              #程序从这里开始
    get_sub('this is help!')
    time.sleep(2)
    pdz = popmail()[1]
    print "这是初始值 %s " % pdz
    while True:
        time.sleep(2)
        try:
            if pdz == popmail()[1]:
                continue
            elif popmail()[0] == 0:
                get_sub("please see the help")
                pdz = popmail()[1]
                continue
            else:
                print func(popmail()[0])
                pdz = popmail()[1]
                print pdz
                continue
        except:
            continue



