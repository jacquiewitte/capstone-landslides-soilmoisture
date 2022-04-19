# ea-python-2022-capstone
<H1>This is the repo for the 2022 Earth Lab Capstone project</H1>

<H3>TITLE</H3>Where can soil moisture improve rainfall-triggered landslide predictability?

<H3>TEAM</H3>Jacquie Witte

<H3>PURPOSE</H3> Address the need to improve our understanding of landslides caused by rainfall. To better characterize
where and when these landslides occur.

<H3>DATA</H3>

<ol type="1">
  <li>NASA Global Landslide Catalog (2007-2016)
  <br>- Assembled and provided by Elsa Culler et al. in csv format.</li>

  <li>NASA SMAP Enhanced L3 Radiometer Global Daily 9 km EASE-Grid Soil Moisture V004
  <br> - Subsetting available via Earthdata 
  <br> - https://search.earthdata.nasa.gov
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

<H3>WORKFLOW</H3>

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

<H3>DELIVERABLES</H3>

<P> - CSV of 2007-2016 Colorado Landslides with co-located GPM precipitation and soil moisture parameters from SMAP, ESA, and Landsat.
<P> - CSV of time series of precipitation and soil moisture parameters leading up to a landslide.
<P> - Jupyter notebook(s) of plots and analysis based on the CSV database.

