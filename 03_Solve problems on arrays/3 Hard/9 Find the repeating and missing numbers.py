'''My brute force'''
# class Solution:
#     def finding(self, arr):
#         n = len(arr)
#         ans = []
#         for i in range(1, n):
#             if i not in arr:
#                 B = i
#             if arr[i] == arr[i-1]:
#                 A = arr[i]
#         ans.append(A)
#         ans.append(B)
#         return ans
# arr =[1, 1, 3, 4, 5]
# a = Solution()
# print(a.finding(arr))




'''My Better approach for space'''
# class Solution:
#     def finding(self, arr):
#         n = len(arr)
#         ans = []
#         arr.sort()
#         for i in range(1, n):
#             if arr[0] != 1:
#                 B = 1
#             if arr[i] != i+1:
#                 B = i+1
#             if arr[i] == arr[i-1]:
#                 A = arr[i]
#         ans.append(A)
#         ans.append(B)
#         return ans
# arr =[1, 1, 3, 4, 5]
# a = Solution()
# print(a.finding(arr))

'''My Beter approach for time'''
# class Solution:
#     def finding(self, arr):
#         n = len(arr)
#         mpp = {}
#         ans = []
#         for i in range(1, n+1):
#             mpp[i] = 0
#         for i in range(n):
#             mpp[arr[i]] += 1
#         for key in mpp:
#             if mpp[key] == 2:
#                 A = key
#             if mpp[key] == 0:
#                 B = key
#         ans.append(A)
#         ans.append(B)
#         return ans
# arr =[1, 1, 3, 4, 5]
# a = Solution()
# print(a.finding(arr))


'''Another way of better approach for time'''
# class Solution:
#     def finding(self, arr):
#         n = len(arr)
#         hashmap = [0] * (n+1)
#         for num in arr:
#             hashmap[num] +=1
#         A, B = -1, -1
#         for i in range(1, n+1):
#             if hashmap[i] == 2:
#                 A = i
#             if hashmap[i] == 0:
#                 B = i
#             if A != -1 and B != -1:
#                 break
#         return [A, B]

# arr =[1, 1, 3, 4, 5]
# a = Solution()
# print(a.finding(arr))



'''Optimal approach-I'''
# class Solution:
#     def finding(self, arr):
#         n = len(arr)
#         SN = (n*(n+1))//2
#         S2N = (n*(n+1)*(2*n+1))//6

#         s = 0
#         s2 = 0
#         for num in arr:
#             s += num
#             s2 += num*num

#         val1 = s - SN   # = reapeating value - messing value
#         val2 = s2 - S2N  # = reapeating value^2 - messing value^2
#         val2 = val2//val1   # = reapeating value + messing value

#         X = (val1 + val2)//2
#         Y = X -  val1
#         return [int(X), int(Y)]
# arr =[1, 1, 3, 4, 5]
# a = Solution()
# print(a.finding(arr))

'''Optimal approach-II'''
class Solution:
    def finding(self, arr):
        n = len(arr)
        xor = 0
        for i in range(n):
            xor = xor ^ arr[i]
            xor = xor ^ (i+1)
        number = (xor & ~(xor-1))
        zero = 0
        one = 0
        for i in range(n):
            if (arr[i] & number) != 0:
                one = one ^ arr[i]
            else: 
                zero = zero ^ arr[i]
        for i in range(1, n+1):
            if (i & number) != 0:
                one = one ^ i
            else:
                zero = zero ^ i
        count = 0
        for i in range(n):
            if arr[i] == zero:
                count += 1
        if count == 2:
            return [zero, one]
        return [one, zero]
arr =[1, 1, 3, 4, 5]
a = Solution()
print(a.finding(arr))