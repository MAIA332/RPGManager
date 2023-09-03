# Computacional Thinking

# Algoritmos de modularização em pseudocódigo

## Nome do trabalho:

***Sistema de gerenciamento de jogos de RPG***

---

## Integrantes do grupo:

Lucas Maia de Morais RA: 44267

Edison Felipe Neves Moreira RA: 44444

Maria Eduarda RA: 45432

---

## INICIO

```jsx
Inicio

op:literal

Escreva "Seja Bem Vindo, vamos começar?"
Escreva "LOGIN (1)| REGISTRAR (2)"

leia op

se op = "1" entao 
	MENU_DE_LOGIN
senao se op = "2" entao
	MENU_REGISTRAR 
```

## MENU_DE_REGISTRO

```jsx
Inicio {(login)}

usuario, usuarios, email, senha: literal
Usuario: cadastro_usuario
Usuarios: arquivo sequencial de Usuario
primeiro_acesso:logico

procedimento login_usuario
	escreva "nome"
	leia usuario.nome
	escreva "idade"
	leia usuario.idade
	escreva "email"
	leia usuario.email
	escreva "senha"
	leia usuario.senha
fim procedimento

{(programa principal)}

login_usuario
abra Usuarios escrita
escreva Usuarios.usuario
feche Usuarios

primeiro_acesso<-verdadeiro
usuario_logado<-usario.email

MENU_DE_LOGIN

fim
```

## MENU_DE_LOGIN

```jsx
Inicio	{(login/save)}
{declarar variaveis}

verificaescolha: literal
opcao: literal
usuario_logado: literal

procedimento verificaescolha(resposta:literal)
	escreva "1-Abrir seus Mundos"
	escreva "2-Criar um novo Mundo"
	escreva "Digite a opcao escolhida:"
	leia resposta
	retorne resposta
fim procedimento

{programa principal}

escreva "Digite seu email"
leia email_id
escreva "Digite sua senha"
leia senha_id
abra usuarios leitura
	se email_id=usuario.email
		então se senha_id=usuario.senha
			usuario_logado<-usario.email
			entao repita
				verificaescolha(opcao)
					caso opcao
						seja "1" faca MENU_MUNDOS
						seja "2" faca MEUS_MUNDOS
						senão escreva "opcao incorreta"
					fim-caso
				senão escreva "Senha Incorreta"
			fim-se
		senao escreva "email incorreto"
	fim se
feche usuario
fim
```

---

## MEUS_MUNDOS

<aside>
💡 Este menu só terá algum retorno caso ele já tenha cadastrado um mundo antes

</aside>

```jsx
inicio
	USE MENU_DE_REGISTRO
	USE MENU_MUNDOS
	
	count:numerico
	op:literal
	select:numerico

	procedimento SEE_MUNDOS()
			para count de 1 ate mundosqtd faca
						abra MUNDO_FILE leitura

						se MUNDO_FILE.NOVO_MUNDO[count].ATIVO = verdadeiro
								leia MUNDO_FILE.NOVO_MUNDO[count]
						fim-se

						feche MUNDO_FILE
				fim-para
	fim-procedimento

	se primeiro_accesso = verdadeiro
		entao 
			Escreva "Ops, nada para ver por aqui"
			MENU_MUNDOS
		senao se primeiro_acesso = falso entao
			Escreva "MEUS MUNDOS"
			
			Escreva "Ver mundos (1) | Deletar um mundo (2)"
			leia op
			se op = "1" entao
					SEE_MUNDOS()
				senao se op ="2" entao
						Escreva "Qual mundo deseja deletar? (Escolha de 1 até x, sendo 1 o primeiro mundo e o ultimo x)"
						SEE_MUNDOS()
						leia op
						abra MUNDO_FILE escrita
						MUNDO_FILE.NOVO_MUNDO[select].ATIVO = falso
						feche MUNDO_FILE
							
						Escreva "Arquivo excluido"
				fim-se
			fim-se
	fim-se

	

```

## MENU_MUNDOS

```jsx
INICIO
USE MENU_DE_REGISTRO

Procedimento MEU_MUNDO (mundo:literal)

	escreva "1 - mundo Pós apocaliptico"
	escreva "2 - mundo Cyberpunk"
	escreva "3 - mundo Ucrónica"
	escreva "escreva o numero do mundo que deseja se aventurar"
	leia mundo
	retorne mundo

fimprocedimento

procedimento MUNDO_ESCOLHIDO(opcao:literal)
    escreva: "mundo 1"
    escreva: "mundo 2"
    escreva: "Qual mundo deseja se aventurar? 1/2"
    leia opcao
fim procedimento

mundo:literal
mundosqtd:numerico

mundosqtd<-mundosqtd+1
primeiro_acesso<-falso

escreva "BEM-VINDO AO MENU DE MUNDOS"
escreva "Aqui voçê irá conhecer os mundos e escolher qual deseja se aventurar.

Escreva "Mundo Pós apocaliptico"
escreva "Após a Terra colapsar se iniciou um evento apocalítico, 
um mundo com mudanças climáticas descontroladas, holocausto nuclear, 
falta de comida e remedios. Uma aventura onde apenas sobreviver é um desafio"

escreva "Mundo de Cyberpunk"
escreva "Em um mundo onde a tecnologia toma conta e a qualidade de vida e a cultura 
já não mais interessa, cidades sombrias onde a corrupção e o crime dominam, seu desafio é sobreviver em mundo marginalizado utilizando a tecnologia e assim derrubar o sistema"

escreva "Mundo estilo Ucrónica"
escreva "Viva momentos os históricos da nossa sociedade e faça parte da historia, em 
Ucrónica voçê irá se aventurar em mundos fictícios baseados em historias já conhecidas,
se aventure, mude a história e crie a realidade que preferir.

MEU_MUNDO(mundo)
  caso mundo
    seja "1" faca MUNDO_POSAPOCALIPTICO
    seja "2" faca MUNDO_CYBERPUNK
    seja "3" faca MUNDO_UCRONICA
    senao escreva "opção incorreta"
  fim-caso

FIM
```

<aside>
📃 Após a execução do menu de mundos, o redirecionamento dependerá da opção selecionada pelo usuário, podendo ir para uma das opções a baixo

</aside>

## MUNDO_CYBERPUNK

```jsx
INICIO
USE MENU_MUNDOS

opcao: literal

NOVO_MUNDO:CONJUNTO[1..100]REGISTRO 
		EMAIL:literal
		MUNDO:literal
		NOME_MUNDO:literal
		ATIVO:logico	
	fim resgistro

MUNDO_FILE:arquivo direto de NOVO_MUNDO

escreva "BEM-VINDO AO MUNDO DE CYBERPUNK"

escreva "Mundo 1: Cyberpunk 2077"

escreva "Cyberpunk 2077  as mega corporações conseguiram se tornar tão poderosas que tem mais poderes que alguns países.
Pessoas vivem em péssimas condições de vida e tem que se virar do jeito que podem.
A internet evoluiu a ponto de pessoas se conectarem a ela com a mente, o mundo é perigoso e cheio de vigaristas e drogados. A principal localização é uma cidade chamada de 
Night City, que fica no estado da Califórnia.
Sua luta é contra grandes corporações e o governo em um mundo de crimonosos e 
desajustados."

escreva "Mundo 2: BLADE RUNNER, O CAÇADOR DE ANDRÓIDES"

escreva "Los Angeles, 2050. A ensolarada Cidade dos Anjos de outrora se tornou
uma capital sombria, poluída, superpopulosa, invadida pelo povo e pela cultural 
oriental. O brilho da luz neon, outdoors digitais voadores e anúncios com a promessa de prosperidade contrastam com a opressão de vielas escuras mergulhadas em chuva ácida e 
adornadas por uma arquietura decadente. Como todo o cenário indica, a raça humana 
devastou as boas condições climáticas da Terra. Em contrapartida, o mesmo avanço 
tecnológico que tanto contribuiu para esse cenário distópico permite o avanço da 
colonização fora do planeta."

	escreva "Nome do seu mundo"
	leia NOVO_MUNDO[mundosqtd].NOME_MUNDO

  MUNDO_ESCOLHIDO(opcao)
    se opcao = 1 
      entao NOVO_MUNDO[mundosqtd].MUNDO <- "Cyberpunk 2077"
        senao se opcao = 2 
          NOVO_MUNDO[mundosqtd].MUNDO <- "BLADE RUNNER"
            senao escreva "opcao invalida"
            fim-se
        fim-se
    fim-se

	NOVO_MUNDO[mundosqtd].ATIVO <- verdadeiro

	NOVO_MUNDO[mundosqtd].EMAIL <- usuario_logado
	
	abra MUNDO_FILE escrita
	escreva MUNDO_FILE.NOVO_MUNDO[mundosqtd]
	feche MUNDO_FILE
	
	MENU_DE_PERSONAGEM 

FIM
```

## MUNDO_PÓSAPOCALIPTICO

```jsx
Inicio
USE MENU_MUNDOS

opcao: literal

NOVO_MUNDO:CONJUNTO[1..100]REGISTRO 
		EMAIL:literal
		MUNDO:literal
		NOME_MUNDO:literal
		ATIVO:logico	
	fim resgistro

MUNDO_FILE:arquivo direto de NOVO_MUNDO

escreva "BEM-VINDO ao MUNDO PÓS APOCALIPTICO

escreva "Mundo 1: UnderRail"

escreva "UnderRail se passa em um mundo pós-apocalíptico no qual grandes corporações se cansaram uma da outra e disputaram uma guerra pelo poder. 
Como eles resolveram isso? Bombardeando a superfície do planeta com bombas nucleares. 
Isso obrigou a humanidade a se deslocar para debaixo da terra com as
corporações sobreviventes. O que levou a um segundo conflito entre elas. Então, dá para considerar que você está vivendo no mundo pós-pós-apocalipse, causado pela ganância de grandes corporações na disputa do monopólio do poder."

escreva "Mundo 2: Encased"

escreva "Encased, a Guerra Fria acabou quando a Dome apareceu, todas as nações se uniram para descobrir os segredos desta estrutura e não tão secretamente enriquecer à custa dos recursos e artefactos encontrados dentro da mesma. Para isso, foi criada uma espécie de força internacional destinada a explorar a Dome, nomeada CRONUS, sendo que qualquer 
pessoa no mundo se pode inscrever na mesma. Esta decisão pode parecer uma forma
fácil de enriquecer e viver uma vida de aventura mas é também ume decisão sem retorno."

	escreva "Nome do seu mundo"
	leia NOVO_MUNDO[mundosqtd].NOME_MUNDO

  MUNDO_ESCOLHIDO(opcao)
    se opcao = 1 
      entao NOVO_MUNDO.MUNDO <- "UnderRail"
        senao se opcao = 2 
          NOVO_MUNDO.MUNDO <- "Encased"
            senao escreva "opcao invalida"
            fim-se
        fim-se
    fim-se

	NOVO_MUNDO[mundosqtd].ATIVO <- verdadeiro

	NOVO_MUNDO[mundosqtd].EMAIL <- usuario_logado

	abra MUNDO_FILE escrita
	escreva MUNDO_FILE.NOVO_MUNDO[mundosqtd]
	feche MUNDO_FILE

	MENU_DE_PERSONAGEM 
Fim
```

## MUNDO_UCRONICA

```jsx
Inicio
USE MENU_MUNDOS

opcao: literal

NOVO_MUNDO:CONJUNTO[1..100]REGISTRO 
		EMAIL:literal
		MUNDO:literal
		NOME_MUNDO:literal
		ATIVO:logico	
	fim resgistro

MUNDO_FILE:arquivo direto de NOVO_MUNDO

escreva "BEM-VINDO AO UCRÓNICA"

escreva "Mundo 1: 11.22.63"

escreva "De volta no tempo até o ano de 1960 em Dallas, Texas, por meio de um portal do tempo descoberto pelo seu amigo de longa data Al Templeton.
O objetivo é prevenir o assassinato de John F. Kennedy em 1963.
No entanto, sua missão é ameaçada por Lee Harvey Oswald e
pelo próprio passado que faz de tudo para permanecer imutável."

escreva "Mundo 2: Man In The High Castle"

escreva "O que teria acontecido com o mundo se as Forças Aliadas tivessem perdido a 
Segunda Guerra Mundial? Vinte anos após a derrota, o planeta agora está dividido entre 
Japão e Alemanha, os maiores Estados Hegemônicos.
À medida que a tensão entre essas duas hegemonias cresce, e isso gera consequências 
drásticas nos Estados Unidos e nos Estados opositores, se aventura entre as 
forças rebeldes e lute contra a ditadura."

	escreva "Nome do seu mundo"
	leia NOVO_MUNDO[mundosqtd].NOME_MUNDO

  MUNDO_ESCOLHIDO(opcao)
    se opcao = 1 
      entao NOVO_MUNDO.MUNDO <- "11.22.63"
        senao se opcao = 2 
          NOVO_MUNDO.MUNDO <- "Man In The High Castle"
            senao escreva "opcao invalida"
            fim-se
        fim-se
    fim-se

	NOVO_MUNDO[mundosqtd].ATIVO <- verdadeiro

	NOVO_MUNDO[mundosqtd].EMAIL <- usuario_logado

	abra MUNDO_FILE escrita
	escreva MUNDO_FILE.NOVO_MUNDO[mundosqtd]
	feche MUNDO_FILE

	MENU_DE_PERSONAGEM 

FIM
```

<aside>
💡 O menu de personagem é uma continuação direta do menu de mundos, representando um modulo de seu funcionamento, podemos concluir isso pois é necessário cadastrar seu personagem e só então salvar os dados do registro mundo e do registro personagem.

</aside>

## MENU_DE_PERSONAGEM

```jsx
Inicio
USE MENU_MUNDOS

personagem: CONJUNTO[1..100]REGISTRO 
	nomecad:literal
	classe: conjunto [1..5][1..2]literal
fim-registro

choice:literal
count:numerico
aux_nome:literal

classes:conjunto[1..3]numerico

procedimento DEF_PERSONAGEM(nome:literal)
		
		classes[1] <- "Caçador"
		classes[2] <- "Brutamontes"
		classes[3] <- "Engenheiro"
		
		personagem[nome].nomecad = nome
		
		Escreva "Caçador (1) | Brutamontes (2) | Engenheiro (3)"
		Escreva "Qual classe deseja escolher?"
		leia choice
		
		personagem[nome].classe[1][1] = "Força"
		personagem[nome].classe[1][1] = "Velocidade"
		personagem[nome].classe[1][1] = "Resistência"
		personagem[nome].classe[1][1] = "Destreza"
		personagem[nome].classe[1][1] = "Vida"
		
		
		se choice = "1" entao
			personagem[nome].classe[2][1] = "10"
			personagem[nome].classe[2][2] = "20"
			personagem[nome].classe[2][3] = "10"
			personagem[nome].classe[2][4] = "15"
			personagem[nome].classe[2][5] = "100"
			
			senao se choice = "2" entao
				personagem[nome].classe[2][1] = "20"
				personagem[nome].classe[2][2] = "10"
				personagem[nome].classe[2][3] = "15"
				personagem[nome].classe[2][4] = "10"
				personagem[nome].classe[2][5] = "100"
			
				senao se choice = "3" entao
					personagem[nome].classe[2][1] = "10"
					personagem[nome].classe[2][2] = "10"
					personagem[nome].classe[2][3] = "10"
					personagem[nome].classe[2][4] = "25"
					personagem[nome].classe[2][5] = "100"
		
				fim-se
			fim-se
		fim-se
fim-procedimento

Escreva "Deseja cadastrar um personagem? (S/N)"
leia opcao
Enquanto choice = "S"
		
		Escreva "Dê um nome para o personagem"
		leia aux_nome
		
		DEF_PERSONAGEM(aux_nome)

fim-enquanto

abra MUNDO_FILE escrita
escreva MUNDO_FILE.personagem
feche MUNDO_FILE
	

```