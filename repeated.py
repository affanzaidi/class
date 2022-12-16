list = [10, 5, 17, 23, 10, 5, 8, 8, 17, 17, 21, 12, 5, 11]
uniques_list = []
repeated_list = []
for i  in list:
    if i not in uniques_list:
        uniques_list.append(i)
    elif i not in repeated_list:
        repeated_list.append(i)
print(repeated_list)


# take 1000 values for 10 seconds and get the most repeated values printed the check for the 11 second with the
# next 1000 values from 100 to 1100

