import spotipy
from spotipy.auth2 import SpotifyClientCredentials

client_credentials_manager= SpotifyClientCredentials(client_id="51aecabcbb3c45548534bf2aa91a4c11", client_secret="96731ba222a74e139b87a3117b6e338a")
sp=spotipy.Spotify(client_credentials_manager=client_credentials_manager)

user_data=sp.current_user()
#Print the user's account display name
print(user_data["display_name"])
