
# Find the length of Largest Common Subsequence in the given String
#This program is written in Python language 
#Time complexity of this program is O(N^2)
#Space Complexity of this program is O(N^2)
def longest_common_subsequence(string1,string2):
    m=len(string1)
    n=len(string2)
    arr=[[0 for i in range(m+1)] for j in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if string1[j-1]==string2[i-1]:
                arr[i][j]=1+arr[i-1][j-1]
            else:
                arr[i][j]=max(arr[i-1][j],arr[i][j-1])


    return arr[-1][-1]



if __name__=='__main__':
    input_string1=list(input("Enter string 1: "))
    input_string2=list(input("Enter string 2: "))
    longest_common_subsequence(input_string1,input_string2)