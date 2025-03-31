import random
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sll
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf



def new_map(num_elements, load_factor, prime=109345121):
    """Crea una nueva tabla de símbolos con separate chaining."""
    capacity = mf.next_prime(int(num_elements / load_factor))
    scale = 1  
    shift = 0 
    
    table = al.new_list()
    for _ in range(capacity):
        al.add_last(table, sll.new_list())
    
    return {
        'prime': prime,
        'capacity': capacity,
        'scale': scale,
        'shift': shift,
        'table': table,
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0
    }


def put(my_map, key, value):
    index = mf.hash_value(my_map, key)
    bucket = my_map['table']['elements'][index]


    def cmp_function(element, node_info):
        return 0 if element == node_info["key"] else -1

    pos = sll.is_present(bucket, key, cmp_function)

    if pos != -1:  
        temp = bucket["first"]
        for _ in range(pos):
            temp = temp["next"]
        temp["info"]["value"] = value
        return my_map


    new_entry = {"key": key, "value": value}
    sll.add_last(bucket, new_entry)


    my_map["size"] += 1
    my_map["current_factor"] = my_map["size"] / my_map["capacity"]


    if my_map["current_factor"] > my_map["limit_factor"]:
        my_map = rehash(my_map)

    return my_map

def default_compare(key, element):
    """
    Compara la llave key con la llave de una entry dada.

    Parameters:
    key (any) - Llave con la que se desea comparar.
    element (map_entry) - Entrada de la tabla de símbolos con la que se desea comparar.

    Returns:
    0 si son iguales, 1 si key > la llave del element, -1 si key < que la llave del element
    """

    entry_key = me.get_key(element)


    if key == entry_key:
        return 0
    elif key > entry_key:
        return 1
    else:
        return -1
    
def contains(my_map, key):
    """
    Verifica si una llave se encuentra en la tabla de simbolos.

    Parameters:
    my_map (map_separate_chaining) - Tabla de simbolos en la cual se desea verificar si la llave se encuentra.
    key (any) - Llave que se desea verificar si se encuentra en la tabla.

    Returns:
    True si la llave se encuentra en la tabla, False en caso contrario.
    """

    index = mf.hash_value(my_map, key)
    

    bucket = my_map['table']['elements'][index]
    

    current = bucket['first']
    while current is not None:
        if current['info']['key'] == key:
            return True
        current = current['next']
    

    return False



def remove(my_map, key):

    index = my_map["shift"] + (key % my_map["prime"]) % my_map["capacity"]


    current = my_map["table"]["elements"][index]["first"]
    

    if current is None:
        return my_map
    

    prev = None
    while current:
        if current["info"]["key"] == key:

            if prev is None:
                my_map["table"]["elements"][index]["first"] = current["next"]
            else:
                prev["next"] = current["next"]
            

            if current["next"] is None:
                my_map["table"]["elements"][index]["last"] = prev
            

            my_map["table"]["elements"][index]["size"] -= 1
            my_map["size"] -= 1
            return my_map
        
        prev = current
        current = current["next"]
    

    return my_map

def get(my_map, key):

    
    index = hash(key) % my_map['capacity']
    

    
    bucket = my_map['table']['elements'][index]
    

    searchpos = 0
    node = bucket['first']
    

    while node is not None:

        if node['info']['key'] == key:
            return node['info']['value']
        node = node['next']
        searchpos += 1
    

    return None
def size(my_map):
    return my_map['size']

def is_empty(my_map):
    return my_map['size'] == 0

def key_set(my_map):
    keys = []
    for element in my_map['table']['elements']:
        current = element['first']
        while current:
            keys.append(current['info']['key'])
            current = current['next']
    return {'elements': keys, 'size': len(keys)}

def value_set(my_map):
    values = []
    for element in my_map['table']['elements']:
        current = element['first']
        while current:
            values.append(current['info']['value'])
            current = current['next']
    return {'elements': values, 'size': len(values)}

def rehash(my_map):
    """
    Realiza un rehashing del mapa, aumentando su capacidad y redistribuyendo las entradas.
    
    :param my_map: El mapa original que necesita ser rehashado.
    :return: El mapa con la nueva capacidad y las entradas reinsertadas.
    """

    new_capacity = mf.next_prime(my_map['capacity'] * 2)  
    

    new_hash_map = new_map(new_capacity, my_map['limit_factor'], my_map['prime'])
    

    for i in range(len(my_map["table"]["elements"])):  
        bucket = my_map["table"]["elements"][i]  
    
        current = bucket["first"]  
    

        while current is not None:
            key = current["info"]["key"]  
            value = current["info"]["value"]  
            
            
            new_hash_map = put(new_hash_map, key, value)  
            
            
            current = current["next"]
    
    
    my_map["table"]["elements"] = new_hash_map["table"]["elements"]
    my_map["capacity"] = new_hash_map["capacity"]
    my_map["size"] = new_hash_map["size"]
    
    
    return my_map






#python3 ./run_tests.py