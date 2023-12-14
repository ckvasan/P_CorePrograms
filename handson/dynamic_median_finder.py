class median_finder:
    nums = []

    def add_num(self, n):
        median_finder.nums.append(n)

    def get_median(self):
        median_finder.nums.sort()
        print(median_finder.nums)
        size = len(median_finder.nums)
        if size % 2 == 0:
            if size == 2 :
                result = median_finder.nums[0] + median_finder.nums[1]
            else :
                result = median_finder.nums[int(size / 2)] + median_finder.nums[int(size / 2) + 1]
            return (result / 2)
        else:
            result = median_finder.nums[size // 2]
            return result



stream = [5, 2, 9, 1, 7, 6, 3, 8, 4]
median_finder = median_finder()

for num in stream:
    median_finder.add_num(num)
    current_median = median_finder.get_median()
    print(f"Current median after adding {num}: {current_median}")
