'''Brute force'''
class Solution:
    def minimise_max_Distance(self, arr, k):
        n = len(arr)
        how_many = [0] * (n - 1)
        for _ in range(k):
            max_section = -1
            max_index = -1

            for i in range(n-1):
                diff = arr[i+1] - arr[i]
                section_lenth = diff/(how_many[i] + 1)
                if section_lenth > max_section:
                    max_section = section_lenth
                    max_index = i
            how_many[max_index] += 1
        
        max_ans = -1
        for i in range(n-1): 
            diff = arr[i+1] - arr[i]
            section_lenth = diff / (how_many[i] + 1)   # we can say Number of section = how_many(new section)+ 1
            max_ans = max(max_ans, section_lenth)
        return max_ans, how_many

                
arr = [1, 2, 3, 4, 5, 9]
k = 2
a = Solution()
print(a.minimise_max_Distance(arr, k))