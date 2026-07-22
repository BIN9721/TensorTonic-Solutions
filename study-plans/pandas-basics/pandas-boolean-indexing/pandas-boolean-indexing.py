import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    df=pd.DataFrame(data)
    filters = df[df[column]>threshold]
    return {
        "filtered_data":filters.to_dict('list'),
        "count":len(filters)
    }