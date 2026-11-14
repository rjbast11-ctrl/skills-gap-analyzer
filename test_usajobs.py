import os, json, requests
from dotenv import load_dotenv

load_dotenv()
headers = {
    "Host": "data.usajobs.gov",
    "User-Agent": os.environ["USAJOBS_EMAIL"],
    "Authorization-Key": os.environ["USAJOBS_KEY"],
}
r = requests.get(
    "https://data.usajobs.gov/api/search",
    headers=headers,
    params={"Keyword": "data analyst", "ResultsPerPage": 25},
)
print("Status:", r.status_code)
data = r.json()
with open("usajobs_sample.json", "w") as f:
    json.dump(data, f, indent=2)
print("Saved usajobs_sample.json")