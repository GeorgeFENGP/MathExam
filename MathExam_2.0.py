# -*- coding: cp936 -*-
# �������ṩ30���ڵļӼ������ԡ�
# 40�����⣬ÿ��2.5�֣�����100�֡�
# ������Сѧ�����ԡ�

import random
import time
import datetime
ver=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
score=0

print "��ӭ�μӱ�����ѧ���ԡ�"
print "���ο��Թ�����40���Ӽ������⣬ÿ��5�֡�"
print "��¼��𰸺����س��鿴�𰸡�"
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
    print "����" + str(i) + "��" +suanshi
    keyInput = int(raw_input("������𰸣�"))
    if keyInput == keyD:
        score=score+5
        pingfen="��ȷ"
        print "�ش���ȷ����5�֡�"        
    else:
        pingfen="����" 
        print "�ش���󣬱��ⲻ�÷֡�"
        print "��ȷ���ǣ�" + suanshi + str(keyD)
    print "��ǰ�÷��ۼƣ�" + str(score) + "��"
    fo=open("������ҵ"+str(ver)+".txt",'a')
    fo.write(str(i)+"."+suanshi+str(keyInput)+"  ->  "+pingfen+"\n")
    fo.close()
    print
print 
print "���������"
print "�����ο��Ե÷�Ϊ" + str(score) + "�֡�"
fo=open("������ҵ"+str(ver)+".txt",'a')
fo.write("�����ο��Ե÷�Ϊ" + str(score) + "�֣���������Ϊ100�֡�")
fo.close()
if score>=90:
    print "���ֺܰ����ٽ�������"
elif score >= 60:
    print "�����пɣ�����Ŭ����"
else:
    print "���ֽϲ�´μ���Ŷ��"

iQuit = raw_input("�뵥���س��˳����ԡ�")
print 
