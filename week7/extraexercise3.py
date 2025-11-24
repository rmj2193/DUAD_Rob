def sum_values(values_list):
    """
    Recorre una lista, intenta convertir cada elemento a float y los va sumando.
    Además va mostrando en pantalla qué se pudo sumar y qué no.
    Al final imprime el total.
    """
    # Inicializamos el acumulador en 0.0 porque vamos a trabajar con números decimales
    total_sum = 0.0

    # Recorremos cada elemento que venga en la lista que nos pasaron
    for element_value in values_list:
        try:
            # Intentamos convertir el valor actual a float.
            # Esto funciona si el valor es algo como "10", "3.5" o 7, pero fallará con "hola".
            numeric_value = float(element_value)

            # Si la conversión funcionó, lo sumamos al total acumulado
            total_sum += numeric_value

            # Avisamos que este valor sí se pudo sumar
            print(f"{numeric_value} \"added successfully\"")

        except ValueError:
            # Si NO se pudo convertir a float, caemos aquí
            # y avisamos cuál elemento fue inválido
            print(f"Invalid element: {element_value}")

    # Al terminar de recorrer toda la lista, mostramos el total final
    print("\"Total sum:\"", total_sum)