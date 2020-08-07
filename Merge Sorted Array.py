def merge(nums1,nums2,m,n):
    #create an empty array to store values of nums1 without the zeros
    new_nums=[]
    #copy the items in nums1 to new_nums
    for i in range(0,m):
        y.append(nums1[i])
    #append the items in nums2 to new_nums
    for i in (range(n)):
        new_nums.append(nums2[i])
    #since we are not returning any values, but modifying nums1
    #we copy items in new_nums to nums1
    for i in range(len(new_nums)):
        nums1[i]=new_nums[i]

    #arrange nums1 to be in ascending order   
    nums1.sort()

    