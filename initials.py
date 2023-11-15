def get_initials(name):
    name_list = name.split(" ")
    initials = ""
    for name_section in name_list:
        initials += name_section[0]
    return initials