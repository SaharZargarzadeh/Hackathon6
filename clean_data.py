# Which columns will you use?
# Clean your columns
# Concatenate the columns needed for your embedding
# Create new column with concatenated and clean text

import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
import streamlit as st

# Load the dataset
df = pd.read_csv('Netflix TV Shows and Movies.csv')

# Prepare text for embedding, handling NaN values
df['title'] = df['title'].fillna('')
df['description'] = df['description'].fillna('')
df['text_for_embedding'] = df['title'] + ' ' + df['description']
