# 🎬 MovieSeek: Semantic Search for Movies  
*A Hackathon6 Project – Built with Streamlit, Hugging Face Transformers & Pinecone*

![License](https://img.shields.io/github/license/SaharZargarzadeh/Hackathon6)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-frontend-orange)
![Status](https://img.shields.io/badge/status-Prototype-green)

## 🌟 Project Overview  
**MovieSeek** is a semantic search engine that allows users to explore movies using natural language queries. Instead of keyword-based filters, our app uses embeddings from pre-trained language models to retrieve relevant results based on meaning—not just syntax.

> This project was created during Hackathon6 to demonstrate how LLM-powered search can be applied to entertainment data such as Netflix and IMDb.

---

## 🔍 Key Features

- 🧠 **Semantic Search** using Hugging Face sentence-transformers and Pinecone vector database  
- 🎞️ Query Netflix/IMDb-style datasets using **natural language**  
- ⚡ **Streamlit App** frontend for interactive movie exploration  
- 📈 Backend pipeline for data cleaning, embedding generation, and storage

---

## 🧠 Motivation  
With countless movies available, it can be overwhelming to choose what to watch. Our goal was to design an intelligent system that understands user intent—even if vague or descriptive—and returns meaningful recommendations.

---

## 🏗️ Architecture & Tech Stack

| Layer        | Technology                                             |
|--------------|--------------------------------------------------------|
| Frontend     | Streamlit                                              |
| Backend      | Python, sentence-transformers, Pinecone, scikit-learn |
| Embedding    | `all-MiniLM-L6-v2` via Hugging Face Transformers       |
| Data Storage | Pinecone Vector DB                                     |
| Dev Tools    | GitHub Codespaces, Jupyter Notebooks                   |

---

## 📂 Repository Structure

Hackathon6/
├── LICENSE
├── README.md
├── Netflix TV Shows and Movies.csv # Raw dataset
├── clean_data.py # Data cleaning script
├── create_dataset.py # Dataset preparation
├── embed_and_store_data.py # Generate and push embeddings
├── search_app.py # Streamlit app entry point


---

## 🚧 Challenges Faced

- 📚 Learning curve with semantic search and vector databases  
- ⏱️ Limited time to integrate frontend with backend  
- 🤝 Team collaboration across different skill levels  
- 🔄 Adjusting scope mid-hackathon due to RAG AI workshop insights

---

## ✅ Achievements

- Successfully implemented **end-to-end semantic search**  
- Created a working **Streamlit interface** for real-time movie queries  
- Promoted **cross-disciplinary teamwork** under tight deadlines  
- Used real-world movie datasets for a meaningful demo

---

## 📚 Lessons Learned

- How to leverage **semantic embeddings** for search and ranking  
- Importance of **cleaning and preprocessing** for real-world datasets  
- How to quickly prototype apps with **Streamlit**  
- Integration between **frontend UX** and backend ML models

---

## 🚀 What's Next

- ✅ Expand dataset coverage with additional metadata (e.g., user reviews, actors)  
- 🔍 Improve retrieval quality using custom fine-tuning  
- 🖥️ Migrate to a more dynamic full-stack framework (e.g., React + FastAPI)  
- 📊 Add interactive data visualizations for richer user feedback

---

## 🛠️ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/SaharZargarzadeh/Hackathon6.git
cd Hackathon6
2. Install dependencies
```bash
pip install -r requirements.txt
# OR manually install:
pip install transformers torch sentence-transformers pinecone-client streamlit scikit-learn
3. Prepare data and embeddings
Run each of the following Python scripts in order:

```bash
python clean_data.py
python create_dataset.py
python embed_and_store_data.py
4. Launch the app
```bash
streamlit run search_app.py
App will open in your browser at http://localhost:8501

📄 License
This project is licensed under the GPL-3.0 License.

🙌 Acknowledgments
Hugging Face for sentence-transformers

Pinecone for vector search infrastructure

Streamlit for the rapid prototyping framework

Hackathon6 mentors and organizers


✅ Let me know if you'd like me to also generate:
- A `requirements.txt` file  
- A badge-friendly GitHub “About” section  
- A banner image for the top of the README  
- A project thumbnail for social media previews
