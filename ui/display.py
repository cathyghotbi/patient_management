def display_patients(patients):
    if not patients:
        print("No patients found.")
        return

    for p in patients:
        print(
            f"Name: {p.name}, "
            f"Age: {p.age()}, "
            f"Diseases: {', '.join(p.diseases)}"
        )
