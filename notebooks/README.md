# 🧠 Lab 5 — End-to-End AI Demonstration Using Gemini API

## 🎯 Goal
In this lab, the Intelligent Repository Reliability Analyzer (IRRA) is implemented as a **fully operational AI system** in Google Colab using the **Gemini API**.  
The system demonstrates two modes of prompt-based reasoning:
- **Zero-shot** — The AI predicts reliability from new repository metrics without prior examples.  
- **Few-shot** — The AI learns from a known example to make more context-aware predictions.  

This work extends the prompt engineering design from **Lab 4**, located in `VGTUThesis/prompts/`, now implemented as an executable, end-to-end pipeline.

---

## ⚙️ Notebook
Link to Colab document: https://colab.research.google.com/drive/1UXoVAv1qfryPWbLiYB6ENWOhcfyq2QnO?usp=sharing

--- 

### 🧩 Process Flow
1. **Input Stage** – Repository metrics (X) provided as structured JSON.  
2. **Reasoning Stage** – Gemini interprets the formula and scale using prompt instructions.  
3. **Inference Stage** – The model calculates RRI and classifies reliability.  
4. **Output Stage** – Results displayed as tables and JSON outputs for integration or analysis.  

✅ Both zero-shot and few-shot runs demonstrate end-to-end AI reasoning — from data input to final prediction.

---

### Reflection

This laboratory work successfully implemented an end-to-end AI agent for repository reliability assessment using the Gemini API in Google Colab.  
The system processes raw repository metrics and computes reliability indices through structured prompt reasoning. The **zero-shot** approach shows the model’s ability to infer outcomes directly from instructions, while the **few-shot** approach enhances contextual understanding through a learned example.  

Gemini handled both structured numeric data and qualitative interpretation (labels like "Good" or "Excellent") effectively, producing explainable results. The prompt-based architecture proved lightweight, interpretable, and flexible for AI-assisted data analysis.  
Future improvements could include adding real-time GitHub API data collection, enhancing Gemini reasoning layer to infer insights (like root causes for low reliability), and implementing visualization dashboards for dynamic monitoring.


---

### ✅ **Summary Checklist**

| Task | Status |
|------|--------|
| Google Colab notebook created | ✅ |
| GEMINI_KEY loaded securely via `userdata` | ✅ |
| Both zero-shot and few-shot prompts implemented | ✅ |
| Demonstrated reasoning → inference → output | ✅ |
| Visual explanation of the process | ✅ |
| Reflection paragraph added | ✅ |
| Notebook linked in GitHub `/notebooks/` directory | ✅ |

---------------

# 🧩 Lab 6 — True Retrieval-Augmented Generation (RAG) Implementation

## 🎯 Goal
In this lab, the Intelligent Repository Reliability Analyzer (IRRA) is expanded into a **fully operational RAG system**.  
Using **ChromaDB** for vector storage and retrieval, and **Gemini API** for reasoning, the system now demonstrates a realistic data-to-AI pipeline that grounds responses in semantically relevant examples. 

> [!NOTE]
In the final cell, the notebook includes an option to persist the RAG system’s latest run to disk, this saves a file to the temporary filesystem inside Google Colab, located at: `/content/last_rag_run.json`. You can view or download this file from the **Files** sidebar in Colab. This feature is included for traceability, allowing you to preserve the retrieved examples, the augmented prompt, and the model’s generated response for later inspection or debugging.

---

## ⚙️ Notebook
Link to Colab document: https://colab.research.google.com/drive/19EcYR_cgOOSATya63Egdjz684ijXMh2H?usp=sharing

--- 

## 📌 Overview of What Was Implemented

### 1. Generate 1,000+ synthetic dataset examples  
A dataset containing over 1,000 examples of repository metric pairs `(X, y)` was generated.  
Each example includes:
- Review Rigor  
- PR Merge Ratio  
- Contributor Diversity Index  
- Issue Resolution Rate  
- Reliability Label (`Poor`, `Moderate`, `Good`, `Excellent`)

---

### 2. Store all examples inside ChromaDB  
- A local persisted vector store is created (`./chroma_storage`).  
- Embeddings generated using: `sentence-transformers/all-MiniLM-L6-v2`  
- Each example stored as:
  - vector embedding  
  - JSON metadata containing metrics  
  - the label  
  - example ID  

---

### 3. Retrieve Top-3 Similar Examples  
For any new repository’s metrics:
1. Embed input X  
2. Query ChromaDB  
3. Retrieve top-3 most semantically similar examples  
4. Display:
   - retrieved metadata  
   - distances (lower distance the higher similarity between query and retrieved document)  
   - GitHub-table view  
   - JSON view  

---

### 4. Augment Prompt and Send to Gemini  
The final prompt includes:
- the new repository metrics  
- the 3 most similar retrieved examples  
- the full qualitative reliability scale  
- an instruction to produce:
  - predicted RRI (0–100)
  - predicted reliability label
  - reasoning (3–5 sentences)
  - retrieved example references
  - GitHub-formatted table of all metrics

---

### 5. End-to-End Execution in Google Colab  
The final pipeline:
Input Metrics Prompt
→ Vector Embedding
→ ChromaDB Vector Similarity Search
→ Retrieve 3 Examples
→ Build Augmented Contextual Prompt
→ Gemini Output (RRI + Label + Reasoning)

---

## 📚 Notebook Structure  

1. **Introduction (Markdown)**  
2. **Install Dependencies (Code)**  
3. **Environment Setup (Markdown + Code)**  
4. **Generate Dataset / Create & Populate ChromaDB (Markdown + Code)**  
6. **Query & Retrieve Top-3 Examples (Markdown + Code)**  
7. **Construct Augmented Prompt / Gemini Prediction (Markdown + Code)**  
9. **Reflection (Markdown)**  

---

## 📊 Example Output Structure  
Gemini returns:

```json
{
  "predicted_rri": 78.3,
  "predicted_label": "Good",
  "reasoning": "Repository demonstrates strong...",
  "retrieved_examples": [124, 876, 331],
  "metrics_table": "| Metric | Value | ..."
}
```

---

### 💬 Reflection

This lab successfully transforms IRRA from a static prompt-based tool into a true RAG-powered system using vector similarity search. The integration of ChromaDB and Gemini successfully bridges structured numeric analysis with contextual memory, improving explanation quality and output grounding. By anchoring predictions in retrieved examples, Gemini produces more accurate, consistent, and explainable outputs. This significantly reduces hallucination risk and increases trust in the predictions.

**Future Improvements / Potential next steps:**

- Replace synthetic data with real live GitHub repository metrics / data ingestion

- Use embeddings for PR/Issue sequences
  
- Add automatic normalization of metrics

- Introduce ranking evaluation metrics (MRR, Recall@k)

- Integrate UI dashboard for reliability insights / similarity scoring visualization

- Reliability trend tracking over time

- Implement evaluation metrics (accuracy & precision) comparing Gemini predictions vs. ground truth labels stored in the DB.

---

### ✅ **Summary Checklist**

| Requirement                   | Status      |
| ----------------------------- | ----------- |
| Secure Gemini API key loaded  | ✅ Completed |
| Generate 1,000+ examples      | ✅ Completed |
| Store examples in ChromaDB    | ✅ Completed |
| Use embeddings for similarity | ✅ Completed |
| Retrieve Top-3 examples       | ✅ Completed |
| Build augmented prompt        | ✅ Completed |
| Send to Gemini                | ✅ Completed |
| Full pipeline demonstrated    | ✅ Completed |
| Reflection included           | ✅ Completed |

---


