from playlists import *

playlists = Playlist()
print("""
*************************************
    Select operation number

1. Get playlists
2. Add music
3. Delete music
4. Find music
5. Total duration of playlists
q. Exit

*************************************
""", end="")
try:
    while True:
        operation = input("Select operation number :")
        if operation == "q" or operation == "Q":
            break
        elif operation == "1":
            playlists.get_playlists()

        elif operation == "2":
            name = input("Name: ")
            artist = input("Artist: ")
            album = input("Album: ")
            duration = input("Duration: ")
            music = (name, artist, album, duration)
            playlists.add_music(music)

        elif operation == "3":
            music = input("Enter music name: ")
            playlists.del_music(music)

        elif operation == "4":
            music = input("Enter music name: ")
            playlists.find_music(music)

        elif operation == "5":
            playlists.get_total_duration()

        else:
            print("Unknown operation")
            time.sleep(1)
            print("Operation cancelled!")
            break
except KeyboardInterrupt:
    print("\nCtrl+C pressed!")

finally:
    playlists.disconnect_playlist_db()
