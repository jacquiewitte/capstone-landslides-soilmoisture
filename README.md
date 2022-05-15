<H1>2022 Earth Lab Capstone project repository</H1>

<H1>Where can soil moisture improve rainfall-triggered landslide predictability?</H1>

<H2>Description</H2>
<P>Landslide prediction is important. There are negative economic, transportation, and habitat impacts resulting from landslides. There are climate change implications where drought or heavier rains affect the number and severity of landslides. The goal of this project is to examine the relationship of soil moisture and precipitation over Colorado, USA. Colorado experiences many landslides each year because of its steep terrain. Some of them occur in remote areas that are difficult to monitor, with most occurring west of the Front Range. Damage from landslides in Colorado is estimated to be millions of dollars per year. A significant fraction of the Colorado population lives in the Rockies. It is also a popular tourist destination year-round and people are moving into the Rockies - it’s a popular area, to say the least.

 ![cnn_newsarticle_glenspringsLandslideCO](https://user-images.githubusercontent.com/50637069/168334226-23d48d21-6e83-4cc9-8e48-a37f61678e1e.png)
 
  
<H2>Purpose</H2>To address the need to improve our understanding of landslides caused by rainfall. To better characterize
where and when these landslides occur by focussing the workflow on the state of Colorado as a case study region.

<H2>Contributions</H2>
<ul type="disk">
  <li>Soil moisture can be a potential indicator of the type of rainfall induced landslide. We can use soil moisture data to group landslides into two types (1) shallow slope failures - saturation induced by rainfall infiltration and (2) run off driven landslides - triggered by intense storms.  This informs the forecaster which models and precipitation products are optimal to use to better predict a landslide event.

  <li>Code presented here is helpful to those who want to know how to read/extract soil moisture parameters measured from NASA, USGS, and ESA satellites. 
</ul>

<H2>Python Packages Used</H2>The following are python packages currently used to run the current list of jupyter notbooks in this repository.
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

<P>Using conda, install by typing <b>`conda install -c conda-forge name-of-package-listed-above`</b> 

<H2>Notebooks</H2>

- All python notebooks are still in the development stage. 
- When notebooks are final the tag `_final.ipynb` will be added to the fiename. 
- All notebooks for testing code are placed in the folder `test_scripts/`. Code in here are exploratory only and should be ignored. Code from these notebooks are for development of the final notebooks. 
  
<H2>Workflow</H2>

- The README.md file will be updated regularly with guidance on the workflow.
- To run these notebooks, you need to have the data listed in the "Data & Formats" section below
- At the moment, each notebook reads and plots the data separately to review whether the data resolution is enough to determine significant correlations and relationships between soil moisture and precipitation data collected thus far, with the Global Landslide Catalog:

  <ul type="disk">
    <li>landslide-esa_soilm_timeseries.ipynb - soil moisture comparison
     <ul type="disk"><li>Works with the CSV output from output_esa_soilm_2007_2016.ipynb</ul>
    <li> landslide_precip_soilm.ipynb - Compares SMAP soil moisture and GPM precipitation
  </ul>

 <H3>Output</H3>
<P>Output are plots inline with the notebooks. Noteworthy plots are exported as PNG files saved under the `plots/` folder.
  
<H2>Data & Formats</H2>

<P>The README.md file will be updated regularly as data needs change.
 
<ol type="1">
  <li>NASA Global Landslide Catalog (2007-2020)
  <br>- https://maps.nccs.nasa.gov/arcgis/apps/MapAndAppGallery/index.html?appid=574f26408683485799d02e857e5d9521 
  <br>- CSV format</li>

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

