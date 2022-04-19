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
<br>    - HDF5 format

(3) ESA Climate Change Initiative soil moisture version 03.3
    - https://cds.climate.copernicus.eu/cdsapp#!/dataset/satellite-soil-moisture?tab=overview
    - netCDF3 format

(4) Landsat Normalized Difference Moisture Index
    - https://www.usgs.gov/landsat-missions/normalized-difference-moisture-index
    - 

(5) GPM IMERG Late Precipitation L3 1 day 0.1 degree x 0.1 degree V06
    - Subsetting available via GES DISC using nearest neighbor gridding in Colorado Domain
    - https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDL_06/summary?keywords=%22IMERG%20late%22
    - netCDF4 format

WORKFLOW:

Read a subset of landslide events from Dataset (1) over Colorado only
       |
       |
       --> Read Datasets 2 - 5 --> match to time/location of Colorado Landslide event 
       	   	   	 |
			 |
			 --> Nearest neighbor, area average parameters (depends on the data set)
			 |
			 |
			 --> Add data to the subsetted Dataset (1) as a dataFrame:
			     	    data source, measurement(s), etc. and export as CSV for future use 
			     	    |
				    |
				    --> time series plots of precipitation accumulation leading up to the landslide
				    --> correlation plots of SMAP vs ESA soil moisture
				    --> distribution plots SMAP, ESA, Landsat soils and GPM

