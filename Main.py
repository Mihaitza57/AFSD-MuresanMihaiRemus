print("hello world")
print("hi github")



text = """România a înregistrat o creștere economică semnificativă în ultimul trimestru,
potrivit datelor publicate de Institutul Național de Statistică. Specialiștii spun că
această evoluție este susținută de creșterea consumului intern și de investițiile din sectorul privat."""

lungime = len(text)
jumatate = lungime // 2
partea1 = text[:jumatate]
partea2 = text[jumatate:]

partea1 = partea1.upper().strip()
partea2 = partea2[::-1]
partea2 = partea2.capitalize()
for semn in ".,!?":
    partea2 = partea2.replace(semn, "")
rezultat = partea1 + " " + partea2
print("Rezultatul final:\n")
print(rezultat)
