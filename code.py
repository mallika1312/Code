def minif(arr,n,m):

    soln=123456789

    arr.sort()

    for i in range(n-m+1):

        soln = int(min(soln,arr[i+m-1]-arr[i]))

    return soln
arr = [7980,22349,999,2799,229900,11101,9999,2195,9800,4999]

n = len(arr)

m = int(input())

print(minif(arr,n,m))
