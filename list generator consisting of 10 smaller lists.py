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








    


