# Array insertion sort implementation

class Insert_Sorter(object):
    # Sorts the integer in unsorted
    # in ascending order
    def asc_sort(self, unsorted):
        input_size = len(unsorted)
        curr_ind = 1

        #ascending loop
        for i in range(1, input_size):
            curr_ind = i
            # Decending loop to slide a value down the array 
            # as long as it is small enough
            while(curr_ind > 0):
                num_holder = unsorted[curr_ind]
                left_num = unsorted[curr_ind - 1]

                # If left index is bigger than right
                # then swap them
                if (left_num >= num_holder):
                    unsorted[curr_ind] = left_num
                    unsorted[curr_ind - 1] = num_holder
                # Base case
                elif(curr_ind == 1 or left_num < num_holder):
                    curr_ind = 0
                curr_ind -= 1
