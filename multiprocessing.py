import multiprocessing
import requests

def downloadfile(url, name):
    response =request.get(url)
    open(f"file{name}.jpg", 'wb').write(response.content)
    pass

url = 'https://unsplash.com/photos/gray-concrete-statue-near-white-wall-sXOGCu6wdU4'

for _ in range(5):
    downloadfile(url, i)