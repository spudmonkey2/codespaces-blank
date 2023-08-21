"""all my functions for 2022 advent of code"""
def import_data(file_loc):
    """imports the data and splits it line by line into a list"""
    advent_data = open(file_loc, "r",)
    advent_data = advent_data.read()
    advent_data = advent_data.splitlines()
    return advent_data

def add_by_split(user_list):
    """Adds all lines in a list that a group between 0 values"""
    list_index = 0
    temp_list =[]
    final_list =[]
    for x in user_list:
        if x != '':
            temp_list.append(int(x))
        elif x == '':
            final_list.append(sum(temp_list))
            temp_list =[]
        list_index += 1
    return final_list

def advent_day_one(day_one_text):
    """Finishes day one of Advent of Code just takes a txt file path"""
    data_list = import_data(day_one_text)
    added_list = add_by_split(data_list)
    added_list.sort(reverse=True)
    print("------------------------------------------------")
    print("Day One")
    print(added_list[0])
    print(added_list[0] + added_list[1] + added_list[2])
    print("------------------------------------------------")

def advent_day_two_p1(day_two_text):
    """Finishes Day Two"""
    day_2_list = import_data(day_two_text)
    point_list = []
    for line in day_2_list:
        if line[2] == "Z":
            if line[0] =="A":
                point_list.append(3)
            elif line[0] == "B":
                point_list.append(9)
            elif line[0] == "C":
                point_list.append(6)
        if line[2] == "Y":
            if line[0] =="A":
                point_list.append(8)
            elif line[0] == "B":
                point_list.append(5)
            elif line[0] == "C":
                point_list.append(2)
        if line[2] == "X":
            if line[0] =="A":
                point_list.append(4)
            elif line[0] == "B":
                point_list.append(1)
            elif line[0] == "C":
                point_list.append(7)
    print(sum(point_list))

def advent_day_two_p2(day_two_text):
    """Finishes Day Two P2"""
    day_2_list = import_data(day_two_text)
    point_list = []
    for line in day_2_list:
        if line[2] == "Z":
            if line[0] =="A":
                point_list.append(8)
            elif line[0] == "B":
                point_list.append(9)
            elif line[0] == "C":
                point_list.append(7)
        if line[2] == "Y":
            if line[0] =="A":
                point_list.append(4)
            elif line[0] == "B":
                point_list.append(5)
            elif line[0] == "C":
                point_list.append(6)
        if line[2] == "X":
            if line[0] =="A":
                point_list.append(3)
            elif line[0] == "B":
                point_list.append(1)
            elif line[0] == "C":
                point_list.append(2)
    print(sum(point_list))
##advent_day_one("adventofcode.com_2022_day_1_input.txt")
##advent_day_two_p1("adventofcode.com_2022_day_2_input.txt")
advent_day_two_p2("adventofcode.com_2022_day_2_input.txt")
