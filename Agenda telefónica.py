class Contacto:
    """
    Representa el Registro o Estructura de datos individual 
    para almacenar la información de un contacto.
    """
    def __init__(self, nombre: str, telefono: str, email: str, categoria: str):
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
        self._categoria = categoria

    # Métodos Getters y Setters 
    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def telefono(self) -> str:
        return self._telefono

    @property
    def email(self) -> str:
        return self._email

    @property
    def categoria(self) -> str:
        return self._categoria


class Agenda:
    """
    Controlador del sistema que administra el Vector de objetos 
    Contacto y ejecuta los procesos principales del negocio.
    """
    def __init__(self):
        # Vector/Arreglo que contendrá los registros de tipo Contacto
        self._contactos = []

    def registrar_contacto(self, nombre: str, telefono: str, email: str, categoria: str) -> bool:
        """Proceso: Registrar un nuevo elemento en la estructura de datos."""
        # Validación básica para evitar nombres vacíos
        if not nombre.strip() or not telefono.strip():
            return False
        
        nuevo_contacto = Contacto(nombre.strip(), telefono.strip(), email.strip(), categoria.strip())
        self._contactos.append(nuevo_contacto)
        return True

    def consultar_contacto(self, nombre_busqueda: str) -> list:
        """Proceso: Consulta de elementos bajo un criterio de coincidencia."""
        resultados = []
        for contacto in self._contactos:
            if nombre_busqueda.lower() in contacto.nombre.lower():
                resultados.append(contacto)
        return resultados

    def obtener_reporte(self) -> list:
        """Característica de Reportería: Retorna los elementos de la estructura."""
        return self._contactos


def ejecutar_menu():
    """Función de interfaz de usuario por consola."""
    agenda = Agenda()
    
    # Datos semilla de prueba
    agenda.registrar_contacto("Maria Elena", "0987654321", "maria@mail.com", "Trabajo")
    agenda.registrar_contacto("Carlos Perez", "0991234567", "carlos@mail.com", "Personal")

    while True:
        print("\n" + "="*40)
        print("         SISTEMA DE AGENDA TELEFÓNICA")
        print("="*40)
        print("1. Registrar Contacto")
        print("2. Consultar Contacto")
        print("3. Visualizar Reporte General")
        print("4. Salir")
        print("="*40)
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            print("\n--- Registrar Nuevo Contacto ---")
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Correo Electrónico: ")
            categoria = input("Categoría (Personal, Trabajo, etc.): ")
            
            exito = agenda.registrar_contacto(nombre, telefono, email, categoria)
            if exito:
                print("¡Contacto registrado exitosamente!")
            else:
                print("Error: El nombre y el teléfono son campos obligatorios.")
                
        elif opcion == "2":
            print("\n--- Consultar Contacto ---")
            criterio = input("Ingrese el nombre a buscar: ")
            resultados = agenda.consultar_contacto(criterio)
            
            if resultados:
                print(f"\nSe encontraron {len(resultados)} coincidencia(s):")
                print(f"{'Nombre':<20} | {'Teléfono':<15} | {'Email':<25} | {'Categoría':<15}")
                print("-" * 80)
                for c in resultados:
                    print(f"{c.nombre:<20} | {c.telefono:<15} | {c.email:<25} | {c.categoria:<15}")
            else:
                print("No se encontraron contactos con ese criterio.")
                
        elif opcion == "3":
            print("\n--- Reportería General de Contactos ---")
            lista_contactos = agenda.obtener_reporte()
            
            if lista_contactos:
                print(f"{'No.':<4} | {'Nombre':<20} | {'Teléfono':<15} | {'Email':<25} | {'Categoría':<15}")
                print("-" * 85)
                for i, c in enumerate(lista_contactos, start=1):
                    print(f"{i:<4} | {c.nombre:<20} | {c.telefono:<15} | {c.email:<25} | {c.categoria:<15}")
            else:
                print("La agenda se encuentra vacía.")
                
        elif opcion == "4":
            print("\nSaliendo del sistema de agenda. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_menu()