def averge_Recort(X):
    measuremens_ordened = sorted(X) 
    size = len(measuremens_ordened) #The size of the list is 15
    for i in measuremens_ordened:
        i = i + 1
        delete_first = measuremens_ordened.pop(i)
        print(delete_first)
        if i == 3:
            break 
    return measuremens_ordened



if __name__ == "__main__":
    X = [3.4, 2.5, 4.8, 2.9, 3.6, 2.8, 3.3, 5.6, 3.7, 2.8, 4.4, 4.0, 5.2, 3.0, 4.8]
    print(f'The measurements ordened are: {averge_Recort(X)}')
    averge_Recort(X)