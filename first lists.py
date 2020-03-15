import random
b=1
random_number_1=random.randint(1,100)
list_of_10_random_number=[random_number_1]
random_number_2=random.randint(1,100)
list1_of_10_random_number=[random_number_2]

while b < 10:
    random_number_1=random.randint(1,100)
    list_of_10_random_number.append(random_number_1)
    b += 1
print (list_of_10_random_number)

for d in range (1,10):
    random_number_2=random.randint(1,100)
    list1_of_10_random_number.append(random_number_2)
print(list1_of_10_random_number)





