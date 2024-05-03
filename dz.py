def print_personal_data(**kwargs):
    sorted_kwargs = dict(sorted(kwargs.items()))
    for key, value in sorted_kwargs.items():
        print(f"{key}: {value}")






def get_words_list(text):
    punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
    result=[]
    text = text.lower
    for i in text:
        if i in punctuation_list:
            text[i].remove
        else:
            result.append(i)
            
            
text_example = "Arrakis, the planet known as Dune, is forever his place."



print(get_words_list(text=text_example))


            
