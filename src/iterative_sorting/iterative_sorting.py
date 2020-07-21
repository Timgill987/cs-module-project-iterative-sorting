# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr) - 1): #-1 because when only 1 elment remians, it will be already be sorted
        minVal = arr[i] #We set the minimum element to be the ith element
        smallest_index = i #And the smallest index to be the ith index

        for j in range(i+1,len(arr)): #Then we check the array from the i+1th element to the end

            if arr[j] < minVal:#If a smaller element than the minimum element is found, we re-assign the minimum element and the minimum index
                minVal = arr[j]
                smallest_index = j

        if smallest_index != i: #If smallest index has changed, i.e, a smaller  element has been found, then we swap that element with the ith element
            print(minVal,'->',arr[i])
            arr[smallest_index] = arr[i]
            arr[i] = minVal
    return arr

    # loop through n-1 elements
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # TO-DO: swap
        # Your code here



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr)-1): #-1 because when only 1 item will be left, we don't need to sort that
        print(arr)
        for j in range(len(arr)-i-1): #In every iteration of the outer loop, one number gets sorted. So the inner loop will run only for the unsorted part
            if arr[j] > arr[j+1]: #If two adjacent elements in the wrong order are found, they are swapped
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
#n( log n ) where N is maximum
def counting_sort(arr, maximum=None):
    #arr = [1,2,5,1,9,7,5,5]
    # Your code here
    if maximum is None:
        return arr
    new_arr = []
    for i in range(0, maximum + 1):
        new_arr.append(0) #new_arr = [0,0,0,0,0,0,0,0,0,0]
    for i in arr: # counts duplicate numbers in an array
        new_arr[i] += 1
    #new_arr = [0,2,1,0,0,3,0,1,0,1]
    arr =[]
    for i in range(0, maximum + 1):
        for j in range(0, new_arr[i]):
            arr.append(i)

#sort(arr) = [1,1,2,5,5,5,7,9]
    return arr
