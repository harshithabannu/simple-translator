# Simple Language Translator

## Overview

This Python script provides a simple language translation system between French and English. It translates common phrases and words based on a predefined dictionary. The script allows users to specify the translation direction between French and English.

## Features

- **Translation Directions:** Supports translation from French to English and vice versa.
- **Customizable Dictionary:** Easily update or add more phrases to the dictionary.
- **Interactive Interface:** User-friendly command-line interface for translation.

## Supported Directions

- **French to English (`fr_to_en`):** Translates French phrases to English.
- **English to French (`en_to_fr`):** Translates English phrases to French.

## Example Phrases

- Bonjour → Hello
- Salut → Hi
- Bonsoir → Good evening
- Bonne journée → Good day
- Au revoir → Goodbye
- À bientôt → See you soon

## Installation

To run the script on your local machine:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/simple-language-translator.git
    ```

2. **Navigate to the project directory:**
    ```sh
    cd simple-language-translator
    ```

3. **Ensure you have Python installed.**

4. **Run the script:**
    ```sh
    python translator.py
    ```

## How to Use

1. **Start the Script:** Run `python translator.py`.
2. **Enter the Word or Phrase:** Type the word or phrase you want to translate.
3. **Specify the Direction:** Choose between 'fr_to_en' (default) or 'en_to_fr'.
4. **View the Result:** The script will display the translation based on the input.

## Customizing the Dictionary

To add or include any language in the translation system:

1. Open the `translator.py` file.
2. Modify the `dictionary` variable to include new translations. You can add new words or phrases and their translations in the dictionary.

For example, to add translations for Spanish:
```python
dictionary = {
    'bonjour': 'hello',
    'hello': 'bonjour',
    ...
    'hola': 'hello',         # Spanish to English
    'hello': 'hola',         # English to Spanish
}

## Example
**An example interaction with the script:**
Simple Language Translator
Supported directions: 'fr_to_en' (default), 'en_to_fr'
Example phrases: Bonjour, Hello, Salut, Hi, Bonsoir, Good evening, etc.

Enter the word or phrase to translate: Bonjour
Enter the direction (fr_to_en or en_to_fr): fr_to_en
The translation of 'Bonjour' is: 'Hello'

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.


## Acknowledgments

Thanks to Python documentation and the programming community for resources and support.
