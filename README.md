# ea-python-2022-capstone
This is the repo for the 2022 Earth Lab Capstone project

TITLE: Where can soil moisture improve rainfall-triggered landslide predictability?

TEAM: Jacquie Witte

PURPOSE: Address the need to improve our understanding of landslides caused by rainfall. To better characterize
where and when these landslides occur.

DATA:

(1) NASA Global Landslide Catalog (2007-2016)
<br>    - Assembled and provided by Elsa Culler et al. in csv format.

(2) NASA SMAP Enhanced L3 Radiometer Global Daily 9 km EASE-Grid Soil Moisture V004
<br>    - Subsetting available via Earthdata
<br>    - https://search.earthdata.nasa.gov/search/granules?p=C1931665183-NSIDC_ECS&pg[0][v]=f&pg[0][gsk]=-start_date&q=SMAP%20Enhanced%20L3%20Radiometer%20Global%20Daily%209%20km%20EASE-Grid%20Soil%20Moisture%20V004&tl=1650327763.795!3!!
<br>    - HDF5 format

(3) ESA Climate Change Initiative soil moisture version 03.3
<br>    - https://cds.climate.copernicus.eu/cdsapp#!/dataset/satellite-soil-moisture?tab=overview
<br>    - netCDF3 format

(4) Landsat Normalized Difference Moisture Index
<br>    - https://www.usgs.gov/landsat-missions/normalized-difference-moisture-index
<br>    - tif files

(5) GPM IMERG Late Precipitation L3 1 day 0.1 degree x 0.1 degree V06
<br>    - Subsetting available via GES DISC using nearest neighbor gridding in Colorado Domain
<br>    - https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDL_06/summary?keywords=%22IMERG%20late%22
<br>    - netCDF4 format

WORKFLOW:

Read a subset of landslide events from Dataset (1) over Colorado only
      <br> |
      <br> |
      <br> --> Read Datasets 2 - 5 --> match to time/location of Colorado Landslide event 
      <br> 	   	   	 |
<br>			 |
<br>			 --> Nearest neighbor, area average parameters (depends on the data set)
<br>			 |
<br>			 |
<br>			 --> Add data to the subsetted Dataset (1) as a dataFrame:
<br>			     	    data source, measurement(s), etc. and export as CSV for future use 
<br>			     	    |
<br>				    |
<br>				    --> time series plots of precipitation accumulation leading up to the landslide
<br>				    --> correlation plots of SMAP vs ESA soil moisture
<br>				    --> distribution plots SMAP, ESA, Landsat soils and GPM

