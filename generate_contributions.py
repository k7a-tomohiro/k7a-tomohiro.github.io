import os
from pathlib import Path
from github_oss_contributions import GitHubOssContributions

USERNAME = "k7a-tomohiro"   # ← 正確な GitHub username
OUT_DIR = Path("website/contributions")
TOKEN = os.getenv('$GITHUB_TOKEN')

client = GitHubOssContributions(username=USERNAME, token=TOKEN)
contributions = client.get_contributions()
print("Contributions fetched successfully:")
print(contributions)
# client.print_contributions()

# Return repository name from issue or PR url.
def get_repo(url: str) -> str:
    remains = url.removeprefix("https://github.com/")
    segments = remains.split("/")
    return segments[1]

# Escape markdown special characters.
def escape(s: str) -> str:
    s.replace("\\", "\\\\")
    s.replace("+", "\\+")
    s.replace("-", "\\-")
    s.replace("*", "\\*")
    s.replace("_", "\\_")
    s.replace("`", "\\`")
    s.replace(".", "\\.")
    s.replace("!", "\\!")
    s.replace("{", "\\{")
    s.replace("}", "\\}")
    s.replace("[", "\\[")
    s.replace("]", "\\]")
    s.replace("(", "\\(")
    s.replace(")", "\\)")

nav = ["  - Contributions:"]
for org, data in contributions.items():
    avatar_url = data.get("avatar_url", "")
    profile_url = data.get("profile_url", "")
    prs = data.get("prs", [])
    issues = data.get("issues", [])

    repo_data = dict()
    for item in prs:
        repo = get_repo(item["url"])
        if repo not in repo_data:
            repo_data[repo] = dict()
        if "prs" not in repo_data[repo]:
            repo_data[repo]["prs"] = list()
        repo_data[repo]["prs"].append(item)
    for item in issues:
        repo = get_repo(item["url"])
        if repo not in repo_data:
            repo_data[repo] = dict()
        if "issues" not in repo_data[repo]:
            repo_data[repo]["issues"] = list()
        repo_data[repo]["issues"].append(item)

    lines = []
    lines.append(f"# [{org}]({profile_url})\n\n")
    for repo, items in repo_data.items():
        prs = items.get("prs", [])
        issues = items.get("issues", [])
        lines.append(f"## [{repo}](https://github.com/{org}/{repo})\n\n")
        lines.append("\n### Pull Requests\n\n")
        for pr in prs:
            lines.append(f"- [{escape(pr['title'])}]({pr['url']})\n")
        lines.append("\n### Issues\n\n")
        for issue in issues:
            lines.append(f"- [{escape(issue['title'])}]({issue['url']})\n")
        content = "".join(lines)

    en = OUT_DIR / f"{org}.md"
    en.write_text(content, encoding="utf-8")
    nav.append(f"      {org}: \"contributions/{org}.md\"")

with open("mkdocs.yaml", "a") as mkdocs:
    mkdocs.write("\n".join(nav))
