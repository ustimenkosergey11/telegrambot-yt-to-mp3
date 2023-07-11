pytube -> cipher.py -> get_throttling_function_name: 
Исправьте старые function_patterns на эти:
    function_patterns = [
        r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
    ]
И тогда бот будет корректно работать :)