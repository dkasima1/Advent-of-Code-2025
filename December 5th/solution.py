import os

class solution:

    ranges = []
    ids = []
    valid = 0
    invalid = 0
    total_fresh = 0

    def final_sum(self):
        return self.roll_count

    def read_txt_file(self, filepath):
        with open(filepath, 'r') as f:
            for line in f:
                curr = line.strip()
                if curr == '':
                    continue
                if curr.count("-") == 1:
                    currRange = curr.split('-')
                    currRange[0] = int(currRange[0])
                    currRange[1] = int(currRange[1])
                    self.ranges.append(currRange)
                else:
                    self.ids.append(int(curr))
            self.ranges.sort()
            self.ids.sort()
    
    def merge_ranges(self):
        finalRanges = [self.ranges[0]]
        for i in range(1,len(self.ranges)):
            if finalRanges[-1][1] >= self.ranges[i][0]:
                finalRanges[-1][1] = max(finalRanges[-1][1], self.ranges[i][1])
            else:
                finalRanges.append(self.ranges[i])
        self.ranges = finalRanges

    def count_invalid(self):
        for i in range(len(self.ids)):
            currId = self.ids[i]
            for j in range(len(self.ranges)):
                start = self.ranges[j][0]
                end = self.ranges[j][1]
                if start <= currId <= end:
                    self.valid += 1
                elif currId < start:
                    self.invalid += 1
                    break
        print(f"Fresh: {self.valid}")
        print(f"Not Fresh: {self.invalid}")
    
    def count_fresh_total(self):
        for i in range(len(self.ranges)):
            self.total_fresh += (self.ranges[i][1] - self.ranges[i][0] + 1)
        print(self.total_fresh)

if __name__ == "__main__":
    print(os.getcwd())
    final = solution()
    final.read_txt_file('./input.txt')
    final.merge_ranges()
    final.count_invalid()
    final.count_fresh_total()