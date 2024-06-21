import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", 'sk-proj-'),
)


def compute(prompt, max_tokens: int = 200):
    # response = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": f"Domanda: {question}\n Risposta:",
    #         }
    #     ],
    #     max_tokens=50,
    #     model="gpt-3.5-turbo",
    # )

    response = client.completions.create(
        model="davinci-002",
        prompt=prompt,
        max_tokens=max_tokens,
    )
    return response.choices[0].text.strip()


if __name__ == '__main__':
    r = compute("Qual è la teoria più accettata sull'origine dell'universo?")
    print(r)
