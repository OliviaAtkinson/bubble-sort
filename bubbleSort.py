mixed_num = [1,5,2,4,8,3,9,7,6]


#function-------------------------
def sorted_array(mixed_num):
    length_of_list = len(mixed_num)
    #calculating the length of the array

    for first_sort in range(length_of_list):
    #first sort of the array, causing the hightest num to move to the end with the loop of num_sort.
        # print (first_sort)
        for num_sort in range(0, length_of_list - first_sort - 1):
                if mixed_num[num_sort] > mixed_num[num_sort + 1]:
                mixed_num[num_sort] , mixed_num[num_sort + 1] = mixed_num[num_sort + 1], mixed_num[num_sort]
        #This nested for loop is continuously comparing the current num (which is the first num of the list) to the num on its right. If the num on the left is larger than the current num then they will swap places until it is in the right place and does not need to move again.

        

sorted_array(mixed_num)

print ("Sorted array is:" )
for first_sort in range(len(mixed_num)): 
    print (mixed_num[first_sort])