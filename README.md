# Oficina de engenharia de prompt do Elas@Conectam: IA e Diversidade
## Pré-configuração para executar meu código
1. Definir a chave da API Gemini como variável global do ambiente Bash, adicionando `export GEMINI_API_KEY={Sua chave da API Gemini}` ao arquivo .bashrc;
2. Testar se a chave está funcionando com uma primeira requisição à API. Por exemplo:
```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${GEMINI_API_KEY}" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"contents":[{"parts":[{"text": "Olá, meu nobre."}]}]}'
```
3. Instalar a biblioteca google-genai com `pip install google-genai`.

## Resumo do conteúdo teórico
- [Link do material](https://drive.google.com/file/d/11dpJJisKI0unFcJ9SZMBLjSHGKvag3Vn/view?pli=1)
- Prompt: instrução à IA Generativa;
- Bom prompt: claro, específico, estruturado e iterativo;
- Iteração: |-> ideia de prompt -> execução -> análise de resultados -> ajustes ->|;
- Componentes de um prompt: diretiva ou intenção, exemplos, formatação da saída, instruções de estilo e papel ou persona;
- Exemplos de tipos de tarefas: sumarização, geração de código, inferência, expansão, transformação, aprendizagem personalizada, classificação;
- Técnicas de prompting: few-shot, zero-shot, geração de pensamento, decomposição, autocrítica e combinação;
- Algumas ferramentas de apoio: *Shumer prompt*, *Promptperfect*, *Chatx*, *Prompts hub - por langchain hub* e *cursor*;
- Limitações e desafios: particularidades do prompt, generalização limitada, intencionalidade e fronteiras do conhecimento;
- Questões de segurança e guardrails;
- Questão se privacidade, ética e direitos autorais;
- Agentes e multiagentes;
- Temperatura;

## Referências do material
- https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering/
- https://dair-ai.thinkific.com/courses/prompt-engineering-devs
- https://developers.google.com/machine-learning/resources/prompt-eng
- https://arxiv.org/abs/2406.06608
