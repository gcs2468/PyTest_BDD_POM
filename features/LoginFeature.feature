@Regression @Smoke
Feature: Login feature

  @Regression @Smoke
  Scenario: Verify the title
    Given I am at login page of OrangeHrm
    Then Verify the title

  @Regression @Smoke
  Scenario: Verify the title two
    Given I am at login page of OrangeHrm
    Then Verify the title two

  @Smoke
  Scenario: Login with valid data
    Given I am at login page of OrangeHrm
    When I enter "Admin" in username field
    And I enter "admin123" in password field
    And I click on login button
    Then I should see Welcome Admin text
    And I click on logout button

  @Regression @Smoke
  Scenario Outline: Login with valid data with examples
    Given I am at login page of OrangeHrm
    When I enter <username> in userid field
    And I enter <password> in password field
    And I click on login button
    Then I should see Welcome Admin text
    And I click on logout button

    Examples:
      | username | password |
      | Admin    | admin123 |
#      | Admin    | admin123 |
#      | Admin    | admin123 |