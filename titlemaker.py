#####################
##   TITLE MAKER   ##
#####################

user_input_text = input("Please Enter Title : ").upper()
max_width = len(user_input_text) + 10
len_user_input_text = len(user_input_text)

if isinstance((max_width - len_user_input_text) / 2, float):
    print("#" * max_width)
    text_first_space = int((max_width - len_user_input_text) / 2) - 1
    print("#" * (text_first_space - 2) + " " * (text_first_space - 1) + user_input_text + " " * (text_first_space - 1) + "#" * (text_first_space - 2))
    print("#" * max_width)


else:
    print("#" * max_width)
    text_first_space = int((max_width - len_user_input_text) / 2)
    print("#" * (text_first_space - 2) + " " * (text_first_space - 1) + user_input_text + " " * (text_first_space - 1) + "#" * (text_first_space - 2))
    print("#" * max_width)