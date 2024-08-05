import requests
import os
import gzip
import json
def download_gh():
    url="https://data.gharchive.org/2023-03-01-10.json.gz"
    path=os.path.join(os.getcwd(),"2023-03-01-10.json.gz")
    #print(os.getcwd())

    response = requests.get(url)

    if response.status_code==200:
        with open(path, "wb") as file:
                file.write(response.content)
    return path


def test_download_gh():
     path=download_gh()
     print(path)
     assert(os.path.exists(path))
     print("File is in correct location")
     assert os.path.getsize(path) > 0,  "Downloaded file is empty"
     print("File is not empty")
     assert path.endswith('.gz'), "File is not a gzip file"
     print("File is a gzip file")
     json_data=[]
     with gzip.open(path,'rt', encoding="utf-8") as filee:
          for i in filee:
               json_data.append(json.loads(i))
     assert len(json_data)>0 
     print("Read file sucessfully")
     print(json_data[2])

     print("end")
        
    

test_download_gh()


