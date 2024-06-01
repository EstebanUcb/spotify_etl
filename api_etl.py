import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# Token de acceso
ACCESS_TOKEN = {"access_token": "BQBGiGMsS3cg48uUyDkdUPh-wsIeCAdzQpVGu1zV0PfaneojyPb1wtfxDFD2o4qu0R6uJsdqCnVWztQrLQW-VCeuXkVuG5me20ZuF-ewb0jF9WowhwQ", "token_type": "Bearer", "expires_in": 3600, "expires_at": 1717202947}

# Autenticación usando el token de acceso
sp = spotipy.Spotify(auth=ACCESS_TOKEN)

# Función para obtener datos de una playlist
def get_playlist_data(playlist_id):
    playlist = sp.playlist(playlist_id)
    playlist_data = {
        'id': playlist['id'],
        'name': playlist['name'],
        'description': playlist['description'],
        'owner': playlist['owner']['display_name'],
        'total_tracks': playlist['tracks']['total']
    }
    return playlist_data

# Función para obtener datos de las pistas de una playlist
def get_tracks_data(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    tracks_data = []
    for item in tracks:
        track = item['track']
        track_data = {
            'id': track['id'],
            'name': track['name'],
            'album_id': track['album']['id'],
            'artist_id': track['artists'][0]['id'],
            'duration_ms': track['duration_ms'],
            'popularity': track['popularity']
        }
        tracks_data.append(track_data)
    return tracks_data

# Función para obtener datos de los artistas
def get_artists_data(artist_ids):
    artists = sp.artists(artist_ids)['artists']
    artists_data = []
    for artist in artists:
        artist_data = {
            'id': artist['id'],
            'name': artist['name'],
            'popularity': artist['popularity'],
            'followers': artist['followers']['total']
        }
        artists_data.append(artist_data)
    return artists_data

# Función para obtener datos de los álbumes
def get_albums_data(album_ids):
    albums = sp.albums(album_ids)['albums']
    albums_data = []
    for album in albums:
        album_data = {
            'id': album['id'],
            'name': album['name'],
            'release_date': album['release_date'],
            'total_tracks': album['total_tracks'],
            'artist_id': album['artists'][0]['id']
        }
        albums_data.append(album_data)
    return albums_data

# IDs de ejemplo
playlist_id = '37i9dQZF1DXcBWIGoYBM5M'  # Ejemplo de una playlist de Spotify

# Obtener datos de la playlist
playlist_data = get_playlist_data(playlist_id)

# Obtener datos de las pistas
tracks_data = get_tracks_data(playlist_id)
track_ids = [track['id'] for track in tracks_data]
artist_ids = list(set([track['artist_id'] for track in tracks_data]))
album_ids = list(set([track['album_id'] for track in tracks_data]))

# Obtener datos de los artistas
artists_data = get_artists_data(artist_ids)

# Obtener datos de los álbumes
albums_data = get_albums_data(album_ids)

# Crear dataframes
df_playlist = pd.DataFrame([playlist_data])
df_tracks = pd.DataFrame(tracks_data)
df_artists = pd.DataFrame(artists_data)
df_albums = pd.DataFrame(albums_data)

# Guardar en CSV
df_playlist.to_csv('playlist.csv', index=False)
df_tracks.to_csv('tracks.csv', index=False)
df_artists.to_csv('artists.csv', index=False)
df_albums.to_csv('albums.csv', index=False)

print("Datos guardados en CSV correctamente.")
