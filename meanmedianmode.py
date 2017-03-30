import time


def median(data):
    data.sort()
    llength = len(data)
    middle = llength/2
    evenmedian = (data[int(middle)] + data[int(middle - 1)]) / 2
    if llength % 2 == 1:
        print('the median is: ' , data[int(middle)])
    else:
        print('the Median is: ' , evenmedian)


def mode(data):
    most = max(set(data), key=data.count)
    print('the mode is: ' , most , '\n')


def mean(data):
    average = sum(data) / len(data)
    print('\nthe mean is: ', average)

def open_data():
    filename = input('Enter filename: ')
    dataset = []
    with open(filename, 'r') as f_obj:
        for line in f_obj:
            line = line.strip() 
            dataset.append(line)

    final_dataset = list(map(float, dataset))
    return final_dataset
     
def man_enter_data():
    length = int(input('How many values are in the list? '))
    print('Enter the values:')

    dataset = []
    for i in range(length):
        nums = float(input())
        dataset.append(nums)
        if len(dataset) == length:
            return dataset
        else:
            continue

def source():
    method = input('Do you want to open a file or enter manually? (OPEN/MANUAL)> ')
    if method == 'OPEN':
        dataset = open_data()
        return dataset

    elif method == 'MANUAL':
        dataset = man_enter_data()
        return dataset

def restart():
    return input('Restart (y/n)? ').lower() == 'y'

        
while True:
    try:
        dataset = source()
        mean(dataset)
        median(dataset)
        mode(dataset)

        if not restart(): break            
        
    except Exception:
        print('There is an error in the program. Restarting program...')
        time.sleep(2)   
        continue
