import openai

def get_car_ai_bio(model, brand,year):
    openai.api_key = ""
    prompt = ''' Deseja-se uma descrição de venda para o carro
    {} {} {} em apenas 250 caracteres. Atue como um
    vendedor de carros experiente, passando os pontos fortes deste carro.
    '''
    prompt = prompt.format(brand, model, year)
    response= openai.Completion.create(
        model ='text-davinci-003',
        prompt='',
        max_tokens=1000
    )
    return response['choices'][0]['text']