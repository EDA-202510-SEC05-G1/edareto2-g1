
from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
import random as rd



def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime((num_elements / load_factor))
    

    table = lt.new_list()  
    

    table["elements"] = [me.new_map_entry(None, None) for _ in range(capacity)]
    table["size"] = capacity 

    return {
        "capacity": capacity,
        "size": 0,
        "prime": prime,
        "scale": rd.randint(1, prime - 1),
        "shift": rd.randint(0, prime - 1),
        "limit_factor": load_factor,
        "current_factor": 0,
        "table": table 
    }

def size(my_map):
    """
    Obtiene la cantidad de elementos en la tabla de símbolos.
    """
    return my_map['size']

def is_available(table, pos):

   entry = lt.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = lt.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def put(my_map, key, value):

    index = mf.hash_value(my_map, key)
    

    _, slot = find_slot(my_map, key, index)
    

    table = my_map['table']['elements']
    

    if table[slot]['key'] == key:
        table[slot]['value'] = value
    else:

        table[slot] = me.new_map_entry(key, value)
        my_map['size'] += 1
        my_map['current_factor'] = my_map['size'] / my_map['capacity']
        

        if my_map['current_factor'] > my_map['limit_factor']:
            my_map = rehash(my_map)
    
    return my_map
def rehash(my_map):
    """
    Realiza un rehash de la tabla de símbolos, creando una nueva tabla con el siguiente primo al doble de la capacidad actual
    y reinsertando los elementos existentes.
    """

    new_capacity = mf.next_prime(2 * my_map['capacity'])
    

    new_table = new_map(new_capacity, my_map['limit_factor'])
    

    for entry in my_map['table']['elements']:
        if entry['key'] is not None:
            new_table = put(new_table, entry['key'], entry['value'])
    
    return new_table

def is_available(table, pos):

   entry = lt.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def contains(my_map, key):
    """
    Valida si una llave dada se encuentra en la tabla de símbolos.
    """
    index = mf.hash_value(my_map, key) 
    found, _ = find_slot(my_map, key, index)  
    return found

def get(my_map, key):
    """
    Obtiene el valor asociado a una llave en la tabla de símbolos.
    Retorna None si la llave no se encuentra.
    """
    index = mf.hash_value(my_map, key)  
    found, slot = find_slot(my_map, key, index) 
    
    if found:
        return my_map['table']['elements'][slot]['value']  
    
    return None  

def remove(my_map, key):
    """
    Elimina una entrada de la tabla de símbolos asociada a una llave dada.
    """
    index = mf.hash_value(my_map, key)
    found, slot = find_slot(my_map, key, index)
    
    if found:
        my_map['table']['elements'][slot] = {'key': "__EMPTY__", 'value': "__EMPTY__"}
        my_map['size'] -= 1
    
    return my_map

def is_empty(my_map):
    """
    Verifica si la tabla de símbolos está vacía.
    """
    return my_map.get('size', 0) == 0

def key_set(my_map):
    keys = [entry["key"] for entry in my_map["table"]["elements"] if entry["key"] is not None and entry["key"] != '__EMPTY__']
    return {"size": len(keys), "elements": keys}

def value_set(my_map):
    """
    Retorna una lista con todos los valores almacenados en la tabla de símbolos.
    """
    values = [entry['value'] for entry in my_map['table']['elements'] if entry['key'] is not None and entry['key'] != "__EMPTY__"]
    return {"size": len(values), "elements": values}




# python3 ./run_tests.py