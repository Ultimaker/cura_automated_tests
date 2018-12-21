Feature: Basic behaviors

  Scenario: Open Ultimaker Cura
    Given "main_window" contains ""
    When we press the button "marketplace_menu"
    Then "cura_main_window" should contain "marketplace_dialog"