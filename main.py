def add_file_together(some_file):
    sum_of_all_numbers = 0
    for i in some_file:
        nums = []
        for char in i:
            if char.isdigit():
                nums.append(char)

        if nums:
            first_num = nums[0]
            last_num = nums[-1]
            nums_str = nums[0] + nums[-1]
            combine_nums = int(nums_str)
            sum_of_all_numbers += combine_nums
    return sum_of_all_numbers

def read_doc(file_path):
     with open(file_path, "r") as file:
         return file.readlines()

some_file = read_doc("day_01.in")
result = add_file_together(some_file)
print(f"sum: {result}")