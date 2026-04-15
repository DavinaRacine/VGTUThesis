# 🧮 End to End Solution Example Using kamranahmedse/developer-roadmap Repository
# Calculating the Repository Reliability Index

This document explains how the **Reliability Index** is calculated for the developer-roadmap repository based on data exported from GitHub using the `Script.py` file whose output is saved in the `Repo_All_Data.xlsx` file.  
It combines multiple quantitative indicators from Pull Requests, Issues, Comments, and Contributors (X Values / Inputs) to measure project reliability, responsiveness, and community health ( Y Value / Output) which is located in the `EndToEnd.xlsx` file.

---

## 📊 Y Value Overview (Reliability Index)

The **Reliability Index** provides a 0–1 score that summarizes how reliably a project manages contributions, pull requests, and issues.

Below table shows the computed four key metrics:

| Metric | Description | Formula |
|:--|:--|:--|
| **Review Rigor Score** | Quality of review process — average comments per pull request | Avg. review comments per PR |
| **PR Merge Ratio** | Efficiency & collaboration | Merged PRs ÷ Total PRs |
| **Contributor Diversity Index** | Breadth of community involvement | Unique PR authors ÷ Total PRs |
| **Issue Resolution Rate** | Responsiveness & issue management | Closed Issues ÷ Total Issues |

These four metrics are normalized and averaged to compute the **Reliability Index** which equals the below formula: (0.25(Review Rigor)+0.25(Merge Ratio)+0.25(Contributor Diversity)+0.25(Issue Resolution Rate)).

---

## 📥 X Value Overview (Expected Input Columns)

The Excel file `Repo_All_Data.xlsx` includes all extracted data using the `Script.py` file. Below table shows important columns:

| Column | Description |
|:--|:--|
| `Record Type` | `"Pull Request"`, `"Issue"`, `"Contributor"`, or `"Comment"` |
| `Parent Type` | `"Pull Request"` or `"Issue"` (for comments only) |
| `State` | `"open"` / `"closed"` |
| `Author` | Username of creator |
| `Merged At` | Timestamp for merged event |


All other columns were used for process mining tool ProM and not needed for the calculation of the reliability index.

---

## 📈 Excel File `EndToEnd.xlsx` Setup

The sheet named **`Data`** is data from the prior mentioned Excel file `Repo_All_Data.xlsx` moved to this `EndToEnd.xlsx` Excel file for analysis. The columns are structured as follows:

| Column | Header |
|:--:|:--|
| A | Record Type |
| B | Parent Type |
| C | ID |
| D | Title |
| E | State |
| F | Author |
| G | Created At |
| H | Closed At |
| I | Merged At |
| J | Labels |
| K | Comments Count |
| L | Contributions |
| M | Comment Text |


The sheet named **`Table`** has the calculation formulas/output and reasonings for the reliability index.
To calculate the four key metrics - Total PRs, Merged PRs, PRs Comments, Unique PR Authors, Total Issues, and Closed Issues were first calculated from the extracted data using Excel formulas. This information is summarized in the below table: 

| Value | Used Rows | 
|:--|:--|
| **Total PRs** | Count all mentions of "Pull Request" in column A in the **`Data`** sheet. |
| **Merged PRs** | Count all mentions of "Pull Request" in column A where column I is not empty in the **`Data`** sheet. |
| **PRs Comments** | Count all mentions of "Comment" in column A where column B is "Pull Request" in the **`Data`** sheet. |
| **Unique PR Authors** | Count all unique values in column F where column A is "Pull Request" in the **`Data`** sheet. | 
| **Total Issues** | Count all mentions of "Issue" in column A in the **`Data`** sheet. | 
| **Closed Issues** | Count all mentions of "Issue" in column A where column E is "closed" in the **`Data`** sheet. | 


---

## 🧮 Reliability Index Interpretation

Below is the Reliability Index classification from the calculated Y Value. 

| RI Range | Reliability Level | Interpretation |
|:--|:--|:--|
| **0.00 – 0.40** | Poor | Unstable repository; poor collaboration or review quality (slow responses, few merges, or minimal collaboration) |
| **0.41 – 0.60** | Moderate | Acceptable quality but needs process improvement (either reviews, merges, or issue handling may be weak) |
| **0.61 – 0.80** | Good | Reliable and actively maintained; good review and issue management (minor inefficiencies or limited contributor diversity) |
| **0.81 – 1.00** | Excellent | Exceptional reliability; strong collaboration and consistency (consistent reviews, merges, contributor engagement, and issue handling) |
