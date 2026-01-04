def before_scenario(context, scenario):
    print(f"\n--- STARTING SCENARIO: {scenario.name} ---")

def after_scenario(context, scenario):
    print(f"--- FINISHED SCENARIO: {scenario.name} ---\n")
