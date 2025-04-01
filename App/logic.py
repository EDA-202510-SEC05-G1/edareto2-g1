import time
import copy
import csv
from datetime import datetime
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
                key_normalized = key.strip().lower()
                if msc.contains(catalog[map_name], key_normalized):
                    sll.add_last(msc.get(catalog[map_name], key_normalized), row)
                else:
                    new_list = sll.new_list()
                    sll.add_last(new_list, row)
                    msc.put(catalog[map_name], key_normalized, new_list)

            insert_in_map("catalog_by_state", row["state_name"])
            insert_in_map("catalog_by_year", str(year))  # año como string
            insert_in_map("catalog_by_category", row["statical_category"])
            insert_in_map("catalog_by_load_time", row["load_time"].strftime("%Y-%m-%d %H:%M:%S"))

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


def req_1(catalog, anio_interes):
    start = time.time()

    anio_interes = int(anio_interes)
    
    # Recorremos todas las claves del mapa y comparamos normalizadas
    key_set = msc.key_set(catalog["catalog_by_year"])["elements"]
    matched_key = None
    for k in key_set:
        if int(k) == anio_interes:
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
    registros = msc.get(catalog["catalog_by_year"], matched_key)
    

    total = registros["size"]
    ultimo_registro = None
    current = registros["first"]

    while current:
        record = current["info"]
        if not ultimo_registro or record["load_time"] > ultimo_registro["load_time"]:
            ultimo_registro = record
        current = current["next"]

    if not ultimo_registro:
        return {
            "execution_time_ms": 0,
            "total": 0,
            "registro": None
        }

    end = time.time()
    elapsed_ms = (end - start) * 1000

    return {
        "execution_time_ms": elapsed_ms,
        "total": total,
        "registro": {
            "year_collection": ultimo_registro["year_collection"],
            "load_time": ultimo_registro["load_time"].strftime("%Y-%m-%d"),
            "source": ultimo_registro["source"],
            "freq_collection": ultimo_registro["freq_collection"],
            "state_name": ultimo_registro["state_name"],
            "commodity": ultimo_registro["commodity"],
            "unit_measurement": ultimo_registro["unit_measurement"],
            "value": ultimo_registro["value"]
        }
    }



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


from datetime import datetime
import time
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sll
from DataStructures.Map import map_separate_chaining as msc

from datetime import datetime
import time

def req_6(catalog, nombre_departamento, fecha_inicio_str, fecha_fin_str):
    start = time.time()

    departamento_normalizado = nombre_departamento.strip().lower()

    # Recorremos claves normalizadas
    key_set = msc.key_set(catalog["catalog_by_state"])["elements"]
    matched_key = None
    for k in key_set:
        if k.strip().lower() == departamento_normalizado:
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

    category_list = msc.get(catalog["catalog_by_state"], matched_key)

    fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d")

    filtered = al.new_list()
    current = category_list["first"]
    while current:
        record = current["info"]
        fecha_carga = record["load_time"]
        if fecha_inicio <= fecha_carga <= fecha_fin:
            al.add_last(filtered, record)
        current = current["next"]

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


    # Convierte las fechas a objetos datetime
    #fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
    #fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d")




def req_7(catalog, nombre_departamento, anio_inicio, anio_fin, orden):
    import time
    from datetime import datetime

    start = time.time()

    departamento_normalizado = nombre_departamento.strip().lower()
    anio_inicio = int(anio_inicio)
    anio_fin = int(anio_fin)

    key_set = msc.key_set(catalog["catalog_by_state"])['elements']
    matched_key = None
    for k in key_set:
        if k.strip().lower() == departamento_normalizado:
            matched_key = k
            break

    if not matched_key:
        return {
            "execution_time_ms": 0,
            "total_registros": 0,
            "analisis": []
        }

    lista = msc.get(catalog["catalog_by_state"], matched_key)

    current = lista["first"]
    ingresos_por_anio = {}

    while current:
        record = current["info"]
        anio = record["year_collection"]
        unidad = record["unit_measurement"]

        if anio_inicio <= anio <= anio_fin and "$" in unidad:
            valor = record["value"]
            try:
                ingreso = float(valor.replace(",", ""))
                if anio not in ingresos_por_anio:
                    ingresos_por_anio[anio] = {
                        "ingresos": 0.0,
                        "total": 0,
                        "invalidos": 0,
                        "census": 0,
                        "survey": 0
                    }
                ingresos_por_anio[anio]["ingresos"] += ingreso
            except:
                ingresos_por_anio.setdefault(anio, {
                    "ingresos": 0.0,
                    "total": 0,
                    "invalidos": 0,
                    "census": 0,
                    "survey": 0
                })["invalidos"] += 1

            ingresos_por_anio[anio]["total"] += 1
            source = record["source"].strip().upper()
            if source == "CENSUS":
                ingresos_por_anio[anio]["census"] += 1
            elif source == "SURVEY":
                ingresos_por_anio[anio]["survey"] += 1

        current = current["next"]

    analisis = []
    for anio, data in ingresos_por_anio.items():
        analisis.append({
            "anio": anio,
            "ingresos": data["ingresos"],
            "total": data["total"],
            "invalidos": data["invalidos"],
            "census": data["census"],
            "survey": data["survey"]
        })

    analisis.sort(key=lambda x: (-x["ingresos"], -x["total"]) if orden == "DESCENDENTE" else (x["ingresos"], -x["total"]))

    if analisis:
        analisis[0]["indicador"] = "MAYOR" if orden == "DESCENDENTE" else "MENOR"
        analisis[-1]["indicador"] = "MENOR" if orden == "DESCENDENTE" else "MAYOR"

    if len(analisis) > 15:
        analisis = analisis[:5] + analisis[-5:]

    end = time.time()
    elapsed_ms = (end - start) * 1000

    return {
        "execution_time_ms": elapsed_ms,
        "total_registros": sum(x["total"] for x in ingresos_por_anio.values()),
        "analisis": analisis
    }



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
