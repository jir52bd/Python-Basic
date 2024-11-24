


#create a list
my_list = [1, 2, 3]

#Creating a reference for the my_list
another_list = my_list

#Modifing the list through reference
another_list.append(4)

#Both reference point to the same list
print(my_list) #output: [1, 2, 3, 4]
print(another_list) #Output: [1, 2, 3, 4]