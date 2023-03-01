x=list(input('enter a string :').split())
y=list(input('enter the substring :').split())
count=0
z=len(x)
for i in range(z):
    if y in x:
        count+=1
print(x)
print(y)
print(count)