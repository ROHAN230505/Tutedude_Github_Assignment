print("Enter your Four Digit no.")
num=int(input())
d= num%10
c= (num//10)%10
b= (num//100)%10
a=(num//1000)%10
newnum= a*1000 + c*100 +b*10 + d*1
print("your nwe no. is ",newnum)
