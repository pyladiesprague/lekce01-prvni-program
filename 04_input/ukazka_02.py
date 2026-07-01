# ---------------------------------------------
#  input vždycky vrací text
# ---------------------------------------------
# Pozor na důležitou věc: cokoliv uživatel napíše, input vrátí
# jako TEXT – i když to vypadá jako číslo.
#
# Když chceš se vstupem počítat, musíš ho nejdřív převést na číslo.
# Spusť soubor a vyzkoušej.


# int(...) převede text na celé číslo:
vek = int(input("Kolik ti je let? "))
print("Za rok ti bude", vek + 1)


# float(...) převede text na desetinné číslo:
strana = float(input("Zadej stranu čtverce v cm: "))
print("Obvod čtverce je", 4 * strana, "cm")


# Kdybychom int(...) / float(...) vynechali, byl by vek text
# a vek + 1 by skončilo chybou – k textu se číslo přičíst nedá.
