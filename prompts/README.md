# 🧠 AI Prompt Design for Reliability Calculation (Prompts Used in Lab 4)

## 📊 Context
This lab demonstrates how Generative AI (GAI) can generate synthetic repository data and calculate a **Repository Reliability Index (RRI)** from four key process metrics extracted from GitHub events.  
The RRI is calculated as the **average of normalized metric scores**, representing a simplified AI reasoning approach. This information is also saved in word document `Prompts.docx` in this location. 

Below are the steps AI used including prompts to generate mock data (X variables) and perform calculations to generate Y variables and interpret the results automatically. There are 3 prompt sections: 1st one represents a zero shot approach, 2nd one represents a few shot approach, 3rd one represents a more detailed approach. Sample output after running third section prompts inside ChatGPT are located in `VGTUThesis/data/Lab4`. 

---
# Section 1 - Zero Shot Approach
## 🧠 Prompt — Zero-Shot (Simple AI Evaluation)
You are an AI agent for repository reliability assessment.
Calculate the Repository Reliability Index (RRI) and reliability classification for each repository using the formula:
RRI=(review_rigor_score+pr_merge_ratio+contributor_diversity_index+issue_resolution_rate)/4

Use the following reliability scale:
-	0–40 → Poor
-	41–60 → Moderate
-	61–80 → Good
-	81–100 → Excellent

Return results both as a table and as JSON with fields: `repository`, `RRI` (rounded to 1 decimal), and `reliability_label`.
Here is the input data:
```json
[
    {"repository": "repo_1", "review_rigor_score": 45.6, "pr_merge_ratio": 96.1, "contributor_diversity_index": 97.9, "issue_resolution_rate": 86.4},
    {"repository": "repo_2", "review_rigor_score": 28.7, "pr_merge_ratio": 49.3, "contributor_diversity_index": 10.5, "issue_resolution_rate": 44.7},
    {"repository": "repo_3", "review_rigor_score": 59.1, "pr_merge_ratio": 41.1, "contributor_diversity_index": 28.9, "issue_resolution_rate": 39.2},
    {"repository": "repo_4", "review_rigor_score": 58.7, "pr_merge_ratio": 44.8, "contributor_diversity_index": 44.2, "issue_resolution_rate": 42.4},
    {"repository": "repo_5", "review_rigor_score": 36.2, "pr_merge_ratio": 41.0, "contributor_diversity_index": 74.5, "issue_resolution_rate": 33.0}
]
```

### Goal
Provide new repository metrics (X) to the AI system and request the calculation of the *Repository Reliability Index (RRI)* and reliability classification.

### Formula
\[
RRI = (review\_rigor\_score + pr\_merge\_ratio + contributor\_diversity\_index + issue\_resolution\_rate) / 4
\]

### Reliability Scale
- 0–40 → **Poor**  
- 41–60 → **Moderate**  
- 61–80 → **Good**  
- 81–100 → **Excellent**

### Input (X)
```json
[
    {"repository": "repo_1", "review_rigor_score": 45.6, "pr_merge_ratio": 96.1, "contributor_diversity_index": 97.9, "issue_resolution_rate": 86.4},
    {"repository": "repo_2", "review_rigor_score": 28.7, "pr_merge_ratio": 49.3, "contributor_diversity_index": 10.5, "issue_resolution_rate": 44.7},
    {"repository": "repo_3", "review_rigor_score": 59.1, "pr_merge_ratio": 41.1, "contributor_diversity_index": 28.9, "issue_resolution_rate": 39.2},
    {"repository": "repo_4", "review_rigor_score": 58.7, "pr_merge_ratio": 44.8, "contributor_diversity_index": 44.2, "issue_resolution_rate": 42.4},
    {"repository": "repo_5", "review_rigor_score": 36.2, "pr_merge_ratio": 41.0, "contributor_diversity_index": 74.5, "issue_resolution_rate": 33.0}
]
```

### Output (Y)
```json
[
  {"repository": "repo_1", "RRI": 81.5, "reliability_label": "Excellent"},
  {"repository": "repo_2", "RRI": 33.3, "reliability_label": "Poor"},
  {"repository": "repo_3", "RRI": 42.1, "reliability_label": "Moderate"},
  {"repository": "repo_4", "RRI": 47.5, "reliability_label": "Moderate"},
  {"repository": "repo_5", "RRI": 46.2, "reliability_label": "Moderate"}
]
```

---
# Section 2 - Few Shot Approach
## 🧠 Prompt — Few-Shot (AI Learns from Example)
You are an AI agent trained to assess repository reliability.
Learn from the example below showing how input metrics map to an RRI and reliability classification. Then apply the same logic to the new repositories provided.

Formula:

RRI=(review_rigor_score+pr_merge_ratio+contributor_diversity_index+issue_resolution_rate)/4

Scale:
-	0–40 → Poor
-	41–60 → Moderate
-	61–80 → Good
-	81–100 → Excellent

Known Example (X → Y):
-	Review Rigor Score: 76.7
-	PR Merge Ratio: 68.4
-	Contributor Diversity Index: 42.1
-	Issue Resolution Rate: 95.4
-	RRI: 70.6 → Good

New Input Data:
```json
[
    {
        "repository": "repo_A",
        "review_rigor_score": 82.3,
        "pr_merge_ratio": 90.4,
        "contributor_diversity_index": 87.9,
        "issue_resolution_rate": 91.0
    },
    {
        "repository": "repo_B",
        "review_rigor_score": 61.1,
        "pr_merge_ratio": 72.5,
        "contributor_diversity_index": 69.3,
        "issue_resolution_rate": 58.8
    },
    {
        "repository": "repo_C",
        "review_rigor_score": 48.2,
        "pr_merge_ratio": 51.4,
        "contributor_diversity_index": 55.0,
        "issue_resolution_rate": 45.9
    }
]
```

Return results both as a table and as JSON with fields: `repository`, `RRI` (rounded to 1 decimal), and `reliability_label`.

### Goal
Provide the AI with one known (X, Y) example to help it “learn” how RRI and reliability are determined, then predict the reliability for new repositories.

### Known Example
| Review Rigor | PR Merge | Diversity | Issue Resolution | RRI | Reliability |
|--------------|-----------|------------|------------------|------|--------------|
| 76.7 | 68.4 | 42.1 | 95.4 | **70.6** | **Good** |

### New Input (X)
```json
[
    {"repository": "repo_A", "review_rigor_score": 82.3, "pr_merge_ratio": 90.4, "contributor_diversity_index": 87.9, "issue_resolution_rate": 91.0},
    {"repository": "repo_B", "review_rigor_score": 61.1, "pr_merge_ratio": 72.5, "contributor_diversity_index": 69.3, "issue_resolution_rate": 58.8},
    {"repository": "repo_C", "review_rigor_score": 48.2, "pr_merge_ratio": 51.4, "contributor_diversity_index": 55.0, "issue_resolution_rate": 45.9}
]
```

### Output (Y)
```json
[
  {"repository": "repo_A", "RRI": 87.9, "reliability_label": "Excellent"},
  {"repository": "repo_B", "RRI": 65.4, "reliability_label": "Good"},
  {"repository": "repo_C", "RRI": 50.1, "reliability_label": "Moderate"}
]
```

---
# Section 3 - Detailed Approach
## ⚙️ Step 1 — Prompt: Generate Mock Metrics (X Variables)

**Prompt:**
> You are an AI assistant analyzing software repository reliability.  
> Generate mock values for the following four metrics for 5 GitHub repositories.  
> Each metric is on a scale from 0 to 100, where higher is better.  
> Metrics:
> - `review_rigor_score` (depth and frequency of code reviews)  
> - `pr_merge_ratio` (percentage of successfully merged pull requests)  
> - `contributor_diversity_index` (number and activity diversity of contributors)  
> - `issue_resolution_rate` (speed and efficiency of resolving issues)  
> Provide results as a JSON array with 5 repositories showing mixed performance levels.

### 🧾 Example Output (Mock X Data)

```json
[
  {"repository_name": "dev-roadmap", "review_rigor_score": 94, "pr_merge_ratio": 91, "contributor_diversity_index": 89, "issue_resolution_rate": 93},
  {"repository_name": "data-analyzer", "review_rigor_score": 78, "pr_merge_ratio": 82, "contributor_diversity_index": 79, "issue_resolution_rate": 74},
  {"repository_name": "webhelper", "review_rigor_score": 62, "pr_merge_ratio": 68, "contributor_diversity_index": 60, "issue_resolution_rate": 58},
  {"repository_name": "testmate", "review_rigor_score": 86, "pr_merge_ratio": 90, "contributor_diversity_index": 88, "issue_resolution_rate": 84},
  {"repository_name": "bugtrack-lite", "review_rigor_score": 42, "pr_merge_ratio": 55, "contributor_diversity_index": 50, "issue_resolution_rate": 39}
]
```

---

## 🧮 Step 2 — Prompt: Calculate Reliability Index (Y Output)

**Prompt:**
> Based on the following repository metrics, calculate the *Repository Reliability Index (RRI)* for each repository.  
> Formula:  
> \[
> RRI = (review\_rigor\_score + pr\_merge\_ratio + contributor\_diversity\_index + issue\_resolution\_rate) / 4
> \]
> Then classify the reliability based on this scale:
> - 0–40 → **Poor**
> - 41–60 → **Moderate**
> - 61–80 → **Good**
> - 81–100 → **Excellent**  
> Return an Excel and JSON output with each repository’s calculated RRI (rounded to 1 decimal) and reliability label.

### ✅ Example Excel Output (With Calculations)

| Repository | Review Rigor | PR Merge | Contributor Diversity | Issue Resolution | RRI (avg) | Reliability |
|-------------|------------------|-------------|------------------|--------------|------------|--------------|
| dev-roadmap | 95 | 92 | 88 | 90 | **91.25** | **Excellent** |
| data-analyzer | 78 | 85 | 80 | 75 | **79.5** | **Good** |
| webhelper | 60 | 65 | 55 | 50 | **57.5** | **Moderate** |
| testmate | 82 | 87 | 90 | 85 | **86.0** | **Excellent** |
| bugtrack-lite | 40 | 40 | 35 | 35 | **37.5** | **Poor** |

### 💡 Example JSON Output

```json
[
  {"repository_name": "dev-roadmap", "reliability_index": 91.25, "reliability_level": "Excellent"},
  {"repository_name": "data-analyzer", "reliability_index": 79.5, "reliability_level": "Good"},
  {"repository_name": "webhelper", "reliability_index": 57.5, "reliability_level": "Moderate"},
  {"repository_name": "testmate", "reliability_index": 86.0, "reliability_level": "Excellent"},
  {"repository_name": "bugtrack-lite", "reliability_index": 37.5, "reliability_level": "Poor"}
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
| dev-roadmap | Excellent | Maintain rigorous code review practices and strong contributor engagement. |
| testmate | Excellent | Keep high merge efficiency and issue responsiveness. |
| data-analyzer | Good | Enhance contributor diversity and speed of issue resolution to reach excellent reliability. |
| webhelper | Moderate | Increase review rigor and contributor activity. |
| bugtrack-lite | Poor | Focus on faster issue resolution and higher-quality reviews to improve reliability. |

---

## 🧠 Step 4 — Prompt: Final AI-driven Interpretation

**Prompt:**
> Based on the RRI results, generate a short paragraph (4–5 sentences) that an AI analyst could include in a reliability assessment report.  
> Mention which repositories show strong software process maturity and which indicate risk areas.

### 🗒️ Example Output

> The AI analysis revealed that dev-roadmap and testmate are the most reliable repositories, showcasing mature development processes and strong contributor engagement. Data-analyzer demonstrates good performance but could enhance its issue resolution rate to achieve excellent reliability. Webhelper is moderately reliable, reflecting areas for improvement in review quality and developer activity. Bugtrack-lite remains high-risk, requiring targeted improvements in collaboration and responsiveness to boost its reliability index.

---

# 📘 Reflection: Pros & Cons of Using ChatGPT for Lab 4

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
