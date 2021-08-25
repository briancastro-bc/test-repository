

def generate_numbers(length: int) -> list:
    nums: list = []
    for i in range(1, length):
        nums.append(i)
    return nums

def add(nums: list):
    sum: int = 0
    for i in nums:
        sum += i
    return sum