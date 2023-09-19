'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.Return the maximum amount of water a container can store.Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # to slow
        # res = 0
        # for l in range(len(height)):
        #     for r in range(l + 1,len(height)):
        #         area = (r - l) * min(height[l], height[r])
        #         res = max(res, area)
        # return res
        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h_left = height[left]
            h_right = height[right]
            width = right - left
            current_water = min(h_left, h_right) * width
            max_water = max(max_water, current_water)

            if h_left < h_right:
                left += 1
            else:
                right -= 1

        return max_water

'''
We start with two pointers, left and right, initially pointing to the first and last elements of the height array, respectively.

We also initialize a variable max_water to keep track of the maximum amount of water trapped, starting with a value of 0.

We enter a loop that continues as long as the left pointer is less than the right pointer. This loop is used to explore different pairs of vertical lines and calculate the trapped water between them.

Inside the loop, we calculate the height of the left line (h_left) and the height of the right line (h_right) at the current positions of the pointers. We also calculate the width of the container, which is the difference between the right and left pointers.

We then calculate the current water trapped between the two lines as the minimum of h_left and h_right (since the water level cannot exceed the height of the shorter line) multiplied by the width of the container.

We update the max_water variable with the maximum of its current value and the current water trapped. This keeps track of the maximum water trapped so far.

Next, we decide which pointer to move. If h_left is less than h_right, it means the left line is shorter, so we move the left pointer to the right. Otherwise, if h_right is less than or equal to h_left, we move the right pointer to the left. This step is crucial because by moving the shorter line inward, we have a chance of finding a taller line and potentially trapping more water.

The loop continues until the left pointer is no longer less than the right pointer, meaning we have explored all possible pairs of lines.

Finally, we return the max_water value, which represents the maximum amount of water that can be trapped between two vertical lines in the array.
'''
