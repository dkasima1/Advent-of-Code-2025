import os

class solution:

    dial = 50
    password = 0
    input_arr = []

    def calculate_new_dial(self):
        for input in self.input_arr:
            direct = input[0]
            rotation = int(input[1::])
            if direct == 'R':
                new_dial = self.dial + rotation
                self.password += new_dial // 100
                self.dial = new_dial % 100
            elif direct == 'L':
                new_dial = (0 if self.dial == 0 else self.dial - 100) - rotation
                self.password += abs(new_dial) // 100
                self.dial = (new_dial + 100) % 100
            
    
    def read_txt_file(self, filepath):
        try:
            with open(filepath, 'r') as f:
                self.input_arr = f.readlines()
                for i in range(len(self.input_arr)):
                    self.input_arr[i] = self.input_arr[i].strip()
        except FileNotFoundError:
            print(f"Error: The file {filepath} was not found.")
    
    def get_password(self):
        return self.password
    
    def get_input_arr(self):
        return self.input_arr

    
if __name__ == "__main__":
    print(os.getcwd())
    find_password = solution()
    find_password.read_txt_file('./input.txt')
    find_password.calculate_new_dial()
    print(find_password.get_password())