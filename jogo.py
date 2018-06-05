import os
import json
import getpass
import platform


maximo_jogadas = 10
numero_cores = 7


def limpar_tela():
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')

		
def salvar_ranking(nome, pontuacao):
	ranking = []
	if os.path.isfile('ranking.json') == True:
		f = open('ranking.json', 'r')
		ranking_dict = json.load(f)
		f.close()
		for i in range(0, len(ranking_dict)):
			ranking.append(ranking_dict[str(i)])
	ranking_jogador = -1
	if len(ranking) > 0:
		for i in range(0, len(ranking)):
			if pontuacao > ranking[i]['pontuacao']:
				ranking.insert(i, {'nome': nome, 'pontuacao': pontuacao})
				ranking_jogador = i
				break
	if ranking_jogador == -1:
		ranking_jogador = len(ranking)
		ranking.append({'nome': nome, 'pontuacao': pontuacao})
	f = open('ranking.json', 'w')
	ranking_json = {}
	for i in range(0, len(ranking)):
		ranking_json[str(i)] = ranking[i]
	json.dump(ranking_json, f)
	f.close()
	print('Você obteve a ' + str(ranking_jogador + 1) + 'ª melhor pontuação!')

	
def vez_jogador_1():
	limpar_tela()
	senha = ''
	apenas_algarismos = False
	while len(senha) != 4 or apenas_algarismos == False:
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
	return senha

	
def vez_jogador_2(senha):
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
			nome = input('Digite seu nome para o ranking.\n')
			salvar_ranking(nome, maximo_jogadas - i)
			acertou = True
			break
	if acertou == False:
		print('Que pena... você não adivinhou a senha. A resposta correta é: ' + senha)


def novo_jogo():
	senha = vez_jogador_1()
	vez_jogador_2(senha)
	input('Pressione ENTER para voltar para o menu principal.')
	

def ver_ranking():
	limpar_tela()
	if os.path.isfile('ranking.json') == True:
		f = open('ranking.json', 'r')
		ranking_dict = json.load(f)
		f.close()
		print('############ RANKING ############')
		for i in range(0, len(ranking_dict)):
			nome = ranking_dict[str(i)]['nome']
			pontuacao = ranking_dict[str(i)]['pontuacao']
			print(str(i + 1) + ' - ' + nome + ' - ' + str(pontuacao))
	else:
		print('Nenhuma pontuação foi registrada. Seja o primeiro a jogar!')
	input()
		

opcao = 0
while opcao != 3:
	limpar_tela()
	print('########## SENHA ##########')
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
