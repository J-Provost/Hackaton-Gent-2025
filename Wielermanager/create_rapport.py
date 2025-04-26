import json
from collections import defaultdict

# Definieer je categorieën
positieve_categorieën = ["time_value", "service_score", "tires_changed", "returns"]
negatieve_categorieën = ["lateness", "coffee"]

# Laad votes
with open("Wielermanager/votes.json", "r") as f:
    votes = json.load(f)

vertrouwen = defaultdict(lambda: {"positief": 0, "negatief": 0, "categorieën": defaultdict(int)})

# Tellen per persoon
for categorie, keuzes in votes.items():
    for werknemer, aantal in keuzes.items():
        vertrouwen[werknemer]["categorieën"][categorie] = aantal
        if categorie in positieve_categorieën:
            vertrouwen[werknemer]["positief"] += aantal
        elif categorie in negatieve_categorieën:
            vertrouwen[werknemer]["negatief"] += aantal

# Schrijven naar .txt bestand
with open("rapporten/vertrouwensrapport.txt", "w", encoding="utf-8") as f:
    f.write("📊 Vertrouwensrapport per werknemer\n")
    f.write("Deze data is een overzicht van wat alle medewerkers denken dat ze het meest van doen.\n")
    f.write("====================================\n\n")

    for werknemer, data in sorted(vertrouwen.items(), key=lambda x: (x[1]['positief'] - x[1]['negatief']), reverse=True):
        totaal = data["positief"] + data["negatief"]
        score = data["positief"] - data["negatief"]
        f.write(f"👤 {werknemer}\n")
        f.write(f"  ↪ Positieve stemmen: {data['positief']}\n")
        f.write(f"  ↪ Negatieve stemmen: {data['negatief']}\n")
        f.write(f"  ↪ Vertrouwensscore: {score}\n")
        f.write(f"  ↪ Stemmen per categorie:\n")
        for cat, val in data["categorieën"].items():
            f.write(f"    - {cat}: {val}\n")
        f.write("\n")

print("✅ Vertrouwensrapport gegenereerd als vertrouwensrapport.txt")
