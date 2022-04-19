# ea-python-2022-capstone
<H2>This is the repo for the 2022 Earth Lab Capstone project</H2>

<u><b>TITLE</b></u>: Where can soil moisture improve rainfall-triggered landslide predictability?

<u><b>TEAM</b></u>: Jacquie Witte

<u><b>PURPOSE</u></b>: Address the need to improve our understanding of landslides caused by rainfall. To better characterize
where and when these landslides occur.

<u><b>DATA</u></b>

<ol type="1">
  <li>NASA Global Landslide Catalog (2007-2016)
  <br>- Assembled and provided by Elsa Culler et al. in csv format.</li>

  <li>NASA SMAP Enhanced L3 Radiometer Global Daily 9 km EASE-Grid Soil Moisture V004
  <br> - Subsetting available via Earthdata 
  <br> - https://search.earthdata.nasa.gov/search/granules?p=C1931665183-NSIDC_ECS&pg[0][v]=f&pg[0][gsk]=-start_date&q=SMAP%20Enhanced%20L3%20Radiometer%20Global%20Daily%209%20km%20EASE-Grid%20Soil%20Moisture%20V004&tl=1650327763.795!3!!
  <br> - HDF5 format</li>

  <li>ESA Climate Change Initiative soil moisture version 03.3
  <br> - https://cds.climate.copernicus.eu/cdsapp#!/dataset/satellite-soil-moisture?tab=overview
  <br> - netCDF3 format</li>

  <li>Landsat Normalized Difference Moisture Index
  <br> - In Landsat 4-7, NDMI = (Band 4 – Band 5) / (Band 4 + Band 5).
  <br> - In Landsat 8, NDMI = (Band 5 – Band 6) / (Band 5 + Band 6).
  <br> - https://www.usgs.gov/landsat-missions/normalized-difference-moisture-index
  <br> - tif files through an API or download request</li>

  <li>GPM IMERG Late Precipitation L3 1 day 0.1 degree x 0.1 degree V06
  <br> - Subsetting available via GES DISC over the Colorado Domain
  <br> - Nearest neighbor remapping of fields between grids in spherical coordinates.
  <br> - https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDL_06/summary?keywords=%22IMERG%20late%22
  <br> - netCDF4 format</li>
</ol>  

<u><b>WORKFLOW</u></b>

Read a subset of landslide events from Dataset (1) over Colorado only
<br>&emsp;|
<br>&emsp;--> Read Datasets 2 - 5 --> match to time/location of Colorado Landslide event 
<br>&emsp;&emsp;|
<br>&emsp;&emsp;--> Nearest neighbor, area average parameters (depends on the data set)
<br>&emsp;&emsp;&emsp;|
<br>&emsp;&emsp;&emsp;--> Add data to the subsetted Dataset (1) as a dataFrame:
<br>&emsp;&emsp;&emsp;&emsp;data source, measurement(s), etc. and export as CSV for future use 
<br>&emsp;&emsp;&emsp;&emsp;&emsp;|
<br>&emsp;&emsp;&emsp;&emsp;&emsp;--> time series plots of precipitation accumulation leading up to the landslide
<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;- note, this may be its own notebook
<br>&emsp;&emsp;&emsp;&emsp;&emsp;--> correlation plots of SMAP vs ESA soil moisture
<br>&emsp;&emsp;&emsp;&emsp;&emsp;--> distribution plots SMAP, ESA, Landsat soils and GPM

<u><b>DELIVERABLES</u></b>

<P> - CSV of 2007-2016 Colorado Landslides with co-located GPM precipitation and soil moisture parameters from SMAP, ESA, and Landsat
<P> - Jupyter notebook(s) of plots and analysis based on the CSV database.

