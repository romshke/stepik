with open('cyrillic.txt', encoding='utf8') as cyrillic, open('transliteration.txt', 'w') as transliteration:
    transliterated_letters = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
    }
    
    text = cyrillic.read()
    result = str()
    
    for _ in text:
        if _ in [chr(_) for _ in range(ord('А'), ord('я') + 1)] + ['Ё', 'ё']:
            
            result += transliterated_letters[_] if _.islower() else transliterated_letters[_.lower()].title()
        else: result += _
        
    transliteration.write(result)