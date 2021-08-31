# Find the length of Largest Common Subsequence in the given array
#This program is written in Python language 
#Time complexity of this program is O(N^2)
#Space Complexity of this program is O(n)
def Longest_Common_sub_Sequence(nums):
    n=len(nums)
    result_array=[1]*n
    for i in range(1,n):
        for j in range(0,i):
            if nums[i]>nums[j]:
                result_array[i]=max(1+result_array[j],result_array[i])

    
    maximum=0
    for i in result_array:
        maximum=max(maximum,i)

    return maximum

if __name__=='__main__':
    array=input("Enter array").split(',')
    array=list(map(int,array))
    length=Longest_Common_sub_Sequence(array)
    print('Length of largest common subsequence is ')
    print(length)