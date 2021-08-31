# Find the length of Largest Common Subsequence in the given array
#This program is written in Python language 
#Time complexity of this program is O(N^2)
#Space Complexity of this program is O(N^2)
def Longest_Common_sub_Sequence(nums):
    sorted_nums=sorted(list(set(nums)))
    n=len(nums)
    m=len(sorted_nums)
    arr2=[]
    for i in range(n+1):
        arr=[]
        for j in range(m+1):
            arr.append(-1)
        arr2.append(arr)
        
    
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                arr2[i][j]=0
            elif sorted_nums[j-1]==nums[i-1]:
                arr2[i][j]=arr2[i-1][j-1]+1
            else:
                arr2[i][j]=max(arr2[i-1][j],arr2[i][j-1])


    return arr2[-1][-1]

if __name__=='__main__':
    array=input("Enter array").split(',')
    array=list(map(int,array))
    length=Longest_Common_sub_Sequence(array)
    print('Length of largest common subsequence is ')
    print(length)