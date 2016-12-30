import time
def mergesortandcount(array):
    mid = len(array) // 2
    if len(array)<=1:
        return 0;

    leftHalf = array[:mid]
    rightHalf = array[mid:]
    leftCount = mergesortandcount(leftHalf)
    rightCount = mergesortandcount(rightHalf)
    array2 = []
    count = merge(leftHalf,rightHalf,array)

    return count+leftCount+rightCount

def merge(leftHalf,rightHalf,array):
#merging Algorithm
    i=j=k=count=0
    while i<len(leftHalf) and j<len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            array[k] = leftHalf[i]
            i = i+1
        else:
            array[k] = rightHalf[j]
            j = j+1
            count = count+len(leftHalf) -i
        k = k+1

    while i<len(leftHalf):
        array[k] = leftHalf[i]
        i = i+1
        k = k+1
    while j<len(rightHalf):
        array[k] = rightHalf[j]
        j = j+1
        k = k+1

    return count

start_time = time.time()
FileName = "/Users/Dinesh_Singh/Desktop/IntegerArray.txt"

f1 = open(FileName)
array = []
with open(FileName) as f:
    c = f.read().splitlines() # c is a list having all the number
#print(len(c))

for j in c:
    array.append(int(j))

totalInversions = mergesortandcount(array)
end_time = time.time()
print("total number of inversions is "+str(totalInversions))

file = open("/Users/Dinesh_Singh/Desktop/Output.txt","w")
i=0
while i<len(array):
    file.write(str(array[i]))
    file.write("\n")
    i = i+1

file.close()
timeTaken = end_time - start_time
print("Total time taken for execution is "+str(timeTaken))


