str="Hello madam , I am a strudent heheheheh and haha"
a=str.split(" ")
# Rstr=a.reverse()
print(a)
temp = len(a[0])
for i in a:
    aa=i
    b=aa[::-1]
    # print(i)
    # print(b)
    if(i==b):
        # print(i," Is a Pallindr0me...")
        if temp<=len(i):
            temp=len(i)
        # print(temp)
for i in a:
    b=i[::-1]
    if temp==len(i):
        if(b==i):
            print("'",i,"'"," is the largest Pallindrome in the given sentence...")