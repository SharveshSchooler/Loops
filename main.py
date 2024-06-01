def perfect(a,b):
    if b==1:
        l=[]
        c=0
        for i in range (1,a):
            if a%i==0:
                c=c+i
                print(c)
def amstrong(a,b):
    if b==2:
        s = str(a)
        l = len(s)
        c = 0
        u = 0
        z = a
        while a > 0:
            n = a % 10
            c = n ** l
            u = u + c
            a = a // 10
            if u == z:
                print(u, "Amstrong")
def fibo(a,b):
    if b==3:
        u = 0
        b = 1
        print(u)
        print(b)
        c = 0
        while a > c:
            c = u + b
            print(c)
            u = b
            b = c
def prime(a,b):
    if b==4:
        for i in range(2,a):
          if  a%i!=0:
             print(a)
             break
def comp(a,b):
    if b==5:
        for i in range(2,a):
          if  a%i==0:
             print(a)
             break
a=int(input("ENTER YOUR INT VALUES :"))
b=int(input("ENTER YOUR CHOICE [1/2/3/4/5] :"))
if b==1:
    perfect(a,b)
elif b==2:
    amstrong(a,b)
elif b==3:
    fibo(a,b)
elif b==4:
    prime(a,b)
elif b==5:
    comp(a,b)
else:
    print("INVALID INPUT ☹️")
