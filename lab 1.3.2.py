import unittest

def find_unsorted_part(nums):
    n = len(nums)
    if n <= 1:
        return (-1, -1)

    left = 0 
    while left < n - 1 and nums[left] <= nums[left + 1]:
        left += 1
    
    if left == n - 1:
        return (-1, -1)

    right = n - 1
    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1

    unsorted_min = min(nums[left:right + 1])
    unsorted_max = max(nums[left:right + 1])

    while left > 0 and nums[left - 1] > unsorted_min:
        left -= 1 

    while right < n - 1 and nums[right + 1] < unsorted_max:
        right += 1

    return (left, right)

class TestUnsortedPart(unittest.TestCase):
    def test_example_case(self):
        nums = [1, 2 , 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        self.assertEqual(find_unsorted_part(nums), (3, 9))

    def test_already_sorted(self):
        nums = [1, 3, 5, 7, 9, 11]
        self.assertEqual(find_unsorted_part(nums), (-1, -1))

    def test_all_unsorted(self):
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(find_unsorted_part(nums), (0, 4))

    def test_one_num(self):
        nums = [67]
        self.assertEqual(find_unsorted_part(nums), (-1, -1))

if __name__ == '__main__':
    unittest.main()

    