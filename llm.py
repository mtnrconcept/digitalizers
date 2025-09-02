import requests

def classify_email(text):
    prompt = f"""Tu es un assistant de tri d'e-mails. Classe l'e-mail suivant dans l'une des catégories suivantes : 'urgent', 'réunion', 'informations', 'à ignorer'.

E-mail : {text}

Réponds uniquement par une des catégories sans explication."""

    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",  # À adapter selon ton modèle
        "prompt": prompt,
        "stream": False
    })

    return res.json()["response"].strip().lower()
