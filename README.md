# InsightGraph: Interactive Intelligence Text Analyzer

InsightGraph is an NLP-powered system that transforms unstructured text into meaningful insights by extracting entities, identifying key topics, and visualizing their relationships through an interactive graph.

It is designed to simulate a lightweight **intelligence analysis workflow**, enabling users to explore connections between people, organizations, locations, and events.

##  Key Features

*  Supports **CSV and JSON (JSONL)** datasets
*  **Named Entity Recognition (NER)** using spaCy
*  **Keyword Extraction** using RAKE
*  Text preprocessing and normalization
*  Interactive **Entity–Keyword Relationship Graph**
*  User Controls:

  * Topic-based filtering
  * Adjustable number of nodes
*  Interactive visualization using **PyVis**

  * Drag, zoom, hover
  * Node size = importance
  * Edge thickness = connection strength

## Pipeline Overview

```
Unstructured Text Data
        ↓
Text Preprocessing
        ↓
Named Entity Recognition (WHO)
        ↓
Keyword Extraction (WHAT)
        ↓
Filtering & Normalization
        ↓
Relationship Mapping
        ↓
Interactive Graph Visualization
```

##  Graph Interpretation

*  **Blue Nodes** → Entities (PERSON, ORG, GPE)
*  **Green Nodes** → Keywords / Topics
*  **Node Size** → Frequency (importance)
*  **Edges** → Co-occurrence relationships
*  **Edge Thickness** → Strength of connection

 Example Insight:

```
U.S. ── covid boosters ── vaccination rollout
American Airlines ── flight incident
```

---

##  Installation

```bash
git clone https://github.com/your-username/InsightGraph.git
cd InsightGraph
pip install -r requirements.txt
```

---

##  Run the Application

```bash
streamlit run app.py
```

---

##  User Interface

*  Upload dataset (CSV / JSON)
*  Sidebar controls:

  * Topic filter (e.g., "covid", "airline")
  * Node count slider
*  Main panel:

  * Interactive relationship graph
*  Expandable sections:

  * Extracted entities
  * Extracted keywords
  * Raw data preview

---

## Project Structure

```
InsightGraph/
│
├── app.py                 # Streamlit UI
├── modules/
│   ├── ner.py            # Named Entity Recognition
│   ├── keyword.py        # Keyword extraction (RAKE)
│   └── graph.py          # Graph construction & visualization
│
├── requirements.txt
└── README.md
```

---

##  Use Cases

* Intelligence & defense analysis
* News and media trend analysis
* Relationship discovery in unstructured data
* Exploratory data analysis for text datasets

---

##  Limitations

* RAKE may generate generic or less meaningful keywords
* Mixed-topic datasets can produce noisy graphs
* Graph interpretation depends heavily on input data quality

---

##  Future Scope

*  Highlight most influential node (central entity detection)
*  Entity-type filtering (PERSON / ORG / GPE selection)
*  Edge labels showing connection strength
*  Cluster detection (topic grouping)
*  Node search and filtering
*  Time-based relationship analysis
*  Advanced keyword extraction (KeyBERT / transformer-based models)
*  Analytical dashboard (charts, summaries, trends)
*  Automatic topic detection and classification

---

##  Tech Stack

* Python
* Streamlit
* spaCy
* NLTK
* RAKE-NLTK
* NetworkX (logic)
* PyVis (visualization)
* Pandas

---

##  Key Learnings

* Built a complete NLP pipeline from scratch
* Understood challenges of unstructured text processing
* Applied graph-based relationship modeling
* Learned importance of filtering and visualization design

---

##  Author

**Shriyash Kothe**

---

##  Final Note

InsightGraph is not just a visualization tool — it represents a step toward transforming raw textual data into structured, interpretable intelligence.

---
