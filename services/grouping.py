from collections import defaultdict

def group_by_disease(patients):
    groups = defaultdict(list)
    for patient in patients:
        for disease in patient.diseases:
            groups[disease].append(patient)
    return groups
