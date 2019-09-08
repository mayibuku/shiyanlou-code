for a in range(1,101): 
    if a>=7 and a%7==0:
        continue
    elif int(str(a)[0])==7:
        continue
    elif a>=10 and int(str(a)[1])==7:
        continue
    print(a)

