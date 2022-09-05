# Radarr API Caller Library Class File
import requests, json

class SonarrApiCaller:

    def __init__(self, host, apikey):
        self.host = host
        self.apikey = apikey
        self.apiEndPoint = self.host + "/api"

    def GetCurrCommands(self):
        try:
            url = self.apiEndPoint + "/command?apikey=" + self.apikey
            r = requests.get(url)

            if r.status_code == 200:
                return r.json()
            else:
                return False
        except:
            return False

    def GetSeries(self):
        try:
            url = self.apiEndPoint + "/series?apikey=" + self.apikey
            r = requests.get(url)

            if r.status_code == 200:
                return r.json()
            else:
                return False
        except:
            return False

    def GetSeriesByID(self, id):
        try:
            url = self.apiEndPoint + "/series/" + str(id) + "?apikey=" + self.apikey
            r = requests.get(url)

            if r.status_code == 200:
                return r.json()
            else:
                return False
        except:
            return False

    def UpdateSeries(self, seriesJson):
        try:
            series = json.dumps(seriesJson)
            url = self.apiEndPoint + "/series?apikey=" + self.apikey
            r = requests.put(url, data=series)

            
            if r.status_code == 202:
                return r.json()
            else:
                return False
        except:
            return False

    def SeriesSearch(self, id):
        try:
            url = self.apiEndPoint + "/command?apikey=" + self.apikey
            r = requests.post(url, data=json.dumps({
                "name": "seriesSearch",
                "seriesId": int(id)
            }))

            if r.status_code == 202:
                return r.json()
            else:
                return False
        except:
            return False



 