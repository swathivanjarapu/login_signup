# def count_substring(string, sub_string):
#     count=0
#     for i in range(len(string)-len(sub_string)+1):
#         if (string[i:i+len(sub_string)] == sub_string):
#             count += 1
#     return count
    

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)



# def miniMaxSum(arr):
#     # Write your code here
#     a=sorted(arr)
#     b=sum(a[:-1])
#     c=sum(a[1:])
#     print(b,c)
   
    

# if __name__ == '__main__':

#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)


# if __name__ == '__main__':
#     s = input()
#     print(any(map(str.isalnum, s)))
#     print(any(map(str.isalpha, s)))
#     print(any(map(str.isdigit, s)))
#     print(any(map(str.islower, s)))
#     print(any(map(str.isupper, s)))


# n=13
# a=bin(n)
# print(a)
# print(a[2:])

# def counterGame(n):
#     # Write your code here
#     a=bin(n-1).count('1')
#     print(a)
#     if a%2==1:
#         return "Louise"
#     else:
#         return "Richard"
# print(counterGame(132))

# n=132
# a=bin(n-1).count('1')
# print(a)

# print("{:6f}\n{:6f}\n{:6f}".format(4/6,7/6,4/2))

# # left rotiation
# a=[1,2,3,4,5]
# d=2
# a=a[d:]+a[:d]
# print(*a)
    



def arrayManipulation(n, queries):
    # Write your code here
    arr=[0]*(n+2)
    print(arr)
    for a,b,k in queries:
        arr[a]+=k
        arr[b+1]-=k
        print(arr)
    maxnum=tamp=0
    for val in arr:
        tamp+=val
        maxnum=max(maxnum,tamp)
    return maxnum
        

