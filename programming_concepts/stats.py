# File - stats.py
# Latest Version - Chapter 11
from math import sqrt


def get_numbers():
    nums = []  # start with an empty list

    # sentinel loop to get numbers
    x = input("Enter a number (<Enter> to quit) >> ")
    while x != "":
        x = float(x)
        nums.append(x)  # add this value to the list
        x = input("Enter a number (<Enter> to quit) >> ")
    return nums


def mean(nums):
    total = 0.0
    for num in nums:
        total = total + num
    return total / len(nums)


def std_dev(nums, xbar):
    sum_dev_sq = 0.0
    for num in nums:
        dev = num - xbar
        sum_dev_sq = sum_dev_sq + dev * dev
    return sqrt(sum_dev_sq / (len(nums) - 1))


def median(nums):
    nums.sort()
    size = len(nums)
    mid_pos = size // 2
    if size % 2 == 0:
        med = (nums[mid_pos] + nums[mid_pos - 1]) / 2.0
    else:
        med = nums[mid_pos]
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
