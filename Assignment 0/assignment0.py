import csv
class CustomList:
    def __init__(self, input):
        if type(input) != list or not all(isinstance(i, int) or isinstance(i, float) for i in input):
            print("Your input is not a list or list of only numbers")
            self.input = []
        else:
            self.input = input
        
    def __str__(self):
        return str(self.input)
    
    def maximum(self, input=[]):
        input = self.input
        if len(input) == 0:
            return None
        if len(input) == 1:
            return self.input[0]
        temp = input[0] if input[0] > input[1] else input[1]
        input[1] = temp
        self.input = input[1:]
        return self.maximum(self.input)
    
    def minimum(self):
        if len(self.input) == 0:
            return None
        min = self.input[0]
        for el in self.input:
            if el < min:
                min = el
        return min

def main():
    arr = []
    with open('random_numbers.csv', mode='r', encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file)
        for col in reader:
            arr.extend(col)
    arr = list(map(int, arr))
    print(arr)
    customList = CustomList(arr)
    print(customList.minimum())
    print(customList.maximum())

main()