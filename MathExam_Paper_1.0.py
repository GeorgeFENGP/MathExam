# -*- coding: cp936 -*-
# ������������ض������ļӼ��������⡣
# ������Сѧ�����ԡ�

import random
j=int(raw_input("pls input the NO. of items:"))+1
for i in range (1,j):
    digA = random.randint(1,int(20+i/10))
    digB = random.randint(1,int(20+i/10))
    digC = random.randint(1,int(20+i/10))
    if digA <= digB and digC <=40:
        suanshi= str(digA) + "+" + str(digB)+ "+" + str(digC)+"="
        keyD = digA + digB + digC
    elif digA >=digB and digC <=40:
        suanshi= str(digA) + "-" + str(digB)+ "+" + str(digC)+"="
        keyD = digA - digB + digC
    else:
        suanshi= str(digA) + "+" + str(digB)+ "="
        keyD = digA + digB
    fo1=open("����.txt","a")
    fo1.write(str(i)+". "+suanshi+"\n")
    fo1.close()
    fo2=open("��.txt","a")
    keyd=str(i)+". "+suanshi+str(keyD)+"\n"
    fo2.write(keyd)
    fo2.close()
    print i
print "DONE!"

