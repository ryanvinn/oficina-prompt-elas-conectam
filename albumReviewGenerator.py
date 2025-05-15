import os
from google import genai

google = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

PROMPT = """
  Gere uma planilha contendo avaliações de álbuns musicais.
  A planilha deve conter uma coluna para o nome do álbum, outra para o nome do
  artista e outra para um comentário breve.
  Por exemplo:
  | NOME DO ÁLBUM   | ARTISTA       | COMENTÁRIO                                    |
  | Let It Be       | The Beatles   | Uma obra-prima atemporal. Essencial.          |
  | Legião Urbana V | Legião Urbana | Voz e letras poderosas. Um álbum emocionante. |
  | Back to Black   | Amy Winehouse | Voz e letras poderosas. Um álbum emocionante. |
  A planilha deve ser gerada em formato CSV, contendo 30 avaliações e variedade
  de gêneros.
  Cada comentário deve estar em apenas uma coluna. Em hipótese alguma divida um
  comentário em duas ou mais colunas.
"""
CSV_FILENAME = "avaliacoes_albuns.csv"
MODEL_NAME = "gemini-2.0-flash"

response = google.models.generate_content(
  model=MODEL_NAME,
  contents=PROMPT,
)

csv_content = response.text.strip().replace('```csv\n', '').replace('```', '')

with open(CSV_FILENAME, 'w', newline='', encoding='utf-8') as f:
  f.write(csv_content)

print("Arquivo CSV gerado com sucesso!")

