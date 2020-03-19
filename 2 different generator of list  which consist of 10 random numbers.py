import random

def generate_random_array_with_numbers(len_of_elems):
    list_of_10_random_number=[]
    condition = 1

    while condition <= 10:
        random_number=random.randint(1,100)
        list_of_10_random_number.append(random_number)
        condition +=1

    print(list_of_10_random_number)
    print(len(list_of_10_random_number))

def generate_random_array_with_numbers_1(len_of_elems):
    list_of_10_random_number_1=[]
    for _condition_1 in range (1,11):
        random_number_1=random.randint(1,100)
        list_of_10_random_number_1.append(random_number_1)
    print (list_of_10_random_number_1)
    print(len(list_of_10_random_number_1))

generate_random_array_with_numbers(10)
generate_random_array_with_numbers_1(10)
