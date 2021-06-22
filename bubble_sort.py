'''Bubblesort algorithm. We create a function that takes an array as input and
when you call it , it applies the bubblesort algorithm'''

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [1,89,4,67,694,2,4,52,34]
bubblesort(arr)

print('The sorted array is:')
for i in range(len(arr)):
    print(arr[i])
