 # -*- coding: utf-8 -*-
print('''

 /$$$$$$$            /$$                   /$$ /$$   /$$$$$$$
| $$__  $$          | $$                  / $$/ $$  | $$__  $$
| $$  \ $$  /$$$$$$ | $$$$$$$  /$$   /$$ /$$$$$$$$$$| $$  \ $$
| $$$$$$$  |____  $$| $$__  $$| $$  | $$|   $$  $$_/| $$$$$$$/
| $$__  $$  /$$$$$$$| $$  \ $$| $$  | $$ /$$$$$$$$$$| $$__  $$
| $$  \ $$ /$$__  $$| $$  | $$| $$  | $$|_  $$  $$_/| $$  \ $$
| $$$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$$  | $$| $$  | $$  | $$
|_______/  \_______/|_______/  \____  $$  |__/|__/  |__/  |__/
                               /$$  | $$
                              |  $$$$$$/
                               \______/
[+]Armazenador de Url.
[+]Rafael Silva - BabyRafa
[+]https://twitter.com/babyrafabr
''')
#Programa pra armazenar sites educativos. para fácil acesso.
site, meta = input('URL: '), input('Descrição: ')
arquivo = open('sites_educativos.txt', 'a')
arquivo.writelines('{site} - {meta}\n' .format(site=site, meta=meta))
arquivo.close()
print()
print("O Site : %s ,  Descrição: %s,  foi salvo com sucesso."  %(site,meta))
