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


 #merge sort algorithm

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge
        i = 0 #to keep leftmost element on the left array
        j = 0 #to keep leftmost element on the right array
        k = 0 #merged array index  

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] =left_arr[i]
                i += 1
               
            else:
                arr[k] =right_arr[j]
                j += 1  
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    

arr_test =[2,3,5,1,7,4,4,4,2,6,0]
merge_sort(arr_test)
print(arr_test)




