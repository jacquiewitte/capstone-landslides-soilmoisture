[![DOI](https://zenodo.org/badge/471110606.svg)](https://zenodo.org/badge/latestdoi/471110606)

<H1>capstone-landslides-soilmoisture project repository</H1>

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
   
  <li>The workflow should perform with any state who's landslide data is archived in the GLC.
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
  <li>scipy
  <li>seaborn
  <li>shapely
  <li>xarray
</ul>  

<P>To install packages separately, using conda, type <b>`conda install -c conda-forge name-of-package-listed-above`</b> 

 
 <H3>Installing the capstone-landslides-soilmoisture Conda Environment</H3>

This repository contains a file called `environment.yml` that contains the python packages to install the capstone-landslides-soilmoisture environment. Included is installation of Jupyter notebook and it's dependencies. 

- Clone/Fork this repository. 
- Once you are in the capstone-landslides-soilmoisture directory, you can create the environment. To do this run: `conda env create -f environment.yml`.
- Once the environment is installed you can activate it using: `conda activate capstone-landslides-soilmoisture`.
- To view a list of all conda environments available on your machine run: `conda info --envs`.
- To view a list of all conda packages installed in capstone-landslides-soilmoisture run: `conda list`.
 
<H2>Notebooks</H2>

- All python notebooks are still in the development stage. 
- When notebooks are final the tag `_final.ipynb` will be added to the fiename. 
- All notebooks for testing code are placed in the folder `test_scripts/`. Code in here are exploratory only and should be ignored. Code from these notebooks are for development of the final notebooks. 
  
<H2>Workflow</H2>

- The README.md file will be updated regularly with guidance on the workflow.
- I am at the stage of determining whether the data resolution and coverage is enough to determine significant correlations and relationships between soil moisture and precipitation data collected thus far.
- The data are co-located with 2015-2020 landslide events in Colorado using the Global Landslide Catalog (GLC) (refer to "Data & Formats" below). 
- Eventually csv files will be created that ties all the data together and can be read using the pandas package. 

<H4>Data Directories</H4>

* To run these notebooks, you need to download <b>daily 2015-2020</b> data listed in the "Data & Formats" section below
   * <b>Note:</b> The data files are large, particularly for SMAP which ignore subsetting. 
   * Links to the data and instructions on what specifically to download are provided used in this study are provided in the "Data & Formats" section below

  
* Data directory structure under your home space (Mac/Linux syntax shown below)
  * GLC data directory: `earth-analytics/data/capstone/landslide`
  * GPM daily precipitation directory: `earth-analytics/data/capstone/gpm_westernUS`
  * GPM IMERG 30min precipitation directory: `earth-analytics/data/capstone/precip_imerg`
  * SMAP daily soil moisture directory:  `earth-analytics/data/capstone/smap_9km`
  * ESA CCI soil moisture directory: `earth-analytics/data/capstone/esa_soil_moisture`

 
<H4>Python Notebooks can be run in the following order:</H4>
 
1. capstone-study-area-final.ipynb
      * An introduction the study region and GLC statistics over Colorado.
2. landslide_precip_soilm_DataExport_final.ipynb
      * Co-located SMAP and ESA CCI soil moistures with GPM precipitation products (daily and 30 min resolutions)
      * Users can choose a US state where landslides are archived in the GLC. Currently, the following states are included:
        <ul>
          <li> Colorado
          <li> Idaho
          <li> Utah
          <li> California
          <li> Oregon
          <li> Washington
        </ul>
      * The result are two a pandas dataFrames that is exported to the `data/` folder. For example,
 
         - `glc_smap_esa_gpm_2015-2020_Colorado.csv` contains the 7-day accummulated precipitation and maximum soil moisture co-located to a GLC landslide.
 
         - `glc_smap_esa_gpm_2015-2020_7day_Colorado.csv` contains the precipitation and soil moisture co-located to a GLC landslide going back for 7-days prior to the landslide. 

3. landslide_precip_soilm_DataAnalyses_final.ipynb
      * Plot analysis that reads the exported CSV files created by `landslide_precip_soilm_DataExport_final.ipynb` above.
      * Output are plots inline with the notebooks. Noteworthy plots are exported as PNG files saved under the `plots/` folder.
  
<H2>Data & Formats</H2>

<P>The README.md file will be updated regularly as data needs change.
 
<ol type="1">
 <li><b>NASA Global Landslide Catalog (2007-2020)</b>
  <ul type="disk">
     <li> LINK: https://maps.nccs.nasa.gov/arcgis/apps/MapAndAppGallery/index.html?appid=574f26408683485799d02e857e5d9521 
     <li> Instructions: From the list of downloadables, choose `NASA Global Landslide Catalog Points (CSV)`
     <li> Citation: https://doi.org/10.1007/s11069-009-9401-4
     <li> Format: CSV format
  </ul>
 </li>

 <li><b>NASA SMAP Enhanced L3 Radiometer Global Daily 9 km EASE-Grid Soil Moisture V004</b>
    <ul type="disk">
       <li> LINK: Data downloadable via Earthdata: https://search.earthdata.nasa.gov
       <li> Instructions: Search under 'SMAP soil moisture' and find the dataset that matches the title above. NOTE: Subsetting is ignored so global files are downloaded.
       <li> Citation: https://doi.org/10.5067/NJ34TQ2LFE90
       <li> Format: HDF5 format
    </ul>
  </li>

 <li><b>ESA Climate Change Initiative (CCI) ACTIVE soil moisture 0.25 degree x 0.25 degree V03.3</b>
    <ul type="disk">  
       <li> LINK: https://cds.climate.copernicus.eu/cdsapp#!/dataset/satellite-soil-moisture?tab=overview
       <li> Instructions: Choose the 'ACTIVE' dataset which calculates the percent saturation soil moisture.
       <li> Citation: https://doi.org/10.1016/j.rse.2012.03.014
       <li> Format: netCDF3 format
    </ul>
  </li>

 <li><b>GPM IMERG Late Precipitation L3 1 day 0.1 degree x 0.1 degree V06</b>
    <ul type="disk"> 
       <li> LINK: https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGDL_06/summary?keywords=%22IMERG%20late%22
       <li> Instructions: Subsetting available via GES DISC over the globe. You can choose Colorado or any state(s) of interest. 
       <li> Nearest neighbor remapping of fields between grids in spherical coordinates.
       <li> Citation: https://doi.org/10.5067/GPM/IMERGDL/DAY/06
       <li> Format: netCDF4 format
    </ul>
  </li>
 
 <li><b>GPM IMERG Final Precipitation L3 Half Hourly 0.1 degree x 0.1 degree V06</b>
    <ul type="disk"> 
       <li> This capstone uses 30 min GPM IMERG data pre-assembled and saved in CSV format by Dr. Elsa Culler (CU-Boulder). The beauty of this data set is that precipitation values have been subset and co-located with GLC landslides by their ID, latitude, and longitude. 
       <li> Instructions: Request this data set by emailing Elsa.Culler@colorado.edu
       <li> Citation: https://doi.org/10.5067/GPM/IMERG/3B-HH/06
       <li> Format: CSV
    </ul>
  </li>
 </ol>  
 
<!-- this has not so relevant
<H3>WORKFLOW (through May)</H3>

<img width="1327" alt="Screen Shot 2022-04-19 at 1 42 02 PM" src="https://user-images.githubusercontent.com/50637069/164083011-ab4995c7-4dd3-4a90-9cd5-75ddaca3db38.png">
-->

