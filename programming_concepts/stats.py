# File - stats.py
# Latest Version - Chapter 11
from math import sqrt


def get_numbers():
    nums = []  # start with an empty list

    # sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = float(xStr)
        nums.append(x)  # add this value to the list
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums


def mean(nums):
    total = 0.0
    for num in nums:
        total = total + num
    return total / len(nums)


def std_dev(nums, xbar):
    sumDevSq = 0.0
    for num in nums:
        dev = num - xbar
        sumDevSq = sumDevSq + dev * dev
    return sqrt(sumDevSq / (len(nums) - 1))


def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size // 2
    if size % 2 == 0:
        med = (nums[midPos] + nums[midPos - 1]) / 2.0
    else:
        med = nums[midPos]
    return med


def main():
    print("This program computes mean, median and standard deviation.")

    data = get_numbers()
    xbar = mean(data)
    std = std_dev(data, xbar)
    med = median(data)

    print(f"\nThe mean is {xbar}, the standard deviation is {std}, the median is {med}")


if __name__ == "__main__":
    main()
