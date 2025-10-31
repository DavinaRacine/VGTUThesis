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
""")

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

---


