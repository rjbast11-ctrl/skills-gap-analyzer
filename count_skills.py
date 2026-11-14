import json

data = json.load(open("adzuna_sample.json"))
tools = ["sql", "python", "tableau", "power bi", "excel", "aws", "azure", "looker"]
hits = 0
for item in data["results"]:
    text = item["description"].lower()
    if any(t in text for t in tools):
        hits += 1
print(f"{hits} of {len(data['results'])} postings mention a common tool")