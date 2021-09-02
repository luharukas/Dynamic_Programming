# Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.
# The Operation are 1) Insert 2) Replace 3) Remove  
# Time Complexity of this program is O(MN)
# Space Complexity of this program is O(MN)


def edit_distance(string1,string2):
    len1=len(string1)
    len2=len(string2)

    arr=[[0 for i in range(len1+1)] for j in range(len2+1)]

    for i in range(len2+1):
        for j in range(len1+1):
            if i==0:
                arr[i][j]==j
            if j==0:
                arr[i][j]==i
            elif string2[i-1]==string1[j-1]:
                arr[i][j]=arr[i-1][j-1]
            else:
                arr[i][j]=1+ min(arr[i-1][j-1],arr[i-1][j],arr[i][j-1])


    print("Total Edit Distance: ",arr[-1][-1])









if __name__=='__main__':
    str1=input("Enter you string1 ")
    str2=input("Enter string2: ")
    edit_distance(str1,str2)
