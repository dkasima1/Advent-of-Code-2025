import os
import math

class solution:

    input_arr = []
    invalid = []

    def final_sum(self):
        return sum(self.invalid)
    
    def return_valid_range(self, range):
        split = range.split('-')
        range_0 = split[0]
        range_1 = split[1]
        final_range = []
        if len(range_0) % 2 == 0:
            final_range.append(range_0)
        else:
            range_0_int = int(range_0)
            new_range_exp = math.ceil(math.log10(range_0_int))
            new_range = 10 ** new_range_exp
            final_range.append(str(new_range))
        if len(range_1) % 2 == 0:
            final_range.append(range_1)
        else:
            range_1_int = int(range_1)
            new_range_exp = math.floor(math.log10(range_1_int))
            new_range = 10 ** new_range_exp - 1
            final_range.append(str(new_range))

        if int(final_range[0]) > int(final_range[1]):
            return None
        return final_range

    def find_invalid_ids(self):
        for i in self.input_arr:
            range_arr = self.return_valid_range(i)
            if not range_arr:
                continue
            start_int = int(range_arr[0])
            end_int = int(range_arr[1])
            if range_arr:
                start = int(range_arr[0][0:len(range_arr[0])//2])
                end = int(range_arr[1][0:len(range_arr[1])//2])
                for j in range(start, end+1):
                    val = int(str(j) + str(j))
                    if start_int <= val <= end_int:
                        self.invalid.append(val)
                    if val > end_int:
                        break

    
    def read_txt_file(self, filepath):
        with open(filepath, 'r') as f:
            input = f.readline()
            self.input_arr = input.split(',')
    
    def get_input_arr(self):
        return self.input_arr

class solution3:

    invalid = set()
    input_arr = []

    def final_sum(self):
        return sum(self.invalid)

    def read_txt_file(self, filepath):
        with open(filepath, 'r') as f:
            input = f.readline()
            self.input_arr = input.split(',')
    
    def find_if_invalid(self, num):
        i = 1
        while i <= len(num) // 2:
            char = num[0:i]
            rep = num.count(char)
            if rep > 1 and rep == math.ceil(len(num) / len(char)):
                self.invalid.add(int(num))
                break
            i += 1
        
    
    def find_invalid(self):
        for input in self.input_arr:
            split = input.split('-')
            range_0 = split[0]
            range_1 = split[1]
            for i in range(int(range_0), int(range_1) + 1):
                self.find_if_invalid(str(i))

if __name__ == "__main__":
    print(os.getcwd())
    final = solution()
    final.read_txt_file('./input.txt')
    input = final.get_input_arr()
    final.find_invalid_ids()
    print(final.final_sum())

    final3 = solution3()
    final3.read_txt_file('./input.txt')
    final3.find_invalid()
    print(final3.final_sum())

    
    