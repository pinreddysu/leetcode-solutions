class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        When solving this problem think of dictionary and how are words are ordered
        like RAJ, RAX, RBX. Same intuition
        1. Find longest prefix match
        -> RA is longest prefix for RAJ and RAX and R is longest prefix match 
        between RAX and RBX. In numbers to find you check if a[i] < a[i+1] because
        that is break point as longest prefix decrease if it cannot generate greater value from current suffix 
        ex: 5,4 cannot generate values > 5,4 but if it is 1,5,4 you can generate
        greater than 1,5,4 like 4,5,1 , 4,1,5 etc
        think of RAZZZZZZZ then longest in this senario then next has to RZZZZZZA
        2. After finding longest index of longest Prefix match swap with first largest value of index where longest prefix end
        3. Reverse from end to dip +1 point
        """
        index = -1
        for i in range(len(nums)-2, -1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break
        if index ==-1:
            return nums.reverse()
        
        for i in range(len(nums)-1,index, -1):
            if nums[index] < nums[i]:
                nums[index], nums[i] = nums[i], nums[index]
                break
        nums[index+1:] = nums[index+1:][::-1]