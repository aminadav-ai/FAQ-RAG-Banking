import unicodedata, re

def normalize(text: str) -> str:
    """Basic ASCII/Unicode normalization and cleanup."""
    text = unicodedata.normalize("NFC", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.lower()
