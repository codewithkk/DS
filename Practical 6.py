list1 = [45,52,78,35,69,87,12,6,8,17,96]
print("List = ",list1)
n = len(list1)
def bubbleSort():
    print("Bubble Sorting")
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if list1[j] > list1[j+1] : 
                list1[j], list1[j+1] = list1[j+1], list1[j] 
    print(list1)

def SelectionSort():
	print("Selection Sorting")
	for i in range(n):
		for j in range(i):
			if list1[i]<list1[j]:
				list1[i],list1[j] = list1[j],list1[i]
	print(list1)
	
def InsertionSort():
    print("Insertion Sorting")
    for i in range(1, n): 
        c = list1[i] 
        j = i-1
        while j >=0 and c < list1[j] : 
                list1[j+1] = list1[j] 
                j -= 1
        list1[j+1] = c
    print(list1)

inp = input("Enter (B) for Bubble Sort, (S) for elsection Sort and (I) for Insertion Sort \n Enter here:")
if inp=="B" or inp=="b":
	bubbleSort()
elif inp=="S" or inp=="s":
	SelectionSort()
elif inp=="I" or inp=="i":
	InsertionSort()
else:
	print("Invalid input")
