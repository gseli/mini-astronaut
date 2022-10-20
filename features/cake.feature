# Created by elizabeth at 20/10/22
Feature: Cake
  As a Customer
  I want to see available cakes
  So that I can choose which to buy

  Scenario: Vegans
    Given some of the cakes can be bought by vegans
    When I mark the vegan cakes
    Then vegan cakes can only be bought by vegans
    And I am a vegan