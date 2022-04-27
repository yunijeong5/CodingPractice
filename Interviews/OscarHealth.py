# Part 1


# Dr. Esposito is in charge of planning when to transfer diabetic patients from a hospital to a sub-acute care facility. In order for a patient to be safely transferred, among other criteria, the patient's glucose level must be stable. The task is to implement can_transfer(glucose_data, threshold), which should return true if the biggest drop over any period of time in insulin readings is less than the threshold. 

'''
glucose_data = [89, 93, 92, 91, 92, 90, 94, 104, 103, 102, 106]
can_transfer(glucose_data, 10) # true, maximum drop is 3, 93-90
can_transfer(glucose_data, 1) # false
'''

# keep track of max number so far, get max_so_far - cur number
# max_drop, when cur number <= max_so_far

def can_transfer(glucose_data, threshold):
    max_so_far = glucose_data[0]
    max_drop = float('-inf')
    
    for i in glucose_data:
        # update max drop
        if i <= max_so_far:
            max_drop = max(max_drop, max_so_far - i)
            
        # update max_so_far
        max_so_far = max(max_so_far, i)
        
    return max_drop < threshold


glucose_data = [89, 93, 60, 91, 92, 90, 94, 104, 103, 102, 106]

print(can_transfer(glucose_data, 10)) # true, maximum drop is 3, 93-90         
        
        
# Part 2
# For some lower-risk patients, the transfer can take place as long as the insulin drop within any sub-range of a specified size is less than the threshold.

'''
glucose_data = [100, 100, 98, 97, 96, 99, 101]
can_transfer_lower_risk(glucose_data, threshold = 4, range_size = 3) # true, biggest drop from 100->96 outside range.
can_transfer_lower_risk(glucose_data, threshold = 4, range_size = 4) # false

-efficiently figure out the max value
-efficiently insert the new values
-efficiently remove the value that exists the range
'''







