# Oficina de engenharia de prompt do Elas@Conectam: IA e Diversidade
## Resumo do conteúdo teórico
[...]
## Pré-configuração para executar meu código
1. Definir a chave da API Gemini como variável global do ambiente Bash,
adicionando 'EXPORT GEMINI_API_KEY={Sua chave da API Gemini}' ao arquivo
.bashrc;
2. Testar se a chave está funcionando com uma primeira requisição à API. Por
exemplo: '''
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${GEMINI_API_KEY}" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Olá, meu caro."
          }
        ]
      }
    ]
  }'
''';
3. Instalar a biblioteca google-genai com 'pip install google-genai'.
