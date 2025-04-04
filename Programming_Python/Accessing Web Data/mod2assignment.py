import re
# user_input = input("Please provide the file name:")

text_file_hanlde = open('sampletxt.txt')
sum_all_nums = 0
count = 0
for line in text_file_hanlde:
    list_nums = re.findall('[0-9]+',line)
    if(len(list_nums)>0):
        for nums in list_nums:
            count = count+1
            sum_all_nums = sum_all_nums + int(nums)

# print(count)
print(sum_all_nums)