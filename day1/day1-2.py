# Find three numbers that sum to 2020, return their product
# Complexity: O(nlog(n))

f = open("day1.txt", "r")

nums = []

for line in f:
    nums.append(int(line))

nums.sort()
nums_set = set(nums)
start = 0
end = len(nums) - 1

searching = True

while start != end and searching:
    sum = nums[start] + nums[end]

    if (sum > 2020):
        end -= 1

    else:
        if (2020 - sum) in nums_set:
            product = nums[start] * nums[end] * (2020 - sum)     
            print(product)
            searching = False

        elif (2020 - sum) < nums[start]:
            end -= 1
        else:
            start += 1
f.close()