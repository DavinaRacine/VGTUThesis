# 🧠 AI Prompt Design for Reliability Calculation (Prompts Used in Lab 4)

## 📊 Context
This lab demonstrates how Generative AI (GAI) can generate synthetic repository data and calculate a **Repository Reliability Index (RRI)** from four key process metrics extracted from GitHub events.  
The RRI is calculated as the **average of normalized metric scores**, representing a simplified AI reasoning approach. This information is also saved in word document `Prompts.docx` in this location. Sample output after running these prompts inside ChatGPT are located in `VGTUThesis/data/Lab4`. 

---

## ⚙️ Step 1 — Prompt: Generate Mock Metrics (X Variables)

**Prompt:**
> You are an AI assistant analyzing software repository reliability.  
> Generate mock values for the following four metrics for 5 GitHub repositories.  
> Each metric is on a scale from 0 to 100, where higher is better.  
> Metrics:
> - `issue_resolution_time` (speed of resolving issues; higher = faster resolution)  
> - `pull_request_merge_rate` (percentage of merged PRs)  
> - `commit_frequency` (normalized to 100; higher = more active)  
> - `code_review_comments` (normalized review depth; higher = more collaborative)  
> Provide results as a JSON array with 5 repositories of mixed performance levels.  

### 🧾 Example Output (Mock X Data)

```json
[
  {"repository_name": "dev-roadmap", "issue_resolution_time": 95, "pull_request_merge_rate": 92, "commit_frequency": 88, "code_review_comments": 90},
  {"repository_name": "data-analyzer", "issue_resolution_time": 78, "pull_request_merge_rate": 85, "commit_frequency": 80, "code_review_comments": 75},
  {"repository_name": "webhelper", "issue_resolution_time": 60, "pull_request_merge_rate": 65, "commit_frequency": 55, "code_review_comments": 50},
  {"repository_name": "testmate", "issue_resolution_time": 82, "pull_request_merge_rate": 87, "commit_frequency": 90, "code_review_comments": 85},
  {"repository_name": "bugtrack-lite", "issue_resolution_time": 40, "pull_request_merge_rate": 50, "commit_frequency": 45, "code_review_comments": 35}
]
```

---

## 🧮 Step 2 — Prompt: Calculate Reliability Index (Y Output)

**Prompt:**
> Based on the following repository metrics, calculate the *Repository Reliability Index (RRI)* for each repository.  
> Formula:  
> \[
> RRI = (issue\_resolution\_time + pull\_request\_merge\_rate + commit\_frequency + code\_review\_comments) / 4
> \]
> Then classify the reliability based on this scale:
> - 0–49 → **Poor**
> - 50–69 → **Moderate**
> - 70–84 → **Good**
> - 85–100 → **Excellent**  
> Return a JSON output with each repository’s calculated RRI (rounded to 1 decimal) and reliability label.

### ✅ Example Output (With Calculations)

| Repository | Issue Resolution | Merge Rate | Commit Frequency | Code Review | RRI (avg) | Reliability |
|-------------|------------------|-------------|------------------|--------------|------------|--------------|
| dev-roadmap | 95 | 92 | 88 | 90 | **91.25** | **Excellent** |
| data-analyzer | 78 | 85 | 80 | 75 | **79.5** | **Good** |
| webhelper | 60 | 65 | 55 | 50 | **57.5** | **Moderate** |
| testmate | 82 | 87 | 90 | 85 | **86.0** | **Excellent** |
| bugtrack-lite | 40 | 50 | 45 | 35 | **42.5** | **Poor** |

### 💡 Example JSON Output

```json
[
  {"repository_name": "dev-roadmap", "reliability_index": 91.25, "reliability_level": "Excellent"},
  {"repository_name": "data-analyzer", "reliability_index": 79.5, "reliability_level": "Good"},
  {"repository_name": "webhelper", "reliability_index": 57.5, "reliability_level": "Moderate"},
  {"repository_name": "testmate", "reliability_index": 86.0, "reliability_level": "Excellent"},
  {"repository_name": "bugtrack-lite", "reliability_index": 42.5, "reliability_level": "Poor"}
]
```

---

## 📈 Step 3 — Prompt: Summarize Insights

**Prompt:**
> Summarize insights from the computed RRI values.  
> Identify which repositories are highly reliable, which are risky, and provide one short suggestion per repository on how to improve reliability.

### 🧩 Example Output Summary

| Repository | Reliability | Suggestion |
|-------------|--------------|-------------|
| dev-roadmap | Excellent | Maintain current review quality and active commits. |
| testmate | Excellent | Keep PR merge rates high and continue strong collaboration. |
| data-analyzer | Good | Improve issue resolution speed slightly to reach excellent reliability. |
| webhelper | Moderate | Increase commit frequency and encourage more code reviews. |
| bugtrack-lite | Poor | Prioritize issue resolution and increase PR reviews to stabilize quality. |

---

## 🧠 Step 4 — Prompt: Final AI-driven Interpretation

**Prompt:**
> Based on the RRI results, generate a short paragraph (4–5 sentences) that an AI analyst could include in a reliability assessment report.  
> Mention which repositories show strong software process maturity and which indicate risk areas.

### 🗒️ Example Output

> The AI analysis identified *dev-roadmap* and *testmate* as the most reliable repositories, both demonstrating high merge rates, consistent commit activity, and rich code review participation. *Data-analyzer* shows good reliability but could benefit from quicker issue turnaround. *Webhelper* exhibits moderate reliability, suggesting a need for increased team activity and review engagement. *Bugtrack-lite* remains a high-risk repository due to slow issue resolution and low collaboration, indicating potential process inefficiencies that require targeted improvement.

---

## 📘 Reflection: Pros & Cons of Using ChatGPT for Lab 4

### ✅ **Pros**
- Rapid generation of realistic mock data for repositories.
- Automatic computation and classification of reliability scores.
- Consistent, replicable results for testing or simulation.
- Time-efficient for academic prototyping without needing live APIs.
- Helpful for idea visualization (metrics, reasoning, structured prompts).

### ⚠️ **Cons**
- Outputs are simulated and not from real GitHub data.
- Model assumptions (averaging metrics) may oversimplify real reliability.
- Requires clear prompt structure; ambiguous prompts can skew results.
- No automatic connection to GitHub APIs — needs separate data collection layer.
- Interpretations depend on language model reasoning, not statistical validation.

---
