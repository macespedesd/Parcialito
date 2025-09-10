import re

texto = "Ciao! Nel 2025, 22 fotografi catturano momenti. Lista: macchina, obiettivo, treppiede. Il prezzo è €85,90. Le stelle (★) ispirano la notte. 16 gatti fotografano, 15 cani editano. Il codice #9911 è speciale. 19 giorni di sessione, 15 di riposo. @tutti fotografano. Il numero magico è 1333. Cosa faresti con 63,80€? La risposta è nella lista: inquadrare, scattare, modificare. Cattura il tuo mondo! 100 parole, 19 interi, 3 decimales, 2 listas."

# palabras (cuenta también con tildes y ñ)
patronp = r"[A-Za-zÁÉÍÓÚáàéèíìóòúùÜüÑñ]+"
palabras = re.findall(patronp, texto)

# enteros que no se confundan con decimales
patrone = r"(?<!\d)\d+(?!\,\d)"
enteros = re.findall(patrone, texto)

# decimales
patronf = r"\d+\,\d+"
decimales = re.findall(patronf, texto)

# listas
patronl = r"[Ll]ista:\s*([^\.!?\n]+)"
listas = re.findall(patronl, texto)


print("Palabras:", len(palabras), palabras)
print("Enteros:", len(enteros), enteros)
print("Decimales:", len(decimales), decimales)
print("Listas:", len(listas), listas)