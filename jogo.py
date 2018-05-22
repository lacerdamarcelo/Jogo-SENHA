import os
import platform
import getpass

maximo_jogadas = 10
numero_cores = 7

def limpar_tela():
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')

def definir_nova_senha():
	senha = ''
	if len(senha) != 4:
		senha = getpass.getpass('Jogador 1, defina a senha com 4 algarismos de 0 a 6:')
		if len(senha) != 4:
			print('Sua senha deve possuir 4 algarismos.')
			input()
		else:
			apenas_algarismos = True
			for char in senha:
				if char < '0' or char > '6':
					apenas_algarismos = False
			if apenas_algarismos == False:
				print('Sua senha deve conter apenas algarismos de 0 a 6')
				input()
			else:
				limpar_tela()
				acertou = False
				for i in range(0, maximo_jogadas):
					senha_adivinhada = input('Tentativa ' + str(i) + ': Jogador 2, tente adivinhar a senha:')
					resposta = []
					for j in range(0, len(senha)):
						if senha_adivinhada[j] == senha[j]:
							resposta.append('2')
						elif senha_adivinhada[j] in senha:
							resposta.append('1')
						else:
							resposta.append('0')
					resposta_texto = ''
					for char in resposta:
						resposta_texto += char
					print('Resposta do sistema: '+ resposta_texto)
					if resposta_texto == '2222':
						print('Parabéns! Você adivinhou a senha!')
						acertou = True
						break
				if acertou == False:
					print('Que pena... você não adivinhou a senha. A resposta correta é: ' + senha)
				input('Pressione ENTER para voltar para o menu principal.')
			
def novo_jogo():
	definir_nova_senha()
	
def ver_ranking():
	pass

opcao = 0
while opcao != 3:
	limpar_tela()
	print('##########SENHA##########')
	print('1 - Novo Jogo')
	print('2 - Ranking')
	print('3 - Sair')
	opcao = int(input('Digite sua opção:'))
	if opcao != 1 and opcao != 2 and opcao != 3:
		print('Opção inválida!')
		input('Pressione ENTER para tentar novamente')
	else:
		if opcao == 1:
			novo_jogo()
		elif opcao == 2:
			ver_ranking()
		elif opcao == 3:
			print('Obrigado por jogar SENHA!')
