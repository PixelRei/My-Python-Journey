#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
def fibonacci(numbers):
    nums = [0, 1]
    for x in range(numbers):
        nums.append(nums[x] + nums[x+1])
    return nums[1:len(nums)-1]

numbers = int(input("How many Fibonacci numbers you want to generate?\n"))
print(fibonacci(numbers))