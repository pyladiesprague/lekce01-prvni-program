# ---------------------------------------------
#  Vzorové řešení: input
# ---------------------------------------------
# Tvoje řešení může vypadat trochu jinak, a to je v pořádku.


# 1) Zeptej se uživatele na jméno a ulož ho do proměnné.
jmeno = input("Jak se jmenuješ? ")


# 2) Pozdrav uživatele jeho jménem (např. Ahoj, Anna).
print("Ahoj,", jmeno)


# 3) Zeptej se ještě na jednu věc (třeba oblíbenou barvu)
#    a vypiš ji ve větě.
barva = input("Jaká je tvoje oblíbená barva? ")
print("Tvoje oblíbená barva je", barva)


# 4) Zeptej se uživatele na jeho věk, převeď ho na číslo
#    a vypiš, kolik mu bude za 10 let.
vek = int(input("Kolik ti je let? "))
print("Za 10 let ti bude", vek + 10)


# 5) Napiš krátký program, který se zeptá na jméno a pak vypíše
#    dva řádky:
#    Ahoj, <jmeno>
#    Vítej v Pythonu!
jmeno = input("Jak se jmenuješ? ")
print("Ahoj,", jmeno)
print("Vítej v Pythonu!")
