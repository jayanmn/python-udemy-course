# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    # first_letter = name[0]
    # inbetween = name[1:3]  # does not include name[3]
    # fourth = name[3]
    # rest = name[4:]
    # return first_letter.upper() + inbetween + fourth.upper() + rest

    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()

    # modified_name = ""
    # curr_index = 0
    # for i in name:
    #     if curr_index == 0 or curr_index == 3:
    #         i = i.upper()
    #     modified_name = modified_name + i
    #     curr_index = curr_index + 1
    # return modified_name
    # pass
