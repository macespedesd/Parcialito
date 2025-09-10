import re

texto = "Bonjour! En 2025, 21 photographes capturent des instants. Liste: appareil, objectif, trépied. Le prix est de 88,30€. Les étoiles (★) inspirent la nuit. 17 chats photographient, 16 chiens éditent. Le code #7788 est spécial. 20 jours d'expo, 14 jours de repos. @tous capturent. Le numéro magique est 1323. Que feriez-vous avec 60,80€? La réponse est dans la liste: cadrer, déclencher, éditer. Capturez votre monde! 100 mots, 20 entiers, 3 decimales, 2 listas."

# palabras (cuenta también con tildes y ñ)
patronp = r"[A-Za-zÁÉÍÓÚáàéèíìóòúùÜüÑñ]+"
palabras = re.findall(patronp, texto)
# enteros que no se confundan con decimales
patrone = r"(?<!\d)\d+(?!\,\d)"
enteros = re.findall(patrone, texto)

# decimales
patronf = r"\d+\,\d+"
decimales = re.findall(patronf, texto)

# listas (captura después de 'lista:')
patronl = r"[Ll]iste:\s*([^\.!?\n]+)"
listas = re.findall(patronl, texto)
#r"(?i)\blista:\s*([^\.\n]+)"

print("Palabras:", len(palabras), palabras)
print("Enteros:", len(enteros), enteros)
print("Decimales:", len(decimales), decimales)
print("Listas:", len(listas), listas)