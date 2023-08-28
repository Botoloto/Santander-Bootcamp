import openai
import pandas as pd

openai_api_key = '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'
openai.api_key = openai_api_key
msgs = []

df = pd.read_excel('names for ia.xlsx')
names = df[['Nomes']].stack().values.tolist()


def gerar_nova_mensagem(user):
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages= [
            {
                "role": "system",
                "content": "Você é um especialista em marketing e conversão bancária."
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem para {user} incentivando a estudar a importância do python no dia a dia das empresas. (máximo 100 caracteres)"

            }
        ]
    )

    return completion.choices[0].message.content.strip('"')

for name in names:
    try:
        msg = gerar_nova_mensagem(name)
        msgs.append(msg)
        print(msg)
    except:
        msgs.append('')
        # print("erro")

df['Frases'] = msgs
# df['Frases'] = df['Frases'].reset_index()
df.to_excel('frases.xlsx')
