def selection_sort(ls):
    for i in range(0, len(ls) - 1):
        minindex = i
        for j in range(i+1, len(ls)):
            if ls[j] < ls[minindex]:
                minindex = j
        if minindex != i:
            ls[i], ls[minindex] = ls[minindex], ls[i]

    
    return ls

print('Enetr input list')
input_lst = input().split()
int_list = [int(i) for i in input_lst]
sorted_list = selection_sort(int_list)
print(f"The givem list is {int_list} and the sorted list is {sorted_list}")