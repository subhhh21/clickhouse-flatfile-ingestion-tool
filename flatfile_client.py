
import pandas as pd

def save_to_csv(rows, columns, filename):
    df = pd.DataFrame(rows, columns=columns)
    df.to_csv(filename, index=False)

def load_from_csv(filename):
    return pd.read_csv(filename)
