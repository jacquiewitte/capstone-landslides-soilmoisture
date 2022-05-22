def findfile(input_files, input_date):
    """
    Returns a single file from a list of files
    
    Parameters
    ----------
    input_files: List of strings
        List of full path to the file
        
    input_date: String
        YYYYMMDD format
        
    Returns
    -------
    file: Str
    """
    file = [x for x in input_files if re.findall(input_date, x)]
    if not file:
        raise ValueError('Date does not exist for '+input_date)
    return file
