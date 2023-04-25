def uppercase_string(string):
    '''принимает на вход строку и возвращает ее со всеми заглавными буквами'''
    return string.upper()

def capitalize_string(string):
    """Принимает на вход строку и возвращает ее с заглавными первыми буквами каждого слова."""
    return ' '.join(word.capitalize() for word in string.split())
