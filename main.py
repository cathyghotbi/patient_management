from services.loader import load_patients
from services.search import (
    search_by_name,
    search_by_disease,
    filter_by_min_age
)
from services.grouping import group_by_disease
from services.storage import save_to_json, save_to_csv
from ui.menu import menu
from ui.display import display_patients

def main():
    patients = load_patients("patients.json")
    groups = {}

    while True:
        menu()
        choice = input("Select an option: ")

        if choice == "1":
            display_patients(patients)

        elif choice == "2":
            name = input("Enter name to search: ")
            display_patients(search_by_name(patients, name))

        elif choice == "3":
            disease = input("Enter disease: ")
            display_patients(search_by_disease(patients, disease))

        elif choice == "4":
            min_age = int(input("Enter minimum age: "))
            display_patients(filter_by_min_age(patients, min_age))

        elif choice == "5":
            groups = group_by_disease(patients)
            for disease, group in groups.items():
                print(f"\nDisease: {disease}")
                display_patients(group)

        elif choice == "6":
            if not groups:
                groups = group_by_disease(patients)
            save_to_json(groups, "disease_groups.json")
            save_to_csv(groups, "disease_groups.csv")
            print("Data saved successfully.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
