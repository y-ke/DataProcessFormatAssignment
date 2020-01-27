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
    leftPart = array[lo : mid + 1]
    rightPart = array[mid + 1 : hi + 1]

    i = 0 # pointer for left part 
    j = 0 # pointer for right part 
    sortedIndex = lo # pointer for sorted part 

    while i < len(leftPart) and j < len(rightPart):

        if comparator(leftPart[i], rightPart[j]):
            array[sortedIndex] = leftPart[i]
            i += 1
        else:
            array[sortedIndex] = rightPart[j]
            j += 1

        sortedIndex += 1

    while i < len(leftPart):
        array[sortedIndex] = leftPart[i]
        i += 1
        sortedIndex += 1

    while j < len(rightPart):
        array[sortedIndex] = rightPart[j]
        j += 1
        sortedIndex += 1


def mergeSort(array, lo, hi, comparator): 
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

    mergeSort(phoneList, 0, len(phoneList) -1, \
                    lambda p1, p2: int(p1.price[1:]) < int(p2.price[1:]))
    
    file = open('outputfile.txt', 'w') 
  
    for iPhone in phoneList:
        file.write(str(iPhone))
        file.write("\n")
        print(iPhone)
    file.close() 
    
    returnList = [x.price for x in phoneList]
    return returnList


class TestJSONSalesDataMethods(unittest.TestCase):

    def test_jsonSalesData(self):
        path = '../instawork_input.txt'
        self.assertEqual(jsonSalesData(path), ['$799', '$799', '$999', '$999', '$1099', '$1099'])

   

if __name__ == '__main__':
    unittest.main()
