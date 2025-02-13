from geopy.geocoders import Nominatim

def obtener_ubicacion(direccion):
    try:
        geolocalizador = Nominatim(user_agent="mi_aplicacion_de_geolocalizacion")
        ubicacion = geolocalizador.geocode(direccion)
        return ubicacion
    except Exception as e:
        print(f"Error al obtener la ubicación: {e}")
        return None

def main():
    try:
        # Ingresar la dirección o lugar que quieres geolocalizar
        direccion_ingresada = input("Ingresa la dirección o lugar: ")

        # Obtener la ubicación
        ubicacion = obtener_ubicacion(direccion_ingresada)

        # Mostrar resultados
        if ubicacion:
            print(f"Ubicación encontrada para '{direccion_ingresada}':")
            print(f"Latitud: {ubicacion.latitude}")
            print(f"Longitud: {ubicacion.longitude}")
            print(f"País: {ubicacion.address.split(',')[-1].strip()}")  # Extraer el país de la dirección completa
        else:
            print(f"No se pudo encontrar la ubicación para '{direccion_ingresada}'.")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")

if __name__ == "__main__":
    main()
