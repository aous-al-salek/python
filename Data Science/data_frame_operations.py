from pandas.core.frame import DataFrame


def drop_rows_containing(target_value: str, data_frame: DataFrame):
    """Drop all rows containing a specific value in a Pandas dataframe.\n
    - "target_value": defines the identifying value\n
    - "data_frame": is the Pandas dataframe"""
    # Loop through all columns of the dataframe
    for data_frame_column in data_frame.columns:
        # Column counter
        itteration_conter = 0
        # Loop through all values in each column
        for v in data_frame[data_frame_column]:
            # If a value in any column or row matches the target value
            if (v == target_value):
                try:
                    # Try to drop the current row inplace
                    data_frame.drop(itteration_conter, inplace=True)
                except:
                    # Pass if unable to drop because the row has already been dropped
                    pass
            # Increment the column counter
            itteration_conter += 1
    # Return the desired datafram
    return data_frame
