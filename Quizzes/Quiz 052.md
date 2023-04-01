# Quiz 052

![image](https://user-images.githubusercontent.com/111758436/223024015-c9bc7d3c-f0fb-4627-b577-bdc07f51ab05.png)

## Codes
### My solution
```.py
# Program for Quiz 052

class MovieDownloader:
    def __init__(self, download_speed):
        if download_speed <= 0:
            raise ValueError("Download speed must be greater than 0")
        self.download_speed = download_speed

    def calculate_download_time(self, movie_size):
        if movie_size <= 0:
            raise ValueError("Movie size must be greater than 0")
        download_time_seconds = movie_size / (self.download_speed * 1024 * 1024 / 8)
        download_time_minutes = int(download_time_seconds // 60)
        download_time_seconds -= download_time_minutes * 60
        return f"{download_time_minutes} minutes {int(download_time_seconds)} seconds"
```
### Test code
```.py
import pytest
from Quiz_052 import MovieDownloader

def test_calculate_download_time():
    downloader = MovieDownloader(download_speed=10)
    movie_size = 1500 * 1024 * 1024  # 1500 MB
    assert downloader.calculate_download_time(movie_size) == "12 minutes 30 seconds"

    downloader = MovieDownloader(download_speed=5)
    movie_size = 500 * 1024 * 1024  # 500 MB
    assert downloader.calculate_download_time(movie_size) == "16 minutes 40 seconds"

def test_download_speed_validation():
    with pytest.raises(ValueError, match=r"Download speed must be greater than 0"):
        downloader = MovieDownloader(download_speed=0)
    with pytest.raises(ValueError, match=r"Download speed must be greater than 0"):
        downloader = MovieDownloader(download_speed=-10)

def test_movie_size_validation():
    downloader = MovieDownloader(download_speed=10)
    with pytest.raises(ValueError, match=r"Movie size must be greater than 0"):
        downloader.calculate_download_time(0)
    with pytest.raises(ValueError, match=r"Movie size must be greater than 0"):
        downloader.calculate_download_time(-100)
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/222615275-3d9fd186-1be8-407c-8a5c-275af487018a.png)
