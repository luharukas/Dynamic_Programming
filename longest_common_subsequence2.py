# Find the length of Largest Common Subsequence in the given String
#This program is written in Python language 
#Time complexity of this program is O(N^2)
#Space Complexity of this program is O(N^2)
def longest_common_subsequence(string1,string2):
    m=len(string1)
    n=len(string2)

    if m==0 or n==0:
        return 0
    elif string1[m-1]==string2[n-1]:
        return 1+longest_common_subsequence(string1[:m-1],string2[:n-1])
    else:
        return max(longest_common_subsequence(string1[:m],string2[:n-1]),longest_common_subsequence(string1[:m-1],string2[:n]))





if __name__=='__main__':
    input_string1=list(input("Enter string 1: "))
    input_string2=list(input("Enter string 2: "))
    result=longest_common_subsequence(input_string1,input_string2)
    print("Longest Common Subsequence is of length ",result)