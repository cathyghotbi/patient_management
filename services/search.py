def search_by_name(patients, name):
    return [p for p in patients if name.lower() in p.name.lower()]

def search_by_disease(patients, disease):
    return [p for p in patients if disease in p.diseases]

def filter_by_min_age(patients, min_age):
    return [p for p in patients if p.age() >= min_age]
