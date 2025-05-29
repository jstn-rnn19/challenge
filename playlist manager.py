class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.is_public = False

    def add_song(self, song_title):
        self.songs.append(song_title)

    def delete_song(self, song_title):
        if song_title in self.songs:
            self.songs.remove(song_title)

    def show_song(self):
        for song in self.songs:
            print(song)

    def toggle_public(self):
        self.is_public = True
    def toggle_private(self):
        self.is_public = False


    def info(self):
        print(f"Name: {self.name}")
        print( f"Songs: {self.songs}" )
        print( f"Public: {self.is_public}" )

s1 = Playlist("justine")

s1.add_song("Museo")
s1.add_song("Dulo ng Hangganan")
s1.info()