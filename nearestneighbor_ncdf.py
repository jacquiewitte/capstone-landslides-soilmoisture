def nearestneighbor_ncdf(input_file, parameter, loc):
    """
    Extracts nearest neighbor value based on location and desired parameter. 
    
    Parameters
    ----------   
    input_file: Str - full path to a single file
    
    parameter: Str 
    
    loc: tuple (degree longtitude, degree latitude)
    
    Returns
    -------
    float
    """
    # read the netcdf file
    data_xr = xr.open_dataset(input_file).squeeze()
    
    # subset the file
    res = data_xr[parameter].sel(indexers={
            'lon': loc[0],
            'lat': loc[1]},
            method="nearest")
    return float(res.values)
