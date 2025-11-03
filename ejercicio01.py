principal = ClasePrincipal()
interna = principal.ClaseInterna(principal)  # Crear instancia de la clase interna
interna.mostrar()
# No puedes acceder directamente a __ClaseInternaOculta
# intento_acceso = principal.__ClaseInternaOculta(principal)  # Esto generará un error
Accesibilidad:

    Las clases internas pueden ser accedidas a través de la clase principal.
    Para acceder a una clase interna, se utiliza la notación clase_principal.ClaseInterna().
    Los atributos privados no pueden ser accedidos directamente desde fuera de la clase, pero pueden ser accedidos por métodos públicos de la clase.
    Si intentas acceder a un atributo privado directamente (ej: mi_instancia.variable_privada), no funcionará y Python lanzará un AttributeError. En su lugar, deberás utilizar los métodos públicos proporcionados por la clase.
    Ejemplo de acceso a la clase interna:
principal = ClasePrincipal()
interna = principal.ClaseInterna(principal)  # Crear instancia de la clase interna
interna.mostrar()