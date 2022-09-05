#!/usr/bin/python3
from SonarrApiCaller import SonarrApiCaller
import logging

file_location = "/home/plex/SonarrMonitorFix/app.log" # Log location, full path but may want to change based on set up

logging.basicConfig(filename=file_location, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s", level=logging.DEBUG)

logging.info("Starting Sonarr Monitor Fixing App.")
print("Starting Sonarr Monitor Fixing App. Check app.log for more info.")

sonarr = SonarrApiCaller("http://localhost:8989", "API KEY GOES HERE") # Set a valid Sonarr API Key

logging.info("Getting all series...")
all_series = sonarr.GetSeries()

logging.info("Finding all series which match monitor criteria...")
series_to_fix = []
for series in all_series:
    try:
        # Monitor criteria (eg. series count less than 336 and statis is continuing)
        if(int(series["episodeCount"]) < 336 and series["status"] == "continuing"):
            for season in series["seasons"]:
                if(season["seasonNumber"] != 0 and season["monitored"] == False):
                    series_to_fix.append(series)
                    break
    except Exception as e:
        if(series["title"]):
            logging.error("Issue with Series: " + str(series["title"]) + " - Message: " + str(e))
        else:
            logging.error(str(e))
        continue

logging.info("Found " + str(len(series_to_fix)) + " series with a season that is not set to Monitored.")

for series in series_to_fix:
    try:
        logging.info("Fixing " + series["title"] + "...")
        series["monitored"] = True
        for season in series["seasons"]:
            if(season["seasonNumber"] != 0):
                season["monitored"] = True

        r = sonarr.UpdateSeries(series)
    except Exception as e:
        if(series["title"]):
            logging.error("Issue with Series: " + str(series["title"]) + " - Message: " + str(e))
        else:
            logging.error(str(e))
        continue