t_atn=input("Enter total attendence: ")
a_atn=input("Enter classes you have attended: ")
tclas=float(t_atn)
aclas=float(a_atn)
prcnt=(aclas/tclas)*100
pr=float(prcnt)
if prcnt == 75:
    print("You'r attenence is on borer")
    print("You can skip 0 class")
elif prcnt>75:
    cnt=0
    print("You are above standard")
    while prcnt>=75:
        prcnt=(aclas/tclas)*100
        tclas=tclas+1
        cnt=cnt+1
    print(cnt)
elif prcnt<75:
    print("Please attend classes")
