def sumpairs(arr,sum):
    arr.sort()
    left=0
    right=len(arr)-1
    while (left<=right):
        if arr[left]+arr[right]>sum:
            right=right-1
        elif arr[left]+arr[right]<sum:
            left=left+1
        elif arr[left]+arr[right]==sum:
            print("two value pairs",arr[left],arr[right])

arr=[5,3,4,8,7,9,19,21]
sum=17

sumpairs(arr,sum)
    
            
        
