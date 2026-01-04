@regression
Feature: Group patients by disease

  Scenario: Group patients correctly
    Given patients with diseases
    When I group patients by disease
    Then Asthma should have 2 patients
    And Diabetes should have 1 patient
