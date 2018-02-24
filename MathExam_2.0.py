# -*- coding: cp936 -*-
# 本程序提供30以内的加减法考试。
# 40道试题，每题2.5分，满分100分。
# 可用于小学生测试。

import random
import time
import datetime
ver=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
score=0

print "欢迎参加本次数学测试。"
print "本次考试共包括40道加减法试题，每题5分。"
print "请录入答案后点击回车查看答案。"
print "******* ******* *******"
print
for i in range (1,41):
    digA = random.randint(1,31)
    digB = random.randint(1,i+10)
    if digA <= digB:
        suanshi= str(digA) + "+" + str(digB)+ "="
        keyD = digA + digB
    else:
        suanshi= str(digA) + "-" + str(digB)+ "="
        keyD = digA - digB
    print "试题" + str(i) + "：" +suanshi
    keyInput = int(raw_input("请输入答案："))
    if keyInput == keyD:
        score=score+5
        pingfen="正确"
        print "回答正确！加5分。"        
    else:
        pingfen="错误" 
        print "回答错误，本题不得分。"
        print "正确答案是：" + suanshi + str(keyD)
    print "当前得分累计：" + str(score) + "分"
    fo=open("寒假作业"+str(ver)+".txt",'a')
    fo.write(str(i)+"."+suanshi+str(keyInput)+"  ->  "+pingfen+"\n")
    fo.close()
    print
print 
print "答题结束。"
print "您本次考试得分为" + str(score) + "分。"
fo=open("寒假作业"+str(ver)+".txt",'a')
fo.write("您本次考试得分为" + str(score) + "分，考试满分为100分。")
fo.close()
if score>=90:
    print "表现很棒，再接再厉！"
elif score >= 60:
    print "表现尚可，继续努力！"
else:
    print "表现较差，下次加油哦！"

iQuit = raw_input("请单击回车退出考试。")
print 
