from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=250) #歌手的名字應該不會超過250個char
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10) # 檔案類型應該不會超過10個字元(mp3等等)
    song_title = models.CharField(max_length=250)
