import requests
from xml.etree import ElementTree
import xmltodict
import pandas as pd

"""def apiCall(url):
    r = requests.get(url)
    return xmltodict.parse(r.content)
    

url = "https://api.entur.io/realtime/v1/rest/vm"
apiResult = apiCall(url)
df = pd.DataFrame.from_dict(apiResult)
print(df)"""

df = pd.DataFrame()