from behave import given, when, then
from datetime import date
from models.patient import Patient
from services.search import search_by_name

@given("a list of patients")
def step_given_patients(context):
    print("Running Given: a list of patients")
    context.patients = [
        Patient("Alice Smith", date(2000, 1, 1), ["Asthma"]),
        Patient("Bob Jones", date(1980, 6, 15), ["Diabetes"])
    ]

@when('I search for the name "{name}"')
def step_when_search_name(context, name):
    print(f"Running When: search for name '{name}'")
    context.result = search_by_name(context.patients, name)

@then("I should get 1 matching patient")
def step_then_one_result(context):
    print("Running Then: check 1 matching patient")
    assert len(context.result) == 1
