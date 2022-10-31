#create a generic feature file
Feature: Tropical Fruits
  In order to eat healthy
  As a fruit lover
  I want to eat tropical fruits

  Scenario: Eat bananas
    Given I have 5 bananas
    When I eat 2 bananas
    Then I should have 3 bananas
