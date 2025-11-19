# This is a function to help organize multiple meetings 
# Author : PORHAY ROUEN
# DATE : Fri, Oct 3, 2025
#-------------------------------#
def findMinRooms(*meetings):
# use Try and Except to handle any errors
    try:
    # Check is there are no meetings 
        if not meetings:
            return 0
    # Create variables to hold the start and end times
        var_start_times = []
        var_end_times = []

    # Check if the values are valid 
        for number in meetings:
            if type(number) not in [list, tuple] or len(number) !=2:
                raise ValueError(f"Each meeting should be a list or tuple with two elements : {number}")

        # Check if the number are valid        
            start_time, end_time = number

        # Check if meeting is number
            if not (type(start_time) not in [int,float]) and type(end_time) not in [int,float] :
                raise ValueError(f"Meeting_times must be number:{number}")
        # check if it correct format         
            if not (0.0 <= start_time <= 24.0 and 0.0 <= end_time <= 24.0):
                raise ValueError(f"Meeting_times should be between 0.0 and 24.0 : {number}")

        # Check you inputs start_time is smaller than end_time
            if start_time >= end_time:
                raise ValueError(f"Start time should be smaller than end time: {number}")

        # Add values to the lists  
            var_start_times.append(start_time)
            var_end_times.append(end_time)
 
    # Sort the var_start_time and var_end_times    
        var_start_times.sort()
        var_end_times.sort()

        used_rooms = 0
        max_rooms = 0
        i,j = 0,0 
        n = len(meetings)

        while i < n :
            if var_start_times[i] < var_end_times[j]:
                used_rooms += 1
                max_rooms = max(max_rooms, used_rooms)
                i += 1
            else: 
                used_rooms -=1
                j += 1
        return max_rooms

    except Exception as e:
        return f"Error: {e}"


#Sample Testing
print(findMinRooms([1.2, 3.4], [2.3, 5.0], [3.1, 8.0]))

print(findMinRooms([1.2, 3.4], [2.3, 5.0], [4.1, 8.0]))

print(findMinRooms([1.2, 3.4], [2.3, 5.0], [3.1, 8.0], [1.0, 10.0]))

