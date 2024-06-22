import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", 'sk-proj-'),
)


def compute(prompt, max_tokens: int = 3000) -> str:
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=max_tokens,
        model="gpt-4o",
    )
    return response.choices[0].message.content.strip()


def compute_base(prompt, max_tokens: int = 3000) -> str:

    response = client.completions.create(
        model="davinci-002",
        prompt=prompt,
        max_tokens=max_tokens,
    )
    return response.choices[0].text.strip()


if __name__ == '__main__':
    r = compute("Qual è la teoria più accettata sull'origine dell'universo?")
    print(r)
