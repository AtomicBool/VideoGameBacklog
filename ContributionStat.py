############################
#####   GPT Genrated   #####
############################

import subprocess
from collections import defaultdict

# 1. Path to your Git repository
repo_path = "./"

# 2. Get commits with line changes per author
# --numstat outputs: added \t deleted \t filename
cmd = ["git", "-C", repo_path, "log", "--pretty=format:%an", "--numstat"]

result = subprocess.run(cmd, capture_output=True, text=True)
lines = result.stdout.splitlines()

contributions = defaultdict(lambda: {"added": 0, "deleted": 0})
current_author = None

for line in lines:
    if line.strip() == "":
        continue
    # If the line has no tab, it's the author name
    if "\t" not in line:
        current_author = line.strip()
        continue
    # Otherwise it's a numstat line: added, deleted, filename
    added, deleted, _ = line.split("\t")
    added = int(added) if added != "-" else 0
    deleted = int(deleted) if deleted != "-" else 0
    contributions[current_author]["added"] += added
    contributions[current_author]["deleted"] += deleted

# 3. Compute total lines and contribution percentage
total_lines = sum(v["added"] + v["deleted"] for v in contributions.values())
contrib_percentage = {author: (v["added"] + v["deleted"]) / total_lines * 100
                      for author, v in contributions.items()}

# 4. Print results
print("Git Repository Contributions (by lines changed):")
for author, stats in contributions.items():
    total = stats["added"] + stats["deleted"]
    print(f"{author}: +{stats['added']} / -{stats['deleted']} lines, total {total} lines, "
          f"percentage {contrib_percentage[author]:.2f}%")