import streamlit as st
import pandas as pd

train_scaled = pd.read_pickle('./data/train_scaled.pkl')
train_unscaled = pd.read_pickle('./data/train_unscaled.pkl')
test = pd.read_pickle('./data/test_data_with_pred.pkl')
