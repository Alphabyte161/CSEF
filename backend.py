# Model output handling and variable calculation
import wget
import os
import xarray as xr

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
for i in range (0, 43):
    urlHRRR[f"url{i}"] = f"https://nomads.ncep.noaa.gov/cgi-bin/filter_hrrr_2d.pl?dir=%2Fhrrr.{date}%2Fconus&file=hrrr.t{run}z.wrfsfcf{i:02d}.grib2&var_DPT=on&var_TMP=on&lev_2_m_above_ground=on"
for i in range (6, 49):
    urlHRRRlag[f"url{i}"] = f"https://nomads.ncep.noaa.gov/cgi-bin/filter_hrrr_2d.pl?dir=%2Fhrrr.{dateLag}%2Fconus&file=hrrr.t{runLag}z.wrfsfcf{i:02d}.grib2&var_DPT=on&var_TMP=on&lev_2_m_above_ground=on"
for file in os.listdir("gribs"):
    try:
        os.remove(f"gribs/{file}")
    except:
        break
for i in range(len(urlHRRR)):
    wget.download(urlHRRR[f"url{i}"], out=f"gribs/HRRR_{date}_{run}_{i:02d}.grib2")
for i in range(6, len(urlHRRRlag)):
    wget.download(urlHRRRlag[f"url{i}"], out=f"gribs/HRRR_{dateLag}_{runLag}_{i:02d}.grib2")
    