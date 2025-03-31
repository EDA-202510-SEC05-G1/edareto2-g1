import time

import csv
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sll
from DataStructures.Map import map_separate_chaining as msc

def new_logic():
    """
    Crea el catálogo para almacenar las estructuras de datos
    """
    catalog = {
        "catalog_array": al.new_list(),  # lista principal
        "catalog_by_state": msc.new_map(100, 4),
        "catalog_by_year": msc.new_map(100, 4),
        "catalog_by_source": msc.new_map(100, 4),
        "catalog_by_commodity": msc.new_map(100, 4),
        "catalog_by_category": msc.new_map(100, 4),
        "catalog_by_unit": msc.new_map(100, 4),
        "catalog_by_freq": msc.new_map(100, 4),
        "catalog_by_reference": msc.new_map(100, 4),
        "catalog_by_load_time": msc.new_map(100, 4)
    }
    return catalog


import time
from datetime import datetime
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sll
from DataStructures.Map import map_separate_chaining as msc

def load_data(catalog, filename):
    start_time = time.process_time()
    min_year = float('inf')
    max_year = float('-inf')

    with open(filename, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["year_collection"] = int(row["year_collection"])
            row["load_time"] = datetime.strptime(row["load_time"], "%Y-%m-%d %H:%M:%S")

            al.add_last(catalog["catalog_array"], row)

            year = row["year_collection"]
            if year < min_year:
                min_year = year
            if year > max_year:
                max_year = year

            def insert_in_map(map_name, key):
                if msc.contains(catalog[map_name], key):
                    sll.add_last(msc.get(catalog[map_name], key), row)
                else:
                    new_list = sll.new_list()
                    sll.add_last(new_list, row)
                    msc.put(catalog[map_name], key, new_list)

            insert_in_map("catalog_by_state", row["state_name"])
            insert_in_map("catalog_by_year", year)
            insert_in_map("catalog_by_source", row["source"])
            insert_in_map("catalog_by_commodity", row["commodity"])
            insert_in_map("catalog_by_category", row["statical_category"])
            insert_in_map("catalog_by_unit", row["unit_measurement"])
            insert_in_map("catalog_by_freq", row["freq_collection"])
            insert_in_map("catalog_by_reference", row["reference_period"])
            insert_in_map("catalog_by_load_time", row["load_time"])

    def sort_criteria(r1, r2):
        if r1["load_time"] > r2["load_time"]:
            return True
        elif r1["load_time"] < r2["load_time"]:
            return False
        else:
            return r1["state_name"] < r2["state_name"]

    catalog["catalog_array"] = al.merge_sort(catalog["catalog_array"], sort_criteria)

    end_time = time.process_time()
    load_duration = end_time - start_time

    total_records = al.size(catalog["catalog_array"])
    first_5 = catalog["catalog_array"]["elements"][:5]
    last_5 = catalog["catalog_array"]["elements"][-5:]

    return {
        "catalog": catalog,
        "load_time": load_duration,
        "total_records": total_records,
        "min_year": min_year,
        "max_year": max_year,
        "first_5": first_5,
        "last_5": last_5
    }


def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
