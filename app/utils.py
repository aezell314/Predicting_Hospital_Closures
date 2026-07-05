import streamlit as st
import pandas as pd

train = pd.read_pickle('./data/train.pkl')
test = pd.read_pickle('./data/test_data_with_pred.pkl')
