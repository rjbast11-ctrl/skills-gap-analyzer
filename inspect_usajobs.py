import json

with open("usajobs_sample.json") as f:
    data = json.load(f)

items = data["SearchResult"]["SearchResultItems"]
print("Postings returned:", len(items))

for item in items[:5]:
    d = item["MatchedObjectDescriptor"]
    details = d.get("UserArea", {}).get("Details", {})
    print("\n" + "=" * 60)
    print("Title:", d.get("PositionTitle"))
    print("Agency:", d.get("OrganizationName"))
    print("Qualification summary length:", len(d.get("QualificationSummary", "")))
    print("Job summary length:", len(details.get("JobSummary", "")))
    print("Major duties:", str(details.get("MajorDuties", ""))[:300])
    print("Qualification summary:", d.get("QualificationSummary", "")[:500])