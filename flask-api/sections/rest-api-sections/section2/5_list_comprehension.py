my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)]
an_doubled_list = [x * 2 for x in range(5)] # will mutliply by 2 and insert

print(an_doubled_list)

for my_number in range(10):
    print(my_number)

[my_number for my_number in range(10)] # list comprehension 

[my_number * 2 for my_number in range(10)]

1 % 2
2 % 2
5 % 2
8 % 3

print([n for n in range(10) if n % 2 == 0])

names_list = [" John", "Rolf", "ANNA"]
lowercase_names = [name.lower().strip() for name in names_list] # list comprehension
print(lowercase_names)
