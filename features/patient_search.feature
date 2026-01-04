@smoke @regression
Feature: Search patients
  As a user
  I want to search patients
  So that I can find specific records

  Scenario: Search patient by name
    Given a list of patients
    When I search for the name "Alice"
    Then I should get 1 matching patient
