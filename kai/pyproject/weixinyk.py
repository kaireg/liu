#!/usr/bin/env python
#liu coding:utf-8 liu

import poplib    #接收，读取邮件
import smtplib   #发送邮件
from email.header import decode_header  #编码解码
from email.mime.text import MIMEText    #设置邮件内容
import email


#以发送为目的的登录，使用SMTP进行登录
sent = smtplib.SMTP('smtp.sina.cn')         #登录的邮箱的smtp服务器地址
sent.login('13125179586@sina.cn','2627932.kai')     #所需要登录的邮箱名和邮箱密码

#设置发送邮件的内容，收件人，发件人，主题，内容等
to = ['13125179586@sina.cn']    #创建一个变量to，将需要发送的邮件人的地址赋值给他
content = MIMEText('0:帮助 1:关机 2:重启 3:放歌 4:关歌 5:打开浏览器 6:关闭浏览器')          #邮件内容
content['Subject'] = 'liu'                  #邮件主题
content['From'] = '13125179586@sina.cn'    #发件人
content['To'] = ','.join(to)                 #收件人，这里是读取变量to，获取收件人地址，
sent.sendmail('13125179586@sina.cn',to,content.as_string())    #实现邮件发送，发送人，接收人，邮件内容等
sent.close()        #关闭邮件

#读取邮件
read = poplib.POP3('pop.sina.cn')       #登录邮件的pop服务器地址
read.user('13125179586@sina.cn')       #登录邮件的用户名
read.pass_('2627932.kai')               #登录邮件的密码
tongji = read.stat()                      #将获取到的返回值赋值给变量
str = read.top(tongji[0],0)               #获取返回的内容的第0行
str2 = []                                 #创建一个空的列表，承载需要的内容
for x in str[1]:                         #将获取到的内容，通过for循环，将其添加到str2
    str2.append(x)
    # try:                                  #解码，编码过程
    #     str2.append(x.decode('utf-8'))
    # except:
    #     try:
    #         str2.append(x.decode('gbk'))
    #     except:
    #         str2.append(x.decode('big5'))
msg = email.message_from_string('\n'.join(str2))        #将获取到的内容，进行重新编排
biaoti = decode_header(msg['Subject'])                  #获取到邮件的主题
biaoti = biaoti[0][0]                                    #获取邮件的主题名称
print biaoti
jishu = tongji[0]
print jishu