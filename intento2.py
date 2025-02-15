from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import difflib

def obtener_ubicacion(direccion):
    try:
        geolocalizador = Nominatim(user_agent="mi_aplicacion_de_geolocalizacion")
        ubicaciones = geolocalizador.geocode(direccion, exactly_one=False)

        if ubicaciones:
            mejor_coincidencia = ubicaciones[0]  # Tomamos la primera opción
            return mejor_coincidencia
        else:
            return None
    except GeocoderTimedOut:
        print("Error: La solicitud de geolocalización tardó demasiado.")
        return None
    except Exception as e:
        print(f"Error al obtener la ubicación: {e}")
        return None

def sugerir_lugar(lugar_ingresado, lugares_conocidos):
    coincidencias = difflib.get_close_matches(lugar_ingresado, lugares_conocidos, n=3, cutoff=0.5)
    return coincidencias if coincidencias else None

def main():
    lugares_comunes = ["Parque Central", "Hospital General", "Universidad Nacional", "Aeropuerto Internacional",
                       "Estadio Olímpico", "Centro Comercial Principal"]

    try:
        # Ingresar la dirección o lugar
        direccion_ingresada = input("Ingresa la dirección o descripción del lugar: ")

        # Sugerir lugares si la entrada es vaga
        sugerencias = sugerir_lugar(direccion_ingresada, lugares_comunes)
        if sugerencias:
            print(f"¿Quizás quisiste decir?: {', '.join(sugerencias)}")

        # Obtener la ubicación
        ubicacion = obtener_ubicacion(direccion_ingresada)

        # Mostrar resultados
        if ubicacion:
            print(f"\nUbicación encontrada para '{direccion_ingresada}':")
            print(f"Latitud: {ubicacion.latitude}")
            print(f"Longitud: {ubicacion.longitude}")
            print(f"Dirección completa: {ubicacion.address}")
        else:
            print(f"No se pudo encontrar la ubicación para '{direccion_ingresada}'.")
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")

if __name__ == "__main__":
    main()
