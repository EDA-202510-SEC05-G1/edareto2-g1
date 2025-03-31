def new_list():
    newlist = {
        "elements": [],
        "size": 0
    }
    return newlist
def get_element(my_list, index):
    return my_list["elements"] [index]

def is_present(my_list, element, cmp_function):

    size = my_list["size"]
    keyexist = False
    if size > 0:
        for keypos in range(0, size):
            info = my_list ["elements"] [keypos ]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
    if keyexist:
        return keypos
    return -1   


def add_first(my_list, element):
    my_list["elements"] = [element] + my_list["elements"]  
    my_list["size"] += 1  
    return my_list


def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["size"] == 0:
        return None  
    return my_list["elements"][0]

def is_empty(my_list):
    return my_list["size"] == 0

def remove_first(my_list):
    if my_list["size"] == 0:
        return None  

    first_element = my_list["elements"][0]  
    my_list["elements"] = my_list["elements"][1:]  
    my_list["size"] = len(my_list["elements"])  
    
    return first_element

def remove_last(my_list):
    if my_list["size"] == 0:
        return None  

    last_element = my_list["elements"][-1]  
    my_list["elements"] = my_list["elements"][:-1]  
    my_list["size"] = len(my_list["elements"])  
    
    return last_element

def insert_element(my_list, element, pos):
    if pos < 0:
        pos = 0  
    elif pos > my_list["size"]:
        pos = my_list["size"]  
    
    my_list["elements"].append(None)  
    for i in range(my_list["size"], pos, -1):
        my_list["elements"][i] = my_list["elements"][i - 1]  

    my_list["elements"][pos] = element  
    my_list["size"] += 1  

    return my_list

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        return my_list  

    deleted_element = my_list["elements"][pos]


    for i in range(pos, my_list["size"] - 1):
        my_list["elements"][i] = my_list["elements"][i + 1]


    my_list["elements"].pop()
    my_list["size"] -= 1

    return my_list

def change_info(my_list, pos, new_info):
    if 0 <= pos < my_list["size"]:
        my_list["elements"][pos] = new_info
    return my_list


def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= my_list["size"]:
        return my_list  # preguntar
    
    if pos_2 < 0 or pos_2 >= my_list["size"]:
        return my_list  

    
    i = 0
    while i < my_list["size"]:
        if i == pos_1:
            t = my_list["elements"][i]
        if i == pos_2:
            my_list["elements"][pos_1] = my_list["elements"][i]
            my_list["elements"][i] = t
        i += 1

    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list["size"]:
        return my_list  


    w = min(pos_i + num_elements, my_list["size"])


    new_list = {"size": 0, "elements": []}
    for i in range(pos_i, w):
        new_list["elements"].append(my_list["elements"][i])
        new_list["size"] += 1

    return new_list

def default_sort_criteria(element_1, element_2):

   if not isinstance(element_1, dict) and not isinstance(element_2, dict):
       return element_1 < element_2
   else: 
       return float(element_1["average_rating"]) < float(element_2["average_rating"])

def selection_sort(my_list, sort_crit):
    elements = my_list["elements"]

    for i in range(len(elements) - 1):
        min_idx = i
        for j in range(i + 1, len(elements)):
            if sort_crit(elements[j], elements[min_idx]):
                min_idx = j
        elements[i], elements[min_idx] = elements[min_idx], elements[i]
        
    return my_list

def shell_sort(my_list, sort_crit):
    if my_list["size"] <= 1:
        return my_list  

    n = my_list["size"]
    gap = n // 2  

    while gap > 0:
        for i in range(gap, n):
            temp = my_list["elements"][i]
            j = i
            while j >= gap and sort_crit(temp, my_list["elements"][j - gap]):
                my_list["elements"][j] = my_list["elements"][j - gap]
                j -= gap
            my_list["elements"][j] = temp
        gap //= 2  

    return my_list

def merge_sort(my_list, sort_crit):
    if my_list["size"] <= 1:
        return my_list  
    
    middle = my_list["size"] // 2  
    left_list = sub_list(my_list, 0, middle)  
    right_list = sub_list(my_list, middle, my_list["size"] - middle)  
    
    left_sorted = merge_sort(left_list, sort_crit)  
    right_sorted = merge_sort(right_list, sort_crit)  
    return merge(left_sorted, right_sorted, sort_crit)  

def merge(left, right, sort_crit):
    result = new_list()  
    left_idx = 0
    right_idx = 0
    
    while left_idx < left["size"] and right_idx < right["size"]:
        if sort_crit(left["elements"][left_idx], right["elements"][right_idx]):
            add_last(result, left["elements"][left_idx])
            left_idx += 1
        else:
            add_last(result, right["elements"][right_idx])
            right_idx += 1
    
    while left_idx < left["size"]:
        add_last(result, left["elements"][left_idx])
        left_idx += 1
    
    while right_idx < right["size"]:
        add_last(result, right["elements"][right_idx])
        right_idx += 1
    
    return result

def quick_sort(my_list, sort_crit):
    if my_list["size"] <= 1:
        return my_list  
    pivot = my_list["elements"][0]
    left = new_list()
    right = new_list()
    equal = new_list()
    for i in range(my_list["size"]):
        current = my_list["elements"][i]
        if sort_crit(current, pivot):
            add_last(left, current)
        elif sort_crit(pivot, current):
            add_last(right, current)
        else:
            add_last(equal, current)
    sorted_left = quick_sort(left, sort_crit)
    sorted_right = quick_sort(right, sort_crit)
    sorted_list = new_list()
    sorted_list["elements"] = sorted_left["elements"] + equal["elements"] + sorted_right["elements"]
    sorted_list["size"] = len(sorted_list["elements"])
    return sorted_list

def insertion_sort(my_list, sort_crit):
    for i in range(1, my_list["size"]):
        key = my_list["elements"][i]
        j = i - 1
        while j >= 0 and sort_crit(key, my_list["elements"][j]):
            my_list["elements"][j + 1] = my_list["elements"][j]
            j -= 1
        my_list["elements"][j + 1] = key