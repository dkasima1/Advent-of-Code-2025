class solution:

    invalid = set()
    input_arr = []

    def final_sum(self):
        return sum(self.invalid)

    def read_txt_file(self, filepath):
        with open(filepath, 'r') as f:
            input = f.readlines()
            for i in input:
                self.input_arr.append(i.strip())
    
    def find_max_for_two(self):
        final = []
        for input in self.input_arr:
            dp = []
            max_digit = '0'
            for i in input:
                if len(dp) == 0:
                    dp.append(i)
                    max_digit = i
                else:
                    dp.append(max_digit + i)
                    if int(i) > int(max_digit):
                        max_digit = i
            for i in range(len(dp)):
                dp[i] = int(dp[i])
            final.append(max(dp))
        return final
    
    def find_max_for_n(self, n):
        final = []
        for strng in self.input_arr:
            dp = []
            for i in range(len(strng)):
                dp.append([])
                for j in range(n):
                    dp[i].append(strng[i])
            for x in range(1,len(dp)):
                for y in range(1,len(dp[x])):
                    dp[x][y] = str(max(int(dp[x-1][y-1] + dp[x][0]), int(dp[x-1][y])))
                dp[x][0] = str(max(dp[x][0], dp[x-1][0]))
            final.append(int(dp[-1][-1]))
        return final




if __name__ == "__main__":
    final = solution()
    final.read_txt_file('./input.txt')
    print(sum(final.find_max_for_two()))
    print(sum(final.find_max_for_n(12)))