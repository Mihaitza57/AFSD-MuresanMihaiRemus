print("hello world")
print("hi github")
# Program care procesează un articol de știri stocat local (fără acces la internet)

# Declaram un șir de caractere cu un text de știri în limba română
text = """România a înregistrat o creștere economică semnificativă în ultimul trimestru,
potrivit datelor publicate de Institutul Național de Statistică. Specialiștii spun că
această evoluție este susținută de creșterea consumului intern și de investițiile din sectorul privat."""

# Împărțim textul în două părți egale
lungime = len(text)
jumatate = lungime // 2
partea1 = text[:jumatate]
partea2 = text[jumatate:]

# --- Operații pe prima parte ---
# Transformăm toate literele în majuscule și eliminăm spațiile de la început și final
partea1 = partea1.upper().strip()

# --- Operații pe a doua parte ---
# Inversăm ordinea caracterelor
partea2 = partea2[::-1]
# Transformăm prima literă în majusculă
partea2 = partea2.capitalize()
# Eliminăm semnele de punctuație (. , ! ?)
for semn in ".,!?":
    partea2 = partea2.replace(semn, "")

# Combinăm cele două părți
rezultat = partea1 + " " + partea2

# Afișăm rezultatul final
print("Rezultatul final:\n")
print(rezultat)
