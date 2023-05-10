###Task1##
import datetime
name = input("Enter your name: ")
age = int(input("Enter your age: "))
Year = 100 - age
print("Hello", name,"You will turn 100 years old in",Year)
##Task2###
input_string = input("Enter a list of integers, separated by commas: ")
input_list = input_string.split(",")
numbers = [int(num) for num in input_list]
if len(numbers) > 0:
    print(sum(numbers))
if  len(numbers) == 0:
    print(0)
input_string = input("Enter a list of integers, separated by commas: ")
input_list = input_string.split(",")
numbers = [int(num) for num in input_list]
##Task3###
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

unique_numbers.sort()

print(unique_numbers)
###Task4###
input_string1 = input("Enter firs list list of integers, separated by commas: ")
input_string2 = input("Enter the secont list of integers, separated by commas: ")
input_list1 = input_string1.split(",")
input_list2 = input_string2.split(",")
numbers1 = [int(num) for num in input_list1]
numbers2 = [int(num) for num in input_list2]

The_Common_Elements = []

for x in numbers1:
    if x in numbers2:
        The_Common_Elements.append(x)
The_Common_Elements.sort()
print("The common elements are", The_Common_Elements)


###Task5###

input_string = input("Enter a string: ")

char_counts = {}

for char in input_string:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1


sorted_keys = sorted(char_counts.keys())


print("Character counts:")
for key in sorted_keys:
    print(key + ": " + str(char_counts[key]))