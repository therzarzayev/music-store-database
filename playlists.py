import mysql.connector as mc
import time


class Music():
    def __init__(self,name, artist, album, duration):
        self.name = name
        self.artist = artist
        self.album = album
        self.duration = duration

    def __str__(self):
        return "\nName: {0}\nArtist: {1}\nAlbum: {2}\nDuration: {3}\n".format(self.name, self.artist, self.album, self.duration)

    def __len__(self):
        return int(self.duration)


class Playlist():

    def __init__(self):
        self.connect_playlist_db()

    def connect_playlist_db(self):
        self.playlistsdb = mc.connect(
            host="host", # host ip or hostname
            user="user_name", # enter yourself username
            password="password", # enter yourself password
            database="music_db", # enter database_name
            auth_plugin="mysql_native_password"
        )
        self.cursor = self.playlistsdb.cursor()
        self.cursor.execute("create table if not exists playlists (id int auto_increment primary key not null, name varchar(255) not null, artist varchar(255) not null, album varchar(255) not null, duration float not null)")
        self.playlistsdb.commit()

    def get_playlists(self):
        sql = "select * from playlists"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        if len(res) == 0:
            print("Empty playlists!")
        else:
            for i in res:
                music = Music(i[1], i[2], i[3], i[4])
                print(music)

    def add_music(self, music):
        sql = "INSERT INTO playlists (name, artist, album, duration) values (%s, %s, %s, %s)"
        print("Music adding...")
        time.sleep(1)
        self.cursor.execute(sql, music)
        print("Music added successfully!\n")
        self.playlistsdb.commit()

    def del_music(self, music):
        sql_q = "SELECT name FROM playlists"
        sql = "delete from playlists where name=%s"
        self.cursor.execute(sql_q)
        res = self.cursor.fetchall()
        print("Delete music from playlists...")
        time.sleep(1)
        if music in [x[0] for x in res]:
            self.cursor.execute(sql, (music,))
            print("Music deleted successfully")
        else:
            print("ERROR: music not found")
        self.playlistsdb.commit()

    def find_music(self, music):
        sql = "SELECT * FROM playlists where name=%s"
        self.cursor.execute(sql,(music,))
        res = self.cursor.fetchall()
        if len(res)== 0:
            print("Music is not available in the playlist!")
        else:
            for i in res:
                msc = Music(i[1], i[2], i[3], i[4])

        print(msc)
    
    def get_total_duration(self):
        sql = "SELECT duration FROM playlists"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        tot=0
        for i in res:
            tot+=i[0]
        time.sleep(1)
        print(f"Total duration: {tot} minutes\n")

    def disconnect_playlist_db(self):
        self.cursor.close()
