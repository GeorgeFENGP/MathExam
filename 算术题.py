# -*- coding: cp936 -*-
# �������ṩ�����ڵļӼ������ԡ�
# 20�����⣬ÿ��5�֣�����100�֡�
# ������Сѧ�����ԡ�

import random
score=0
print "��ӭ�μӱ�����ѧ���ԡ�"
print "���ο��Թ�����20���Ӽ������⣬ÿ��5�֡�"
print "��¼��𰸺����س��鿴�𰸡�"
print "******* ******* *******"
print
for i in range (1,21):
    digA = random.randint(1,100)
    digB = random.randint(1,100)
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
        print "�ش���ȷ����5�֡�"        
    else:
        print "�ش���󣬱��ⲻ�÷֡�"
        print "��ȷ���ǣ�" + suanshi + str(keyD)
    print "��ǰ�÷��ۼƣ�" + str(score) + "��"
    print
print 
print "���������"
print "�����ο��Ե÷�Ϊ" + str(score) + "�֡�"
if score>=90:
    print "���ֺܰ����ٽ�������"
elif score >= 60:
    print "�����пɣ�����Ŭ����"
else:
    print "���ֽϲ�´μ���Ŷ��"

iQuit = raw_input("�뵥���س��˳����ԡ�")
print 
