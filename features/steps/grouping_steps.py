from behave import given, when, then
from datetime import date
from models.patient import Patient
from services.grouping import group_by_disease

@given("patients with diseases")
def step_given_patients(context):
    print("Running Given: patients with diseases")
    context.patients = [
        Patient("Alice", date(2000, 1, 1), ["Asthma"]),
        Patient("Bob", date(1980, 1, 1), ["Asthma", "Diabetes"])
    ]

@when("I group patients by disease")
def step_when_group(context):
    print("Running When: group patients by disease")
    context.groups = group_by_disease(context.patients)

@then("Asthma should have 2 patients")
def step_then_asthma(context):
    print("Running Then: check Asthma has 2 patients")
    assert len(context.groups["Asthma"]) == 2

@then("Diabetes should have 1 patient")
def step_then_diabetes(context):
    print("Running Then: check Diabetes has 1 patient")
    assert len(context.groups["Diabetes"]) == 1
