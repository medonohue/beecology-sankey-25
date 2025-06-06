
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/sankey-data")
def get_sankey_data():
    df = pd.read_csv("bee_flower_data_cleaned.csv")
    labels = pd.unique(df[['species', 'flower_family']].values.ravel())
    label_map = {label: i for i, label in enumerate(labels)}
    return {
        "labels": labels.tolist(),
        "sources": [label_map[row['species']] for _, row in df.iterrows()],
        "targets": [label_map[row['flower_family']] for _, row in df.iterrows()],
        "values": df['count'].tolist()
    }
