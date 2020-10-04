import time

epoch = time.time()


# Get Days Since Epoch

secs_in_a_day = 24 * 60 *60  ## Calculate secs in a day

my_date = epoch // secs_in_a_day ## Divide epoch by secs in a day to get number of days since epoch

num_days = int(my_date) # Change the days to an integer



# Get Time

t_secs = epoch % secs_in_a_day    # This shows me the remaing seconds for today
c_hours = int(t_secs // (60 * 60)) # Get the hours for today
t_mins = int(t_secs // 60) # Total mins from today
c_mins = int(t_mins % 60) # Get mins for time
c_secs = int(t_secs % 60)  # Get reminder of seconds for time

print(" The time is ", c_hours, ":", c_mins, ":", c_secs, " on ", num_days, " days since epoch")





