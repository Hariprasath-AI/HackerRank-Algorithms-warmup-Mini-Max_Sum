# Please read the problem statement in readme.md file
# Here we are not going to perform the adding by n number of times
# The logic is to claculate the Minimum sum and Maximum sum
# First, sort the given array. 
# After sorting, from the add from 1st element of the array till the last before element i.e., n-1th element. This will be the Minimum sum.
# Next for Maximum sum, add from the 2nd element of the array till last element i.e., nth element.
# Just make our code as simple as possible... 

def sort(arr):
    new_arr = arr
    n = len(new_arr)

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(new_arr) - 1):
            if new_arr[i] > new_arr[i + 1]:
                swapped = True
                new_arr[i], new_arr[i + 1] = new_arr[i + 1], new_arr[i]
    
    return new_arr

def miniMax_sum(arr):
    sorted_arr = sort(arr)
    n = len(sorted_arr)
    Min = 0 
    for i in range(0, n - 1):
        Min += sorted_arr[i]
    
    Max = 0
    for i in range(1, n):
        Max += sorted_arr[i]
    
    print(Min, Max)

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    miniMax_sum(arr)

