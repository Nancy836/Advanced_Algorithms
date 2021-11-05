from collections import Counter  # importing the dict subclass Counter to count how many times
# each color appears and store the colors and their counts in a dictionary as keys and values


def matchingSocks(n, ar):

    dictionary = Counter(ar)  # using the Counter which will store the colors as keys and their counts as values in a dictionary
    count = dictionary.values()  # count is the number of times each color appears in the array
    pairs = 0

    for x in count:  # let the value in the dictionary be x
        pairs = pairs + x // 2  # dividing the count values by 2 to get the number of pairs, whole numbers only.

    return pairs


n1 = 30
array1 = (30,1,9,94,5,9,7,5,7,29,5,7,9,1,2,5,8,22,10,9,9,15,2,9,10,10,2,7,3) # first array with 30 elements
print(matchingSocks(n1,array1))

n2 = 80
array2 = (8,19,9,15,10,11,16,19,7,8,3,13,17,17,8,4,9,14,15,11,12,20,20,\
         7,12,6,18,9,20,9,15,13,16,4,2,10,7,16,14,5,18,1,13,7,11,9,8,9,2,\
         10,8,3,11,9,2,7,17,13,19,2,19,6,7,19,8,20,10,18,15,3,16,19,1,9,13,17,14,4,6,15) # first array with 80 elements

print(matchingSocks(n2,array2))