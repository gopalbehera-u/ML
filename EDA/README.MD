# 📊 LLM-Powered EDA Tool

Upload any CSV and get automated EDA insights powered by local LLM (Gemma2).

---

## 📁 Files
| File | Description |
|------|-------------|
| `app.py` | Gradio web app — upload CSV → get EDA + AI insights |
| `EDA_LLM.ipynb` | EDA notebook |
| `Netflix_EDA_LLM.ipynb` | Netflix dataset EDA using LLM |
| `netflix_titles.csv` | Dataset — 8807 rows, 12 columns |

---

## 🗃️ Netflix Dataset
| Column | Description |
|--------|-------------|
| show_id | Unique ID |
| type | Movie or TV Show |
| title | Title name |
| director | Director name |
| cast | Cast members |
| country | Country of origin |
| date_added | Date added to Netflix |
| release_year | Year of release |
| rating | Content rating |
| duration | Duration in mins or seasons |
| listed_in | Genre |
| description | Short description |

---

## ⚙️ How app.py Works
1. Upload any CSV file
2. Auto fills missing values — mean for numeric, mode for categorical
3. Generates data summary
4. Sends summary to **Gemma2 LLM** via Ollama for AI insights
5. Generates histograms for all numeric columns
6. Generates correlation heatmap
7. Shows everything in Gradio UI

---

## 🤖 AI Model Used
- **Model:** Gemma2:2b,llama3
- **Tool:** Ollama (runs locally)

---

## 🚀 How to Run
```bash
pip install gradio pandas matplotlib seaborn ollama
ollama pull gemma2:2b,llama3
python app.py
```

---

## 🛠️ Libraries
`pandas` `matplotlib` `seaborn` `gradio` `ollama`