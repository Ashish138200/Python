phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

for no in phone_numbers.values():
    print(no,end=' ')