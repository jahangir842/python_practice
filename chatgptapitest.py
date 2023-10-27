import openai
openai.api_key = "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"

def Senitment_analysis(text):
    messages = [
        {"role": "system", "content": """You are trained to analyze and detect the sentiment of given text.
                                        If you're unsure of an answer, you can say "not sure" and recommend users to review manually."""},
        {"role": "user", "content": f"""Analyze the following text and determine if the sentiment is: positive or negative.
                                        Return answer in single word as either positive or negative: {text}"""}
        ]

    response = openai.ChatCompletion.create(
                      model="gpt-3.5-turbo",
                      messages=messages,
                      max_tokens=1,
                      n=1,
                      stop=None,
                      temperature=0)

    response_text = response.choices[0].message.content.strip().lower()

    return response_text

# calling the function
input = 'I hate fast food'
response = Senitment_analysis(input)
print(input,': The Sentiment is', response)