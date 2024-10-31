# Importe le générateur de texte
from text_generator import TextGenerator

# Crée une instance du générateur
generator = TextGenerator("asi/gpt-fr-cased-small")

# Demande le prompt à l'utilisateur
print("Entrez votre début d'histoire (par exemple: 'Il était une fois...'): ")
prompt = input()

# Génération du texte
generated_texts = generator.generate_text(
    prompt=prompt,
    max_length=200,
    num_return_sequences=3,
    temperature=0.9
)

# Affiche les textes générés
for i, text in enumerate(generated_texts, 1):
    print(f"\nHistoire générée #{i}:")
    print(text)

# Demande si l'utilisateur veut générer une autre histoire
while True:
    print("\nVoulez-vous générer une autre histoire ? (oui/non): ")
    reponse = input().lower()
    if reponse != 'oui':
        break
        
    print("\nEntrez votre nouveau début d'histoire: ")
    prompt = input()
    
    generated_texts = generator.generate_text(
        prompt=prompt,
        max_length=200,
        num_return_sequences=3,
        temperature=0.9
    )
    
    for i, text in enumerate(generated_texts, 1):
        print(f"\nHistoire générée #{i}:")
        print(text) 