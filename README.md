# Sistema de Proteção de Informações

Projeto educativo em Python que reúne conceitos de criptografia, hash,
integridade, autenticação e espaço de combinações.

## Requisitos
- Python 3.10 ou superior
- Nenhuma biblioteca externa

## Como executar
1. Extraia a pasta do projeto.
2. Abra a pasta no VS Code.
3. Abra o terminal integrado.
4. Execute:

```bash
python main.py
```

No Windows, se `python` não funcionar, tente:

```bash
py main.py
```

## Arquivos
- `main.py`: menu principal.
- `criptografia.py`: cifra e decifra usando Cifra de César.
- `hash_utils.py`: SHA-256 e comparação de integridade.
- `autenticacao.py`: cadastro e autenticação com PBKDF2-HMAC-SHA256 e salt aleatório.
- `combinacoes.py`: cálculo de possibilidades e simulação didática local.

## Conceitos importantes e limites
- A Cifra de César é um exemplo histórico para aprendizagem. **Não protege dados reais**.
- SHA-256 é útil para resumos e integridade, mas **não deve ser usado sozinho para armazenar senhas**.
- O módulo de autenticação usa PBKDF2-HMAC-SHA256, salt aleatório e comparação segura.
  É um exemplo didático local, não um sistema pronto para produção.
- A demonstração de tentativas usa somente uma pequena lista fictícia embutida.
  Ela não tenta descobrir senhas reais nem acessa serviços externos.
- O arquivo `usuarios.json` é criado automaticamente após o primeiro cadastro.
  Ele guarda salt e hash derivados, não a senha em texto puro.
- Para um sistema real, também seriam necessários controles como limitação de tentativas,
  recuperação segura de conta, proteção do arquivo, HTTPS, auditoria e gestão de segredos.

## Testes manuais sugeridos
1. Codifique `Ola Mundo` com deslocamento 3 e depois decodifique.
2. Gere o hash de `casa`; gere novamente e compare.
3. Compare `casa` com `casas` na opção de integridade.
4. Cadastre um usuário com senha de pelo menos 8 caracteres.
5. Faça login com a senha correta e depois com uma incorreta.
6. Calcule as combinações para tamanhos 1, 2 e 3.
7. Execute a simulação didática.
