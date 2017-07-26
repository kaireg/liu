#/usr/bin/env python
#coding:utf-8

'''
2.1

  p36
'''


# b = 'liu'
# c = 'kai'
#
# print '%s' %b,c

'''
2.2
#!/usr/bin/env python
1 + 2 *4
'''

'''
a.计算这个计算式的值
b.啥也不会输出
c.没有输出
d.解释器会实时显示输出，而ide不会
e.给一个输出
'''
# print (1 + 2 * 4)


'''
2.3  四则运算
'''
# print 5 + 3   #加
# print 5 - 3   #减
# print 5 * 3   #乘
# print 5 / 3   #传统除法
# print 5 // 3  #浮点除法（四舍五入）
# print 5 % 3   #取余
# print 5 ** 3  #乘方


'''
2.4 raw_input函数的使用
'''
# a
# inp = raw_input('请输入一个字符串：')
# print inp

# b
# inp = raw_input('请输入一个数字：')
# inp = int(inp)
# print type(inp)
# print inp


'''
2.5 循环和数字
'''

# a  while循环
# i = 0
# while  i <= 10:
#     print i
#     i += 1

# b   for循环
# for i in range(0,11):
#     print i


'''
2.6 条件判断
'''

# inp = raw_input('请你输入一个自然数：')
# inp = int(inp)
# if inp == 0:
#     print "你输入的数是0"
# elif inp > 0:
#     print "你输入的是正数"
# elif inp < 0 :
#     print "你输入的是负数"

'''
2.7 循环和字串
'''

# inp = raw_input('请输入一串字符串：')
#
# for i in inp:
#     print i
#
# i = 0
# while i < len(inp):
#     print inp[i]
#     i += 1


'''
2.8  2.9 循环的操作符
'''

# list = [1,2,3,8,9]
# tuple = (4,5,6,7,0)
#
# i = 0
# j = 0
# while i <len(list):
#     j += list[i]
#     i +=1
# print j
#
# y = 0
# for x in tuple:
#     y += x
#
# print y
#
# print y/float(len(tuple))


'''
2.10 带循环和条件判断的用户输入的
'''
#
# while 1:
#     inp = int(raw_input("请输入一个1-100的数:"))
#     if inp == 10:
#         print "nice，你中奖了"
#         break
#     else:
#         print "错了！在猜猜看!"
#

'''
2.11 带文本菜单的程序
'''
# list = [1,2,3,8,9]
# j = 0
# print "1:取5个数的和"
# print "2:取5个数的平均值"
# print "x:退出"
#
# while 1:
#     inp = raw_input("请输入你想执行的编号:")
#     if inp == 'x':
#         print "谢谢使用！"
#         break
#     elif int(inp) == 1:
#         for i in list:
#             j += i
#         print j
#     elif int(inp) == 2:
#         for i in list:
#             j += i
#         print j/float(len(list))


'''
2.15 元素排序
'''


# a, b, c = input("Enter (a, b, c): ")
# if b>a:
#     t=a
#     a=b
#     b=t
# if c>a:
#     t=a
#     a=c
#     c=t
# if c>b:
#     t=b
#     b=c
#     c=t
# print a,b,c