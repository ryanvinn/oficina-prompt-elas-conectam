import os
from google import genai

google = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

csv_string = ''
with open('avaliacoes_albuns.csv', 'r') as file:
    csv_string = file.read()

PROMPT = """
  Planilha de avaliações musicais:
  {}
  A partir da planilha de avaliações musicais acima, contendo as colunas nome do
  álbum, artista e comentário, realize as seguintes tarefas:
  - Gerar a coluna adicional de classificação de gênero, com a classificação de
  gênero para cada álbumi (por exemplo, rock, pop, hip-hop, MPB, etc);
  - Gerar a coluna adicional de emoção predominante na avaliação, com a emoção
  predominante de cada avaliação (por exemplo, feliz, triste, entusiasmado, etc);
  - Gerar a coluna adicional de resumo de crítica, com o resumo da crítica de
  cada álbum;
  Mantenha inauterado o conteúdo das colunas originais.
  Por exemplo:
  | NOME DO ÁLBUM | ARTISTA | GÊNERO  | COMENTÁRIO | EMOÇÃO       | RESUMO |
  | [...]         | [...]   | Pop     | [...]      | Feliz        | [...]  |
  | [...]         | [...]   | Rock    | [...]      | Triste       | [...]  |
  | [...]         | [...]   | MPB     | [...]      | Neutro       | [...]  |
  | [...]         | [...]   | Hip-hop | [...]      | Entusiasmado | [...]  |
  A planilha deve ser gerada em formato CSV.
  Na coluna de resumo, não repita o conteúdo do comentário. Gere uma síntese
  de até 15 caracteres.
""".format(csv_string)
CSV_FILENAME = "avaliacoes_albuns_final.csv"
MODEL_NAME = "gemini-2.0-flash"

response = google.models.generate_content(
  model=MODEL_NAME,
  contents=PROMPT,
  config = {
    "temperature": 0.5,
  }
)

csv_content = response.text.strip().replace('```csv\n', '').replace('```', '')

with open(CSV_FILENAME, 'w', newline='', encoding='utf-8') as f:
  f.write(csv_content)

print("Arquivo CSV gerado com sucesso!")
