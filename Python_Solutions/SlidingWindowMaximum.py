class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            #we pop elements from queue until we are able maintain a decreasing order of elements
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            #once we have ensured the decreasing order we can append the current index to our queue
            q.append(r)

            #remove left index from queue if its out of our current window
            if l > q[0]:
                q.popleft()

            #now we have a queue with some values
            #if we have travelled the size of our window, k, we can add leftmost element to our result
            if r+1 >= k:
                res.append(nums[q[0]])
                l+=1
            r+=1

        return res