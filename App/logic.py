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

        "catalog_by_category": msc.new_map(100, 4),
        "catalog_by_load_time": msc.new_map(100, 4)
    }
    return catalog


import time
import csv
from datetime import datetime
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sll
from DataStructures.Map import map_separate_chaining as msc

def load_data(catalog, filename):
    start_time = time.time()
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
            insert_in_map("catalog_by_category", row["statical_category"])
            insert_in_map("catalog_by_load_time", row["load_time"])

    def sort_criteria(r1, r2):
        if r1["load_time"] > r2["load_time"]:
            return True
        elif r1["load_time"] < r2["load_time"]:
            return False
        else:
            return r1["state_name"] < r2["state_name"]

    catalog["catalog_array"] = al.merge_sort(catalog["catalog_array"], sort_criteria)

    end_time = time.time()
    load_duration = (end_time - start_time) * 1000  # en milisegundos

    total_records = al.size(catalog["catalog_array"])
    first_5 = catalog["catalog_array"]["elements"][:5]
    last_5 = catalog["catalog_array"]["elements"][-5:]

    return {
        "catalog": catalog,
        "execution_time_ms": load_duration,
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
import time
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sll
from DataStructures.Map import map_separate_chaining as msc

def req_5(catalog, categoria_estadistica, anio_inicio, anio_fin):
    start = time.time()

    categoria_normalizada = categoria_estadistica.strip().lower()

    # Recorremos todas las claves del mapa y comparamos normalizadas
    key_set = msc.key_set(catalog["catalog_by_category"])["elements"]
    matched_key = None
    for k in key_set:
        if k.strip().lower() == categoria_normalizada:
            matched_key = k
            break

    if not matched_key:
        return {
            "execution_time_ms": 0,
            "total": 0,
            "census_count": 0,
            "survey_count": 0,
            "records": []
        }

    # Obtenemos la lista enlazada de registros por esa categoría
    category_list = msc.get(catalog["catalog_by_category"], matched_key)

    # Filtrar por año
    filtered = al.new_list()
    current = category_list["first"]
    while current:
        record = current["info"]
        year = record["year_collection"]
        if int(anio_inicio) <= int(year) <= int(anio_fin):
            al.add_last(filtered, record)
        current = current["next"]

    # Ordenar por load_time descendente y state_name ascendente
    def sort_criteria(r1, r2):
        if r1["load_time"] > r2["load_time"]:
            return True
        elif r1["load_time"] < r2["load_time"]:
            return False
        else:
            return r1["state_name"] < r2["state_name"]

    sorted_filtered = al.merge_sort(filtered, sort_criteria)

    total = al.size(sorted_filtered)
    census_count = 0
    survey_count = 0
    final_records = []

    for rec in sorted_filtered["elements"]:
        tipo = rec["source"].strip().upper()
        if tipo == "CENSUS":
            census_count += 1
        elif tipo == "SURVEY":
            survey_count += 1

        final_records.append({
            "source": tipo,
            "year_collection": rec["year_collection"],
            "load_time": rec["load_time"].strftime("%Y-%m-%d"),
            "freq_collection": rec["freq_collection"],
            "state_name": rec["state_name"],
            "unit_measurement": rec["unit_measurement"],
            "commodity": rec["commodity"]
        })

    if total > 20:
        final_records = final_records[:5] + final_records[-5:]

    end = time.time()
    elapsed_ms = (end - start) * 1000

    return {
        "execution_time_ms": elapsed_ms,
        "total": total,
        "census_count": census_count,
        "survey_count": survey_count,
        "records": final_records
    }


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
