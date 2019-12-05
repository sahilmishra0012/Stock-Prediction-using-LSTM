import downloader
import os

def daata():
    data=downloader.load_yahoo_quote('GOOG','20190819','20190919')
    return data