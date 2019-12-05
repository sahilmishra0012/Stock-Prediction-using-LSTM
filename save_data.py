import downloader
import os

class SaveData():
    def __init__(self,symbol):
        self.__symbol=symbol

    @property
    def symbol(self):
        return self.__symbol

    def save(self,file_dir,file_name,data):
        data_path=os.path.join(file_dir,file_name)
        if os.path.isdir(file_dir):
            data.to_csv(data_path,index=False)
        else:
            os.makedirs(file_dir)
            data.to_csv(data_path,index=False)