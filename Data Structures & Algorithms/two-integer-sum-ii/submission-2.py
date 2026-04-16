class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow, fast = 0, len(numbers) - 1
        while slow < fast:
            curr = numbers[slow] + numbers[fast]
            if curr == target:
                return [slow + 1, fast + 1]
            elif curr < target:
                slow += 1
            elif curr > target:
                fast -= 1
        