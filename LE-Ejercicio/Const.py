import openai

openai.api_key = "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"

response = openai.Completion.create(engine="text-davinci-002", prompt = '#Una charla normal entre comprador y vendedor de un departamento', max_tokens=12)

def Talking():
    

    while True:
        prompt = 'a:' + str(input()) + '\nb:'

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt = prompt,
            max_tokens=12,
            temperature=0.7,
            stop='\n',
            best_of=3
        )

        print(response['choices'][0]['text'])
        print('')

Talking()