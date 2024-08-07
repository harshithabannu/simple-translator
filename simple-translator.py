def translate(word, direction='fr_to_en'):
    # Dictionary for translation
    dictionary = {
        'bonjour': 'hello',
        'hello': 'bonjour',
        'salut': 'hi',
        'hi': 'salut',
        'bonsoir': 'good evening',
        'good evening': 'bonsoir',
        'bonne journée': 'good day',
        'good day': 'bonne journée',
        'bonne soirée': 'good evening',
        'bonne nuit': 'good night',
        'good night': 'bonne nuit',
        'enchanté(e)': 'nice to meet you',
        'nice to meet you': 'enchanté(e)',
        'ravie(e)': 'delighted to meet you',
        'delighted to meet you': 'ravie(e)',
        'comment allez-vous?': 'how are you?',
        'comment vas-tu?': 'how are you?',
        'how are you?': 'comment allez-vous? or comment vas-tu?',
        'ça va.': 'I\'m doing well.',
        'i\'m doing well.': 'ça va.',
        'au revoir': 'goodbye',
        'goodbye': 'au revoir',
        'à bientôt': 'see you soon',
        'see you soon': 'à bientôt',
        'salut!': 'bye!',
        'bye!': 'salut!',
        'enchanté(e) de faire votre connaissance': 'pleased to meet you',
        'pleased to meet you': 'enchanté(e) de faire votre connaissance'
    }

    # Translate the word or phrase
    return dictionary.get(word.lower(), 'Translation not found')

def main():
    print("Simple Language Translator")
    print("Supported directions: 'fr_to_en' (default), 'en_to_fr'")
    print("Example phrases: Bonjour, Hello, Salut, Hi, Bonsoir, Good evening, etc.")
    
    word = input("Enter the word or phrase to translate: ")
    direction = input("Enter the direction (fr_to_en or en_to_fr): ")

    if direction not in ['fr_to_en', 'en_to_fr']:
        direction = 'fr_to_en'  # Default direction

    translation = translate(word, direction)
    print(f"The translation of '{word}' is: '{translation}'")

if __name__ == "__main__":
    main()
