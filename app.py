# app.py

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

from modules.ner import apply_ner
from modules.keyword import apply_keywords
from modules.graph import build_interactive_graph

st.set_page_config(page_title="InsightGraph", layout="wide")

st.title(" InsightGraph")
st.caption("Extract relationships between entities and topics from text data")

uploaded_file = st.file_uploader("Upload CSV or JSON file", type=["csv", "json"])

if uploaded_file is not None:

    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file, on_bad_lines='skip', low_memory=False)
    else:
        df = pd.read_json(uploaded_file, lines=True)

    # Limit size
    df = df.head(50)

    # Create combined text
    if "headline" in df.columns and "short_description" in df.columns:
        df["combined_text"] = (
            df["headline"].fillna("") + " " +
            df["short_description"].fillna("")
        )
    else:
        df["combined_text"] = df.iloc[:, 0].astype(str)

    df["combined_text"] = df["combined_text"].str[:300]

    # Sidebar controls
    st.sidebar.header("Controls")

    topic = st.sidebar.text_input("Filter Topic (e.g., covid, airline)")

    top_n = st.sidebar.slider(
        "Number of Nodes",
        min_value=5,
        max_value=30,
        value=10
    )

    # Apply topic filter
    if topic:
        df = df[df["combined_text"].str.contains(topic, case=False, na=False)]

    # Processing
    @st.cache_data
    def process_data(df):
        df = apply_ner(df, column="combined_text")
        df = apply_keywords(df, column="combined_text")
        return df

    with st.spinner("Analyzing text..."):
        df = process_data(df)

    # MAIN OUTPUT (GRAPH)
    st.subheader(" Relationship Graph")

    graph_df = df.head(30)
    net = build_interactive_graph(graph_df, top_n=top_n)

    net.save_graph("graph.html")

    with open("graph.html", "r", encoding="utf-8") as f:
        html = f.read()

    components.html(html, height=700,width = None)

    # OPTIONAL DETAILS (clean UX)
    with st.expander(" View Extracted Entities"):
        st.dataframe(df[["combined_text", "entities"]])

    with st.expander(" View Extracted Keywords"):
        st.dataframe(df[["combined_text", "keywords"]])

    with st.expander(" View Raw Data"):
        st.dataframe(df.head())

else:
    st.info("Upload a dataset to begin analysis.")