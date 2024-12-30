# swap method (ls[j], ls[j+1] = ls[j+1], ls[j]) is costly
def insertion_sort(ls):
    for i in range(1, len(ls)): # iterating through the list from 1 to n
        j = i - 1 # initializing the value of j to i-1

        # while loop
        # while ls[j] > ls[j+1] and j >= 0: #
        #     ls[j], ls[j+1] = ls[j+1], ls[j]
        #     j -= 1 ## j will go to left for example 5,4,3,2,1

        # fo rloop
        for j in range(i-1, -1, -1): # wrong for j in range(i-1, 0, -1) # to include 0th index we have chynge the range till -1, otherwise 0th index will not be sorted
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
                j -= 1
            else:
                break
    return ls

## shifting method
def insertion(ls):
    for i in range(1, len(ls)):
        #print('i: ',i)
        temp = ls[i]
        #print('temp: ',temp)
        #temp = ls[i] # storing the ith value in the temp var
        for j in range(i-1, -1, -1):
            if ls[j] > temp:
                #print(f"in if statement: {ls[j]} greater than {temp}")
                ls[j+1] = ls[j] # j+1 = i
                ls[j] = temp
                #print(ls)

            else:
                #print(f"in else statement, in the position {j+1}, temp value {temp} is storing")
                #ls[j+1] = temp
                #print(ls)
                break
    return ls
input = input().split()
int_list = [int(x) for x in input] ## convertin to integer value
print('Given list is:', int_list)
#print(int_list)
sorted_list = insertion(int_list)
print('After sorted the list is:', sorted_list)