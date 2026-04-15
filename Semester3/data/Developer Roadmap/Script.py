import requests
import pandas as pd
import time
import os
import re
from datetime import datetime

# -------------------------------
# GitHub API settings
# -------------------------------
repo = "kamranahmedse/developer-roadmap"   # Change to your target repo
token = ""      # Replace with your token
headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}

# -------------------------------
# Helper Functions
# -------------------------------

def clean_text(text):
    """Remove illegal characters for Excel export."""
    if not isinstance(text, str):
        return text
    # Remove ASCII control characters
    text = re.sub(r"[\x00-\x1F\x7F]", "", text)
    # Remove problematic Unicode chars Excel doesn't like
    text = re.sub(r"[\u200B-\u200F\u202A-\u202E\u2060-\u206F\uFEFF]", "", text)
    return text

def fetch_all_pages(url, delay=0.7):
    """Fetch paginated results from GitHub API."""
    all_data = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 403 and "X-RateLimit-Remaining" in response.headers:
            if response.headers["X-RateLimit-Remaining"] == "0":
                reset_time = int(response.headers["X-RateLimit-Reset"])
                sleep_duration = max(reset_time - time.time(), 0) + 5
                print(f"⏳ Rate limit exceeded. Sleeping {sleep_duration:.1f}s...")
                time.sleep(sleep_duration)
                continue
        elif response.status_code != 200:
            print(f"Error fetching {url}: {response.status_code}, {response.text}")
            break
        page_data = response.json()
        if isinstance(page_data, list):
            all_data.extend(page_data)
        else:
            break
        url = response.links['next']['url'] if 'next' in response.links else None
        time.sleep(delay)
    return all_data

# -------------------------------
# Fetch Data
# -------------------------------
print("Fetching Pull Requests...")
prs_data = fetch_all_pages(f"https://api.github.com/repos/{repo}/pulls?state=all&per_page=100")
print(f"PRs fetched: {len(prs_data)}")

print("Fetching Issues...")
issues_data = fetch_all_pages(f"https://api.github.com/repos/{repo}/issues?state=all&per_page=100")
issues_data = [i for i in issues_data if "pull_request" not in i]  # remove PRs
print(f"Issues fetched: {len(issues_data)}")

print("Fetching Contributors...")
contributors_data = fetch_all_pages(f"https://api.github.com/repos/{repo}/contributors?per_page=100")
print(f"Contributors fetched: {len(contributors_data)}")

# -------------------------------
# Build Unified Records
# -------------------------------
all_records = []

# Pull Requests
for pr in prs_data:
    all_records.append({
        "Record Type": "Pull Request",
        "Parent Type": "N/A",
        "ID": pr.get("number"),
        "Title": pr.get("title"),
        "State": pr.get("state"),
        "Author": pr.get("user", {}).get("login", "Unknown"),
        "Created At": pr.get("created_at"),
        "Closed At": pr.get("closed_at"),
        "Merged At": pr.get("merged_at"),
        "Labels": ", ".join([label["name"] for label in pr.get("labels", [])]),
        "Comments Count": pr.get("comments"),
        "Contributions": "N/A",
        "Comment Text": "N/A",
    })

    # PR Comments
    comments_url = f"https://api.github.com/repos/{repo}/issues/{pr['number']}/comments?per_page=100"
    comments = fetch_all_pages(comments_url)
    for c in comments:
        all_records.append({
            "Record Type": "Comment",
            "Parent Type": "Pull Request",
            "ID": pr.get("number"),
            "Title": pr.get("title"),
            "State": pr.get("state"),
            "Author": (c.get("user") or {}).get("login", "Unknown"),
            "Created At": c.get("created_at"),
            "Closed At": pr.get("closed_at"),
            "Merged At": pr.get("merged_at"),
            "Labels": ", ".join([label["name"] for label in pr.get("labels", [])]),
            "Comments Count": "N/A",
            "Contributions": "N/A",
            "Comment Text": c.get("body", ""),
        })

    # PR Review Comments
    review_comments_url = f"https://api.github.com/repos/{repo}/pulls/{pr['number']}/comments?per_page=100"
    review_comments = fetch_all_pages(review_comments_url)
    for rc in review_comments:
        all_records.append({
            "Record Type": "Comment",
            "Parent Type": "Pull Request",
            "ID": pr.get("number"),
            "Title": pr.get("title"),
            "State": pr.get("state"),
            "Author": (rc.get("user") or {}).get("login", "Unknown"),
            "Created At": rc.get("created_at"),
            "Closed At": pr.get("closed_at"),
            "Merged At": pr.get("merged_at"),
            "Labels": ", ".join([label["name"] for label in pr.get("labels", [])]),
            "Comments Count": "N/A",
            "Contributions": "N/A",
            "Comment Text": rc.get("body", ""),
        })

# Issues
for issue in issues_data:
    all_records.append({
        "Record Type": "Issue",
        "Parent Type": "N/A",
        "ID": issue.get("number"),
        "Title": issue.get("title"),
        "State": issue.get("state"),
        "Author": issue.get("user", {}).get("login", "Unknown"),
        "Created At": issue.get("created_at"),
        "Closed At": issue.get("closed_at"),
        "Merged At": "N/A",
        "Labels": ", ".join([label["name"] for label in issue.get("labels", [])]),
        "Comments Count": issue.get("comments"),
        "Contributions": "N/A",
        "Comment Text": "N/A",
    })

    # Issue Comments
    comments_url = f"https://api.github.com/repos/{repo}/issues/{issue['number']}/comments?per_page=100"
    comments = fetch_all_pages(comments_url)
    for c in comments:
        all_records.append({
            "Record Type": "Comment",
            "Parent Type": "Issue",
            "ID": issue.get("number"),
            "Title": issue.get("title"),
            "State": issue.get("state"),
            "Author": (c.get("user") or {}).get("login", "Unknown"),
            "Created At": c.get("created_at"),
            "Closed At": issue.get("closed_at"),
            "Merged At": "N/A",
            "Labels": ", ".join([label["name"] for label in issue.get("labels", [])]),
            "Comments Count": "N/A",
            "Contributions": "N/A",
            "Comment Text": c.get("body", ""),
        })

# Contributors
for contr in contributors_data:
    all_records.append({
        "Record Type": "Contributor",
        "Parent Type": "N/A",
        "ID": "N/A",
        "Title": "N/A",
        "State": "N/A",
        "Author": contr.get("login"),
        "Created At": "N/A",
        "Closed At": "N/A",
        "Merged At": "N/A",
        "Labels": "N/A",
        "Comments Count": "N/A",
        "Contributions": contr.get("contributions"),
        "Comment Text": "N/A",
    })

# -------------------------------
# Export to Excel
# -------------------------------
df = pd.DataFrame(all_records)

# Clean text fields before export
df = df.applymap(clean_text)

# Fix datetime conversion for Created/Closed/Merged
for col in ["Created At", "Closed At", "Merged At"]:
    df[col] = pd.to_datetime(df[col], errors="coerce").dt.tz_localize(None)

# Sort by Created At
df = df.sort_values(by="Created At", na_position="last")

output_folder = "output"
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, "Repo_All_Data.xlsx")

df.to_excel(output_file, index=False)
print(f"\n Data exported successfully to: {output_file}")
