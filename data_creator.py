import downloader
import pandas as pd

class Create():

    def create_data(self,symbol,start_date,end_date):
        data=downloader.load_yahoo_quote(symbol,start_date,end_date)
        column=data[0].split(',')
        new_data=data[1:-1]
        data_list=[]
        for i in new_data:
            data_list.append(i.split(','))

        df=pd.DataFrame(data_list,columns=column)
        return df