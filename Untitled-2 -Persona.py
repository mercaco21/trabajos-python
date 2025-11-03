def procesar_datos(datos):
  """Procesa datos de diferentes tipos."""
  if isinstance(datos, list):
      # Si los datos son una lista, se itera y se imprime cada elemento
      for item in datos:
          print(f"Elemento de la lista: {item}")
  elif isinstance(datos, dict):
      # Si los datos son un diccionario, se itera y se imprime cada clave y valor
      for key, value in datos.items():
          print(f"Clave: {key}, Valor: {value}")
  else:
      # Si los datos son de otro tipo, se muestra un mensaje
      print(f"Tipo de dato desconocido: {type(datos)}")

# Ejemplos de uso
procesar_datos([1, 2, 3])     # Salida para una lista
procesar_datos({"a": 1, "b": 2}) # Salida para un diccionario
procesar_datos(123)           # Salida para otro tipo de dato