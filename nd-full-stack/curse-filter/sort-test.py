our_list = []

while True:
    try:
        number_in_list = int(raw_input("How many items are in your list to sort? "))
    except ValueError:
        print "I need an actual number! "
        continue
    
    for i in range(0, number_in_list):
        if i == 0:
            our_list.append(raw_input('Enter the first item in your list to sort: '))
        else:
            our_list.append(raw_input('Enter the next item in your list to sort: '))
    break

our_sorted_list = sorted(our_list)

print(our_sorted_list)
