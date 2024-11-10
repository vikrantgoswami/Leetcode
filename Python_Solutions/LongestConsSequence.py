class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)
        max_len_of_subseq = 0

        for num in set_of_nums:
            if num-1 not in set_of_nums:
                len_of_subseq = 1
                #start of a new sequence
                seq_num = num
                while seq_num+1 in set_of_nums:
                    seq_num += 1
                    len_of_subseq += 1
                max_len_of_subseq = max(max_len_of_subseq,len_of_subseq)
        return max_len_of_subseq