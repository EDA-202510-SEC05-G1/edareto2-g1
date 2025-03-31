def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist
def get_element (my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node ["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    new = {"info": element, "next": my_list["first"]}
    my_list["first"] = new
    if my_list["size"] == 0:
        my_list["last"] = new 
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    new = {"info": element, "next": None}
    
    if my_list["size"] == 0:
        
        my_list["first"] = new
        my_list["last"] = new 
    else:
        my_list["last"]["next"] = new
        my_list["last"] = new
    
    my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["size"] == 0:
        return None  
    return my_list["first"]["info"]

def last_element(my_list):
    return my_list["last"]["info"] if my_list["last"] else None


def is_empty(my_list):
    return my_list["first"] is None

def remove_first(my_list):
    if my_list["first"] is None:
        return None
    removed_element = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1
    return removed_element

def remove_last(my_list):
    if my_list["first"] is None:
        return None
    
    if my_list["first"] == my_list["last"]:
        removed_element = my_list["first"]["info"]
        my_list["first"] = my_list["last"] = None
        my_list["size"] -= 1
        return removed_element
    
    t = my_list["first"]
    while t["next"] != my_list["last"]:
        t = t["next"]
    removed_element = my_list["last"]["info"]
    t["next"] = None
    my_list["last"] = t
    my_list["size"] -= 1
    return removed_element


def insert_element(my_list, element, pos):
    new_node = {"info": element, "next": None}
    
    if pos == 0:
        new_node["next"] = my_list["first"]
        my_list["first"] = new_node
        if my_list["last"] is None:
            my_list["last"] = new_node
    else:
        temp = my_list["first"]
        for i in range(pos - 1):
            if temp is None:
                return my_list  
        new_node["next"] = temp["next"]
        temp["next"] = new_node
        if new_node["next"] is None:
            my_list["last"] = new_node
    
    my_list["size"] += 1
    return my_list


def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        return my_list  

    if pos == 0:
        my_list["first"] = my_list["first"]["next"]
        if my_list["first"] is None:  
            my_list["last"] = None  
    else:
        prev = my_list["first"]
        i = 0
        while i < pos - 1:
            prev = prev["next"]
            i += 1

        prev["next"] = prev["next"]["next"]
        if prev["next"] is None:  
            my_list["last"] = prev  

    my_list["size"] -= 1
    return my_list


def change_info(my_list, pos, new_info):
    temp = my_list["first"]
    for i in range(pos):
        if temp is None:
            return my_list  
        temp = temp["next"]
    temp["info"] = new_info
    return my_list


def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= my_list["size"] or pos_2 < 0 or pos_2 >= my_list["size"]:
        return my_list  
    if pos_1 == pos_2:
        return my_list
    
    node_1 = my_list["first"]
    node_2 = my_list["first"]
    
    for i in range(pos_1):
        node_1 = node_1["next"]
    for i in range(pos_2):
        node_2 = node_2["next"]
    
    node_1["info"], node_2["info"] = node_2["info"], node_1["info"]
    return my_list


def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list["size"]:
        return {"first": None, "last": None, "size": 0}  
    new_sublist = {"first": None, "last": None, "size": 0}
    r = my_list["first"]
    count = 0

    while count < pos_i:
        r = r["next"]
        count += 1

    new_first = r
    new_last = new_first
    new_size = 1
    count = 1

    while count < num_elements and new_last["next"] is not None:
        new_last = new_last["next"]
        count += 1
        new_size += 1

    new_sublist["first"] = new_first
    new_sublist["last"] = new_last
    new_sublist["size"] = new_size

    return new_sublist

def default_sort_criteria(element_1, element_2):

   if not isinstance(element_1, dict) and not isinstance(element_2, dict):
       return element_1 < element_2
   else: 
       return float(element_1["average_rating"]) < float(element_2["average_rating"])

def selection_sort(my_list, sort_crit):
    if not my_list or my_list.get("size") <= 1:
        return my_list

    current = my_list["first"]

    while current:
        min_node = current
        searcher = current.get("next")

        while searcher:
            if sort_crit(searcher["info"], min_node["info"]):
                min_node = searcher
            searcher = searcher.get("next")

        if min_node != current:
            current["info"], min_node["info"] = min_node["info"], current["info"]

        current = current.get("next")

    return my_list

def shell_sort(my_list, sort_crit):
    if my_list["size"] <= 1:
        return my_list  

    
    arr = []
    current = my_list["first"]
    while current:
        arr.append(current["info"])
        current = current["next"]
    
    
    n = len(arr)
    gap = n // 2  
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and not sort_crit(arr[j - gap], temp):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    
    
    current = my_list["first"]
    for value in arr:
        current["info"] = value
        current = current["next"]
    
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
    left_node = left["first"]
    right_node = right["first"]
    
    while left_node and right_node:
        if sort_crit(left_node["info"], right_node["info"]):
            add_last(result, left_node["info"])
            left_node = left_node["next"]
        else:
            add_last(result, right_node["info"])
            right_node = right_node["next"]
    
    while left_node:
        add_last(result, left_node["info"])
        left_node = left_node["next"]
    
    while right_node:
        add_last(result, right_node["info"])
        right_node = right_node["next"]
    
    return result

def quick_sort(my_list, sort_crit):
    if my_list["size"] <= 1:
        return my_list  

    pivot = my_list["first"] 
    left = new_list()
    right = new_list()
    equal = new_list()

    current = my_list["first"]
    while current:
        if sort_crit(current["info"], pivot["info"]):  
            add_last(left, current["info"])
        elif sort_crit(pivot["info"], current["info"]):  
            add_last(right, current["info"])
        else:  
            add_last(equal, current["info"])
        current = current["next"]

    sorted_left = quick_sort(left, sort_crit)
    sorted_right = quick_sort(right, sort_crit)

    # Combinamos las listas en orden
    sorted_list = new_list()
    
    if sorted_left["first"]:
        sorted_list["first"] = sorted_left["first"]
        sorted_list["last"] = sorted_left["last"]
        sorted_list["size"] += sorted_left["size"]

    if equal["first"]:
        if sorted_list["first"]:
            sorted_list["last"]["next"] = equal["first"]
        else:
            sorted_list["first"] = equal["first"]
        sorted_list["last"] = equal["last"]
        sorted_list["size"] += equal["size"]

    if sorted_right["first"]:
        if sorted_list["first"]:
            sorted_list["last"]["next"] = sorted_right["first"]
        else:
            sorted_list["first"] = sorted_right["first"]
        sorted_list["last"] = sorted_right["last"]
        sorted_list["size"] += sorted_right["size"]

    return sorted_list

def insertion_sort(my_list, sort_crit):
    if my_list["size"] < 2:
        return my_list  
    
    sorted_list = new_list()
    current = my_list["first"]
    
    while current:
        element = current["info"]
        if is_empty(sorted_list):
            add_first(sorted_list, element)
        else:
            temp = sorted_list["first"]
            prev = None
            while temp and sort_crit(temp["info"], element):
                prev = temp
                temp = temp["next"]
            
            if prev is None:
                add_first(sorted_list, element)
            else:
                new_node = {"info": element, "next": temp}
                prev["next"] = new_node
                if temp is None:
                    sorted_list["last"] = new_node
                sorted_list["size"] += 1
        
        current = current["next"]
    
    return sorted_list