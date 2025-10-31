# 🧠 Lab 5 — End-to-End AI Demonstration Using Gemini API

## 🎯 Goal
In this lab, the Intelligent Repository Reliability Analyzer (IRRA) is implemented as a **fully operational AI system** in Google Colab using the **Gemini API**.  
The system demonstrates two modes of prompt-based reasoning:
- **Zero-shot** — The AI predicts reliability from new repository metrics without prior examples.  
- **Few-shot** — The AI learns from a known example to make more context-aware predictions.  

This work extends the prompt engineering design from **Lab 4**, located in `VGTUThesis/prompts/`, now implemented as an executable, end-to-end pipeline.

---

## ⚙️ Notebook Setup
```python
# Import necessary libraries
import os
from google.colab import userdata
from google.colab import output

# Securely load Gemini API key from Colab secrets
GEMINI_KEY = userdata.get('GEMINI_KEY')

# Install and import Gemini client
!pip install -q google-generativeai
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=GEMINI_KEY)
