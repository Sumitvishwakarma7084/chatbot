from openai import OpenAI
client = OpenAI(api_key="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")

response = client.responses.create(
    model="gpt-4.1",
    input="50 interview question for c++.",
)

print(response.output_text)
