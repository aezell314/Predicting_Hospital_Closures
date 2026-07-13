import streamlit as st
import pandas as pd

data_path = Path(__file__).parent / "data" / "train_scaled.pkl"
train_scaled = pd.read_pickle(str(data_path))

data_path = Path(__file__).parent / "data" / "train_unscaled.pkl"
train_unscaled = pd.read_pickle(str(data_path))

data_path = Path(__file__).parent / "data" / "test_data_with_pred.pkl"
test = pd.read_pickle(str(data_path))
