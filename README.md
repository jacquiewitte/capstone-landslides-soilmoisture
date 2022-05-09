# capstone-landslides-soilmoisture
<H1>Repo for the 2022 Earth Lab Capstone project</H1>

<H3>TITLE</H3>Where can soil moisture improve rainfall-triggered landslide predictability?

<H3>TEAM</H3>Jacquie Witte

<H3>DESCRIPTION</H3>Landslide prediction is important. There are negative economic, transportation, and habitat impacts resulting from landslides. There are climate change implications where drought or heavier rains affect the number and severity of landslides. This project examines the relationship of soil moisture and precipitation over Colorado, USA. A lot of people live in the Rockies. It is a popular tourist destination year-round, people are moving into the Rockies - it’s a popular area, to say the least.

<H3>PURPOSE</H3>Address the need to improve our understanding of landslides caused by rainfall. To better characterize
where and when these landslides occur.

<H3>CONTRIBUTIONS</H3>
<ul type="disk">
  <li>Soil moisture can be a potential indicator of the type of rainfall induced landslide. We can use soil moisture data to group landslides into two types (1) shallow slope failures - saturation induced by rainfall infiltration and (2) run off driven landslides - triggered by intense storms.  This informs the forecaster which models and precipitation products are optimal to use to better predict a landslide event.

  <li>Code presented here is helpful to those who want to know how to read/extract soil moisture parameters measured from NASA, USGS, and ESA satellites. 
</ul>

<H3>Python packages</H3>The following are python packages currently used to run the current list of jupyter notbooks in this repository.
<ul type="disk">
  <li>os
  <li>glob
  <li>datetime
  <li>earthpy
  <li>geopandas
  <li>folium
  <li>h5py (pip install h5py)
  <li>matplotlib
  <li>numpy
  <li>pandas
  <li>re
  <li>seaborn
  <li>shapely
  <li>xarray
</ul>  

<P>Using conda, install by typing <b>'conda install -c conda-forge name-of-package-listed-above'</b> 
<P>All python code are contained within Jupyter Notebooks and at the moment there is no order of notebooks to run. Each notebook is self contained and somewhat self-explanatory.   
    
<H3>DATA & FORMATS</H3>

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

<!-- this has not so relevant
<H3>WORKFLOW (through May)</H3>

<img width="1327" alt="Screen Shot 2022-04-19 at 1 42 02 PM" src="https://user-images.githubusercontent.com/50637069/164083011-ab4995c7-4dd3-4a90-9cd5-75ddaca3db38.png">
-->

