def select_employees_for_categories(employee_names):
    categories = [
        'time_value',
        'coffee',
        'tires_changed',
        'returns',
        'service_score',
        'lateness'
    ]
    picks = {}
    print("\nKies per categorie de naam van de werknemer die je kiest:")
    for category in categories:
        print(f"\nCategorie: {category.replace('_', ' ').capitalize()}")
        print("Beschikbare werknemers:", ", ".join(employee_names))
        choice = input("> Jouw keuze: ")
        while choice not in employee_names:
            print("Ongeldige keuze. Kies opnieuw.")
            choice = input("> Jouw keuze: ")
        picks[category] = choice
    return picks