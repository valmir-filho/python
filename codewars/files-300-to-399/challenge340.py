"""
Pig latin is created by taking all the consonants before the first vowel (for the purposes of this kata,
a "vowel" is any letter from the set a, e, i, o, u) of a word and moving them to the back of the word followed by the letters "ay".

"hello" => "ellohay"
"creating" => "eatingcray"

If the first letter of the word is a vowel, the string is left the same and the letters "way" are appended to the end.

"algorithm" => "algorithmway"

If a word has no vowels, just append "ay" to the end of it.

"gym" => "gymay"

This problem is different from other variations in that it expects casing to remain the same so:

"Hello World" => "Ellohay Orldway"

as well as punctuation (for the purposes of this kata, "punctuation" includes ,, ., !, ?, :, ;).

"Pizza? Yes please!" => "Izzapay? Esyay easeplay!"

Numbers should be left as-is.

"0875568" => "0875568"

Your job is to take a string and translate it to Pig Latin. The string will never be undefined but may contain both numbers and letters.
A word will never be a combination of numbers and letters. Also, there will never be punctuation at the beginning of a word and the only
capital letter in a word will be the first letter meaning there are zero all capitalized words.
"""

import string


def translate(sentence):
   
    vowels = "aeiou"

    def translate_word(word):
        """Função auxiliar para traduzir uma única palavra."""
        # Regra 6: Números devem ser mantidos como estão.
        if word.isdigit():
            return word

        # Separa a pontuação do final da palavra.
        punctuation = ""
        # Itera do final da palavra para extrair qualquer pontuação.
        while word and word[-1] in string.punctuation:
            punctuation = word[-1] + punctuation
            word = word[:-1]

        # Se a palavra estiver vazia após remover a pontuação, retorna apenas a pontuação.
        if not word:
            return punctuation

        # Regra 4: Preserva a capitalização original.
        is_capitalized = word[0].isupper()
        # Converte a palavra para minúsculas para processamento.
        proc_word = word.lower()
        
        first_vowel_index = -1
        # Encontra o índice da primeira vogal.
        for i, char in enumerate(proc_word):
            if char in vowels:
                first_vowel_index = i
                break

        translated_word = ""
        # Regra 3: Se não houver vogais, apenas adiciona "ay".
        if first_vowel_index == -1:
            translated_word = proc_word + "ay"
        # Regra 2: Se a palavra começa com vogal, adiciona "way".
        elif first_vowel_index == 0:
            translated_word = proc_word + "way"
        # Regra 1: Se a palavra começa com consoante(s).
        else:
            consonants = proc_word[:first_vowel_index]
            rest_of_word = proc_word[first_vowel_index:]
            translated_word = rest_of_word + consonants + "ay"
            
        # Restaura a capitalização se a palavra original era capitalizada.
        if is_capitalized:
            translated_word = translated_word.capitalize()
            
        # Anexa a pontuação de volta ao final da palavra traduzida.
        return translated_word + punctuation

    # Divide a frase em palavras.
    words = sentence.split(' ')
    # Traduz cada palavra usando uma list comprehension.
    translated_words = [translate_word(word) for word in words]
    # Junta as palavras traduzidas de volta em uma frase.
    return ' '.join(translated_words)
