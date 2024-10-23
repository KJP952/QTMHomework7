#Question 1
# Valid variables : _data, myVar
# Invalid variables: 2nd_value, class, t0T4L-4M0UnT

# Python variable must start with a letter or underscore which is why 2nd_value does not work. There are words that are reserved in
# python is one of them. t0T4L-4M0UnT does not work because python does not allow dashes for variables.

#Question 2

# 3 is 3.0 returns false because 3 is an int value where 3.0 is a float value, because they are two different data types it returns False.
# 3 = 3.0 returns true because the = is not comparing data type, but the value and they are both value of three so it returns true.

#Question 3

s = "DataScienceIsAwesome"
print(s[4:11])
print(s[::-1])
print(s[0:20:2])

#Question 4

grades = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 80,
    "Eve": 95
}

grades.update({"David":87})
grades.update({"Alice":95})
grades.pop("Charlie")
print(grades)

#Question 5

# / is a division operator and // is a floor division operator. The / operator is a typical division where it will divide
# the two numbers and return the exact quotient. // also divides the two numbers but it will round it down to an int if the quotient
# has a remainder. For example 15 / 6 = 2.5 but 15 // 6 is 2. A error if used interchangeably is the loss of the decimal values
# which can result is incorrect outputs in a larger function.

#Question 6

names = ["Andrew", "Betty", "Charlie", "Daniel", "Edward", "Frank", "George", "Hannah", "Isaac", "Jack"]

for n in names:
    if "a" in n or "A" in n:
        print(n)

#Question 7

# x would be 25. The operation would start with x = 5 and the parentehsies (x-1) = 4
# next would be x * (4) which is 5 * 4 = 20. Because there is += you add to the current value of x which is 20 + 5.

#Question 8

lst = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

print(lst[0][1][1])
lst[1][1][0] = 10
print(lst)

#Question 9

# result = "long" if len(my_list) else "short"

#Question 10

Num = [(x, x**3) for x in range(1,11)]
print(Num)