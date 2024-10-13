def selection_sort_algorithm(arr): #O(nkare)
    n = len(arr)

    for i in range(0,n-1):
        min_idx = i

        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:

                min_idx = j

        arr[i],arr[min_idx] =arr[min_idx],arr[i]  

array = [2,6,5,1,3,4]
selection_sort_algorithm(array)
print(array)

#insertion sort algorithm
def insertion_sort_algo(arr):

    for i in range(1,len(arr)):
        j = i
        while arr[j-1] > arr[j] and j> 0 :
            arr[j-1],arr[j] = arr[j],arr[j-1] 
            j -= 1


insertion_sort_algo(array)
print(array)
 