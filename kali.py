
a=0
j={}
s=str(input("pls enter the word :"))
i=int(input("pls give us the index of the letter :"))
while i>=len(s):
    i=int(input("pls give us index less than from the max lenth of the word you have enter right now :"))

for n in s:
    j[a]=n
    a+=1
p=j[i].swapcase()
print(p)


