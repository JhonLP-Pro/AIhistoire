from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class TextGenerator:
    def __init__(self, model_name="asi/gpt-fr-cased-small"):
        """
        Initialise le générateur de texte avec un modèle GPT-2 français
        Args:
            model_name: Nom du modèle à utiliser (par défaut: "asi/gpt-fr-cased-small")
        """
        # Charge le tokenizer et le modèle pré-entraîné
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        
        # Déplace le modèle sur GPU si disponible
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)
        
        # Configure le modèle en mode évaluation
        self.model.eval()

    def generate_text(self, prompt, max_length=100, num_return_sequences=1, 
                     temperature=0.7, top_k=50, top_p=0.95):
        """
        Génère du texte à partir d'un prompt donné
        
        Args:
            prompt: Texte d'entrée pour initier la génération
            max_length: Longueur maximale du texte généré
            num_return_sequences: Nombre de séquences à générer
            temperature: Contrôle la créativité (plus haute = plus créatif)
            top_k: Nombre de tokens les plus probables à considérer
            top_p: Probabilité cumulative maximale pour le nucleus sampling
            
        Returns:
            Liste des textes générés
        """
        try:
            # Encode le prompt
            inputs = self.tokenizer.encode(prompt, return_tensors="pt")
            inputs = inputs.to(self.device)

            # Génère le texte avec les paramètres spécifiés
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs,
                    max_length=max_length,
                    num_return_sequences=num_return_sequences,
                    temperature=temperature,
                    top_k=top_k,
                    top_p=top_p,
                    pad_token_id=self.tokenizer.eos_token_id,
                    do_sample=True
                )

            # Décode et retourne les séquences générées
            generated_texts = []
            for output in outputs:
                generated_text = self.tokenizer.decode(output, skip_special_tokens=True)
                generated_texts.append(generated_text)
                
            return generated_texts

        except Exception as e:
            print(f"Erreur lors de la génération du texte: {str(e)}")
            return [] 