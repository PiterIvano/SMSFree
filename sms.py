import requests
import colorama
from colorama import Fore, Back, Style
r = "\033[0;31m"; v = "\033[0;32m"; a = "\033[0;34m"; y = "\033[0;33m"; x = "\033[0;0m"; print(f"{v}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"); print(f"▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒"); print(f"▒▒█▒▒▒▄██████████▄▒▒▒▒"); print(f"▒█▐▒▒▒████████████▒▒▒▒"); print(f"▒▌▐▒▒██▄▀██████▀▄██▒▒▒"); print(f"▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒"); print(f"▐┼▐▒▒██████████████▒▒▒"); print(f"▐▄▐████─▀▐▐▀█─█─▌▐██▄▒"); print(f"▒▒█████───PITER──▐███▌"); print(f"▒▒█▀▀██▄█─▄───▐─▄███▀▒"); print(f"▒▒█▒▒███████▄██████▒▒▒"); print(f"▒▒▒▒▒██████████████▒▒▒"); print(f"▒▒▒▒▒██████████████▒▒▒"); print(f"▒▒▒▒▒█████████▐▌██▌▒▒▒"); print(f"▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒"); print(f"▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒"); print(f"▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"); to = input(f"{r}Ponga el numero-> ");msg = input(f"Ponga el Mensaje-> {v}"); resp = requests.post('https://textbelt.com/text', {'phone': to, 'message': msg, 'key': 'textbelt'})
if resp.json()['success'] == True:print("Mensaje enviado"); print(f"{v}Enviado a {to}")
elif resp.json()['success'] == "{'success': False, 'error': 'Only one test text message is allowed per day.', 'quotaRemaining': 0}":print("Mensaje no enviado, ya llego al limite por hoy\n solo puede enviar 1 sms cada 12 horas")
else:print("Error")
