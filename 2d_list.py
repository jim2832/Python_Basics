nums = [
    [1, 2, 3],
    [5, 7, 1],
    [0, 2, 10]
]

#print(nums[0][2])

#巢狀迴圈
for i in range(len(nums)):
    for j in range(len(nums[0])):
        print(nums[i][j])

for row in nums:
    for col in row:
        print(col)