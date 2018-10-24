import time
import os, sys
os.system("clear")
banner = '''
_  __    _____
| |/ /_ _|_   _|
| ' /| '_ \| |
| . \| |_) | |
|_|\_\ .__/|_|
     |_|
'''
print(banner)
meu = '<^>'
try:
	word = str(input('palavra: '))
	print("hash original: ", word)
except Exception as erro:
	print("aconteceu um erro em", erro)


def loading():
	import time
	loading = 'carregando(1)'
	time.sleep(2)
	print(loading)
	loading2 = 'carregando(2)'
	time.sleep(3)
	print(loading2)
	loading3 = 'carregando(3)'
	time.sleep(3)
	print(loading3)
	time.sleep(2)

if len(word) >= 1:
	loading()
	for palavra in word:
		if 'a' in word:
			f = word.replace('a', meu[1: 2])
			print(f)
			for x in f:
				k = word.replace('^'[2: 2], '<<^<')
				print(k, f)
		elif 'b' in word:
			f = word.replace('b'[0: -4], meu)
			print(f)
		elif 'c' in word:
			f = word.replace('c'[0: -4], meu)
			print(f)
		elif 'd' in word:
			f = word.replace('d'[0: -4], meu)
			print(f)
		elif 'e' in word:
			f = word.replace('e'[0: -4], meu)
			print(f)
		elif 'f' in word:
			f = word.replace('f'[0: -4], meu)
			print(f)
		elif 'g' in word:
			f = word.replace('g'[0: -4], meu)
			print(f)
		elif 'h' in word:
			f = word.replace('h'[0: -4], meu)
			print(f)
		elif 'i' in word:
			f = word.replace('i'[0: -4], meu)
			print(f)
		elif 'j' in word:
			f = word.replace('j'[0: -4], meu)
			print(f)
		elif 'k' in word:
			f = word.replace('k'[0: -4], meu)
			print(f)
		elif 'l' in word:
			f = word.replace('l'[0: -4], meu)
			print(f)
		elif 'm' in word:
			f = word.replace('m'[0: -4], meu)
			print(f)
		elif 'n' in word:
			f = word.replace('n'[0: -4], meu)
			print(f)
		elif 'o' in word:
			f = word.replace('o'[0: -4], meu)
			print(f)
		elif 'p' in word:
			f = word.replace('p'[0: -4], meu)
			print(f)
		elif 'q' in word:
			f = word.replace('q'[0: -4], meu)
			print(f)
		elif 'r' in word:
			f = word.replace('r'[0: -4], meu)
			print(f)
		elif 's' in word:
			f = word.replace('s'[0: -4], meu)
			print(f)
		elif 't' in word:
			f = word.replace('t'[0: -4], meu)
			print(f)
		elif 'u' in word:
			f = word.replace('u'[0: -4], meu)
			print(f)
		elif 'v' in word:
			f = word.replace('v'[0: -4], meu)
			print(f)
		elif 'w' in word:
			f = word.replace('w'[0: -4], meu)
			print(f)
		elif 'x' in word:
			f = word.replace('x'[0: -4], meu)
			print(f)
		elif 'y' in word:
			f = word.replace('y'[0: -4], meu)
			print(f)
		elif 'z' in word:
			f = word.replace('z'[0: -4], meu)
			print(f)
print("finalizado!!!")