import random
import time
# binary search helps to search the ordered list faster then serching it randdomly

# the main target of this project is to prove that binary search is faster then naive search

# naive search : scan entire list and ask if it is equal to the target
# if yes ,return the index
# if no, then return -1

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search uses divide and conquer//
# we will leverage the fact that our list is sorted
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low: #if target is not in list it return this
        return -1

    # example l=[1,2,4,5,6]   #should return 3
    midpoint = (low+high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:  # target > l[midpoint]:
        return binary_search(l, target, midpoint + 1, high)


if __name__ == '__main__':
    # this below 4 line that has been commentted out isto check wheather  i runs right or not,normal test  to check the code

    #l = [1, 3, 5, 10, 12]
    #target = 10
    #print(naive_search(l, target))
    #print(binary_search(l, target))

    #now we are checking that even if we have huge legth we do not have to search the entire list and binary search is much faster then naive

    length = 10000
    #build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list)< length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time", (end - start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time", (end - start) / length, "seconds")




