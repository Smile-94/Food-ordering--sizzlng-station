def category_directory_path(instance,filename):
    return 'Catagory{0}/{1}'.format(instance.category_name,filename)


def food_directory_path(instance,filename):
    return 'Food/{0}'.format(filename)

def set_menu_directory_path(instance,filename):
    return 'Set_Menu/{0}'.format(filename)