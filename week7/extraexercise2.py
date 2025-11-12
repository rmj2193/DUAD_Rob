def convertir_to_int(values_list):
    #Try to convert each element to int and report result
    for element_value in values_list:
        try:
            converted_value = int(element_value)
            print(f"\"{element_value}\" \"converted to\" {converted_value}")
        except ValueError:
            print(f"Could not convert element: {element_value}")