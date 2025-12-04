import os

class solution:

    roll_count = 0 
    input_arr = []

    def final_sum(self):
        return self.roll_count

    def read_txt_file(self, filepath):
        with open(filepath, 'r') as f:
            input = f.readlines()
            for i in input:
                self.input_arr.append(i.strip())
            for i in range(len(self.input_arr)):
                self.input_arr[i] = list(self.input_arr[i])
    
    def check_bounds(self, i, j):
        if i < 0 or i >= len(self.input_arr) or j < 0 or j >= len(self.input_arr[0]):
            return False
        return True
    
    def check_current_pos(self, i, j):
        if self.check_bounds(i,j) and self.input_arr[i][j] == '@':
            return 1
        return 0

    
    def find_roll_count(self):
        for i in range(len(self.input_arr)):
            for j in range(len(self.input_arr[i])):
                # Check all 8 positions
                if self.input_arr[i][j] == '.':
                    continue
                n = self.check_current_pos(i-1, j)
                ne = self.check_current_pos(i-1, j+1)
                e = self.check_current_pos(i, j+1)
                se = self.check_current_pos(i+1, j+1)
                s = self.check_current_pos(i+1, j)
                sw = self.check_current_pos(i+1, j-1)
                w = self.check_current_pos(i, j-1)
                nw = self.check_current_pos(i-1, j-1)
                if sum((n,ne,e,se,s,sw,w,nw)) < 4:
                    self.roll_count += 1
    
    def find_roll_count_p2(self):
        iter = 1
        while iter > 0:
            iter = 0
            for i in range(len(self.input_arr)):
                for j in range(len(self.input_arr[i])):
                    # Check all 8 positions
                    if self.input_arr[i][j] == '.' or self.input_arr[i][j] == 'x':
                        continue
                    n = self.check_current_pos(i-1, j)
                    ne = self.check_current_pos(i-1, j+1)
                    e = self.check_current_pos(i, j+1)
                    se = self.check_current_pos(i+1, j+1)
                    s = self.check_current_pos(i+1, j)
                    sw = self.check_current_pos(i+1, j-1)
                    w = self.check_current_pos(i, j-1)
                    nw = self.check_current_pos(i-1, j-1)
                    if sum((n,ne,e,se,s,sw,w,nw)) < 4:
                        self.roll_count += 1
                        self.input_arr[i][j] = 'x'
                        iter += 1
    
    




if __name__ == "__main__":
    print(os.getcwd())
    final = solution()
    final.read_txt_file('./input.txt')
    final.find_roll_count_p2()
    print(final.final_sum())