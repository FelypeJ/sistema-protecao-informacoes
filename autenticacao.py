import hashlib
import hmac
import json
import os
from pathlib import Path

ARQUIVO_USUARIOS = Path(__file__).with_name("usuarios.json")
ITERACOES = 600_000

def _carregar_usuarios():
    if not ARQUIVO_USUARIOS.exists():
        return {}
    try:
        return json.loads(ARQUIVO_USUARIOS.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        raise RuntimeError("Não foi possível ler o arquivo de usuários.")

def _salvar_usuarios(usuarios):
    ARQUIVO_USUARIOS.write_text(
        json.dumps(usuarios, indent=4, ensure_ascii=False),
        encoding="utf-8"
    )

def cadastrar_usuario(usuario, senha):
    if not usuario:
        raise ValueError("O nome de usuário não pode ficar vazio.")
    if len(senha) < 8:
        raise ValueError("Use uma senha com pelo menos 8 caracteres.")

    usuarios = _carregar_usuarios()
    if usuario in usuarios:
        raise ValueError("Esse usuário já está cadastrado.")

    salt = os.urandom(16)
    derivacao = hashlib.pbkdf2_hmac(
        "sha256", senha.encode("utf-8"), salt, ITERACOES
    )
    usuarios[usuario] = {
        "salt": salt.hex(),
        "hash": derivacao.hex(),
        "iteracoes": ITERACOES
    }
    _salvar_usuarios(usuarios)

def autenticar_usuario(usuario, senha):
    usuarios = _carregar_usuarios()
    registro = usuarios.get(usuario)
    if registro is None:
        return False

    salt = bytes.fromhex(registro["salt"])
    hash_armazenado = bytes.fromhex(registro["hash"])
    iteracoes = int(registro["iteracoes"])

    tentativa = hashlib.pbkdf2_hmac(
        "sha256", senha.encode("utf-8"), salt, iteracoes
    )
    return hmac.compare_digest(tentativa, hash_armazenado)
