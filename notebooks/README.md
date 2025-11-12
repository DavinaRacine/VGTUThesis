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

# 🧩 Lab 6 — Retrieval-Augmented Generation (RAG) Integration with Gemini

## 🎯 Goal
This laboratory extends the Intelligent Repository Reliability Analyzer (IRRA) by integrating a **Retrieval-Augmented Generation (RAG)** pipeline.  
The objective is to enable context-aware reasoning by combining **vector-based retrieval (ChromaDB)** with **natural language generation (Gemini API)**, allowing the system to recall relevant repository examples before producing reliability predictions.

---

## ⚙️ Notebook
Link to Colab document: https://colab.research.google.com/drive/1FKSsJP4ar_V_xQETzDCJZIApyrfa7uxI?usp=sharing

---

### 🧠 System Architecture
The IRRA system now consists of three layers:

1. **Retrieval Layer (ChromaDB)**  
   - Stores historical repository examples and their computed reliability classifications as semantic vectors.  
   - When the user issues a query, ChromaDB retrieves the most relevant examples based on vector similarity.  

2. **Augmentation Layer**  
   - Combines retrieved examples with the user’s new input metrics, forming a context-rich prompt for Gemini.  

3. **Generation Layer (Gemini API)**  
   - Gemini interprets the combined context and generates a predicted **Reliability Index** and **qualitative rating** (Poor → Excellent).  

---

### ⚙️ Demonstration Flow
1. The notebook embeds repository summaries into **ChromaDB**.  
2. A **user prompt** (e.g., “Find repositories with strong review rigor and high resolution rates”) is sent to retrieve top 3 examples.  
3. Retrieved examples are displayed in a formatted **table**.  
4. The examples are injected into a **Gemini prompt**, which predicts reliability for a new repository.  
5. The output demonstrates **retrieval → reasoning → generation** in a complete end-to-end pipeline.

---

### 💬 Reflection
This lab successfully implements a lightweight RAG architecture for the thesis system.  
By connecting **vector retrieval** and **generative reasoning**, IRRA can now make informed predictions using both structured data and contextual memory.  
Gemini produced more consistent, evidence-based reasoning when provided with retrieved examples, proving the effectiveness of augmentation.  

Future improvements could include:
- Expanding the ChromaDB collection with real GitHub repository embeddings.  
- Using multiple retrieval layers (e.g., issues, pull requests, metrics).  
- Visualizing similarity scores and RRI predictions through dashboards.  

---

### ✅ **Summary Checklist**

| Task | Status |
|------|--------|
| Google Colab RAG notebook created | ✅ |
| GEMINI_KEY loaded securely via `userdata` | ✅ |
| ChromaDB vector retrieval implemented | ✅ |
| Top 3 results displayed in table form | ✅ |
| Combined context + user query sent to Gemini | ✅ |
| Reflection and architectural explanation included | ✅ |
| Notebook linked in GitHub `/notebooks/` directory | ✅ |

---



