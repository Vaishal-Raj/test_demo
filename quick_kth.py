def partition(arr,low,high):
    pivot=arr[low]
    i=low+1
    j=high
    while(i<=j):
        while(i<=j and arr[i]<=pivot):
            i+=1
        while(i<=j and arr[j]>pivot):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

    
def quicksort(arr,lb,ub,k):
    if(lb<=ub and k>0):
        pivot=partition(arr,lb,ub)
        if(pivot==k-1):
            return arr[pivot]
        elif pivot>k-1:
            return quicksort(arr,lb,pivot,k)
        else:
            return quicksort(arr,pivot+1,ub,k)
    else:
        return -1

arr=[10,5,7,1,0,2,3]
print(quicksort(arr,0,len(arr)-1,3))
print(arr)
