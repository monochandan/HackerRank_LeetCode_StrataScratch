def bubble_sort(ls):
    #c = 0
    for i in range(0, len(ls) - 1): # tracks the number of passes. This loop tracks 
        # the number of passes. After each pass, the largest element "bubbles up" to its correct position, 
        # so the next pass doesn't need to check the already sorted part of the list.
        for j in range(0, len(ls)-1-i): ## till ith element is already sorted in the most right position
            # for example  if i = 1 and length of the list is 6, then 6th and 5th element are already sorted, 
            # so we will check only till 4th element.

            # if c == len(ls) - 1:
            # break

            if ls[j] > ls[j+1]: # checking if left one is greater than the right one
                ls[j], ls[j+1] = ls[j+1], ls[j]
            # c += 1   

    return ls

user_input = input().split()
int_lst = [int(i)for i in user_input]
sorted_list = bubble_sort(int_lst)
print(sorted_list)
