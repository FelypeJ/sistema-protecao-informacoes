import hashlib
import hmac

def gerar_hash(texto):
    """Gera SHA-256 de um texto codificado em UTF-8."""
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()

def verificar_integridade(texto_original, texto_recebido):
    """Compara hashes para verificar se os textos são idênticos."""
    hash_original = gerar_hash(texto_original)
    hash_recebido = gerar_hash(texto_recebido)
    return hmac.compare_digest(hash_original, hash_recebido)
