def binary_search(list, numberToFind):

    firstElem = 0  
    lastElem = len(list) - 1 
    middle = int((len(list))/2) 
    while firstElem <= lastElem:  
        if numberToFind == list[middle]: 
            return middle 
        if numberToFind < list[middle]: 
            lastElem = middle - 1 
        if numberToFind > list[middle]: 
            firstElem = middle + 1 

        middle = int((firstElem + lastElem) / 2)  

    return -1 


ourList = [1,2,3,7,8,9,11,15,18,19,27]
print("hello")
print(binary_search(ourList, 8))
print(binary_search(ourList, 19))