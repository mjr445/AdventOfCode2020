# Find two numbers that sum to 2020, return their product
# Complexity: O(nlog(n))

f = open("day1.txt", "r")

nums = []

for line in f:
    nums.append(int(line))

start = 0
end = len(nums) - 1
searching = True
nums.sort()
while start != end and searching:
    sum = nums[start] + nums[end]
    if (2020 == sum):
        product = nums[start] * nums[end]
        print(product)
        searching = False

    elif (sum > 2020):
        end -= 1
    elif (sum < 2020):
        start += 1

f.close()