ways_array = []

def num_of_ways():
    return len(ways_array)
    
def ways_to_attend_classes(days):
    global ways_array
    pattern = ""
    ways_possible(days, pattern, ways_array)
    return ways_array

def ways_possible(days, pattern, ways_array):
    if days == 0:
        ways_array.append(pattern)
    else:
        # For given day there are two possibilities
        ways_possible(days - 1, pattern + 'A', ways_array)  # absent in class
        ways_possible(days - 1, pattern + 'P', ways_array)  # present in class

# Filter out ways where 4 or more consective days classes are missed
def invalid_ways_to_attend_classes():
    return list(filter(lambda way: "AAAA" in way, ways_array))
    
# Filter days where graduation is missed
def missed_graduation():
    return list(filter(lambda way: "A" == way[-1], ways_array))

def probability_to_miss_gradution_ceremony(days, all_missed_graduation):
    invalid_ways = invalid_ways_to_attend_classes()
    num_invalid_skips = len(list(filter(lambda way: "A" == way[-1], invalid_ways)))
    return f"{(all_missed_graduation - num_invalid_skips)}/{num_of_ways()-len(invalid_ways)}"

days = int(input('Enter the number of days '))
number_ways_to_attend = ways_to_attend_classes(days)
all_missed_graduation = len(missed_graduation())
print(probability_to_miss_gradution_ceremony(days,all_missed_graduation))
