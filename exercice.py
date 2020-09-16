#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    stringLength = len(string)

    if stringLength % 2 == 0:
        return True
    else:
        return False


def remove_third_char(string: str) -> str:
    string_without_third_chr = string[0:3] + string[4::]
    return string_without_third_chr


def replace_char(string: str, old_char: str, new_char: str) -> str:
    new_string = string.replace(old_char, new_char)
    return new_string


def get_nb_char(string: str, char: str) -> int:
    nb_char = 0

    for i in string:
        if i == char:
            nb_char += 1

    return nb_char


def get_nb_words(sentence: str) -> int:
    nb_words = 1

    for i in sentence:
        if i == ' ':
            nb_words += 1

    return nb_words


def main() -> None:
    string = "Bonjour!"
    parity = 'pair' if is_even_len(string) else 'impair'
    print(f"Le nombre de caractère dans la chaine '{string}' est {parity}")

    string = "Sam est cool!"
    print(f"On supprime le 3e caratère dans la chaine '{string}'. Résultat: {remove_third_char(string)}")

    string = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: '{string}'. Résultat: {replace_char(string, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_nb_char(string, 'l')}")
    
    string = "Baby shark doo doo doo doo doo doo"
    print(f"Le nombre de mots dans la chaine {string} est: {get_nb_words(string)}")


if __name__ == '__main__':
    main()
