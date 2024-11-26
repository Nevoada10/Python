import time

print("Epoch date:", time.ctime(0))  # Convert time into a string since epoch, epoch = time reference for computer

print("Seconds since epoch:", round(time.time()), "seconds")  # How many seconds have passed since epoch.

# One way to get today's date:
print("Current date:", time.ctime(time.time()))
# time.time() shows how many seconds have passed since epoch.
# # time.ctime converts seconds into string dates.

time_object = time.localtime()  # Structure local time
utc_time_object = time.gmtime()
print("Current time object", time_object)

current_time = time.strftime("%d %B %Y %H:%M:%S", time_object)  # Format
print("Current time w/ string format time:", current_time)

print("UTC time object:", utc_time_object)

time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y")
print("Creating a time object of a date:", time_object)

"""
https://docs.python.org/3/library/time.html # Meaning of abbreviations.
"""

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst =  daylight saving time)
time_tuple = (2023, 1, 3, 14, 00, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)  # Converts a tuple into a readable string.
print("Guess arrival", time_string)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst =  daylight saving time)
time_tuple = (2024, 1, 3, 12, 00, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)  # Converts a tuple into seconds since epoch.
print("Seconds of Paris first birthday since epoch:", time_string)

trip_day = time.ctime(time_string)
print("Paris first birthday:", trip_day)

################################################################################################################
print("-")

# Date of depart
time_tuple_SP = (2023, 1, 2, 20, 00, 00, 0, 0, 0)
time_string_SP = time.mktime(time_tuple_SP)
print("São Paulo depart:", time.ctime(time_string_SP))

# Date of arrival
time_tuple_Paris = (2023, 1, 3, 12, 00, 00, 0, 0, 0)
time_string_Paris = time.mktime(time_tuple_Paris)
print("Paris arrival:", time.ctime(time_string_Paris))

# Time of travel:
GMT_SP = -3
GMT_Paris = +2
trip_time = ((time_string_Paris - time_string_SP) / 3600)
trip_real_time = ((time_string_Paris - time_string_SP) / 3600) - (GMT_Paris - GMT_SP)
# Going to the "right" in SP-Paris example.
# If you go to the "right", you need to remove the extra timezone.
# If you go to the "left", you need to add the extra timezone.
print("Trip apparent time: ", trip_time, "hours")
print("Trip real time:", trip_real_time, "hours.")
