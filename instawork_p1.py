import re
import unittest

class Phone:
    def __init__(self, name, color, price, storage, rating, url):
        self.name = name
        self.color = color
        self.price = price
        self.storage = storage
        self.rating = rating
        self.url = url
        

    def __str__(self):
        return str.format("Name: {}, Color: {}, Price: {}, Storage: {}, Rating: {}, Url: {}",\
                          self.name, self.color, self.price, self.storage, self.rating, self.url)


def merge(array, lo, hi, mid, comparator):
    left_part = array[lo : mid + 1]
    right_part = array[mid + 1 : hi + 1]

    i = 0 # pointer for left part 
    j = 0 # pointer for right part 
    sorted_index = lo # pointer for sorted part 

    while i < len(left_part) and j < len(right_part):

        if comparator(left_part[i], right_part[j]):
            array[sorted_index] = left_part[i]
            i += 1
        else:
            array[sorted_index] = right_part[j]
            j += 1

        sorted_index += 1

    while i < len(left_part):
        array[sorted_index] = left_part[i]
        i += 1
        sorted_index += 1

    while j < len(right_part):
        array[sorted_index] = right_part[j]
        j += 1
        sorted_index += 1


def merge_sort(array, lo, hi, comparator): 
    if lo >= hi:
        return

    mid = lo + int((hi - lo) / 2)

    merge_sort(array, lo, mid, comparator)
    merge_sort(array, mid + 1, hi, comparator)
    merge(array, lo, hi, mid, comparator)




def jsonSalesData(file_path: str):
    lineList = []
    f = open(file_path, 'r')

    lineList = [line.strip('\n') for line in f if '[' in line and ']' in line]


    phoneList = []
    for phone in lineList:
        
        info = phone.replace('[', '').replace(']', '').replace('“', '').replace('”', '')[:-1]
        
        splitInfo = info.split(", ")
        iPhone = Phone(splitInfo[0], splitInfo[1], splitInfo[2], splitInfo[3], splitInfo[4], splitInfo[5])

        phoneList.append(iPhone)

    merge_sort(phoneList, 0, len(phoneList) -1, \
                    lambda p1, p2: int(p1.price[1:]) < int(p2.price[1:]))
    
    file = open('outputfile.txt', 'w') 
  
    for iPhone in phoneList:
        file.write(str(iPhone))
        file.write("\n")
        print(iPhone)
    file.close() 
    
    returnList = [x.price for x in phoneList]
    return returnList


class TestStringMethods(unittest.TestCase):

    def test_jsonSalesData(self):
        path = '/Users/yujingke/Desktop/instawork_input.txt'
        self.assertEqual(jsonSalesData(path), ['$799', '$799', '$999', '$999', '$1099', '$1099'])

   

if __name__ == '__main__':
    unittest.main()
