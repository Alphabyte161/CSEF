# Model output handling and variable calculation
import wget
import os
import xarray as xr
# User input for run and date
date = int(input("Enter date in YYYYMMDD: "))
run = int(input("Enter valid run time in HH: "))
urlHRRR = {}
urlHRRRlag = {}
dateLag = date
if run == 00:
    runLag = 18
    dateLag = date - 1
else:
    runLag = run - 6
# URLs 
for i in range (0, 43):
    urlHRRR[f"url{i}"] = f"https://nomads.ncep.noaa.gov/cgi-bin/filter_hrrr_2d.pl?dir=%2Fhrrr.{date}%2Fconus&file=hrrr.t{run:02d}z.wrfsfcf{i:02d}.grib2&var_DPT=on&var_TMP=on&lev_2_m_above_ground=on"
for i in range (6, 49):
    urlHRRRlag[f"url{i}"] = f"https://nomads.ncep.noaa.gov/cgi-bin/filter_hrrr_2d.pl?dir=%2Fhrrr.{dateLag}%2Fconus&file=hrrr.t{runLag:02d}z.wrfsfcf{i:02d}.grib2&var_DPT=on&var_TMP=on&lev_2_m_above_ground=on"
# Delete old files if present
for file in os.listdir("gribs"):
    try:
        os.remove(f"gribs/{file}")
    except:
        break
# Grib downloading
for i in range(len(urlHRRR)):
    wget.download(urlHRRR[f"url{i}"], out=f"gribs/HRRR_{date}_{run:02d}_{i:02d}.grib2")
for i in range(6, 49):
    wget.download(urlHRRRlag[f"url{i}"], out=f"gribs/HRRR_{dateLag}_{runLag:02d}_{i:02d}.grib2")
# store datasets
dsHRRR = {}
dsHRRRlag = {}
for i in range(len(urlHRRR)):
    dsHRRR[f"ds{i:02d}"] = xr.open_dataset(f"gribs/HRRR_{date}_{run:02d}_{i:02d}.grib2", engine="cfgrib")
for i in range(6, 49):
    dsHRRRlag[f"ds{i-6:02d}"] = xr.open_dataset(f"gribs/HRRR_{dateLag}_{runLag:02d}_{i:02d}.grib2", engine="cfgrib")
# merge time-lagged HRRR
mergedHRRR = {}
for i in range(43):
    j = f"ds{i:02d}"
    mergedHRRR[j] = xr.concat([dsHRRRlag[j], dsHRRR[j]], dim="time")
# final data for usage in plots
outputs = {}
for i in range(43):
    data = mergedHRRR[f"ds{i:02d}"]
    outputs[i] = {
        "temp": {
            "max": data.t2m.max(dim="time"),
            "min": data.t2m.min(dim="time"),
            "avg": data.t2m.mean(dim="time")
        },
        "dpt": {
            "max": data.d2m.max(dim="time"),
            "min": data.d2m.min(dim="time"),
            "avg": data.d2m.mean(dim="time")
        }
    }