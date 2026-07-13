from pathlib import Path
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    base_dir = Path(__file__).parent
    train_scaled = pd.read_pickle(base_dir / "data" / "train_scaled.pkl")
    train_unscaled = pd.read_pickle(base_dir / "data" / "train_unscaled.pkl")
    test = pd.read_pickle(base_dir / "data" / "test_data_with_pred.pkl")
    return train_scaled, train_unscaled, test

train_scaled, train_unscaled, test = load_data()

