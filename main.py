# 1)
number = 10234100042140
str_number = str(number)
counter = 0

for i in range(len(str_number)):
    if str_number[i] == '0':
        counter += 1

print(counter)
# 2)#########################################
number = 43500034000
str_number = str(number)
counter = 0

for i in (str_number[::-1]):
    if i == '0':
        counter += 1
    else:
        break

print(counter)
# 3)#########################################
my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [36, 6, 4, 8]
my_result = []

for i in range(len(my_list_1)):
    if i % 2 == 0:
        my_result.append(my_list_1[i])
for i in range(len(my_list_2)):
    if i % 2 != 0:
        my_result.append(my_list_2[i])

print(my_result)
# 4)#########################################
my_list = [1, 2, 3, 4, 5, 6]
new_list = my_list[1:] + [my_list[0]]
print(new_list)
# 5)#########################################
my_list = [1, 2, 3, 4]
first = my_list.pop(0)
my_list.append(first)
print(my_list)
# 6)#########################################
my_string = '34 75 64 25 46'
my_string = my_string.split()
suma = 0

for i in my_string:
    if i.isdigit():
        suma += int(i)

print(suma)
# 7)#########################################
my_str = "My long string"
l_limit = "o"
r_limit = "g"

l_idx = my_str.find(l_limit) + 1
r_idx = my_str.rfind(r_limit)
result = my_str[l_idx: r_idx]

print(result)
# 8)#########################################
my_str = 'abcde'
result = []

for i in range(0, len(my_str), 2):
    if i < len(my_str) - 1:
        result.append(my_str[i] + my_str[i + 1])
    else:
        result.append(my_str[i] + '_')

print(result)
# 9)
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
counter = 0

for i in range(1, len(my_list) - 1):
    if my_list[i] > sum([my_list[i - 1], my_list[i + 1]]):
        counter += 1

print(counter)