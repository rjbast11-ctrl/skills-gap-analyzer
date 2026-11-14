import os, json, requests
from dotenv import load_dotenv

load_dotenv()
params = {
    "app_id": os.environ["ADZUNA_APP_ID"],
    "app_key": os.environ["ADZUNA_APP_KEY"],
    "what": "data analyst",
    "results_per_page": 25,
    "content-type": "application/json",
}
r = requests.get("https://api.adzuna.com/v1/api/jobs/us/search/1", params=params)
print("Status:", r.status_code)
data = r.json()
with open("adzuna_sample.json", "w") as f:
    json.dump(data, f, indent=2)
print("Saved adzuna_sample.json")

results = data.get("results", [])
print("Postings returned:", len(results))
lengths = [len(item.get("description", "")) for item in results]
if lengths:
    print("Description length - min:", min(lengths), "max:", max(lengths),
          "avg:", sum(lengths) // len(lengths))

for item in results[:3]:
    print("\n" + "=" * 60)
    print("Title:", item.get("title"))
    print("Company:", item.get("company", {}).get("display_name"))
    print("Description:", item.get("description"))