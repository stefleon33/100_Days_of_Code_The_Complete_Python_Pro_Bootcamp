# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# print(format_name(input("What is your first name?"), input("What is your last name?")))


def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        return True
    elif year % 400 == 0:
        return True

print(is_leap_year(int(input("Enter a year: \n"))))


#or
#
# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
