def max_list_sum(list_a,n):
    center=int(n/2)
    if n == 1:
        if list_a[0]>0:
            return list_a[0]
        else:
            return 0
    left_temp=max_list_sum(list_a[0:center],center)
    right_temp=max_list_sum(list_a[center:n],center)
    sum=0
    left_max=0
    i=center-1
    while i>=0:
        sum+=list_a[i]
        left_max=max(sum,left_max)
        i-=1
    sum=0
    right_max=0
    i=center
    while i<n:
        sum+=list_a[i]
        right_max=max(sum,right_max)
        i+=1
    sum=left_max+right_max
    sum=max(sum,left_temp,right_temp)
    return sum


