#!/usr/bin/env python 

"""
Hello World Multi Language 
According to the language configured on env 
Usage: 
    Have LANG variable configured accordingly ex:
    export LANG = pt_BR 
Execution: 
    python3 hello.py
"""


__version__ = "0.0.1"
__author__ = "Lucas"
__license__ = "unlicense"

import os



current_language = os.getenv("LANG","en_US")[:5]





msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá Mundo"

elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"

elif current_language == "fr_FR":
    msg = "Bonjour Monde!"

    




print(msg)



