Feature: Give optimisation_fiscal

    étant donnee une entreprise
    je veux savoir si elle pratique potentiellement l'evasion fiscal
    Afin de pouvoir la sanctionner

    Scenario: retourner fraud_detected
        Given une entreprise TAG HEUER
        When demande optimisation_fiscal
        Then retourner fraud_detected True

    Scenario Outline: retourner fraud_detected
    Given une entreprise <entreprise>
    When demande optimisation_fiscal
    Then retourner fraud_detected <fraud>

    Examples:
        | entreprise              | fraud |
        | TAG HEUER               | True  |







