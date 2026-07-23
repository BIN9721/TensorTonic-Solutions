import pandas as pd

def set_index_column(data, index_col):
    """
    Returns: dict with 'index_values', 'columns', 'data'
    """
    df=pd.DataFrame(data)
    df=df.set_index(index_col)
    return {
        "index_values": df.index.tolist(),
        "columns": df.columns.tolist(),
        "data": {col: df[col].tolist() for col in df.columns}
    }