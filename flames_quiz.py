FLAMES = {
    1: "Firends",
    2: "Lovers",
    3: "Admirers",
    4: "Marriage",
    5: "Enemies",
    0: "Secret Lovers",
}

def get_common_char(first, second):
    return set(first).intersection(set(second))

def name_check_and_return(name, common):
    temp = ""
    for ele in common:
        temp = name.lower().replace(ele, "")
        name = temp
    return temp
    
def name_checker(gender):
    name = input(f"Enter {gender} valid First Name: ")
    if name.isalpha():
        return name.lower()
    else:
        return name_checker(gender)


if __name__ == "__main__":
    first_name, second_name = name_checker("Male"), name_checker("Female")
    
    common_chars = get_common_char(first_name.lower(), second_name.lower())

    first = name_check_and_return(first_name, common_chars)
    second = name_check_and_return(second_name, common_chars)
    
    total_char_sum = len(first) + len(second)
    
    final_key = total_char_sum % 6
    
    print(FLAMES[final_key])
