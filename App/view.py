

import sys
from App import logic as lg
import csv

def new_logic():
    """
        Se crea una instancia del controlador
    """
    return lg.new_logic()
    

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control, filename):
    """
    Carga los datos y muestra información general
    """
    result = lg.load_data(control, filename)
    
    print("Tiempo de ejecución: {:.2f} ms".format(result["execution_time_ms"]))
    print("Total de registros cargados:", result["total_records"])
    print("Menor año de recolección:", result["min_year"])
    print("Mayor año de recolección:", result["max_year"])

    print("\nPrimeros 5 registros:")
    for rec in result["first_5"]:
        print(rec)

    print("\nÚltimos 5 registros:")
    for rec in result["last_5"]:
        print(rec)


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    print(lg.get_data(control,id))

def print_req_1(control):
    """
    Función que imprime la solución del Requerimiento 1 en consola
    """
    anio = input("Ingrese el año: ")
    result = lg.req_1(control, anio)
    
    print(result)



def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    departamento = input("Ingrese el departamento: ")
    result = lg.req_2(control, departamento)

    if result is None:
        print("No se encontraron registros para este departamento.")
    else:
        print("\n--- Resultado del Requerimiento 2 ---\n")
        print(f"Tiempo de ejecución: {result['execution_time_ms']} ms")
        print(f"Total de registros: {result['total_records']}")

        last_record = result['last_record_linked']

        if last_record:
            print("\nÚltimo registro cargado:")
            print("  - Primer registro:")
            print(f"      Año de recolección: {last_record['first']['info']['year_of_collection']}")
            print(f"      Fecha de carga: {last_record['first']['info']['load_time']}")
            print(f"      Fuente: {last_record['first']['info']['source']}")
            print(f"      Frecuencia de colección: {last_record['first']['info']['collection_frequency']}")
            print(f"      Estado: {last_record['first']['info']['state_name']}")
            print(f"      Producto: {last_record['first']['info']['commodity']}")
            print(f"      Unidad de medida: {last_record['first']['info']['unit_of_measurement']}")
            print(f"      Valor: {last_record['first']['info']['value']}")

            print("  - Último registro:")
            print(f"      Año de recolección: {last_record['last']['info']['year_of_collection']}")
            print(f"      Fecha de carga: {last_record['last']['info']['load_time']}")
            print(f"      Fuente: {last_record['last']['info']['source']}")
            print(f"      Frecuencia de colección: {last_record['last']['info']['collection_frequency']}")
            print(f"      Estado: {last_record['last']['info']['state_name']}")
            print(f"      Producto: {last_record['last']['info']['commodity']}")
            print(f"      Unidad de medida: {last_record['last']['info']['unit_of_measurement']}")
            print(f"      Valor: {last_record['last']['info']['value']}")

            print(f"\nTamaño del registro: {last_record['size']}")

        print("\n-------------------------------------\n")


def print_req_3(control):
    """
    Función que imprime la solución del Requerimiento 3 en consola
    """
    producto = input("Ingrese el producto: ")
    anio_inicio = input("Ingrese el año de inicio (YYYY): ")
    anio_fin = input("Ingrese el año de fin (YYYY): ")

    result = lg.req_3(control, producto, anio_inicio, anio_fin)

    if not result or result['total_records'] == 0:
        print("No se encontraron registros para los parámetros proporcionados.")
        return

    print("\n--- Resultado del Requerimiento 3 ---\n")
    print(f" Tiempo de ejecución: {result['execution_time_ms']:.2f} ms")
    print(f" Total de registros procesados: {result['total_records']}")

    print("\n Detalles de los registros encontrados:")

    for index, record in enumerate(result['records'], start=1):
        print(f"\n Registro #{index}")
        print(f"   Año de recolección: {record.get('year_of_collection', 'Desconocido')}")
        print(f"   Fecha de carga: {record.get('load_time', 'Desconocido')}")
        print(f"   Fuente: {record.get('source', 'Desconocido')}")
        print(f"   Frecuencia de recolección: {record.get('collection_frequency', 'Desconocido')}")
        print(f"   Departamento: {record.get('state_name', 'Desconocido')}")
        print(f"   Producto: {record.get('commodity', 'Desconocido')}")
        print(f"   Unidad de medida: {record.get('unit_of_measurement', 'Desconocido')}")
        print(f"   Valor: {record.get('value', 'Desconocido')}")

    print("\n Fin del resultado del Requerimiento 3")


def print_req_4(catalog):
    """
    Carlos Alberto Quijano Mier
    Función que imprime la solución del Requerimiento 4 en consola
    """
    categoria_estadistica = input("Ingrese la categoría: ")
    anio_inicio = int(input("Ingrese el año de inicio: "))
    anio_fin = int(input("Ingrese el año de final: "))

    result = lg.req_4(catalog, categoria_estadistica, anio_inicio, anio_fin)

    if result is None:
        print("No se encontraron registros para este departamento.")
    else:
        print("Tiempo de ejecución:", result["delta_time"], "ms")
        print("Total de registros:", result["total_records"])
        print("Total de surveys:", result["total_survey"])
        print("Total de census:", result["total_census"])
        print("Records:")
        for record in result["records"]:
            print(record)

def print_req_5(control):
    """
    Función que imprime la solución del Requerimiento 5 en consola
    y solicita los parámetros al usuario.
    """
    print("📥 Por favor, ingresa los parámetros para el Requerimiento 5:\n")
    
    categoria_estadistica = input("🔎 Categoría estadística: ")  # Ej: INVENTORY
    anio_inicio = input("📅 Año de inicio (YYYY): ")             # Ej: 2007
    anio_fin = input("📅 Año de fin (YYYY): ")                   # Ej: 2010

    # Llamar a la función req_5 con los parámetros proporcionados
    resultado = lg.req_5(control, categoria_estadistica, anio_inicio, anio_fin)

    print(resultado)





def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    state_name = input("Ingrese el nombre del estado: ")
    start_date = input("Ingrese la fecha de inicio (formato YYYY-MM-DD): ")
    end_date = input("Ingrese la fecha de fin (formato YYYY-MM-DD): ")
    result = lg.req_6(control, state_name, start_date, end_date)

    print(result)

def print_req_7(control):
    """
    Función que imprime la solución del Requerimiento 7 en consola
    """
    state_name = input("Ingrese el nombre del estado: ")
    start_date = input("Ingrese el año de inicio: ")
    end_date = input("Ingrese el año de fin: ")
    orden = input("Ingrese el tipo de ordenamiento (ASCENDENTE o DESCENDENTE): ").strip().upper()

    result = lg.req_7(control, state_name, start_date, end_date, orden)
    print(result)


def print_req_8(control):
    result = req_8(control)
    
    print(f"Tiempo de ejecución del requerimiento 8: {result['execution_time_ms']} ms")
    print(f"Número total de departamentos: {result['total_departments']}")
    print(f"Tiempo promedio de carga de todos los departamentos: {result['avg_load_time']} años")
    print(f"Menor año de inicio de recopilación de registros: {result['min_year']}")
    print(f"Mayor año de inicio de recopilación de registros: {result['max_year']}")
    
    print("\nDepartamento con mayor diferencia promedio entre la recopilación y carga de registros:")
    department_info = result['department_with_max_diff']
    print(f"Nombre del departamento: {department_info['department_name']}")
    print(f"Tiempo promedio entre recopilación y carga de registros: {department_info['avg_diff']} años")
    print(f"Número de registros del departamento: {department_info['num_records']}")
    print(f"Menor año de inicio de recopilación de registros del departamento: {department_info['min_year']}")
    print(f"Mayor año de inicio de recopilación de registros del departamento: {department_info['max_year']}")
    print(f"Menor tiempo entre recopilación y carga de un registro: {department_info['min_diff']} años")
    print(f"Mayor tiempo entre recopilación y carga de un registro: {department_info['max_diff']} años")
    print(f"Número total de registros con tipo de fuente/origen 'SURVEY': {department_info['survey_count']}")
    print(f"Número total de registros con tipo de fuente/origen 'CENSUS': {department_info['census_count']}")



# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control,"data/agricultural-100.csv")
            
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)