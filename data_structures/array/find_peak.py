def find_peak(arr):
    for i,n in enumerate(arr):
        if i==0 or i==len(arr)-1:
            pass
        else:
            if arr[i-1] < arr[i] and arr[i+1]<arr[i]:
                return arr[i]
arr=[5,10,20,25,30,24,78]
print(arr[::-1])
print(find_peak(arr))