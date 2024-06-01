import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import datetime

def get_spotify_data():
    # Configuración de autenticación con la API de Spotify
    scope = "user-library-read user-read-recently-played"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                                   client_id='a4563a0e308a48fc8bc9b6bdf6e47c7e',
                                                   client_secret='a986dd6cd27941eab7a136a5e5cdc5b9',
                                                   redirect_uri='http://localhost:8888/callback'))

    # Obtener los datos de reproducción recientes
    recently_played = sp.current_user_recently_played(limit=50)  # Limitamos a las últimas 50 canciones reproducidas

    # Obtener las canciones guardadas en la biblioteca del usuario
    saved_tracks = sp.current_user_saved_tracks(limit=50)  # Limitamos a las últimas 50 canciones guardadas

    return recently_played, saved_tracks

def process_spotify_data(recently_played, saved_tracks):
    # Procesar datos de reproducción recientes
    recent_tracks_data = []
    for item in recently_played['items']:
        track = item['track']
        track_data = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'genre': '',  # No disponible directamente desde la API de Spotify
            'played_at': datetime.datetime.strptime(item['played_at'], "%Y-%m-%dT%H:%M:%S.%fZ"),
            'duration_ms': track['duration_ms'],
            'repeat_count': 1
        }
        recent_tracks_data.append(track_data)

    # Procesar datos de canciones guardadas
    saved_tracks_data = []
    for item in saved_tracks['items']:
        track = item['track']
        track_data = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'genre': '',  # No disponible directamente desde la API de Spotify
            'played_at': None,  # No aplicable para canciones guardadas
            'duration_ms': track['duration_ms'],
            'repeat_count': 0  # No aplicable para canciones guardadas
        }
        saved_tracks_data.append(track_data)

    # Combinar los datos de reproducción recientes y las canciones guardadas
    all_tracks_data = recent_tracks_data + saved_tracks_data

    # Crear un DataFrame de Pandas
    df = pd.DataFrame(all_tracks_data)

    return df

def main():
    # Obtener datos de Spotify
    recently_played, saved_tracks = get_spotify_data()

    # Procesar datos
    df = process_spotify_data(recently_played, saved_tracks)

    # Guardar los datos en un archivo CSV
    df.to_csv('spotify_playback_data.csv', index=False)

    print("Datos guardados exitosamente en spotify_playback_data.csv")

if __name__ == "__main__":
    main()


