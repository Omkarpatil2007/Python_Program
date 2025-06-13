no=int(input("enter the no:"))
rev_no=0

while no!=0:
    digit=no%10
    rev_no=rev_no*10+digit
    no//=10
print(rev_no)
    
