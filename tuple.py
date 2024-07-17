#TASK 1 create a tuple in python

#original  tuple
my_tuple=( 'rahul','shivam',9, 8, 7, 6 , 5)
#adding a new element to the  tuple
new_element=3
updated_tuple=my_tuple + (new_element,)
#removing  an element from the tuple
updated_tuple=my_tuple[:1]+my_tuple[3:]


print(updated_tuple)
