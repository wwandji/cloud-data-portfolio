
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def load_laundry():
    return pd.read_csv(DATA_DIR / "laundryflow_orders.csv")

def load_ayoka():
    return pd.read_csv(DATA_DIR / "ayoka_orders.csv")
