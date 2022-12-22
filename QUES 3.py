#input list
list1=list(map(int,input("ENTER THE NUMBERS SEPARATED BY SPACE TO GET THEIR SQUARE:").split()))
#blank list
list2=[]
for e in list1:
    t=(e,e*e)
    list2.append(t)
# Printing the final result
print("LIST CONTAINING (n,n^2) IS:")
print(list2)
