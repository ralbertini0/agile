Feature: Give head quarter

    étant donnee un CEO
    je veux savoir si le CEO est toujours le meme
    Afin de ne pas confondre deux societe

    Scenario: retourner entreprise
        Given un CEO Bernard Arnault
        When demande entreprise
        Then retourner entreprise LVMH

    Scenario Outline: retourner entreprise
    Given un CEO <CEO>
    When demande entreprise
    Then retourner entreprise <entreprise>

    Examples:
        | CEO                | entreprise |
        | Bernard Arnault    | LVMH       |





