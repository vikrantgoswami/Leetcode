class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        #bucket sort approach
        bucket_list = [[] for i in range(len(nums)+1)] #we want as much elements as the length of nums
        #why? so that we can count the frequency of each character in case all elements are same

        #lets store the frequency of each element in a map first
        num_freq = {}
        for i in nums:
            num_freq[i] = num_freq.get(i,0)+1
        #print(num_freq)
        #num_freq = {1:3, 2:2, 3:1}
        #now we know how many times a number appears in the dictionary
        #now we can add it to bucket list
        for i, num in num_freq.items():
            bucket_list[num].append(i)
            #we add on each index the elems which occur that many times
        #print(bucket_list)
        #bucket_list = [[], [3], [2], [1]]
        #so in bucket_list the array at higher indexes contains the numbers which occur most
        for i in range(len(bucket_list)-1,-1,-1):
            #print(bucket_list[i])
            print(i)
            for j in bucket_list[i]:
                #print(j)
                res.append(j)
                #print('res ',res)
                if len(res) == k:
                    return res
