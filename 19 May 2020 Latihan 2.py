

# 1,2,5,3,4,8,7,6,12,45,33,98,54,7,6,45,34,6,12,3,5,66,5,2,3,65,77,5,4,33,2,88,7,88,73,1
list = [7,5,8,9,6,6,4,7,1,2,3,6]
result = ''
resultsum = 0
list6 = []
print('ENTER THE FOLLOWING NUMBER TO RUN')
print('[1] TO GET ASCENDING LIST')
print('[2] TO GET DESCENDING LIST')
print('[3] TO GET THE MAXIMUM NUMBER IN THE LIST')
print('[4] TO GET THE MINIMUM NUMBER IN THE LIST')
print('[5] TO GET THE MODE FROM THE LIST')
print('[6] TO GET THE MEDIAN FROM THE LIST')
print('[7] TO GET AVERAGE NUMBER FROM THE LIST')
print('[8] TO GET THE Q1 OF THE LIST')
print('[9] TO GET THE Q3 OF THE LIST')
print('[10] TO GET OUTLIERS FROM THE LIST')
print('[11] TO TERMINATE PROGRAM')
userinput = int(input('ENTER COMMAND:  '))


if userinput == 1:
    for i in range(0,len(list)):
        # print(i)
        for j in range(i+1,len(list)):
            # print(j)
            if (list[i] > list[j]): #<<============= kalau list i lebih gede
                result = list[i] #<============= dia swap tempat
                # print(i)
                list[i] = list[j]#<============= sama fungsi swap
                # print(i)
                list[j] = result#<============== masih fungsi swap
                # print(j)
    for i in range(0,len(list)):
        print(list[i], end=',')
elif userinput == 2: #<<============= untuk nyari list descending NOTE:SOAL NO 1B
    for i in range(0,len(list)):
        # print(i)
        for j in range(i+1,len(list)):
            # print(j)
            if (list[i] < list[j]): #<========= sama cuma arahnya dibalik aja
                # print(i)
                result = list[i]
                # print(i)
                list[i] = list[j]
                # print(i)
                list[j] = result
                # print(j)
    for i in range(0,len(list)):
        print(list[i], end=',')
elif userinput == 3: #<<============= untuk max number
    for i in range(0,len(list)):
        # print(i)
        for j in range(i+1,len(list)):
            # print(j)
            if (list[i] > list[j]):
                # print(i)
                result = list[i]
                # print(i)
                list[i] = list[j]
                # print(i)
                list[j] = result
                # print(j)
    for i in range(-1,0): #<<============= karena fungsi nyusun list udah jadi
        print(list)
        print(list[i]) #<<============= tinggal cari angka paling terakhir di list NOTE:SOAL NO 2A
elif userinput == 4:
    for i in range(0,len(list)):
        # print(i)
        for j in range(i+1,len(list)):
            # print(j)
            if (list[i] > list[j]):
                # print(i)
                result = list[i]
                # print(i)
                list[i] = list[j]
                # print(i)
                list[j] = result
                # print(j)
    for i in range(0,1): #<<============= karena fungsi nyusun list udah jadi
        print(list)
        print(list[i]) #<<============= tinggal cari angka paling awal di list NOTE:SOAL NO 2B
elif userinput == 5:
    for i in range(0,len(list)):
        # print(i)
        for j in range(i+1,len(list)):
            # print(j)
            if (list[i] > list[j]): #<<============= kalau list i lebih gede
                result = list[i] #<============= dia swap tempat
                # print(i)
                list[i] = list[j]#<============= sama fungsi swap
                # print(i)
                list[j] = result#<============== masih fungsi swap
                # print(j)
    for i in range(0,len(list)):
        tolist = (list[i])
        list6.append(tolist)
        def mode(y):
            most_count = (0,0)
            for x in y:
                appear = y.count(x)
                if appear > most_count[0]:
                    most_count = (appear,x)
            return most_count[1]
    print(list6)        
    print(mode(list6))
elif userinput == 6:
    for i in range(0,len(list)):
        # print(i)
        for j in range(i+1,len(list)):
            # print(j)
            if (list[i] > list[j]): #<<============= kalau list i lebih gede
                result = list[i] #<============= dia swap tempat
                # print(i)
                list[i] = list[j]#<============= sama fungsi swap
                # print(i)
                list[j] = result#<============== masih fungsi swap
                # print(j)
    for i in range(0,len(list)):
        tolist = (list[i])
        list6.append(tolist) # <=== titik dimana list6 udah ngurut dari kecil ke besar
    
        if len(list6) % 2 == 0:
            median1 = list6[len(list6)//2]
            median2 = list6[len(list6)//2 - 1]
            median = (median1 + median2)/2
        else:
            median = list6[len(list6)//2]
    print(list6)
    print(median)
elif userinput == 7:
    for i in range(0,len(list)):
        # print(i)
        for j in range(i+1,len(list)):
            # print(j)
            if (list[i] > list[j]): #<<============= kalau list i lebih gede
                result = list[i] #<============= dia swap tempat
                # print(i)
                list[i] = list[j]#<============= sama fungsi swap
                # print(i)
                list[j] = result#<============== masih fungsi swap
                # print(j)
    for i in range(0,len(list)):
        tolist = (list[i])
        list6.append(tolist)
    for i in range(0, len(list)):
        resultsum = resultsum + list[i]
        mean = resultsum / len(list)
    print(list6)
    print(mean)
elif userinput == 8:
    for i in range(0,len(list)):
        # print(i)
        for j in range(i+1,len(list)):
            # print(j)
            if (list[i] > list[j]): #<<============= kalau list i lebih gede
                result = list[i] #<============= dia swap tempat
                # print(i)
                list[i] = list[j]#<============= sama fungsi swap
                # print(i)
                list[j] = result#<============== masih fungsi swap
                # print(j)
    for i in range(0,len(list)):
        tolist = (list[i])
        list6.append(tolist) # <=== titik dimana list6 udah ngurut dari kecil ke besar
    del1 = int(len(list6)//2)
    del2 = int(len(list6))
    median1 = list6.copy()
    del median1[del1:del2]
    if len(median1) % 2 == 0:
        firstq = median1[len(median1)//2]
        secondq = median1[len(median1)//2 - 1]
        q1 = (firstq + secondq)/2
    else:
        q1 = median1[len(median1)//2]
    print(median1)
    print(list6)
    print(q1)
elif userinput == 9:
    for i in range(0,len(list)):
        # print(i)
        for j in range(i+1,len(list)):
            # print(j)
            if (list[i] > list[j]): #<<============= kalau list i lebih gede
                result = list[i] #<============= dia swap tempat
                # print(i)
                list[i] = list[j]#<============= sama fungsi swap
                # print(i)
                list[j] = result#<============== masih fungsi swap
                # print(j)
    for i in range(0,len(list)):
        tolist = (list[i])
        list6.append(tolist) # <=== titik dimana list6 udah ngurut dari kecil ke besar
    del1 = 0
    del2 = int(len(list6)//2)
    median2 = list6.copy()
    del median2[del1:del2]
    if len(median2) % 2 == 0:
        firstq = median2[len(median2)//2]
        secondq = median2[len(median2)//2 - 1]
        q3 = (firstq + secondq)/2
    else:
        q3 = median2[len(median2)//2]
    print(median2)
    print(list6)
    print(q3)
# elif userinput == 10:
# elif userinput == 11:
#     break
# else:
#     print('incorrect input')