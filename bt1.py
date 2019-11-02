
'''loop = True
while loop:
    x =input('Insert a number: ')
    try:
        n = int(x)
        a = 10/n
        print('Answer {}'.format(a))
        loop = False
    except ValueError:
        print('Wrong number')
    except ZeroDivisionError:
        print("cannot divide to zero")'''
    
'''algorithm'''
'''
NOTE: index 
menu = ['com','canh','thit']
print(menu[0])
print(menu[-1])
NOTE: loop items and index
for index, item in enumerate(menu);
    print(index,item)
NOTE: update
menu[0] = 'pho'
menu[1], menu[2] = menu[2], menu[1]
'''
'''from random import randint
input_list = []
for i in range(10):
    input_list.append(randint(1,10))
print(input_list)
print(input_list[0], input_list[1], input_list[2])
print(input_list[-3], input_list[-2], input_list[-1])
for i in range(len(input_list)):
    for m in range(len(input_list)):
        if input_list[i] < input_list[m]:
            input_list[i], input_list[m] = input_list[m], input_list[i]
print(input_list)
for i in range(len(input_list)):
    for m in range(len(input_list)):
        if input_list[i] > input_list[m]:
            input_list[i], input_list[m] = input_list[m], input_list[i]
print(input_list)

input_list.sort()
print(input_list)'''

'''nums = [5,6,1,9,3]'''

'''swapped = True
while swapped:
    swapped = False 
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            swapped = True
print(nums)'''

'''
for i in range(len(nums)):
    lowest_value_index = i
    for j in range(i+1, len(nums)):
        if nums[j] < nums[lowest_value_index]:
            lowest_value_index = j
    nums[j], nums[lowest_value_index] = nums[lowest_value_index], nums[j]
print(nums)'''

'''Quick review dictionary
person = {
    "name": "Duc",
    "age": 21,
    "university": ["FTU"]
    "ex": 3,
}
NOTE:  loop by key
for key in person:
    print(key)
NOTE: loop by value
for value in person.values():
    print(value)
NOTE: loop by items
for key, value in person.items()
    print(key,value)
NOTE: create and update
person["gender"] = "male"
person["ex"] = 5
NOTE: change a key to other key
person ["sex"] = person.pop("gender")'''

nums = [16, 2, 4, 2, 128, 64, 16, 7, 1, 64, 32, 16, 5, 8]
con = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] * nums[j] == 256:
            if nums[i] not in con and i!=j:
                con.append(nums[i]) 
                con.append(nums[j])
                print(nums[i], i, nums[j], j)


