import random
'''
def generate_random_number_list_10x10(amount_of_lists,len_of_elements):
    main_list=[]
    
    for _variable_1 in range (amount_of_lists):
        columnlist=[]
        for _variable_2 in range (len_of_elements):
            random_number=random.randint(1,100)
            columnlist.append(random_number)
        main_list.append(columnlist)
    print(main_list)
    print(len(main_list))

generate_random_number_list_10x10(29,1)
'''
'''
def generate_random_number_list_10(len_of_elements):
    single_list_of_10_random_numbers=[]
    for _variable_1 in range (len_of_elements):
        random_number=random.randint(1,100)
        single_list_of_10_random_numbers.append(random_number)
    return single_list_of_10_random_numbers

def generate_random_number_list_10x10_1(amount_of_lists):
    main_list=[]
    for _variable_1 in range (amount_of_lists):
        singlelist=generate_random_number_list_10(10)
        main_list.append(singlelist)
    print(*main_list,sep='\n')

generate_random_number_list_10x10_1(10)
'''
'''
def generate_random_number_list_10(len_of_elements):
    return[print((random.randint(1,100))) for x in range (len_of_elements)]

my_random_list=generate_random_number_list_10(10)
'''

'''
def generate_random_number_list_10(len_of_elements):
    my_list=[]
    [my_list.append(random.randint(1,100)) for x in range (len_of_elements)]
    return print(my_list)
 


random_list=generate_random_number_list_10(10)
'''
'''
def generate_random_number_list_10(len_of_elements):
    
    my_list=[random.randint(1,100) for x in range (len_of_elements)]
    return my_list
 

def generate_list_consist_of_10_smaller_list(amount_of_list):
    big_list=[generate_random_number_list_10(10) for x in range (amount_of_list)]
    return print(*big_list,sep='\n')

bigger_list=generate_list_consist_of_10_smaller_list(10)
'''
'''
def generate_random_number_list_10(len_of_elements):
    
    my_list=[random.randint(1,100) for x in range (len_of_elements)]
    return my_list
 

def generate_list_consist_of_10_smaller_list(amount_of_list,len_of_elements,variable):
    big_list=[generate_random_number_list_10(len_of_elements) for x in range (amount_of_list)]
    if (variable % 2)==0:
        print(big_list[1:amount_of_list:2])
    if (variable % 2)!=0: 
        print(big_list[0:amount_of_list:2])
    print(big_list)

generate_list_consist_of_10_smaller_list(10,4,10)
'''

def generate_random_number_list_10(len_of_elements):
    
    my_list=[random.randint(1,100) for x in range (len_of_elements)]
    return my_list

def generate_list_consist_of_10_smaller_list(amount_of_list,len_of_elements,variable):
    
    big_list=[generate_random_number_list_10(len_of_elements) for x in range (amount_of_list)]
    print (*big_list,sep="\n")
    if variable%2 == 0:
        print("Even variable has been entered: "+repr(variable)+" so program have filtered all even number from the list ")
        filtered_list = [list(filter(lambda x: x%2==0, num)) for num in big_list]
        print (*filtered_list,sep="\n")
        f=open('even.txt', 'w')
        print(*big_list,sep="\n",file=f)
        print("Even variable has been entered: "+repr(variable)+" so program have filtered all even number from the list ",file=f)
        print(*filtered_list,sep="\n",file=f)
    
    if variable%2 != 0:
        print("Odd variable has been entered: "+repr(variable)+" so program have filtered all odd number from the list ")
        filtered_list = [list(filter(lambda x: x%2!=0, num)) for num in big_list]
        print (*filtered_list,sep="\n")
        f=open('odd.txt', 'w')
        print(*big_list,sep="\n",file=f)
        print("Odd variable has been entered: "+repr(variable)+" so program have filtered all odd number from the list ",file=f)
        print(*filtered_list,sep="\n",file=f)
       
generate_list_consist_of_10_smaller_list(10,10,8)








    


