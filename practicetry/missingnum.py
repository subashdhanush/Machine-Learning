nums = [1, 2, 3, 5, 6]
n = len(nums) + 1
print(n)
expected_sum = n * (n + 1) // 2
print("expected_sum",expected_sum)
actual_sum = sum(nums)
print("actual_sum",actual_sum)
print("Missing number:", expected_sum - actual_sum)
