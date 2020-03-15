import random
list_of_10_random_number=[]
condition = 1

while condition <= 10:
    random_number=random.randint(1,100)
    list_of_10_random_number.append(random_number)
    condition +=1

print(list_of_10_random_number)

list_of_10_random_number_1=[]

for condition_1 in range (1,11):
    random_number_1=random.randint(1,100)
    list_of_10_random_number_1.append(random_number_1)
print (list_of_10_random_number_1)

print(len(list_of_10_random_number))
print(len(list_of_10_random_number_1))
