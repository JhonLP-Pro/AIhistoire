try:
    import transformers
    print(f"Transformers version: {transformers.__version__}")
    print("Transformers est correctement installé !")
except ImportError:
    print("Transformers n'est pas installé")

try:
    import torch
    print(f"PyTorch version: {torch.__version__}")
    print("PyTorch est correctement installé !")
except ImportError:
    print("PyTorch n'est pas installé") 