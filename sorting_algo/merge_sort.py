import sys

def merge_sort(ls): # main function, initiate the merge sort process
    ls = merge_sort_helper(ls, 0, len(ls) - 1)
    return ls
def merge_sort_helper(ls, first, last): # every time the function will be called when to mafke the list devide into 2 parts, 
    # untill each sub list contains only one element
    if first < last:
        middle = (first + last)//2
        print(f"middle: {middle}, firts: {first}, last: {last}")
        merge_sort_helper(ls, first, middle) # sort the left half of the lsit
        merge_sort_helper(ls, middle+1, last) # sort the right half of the list 
        ls = merge(ls, first, middle, last) # after both halves are sorted, than the merge function is called to combine them into single sorted list.
        return ls

def merge(ls, first, middle, last):
    left = ls[first:middle+1] # exclusive to middle, middle - 1
    right = ls[middle+1:last+1] # last + 1 , otherwise last values will be lost

    left.append(sys.maxsize)
    right.append(sys.maxsize)

    i = j = 0

    for k in range(first, last + 1):
        if left[i] <= right[j]:
            ls[k] = left[i]
            i += 1
        else:
            ls[k] = right[j]
            j += 1
    return ls


user_input = input().split()
int_list = [int(i) for i in user_input]
sorted_list = merge_sort(int_list)
print(sorted_list)





