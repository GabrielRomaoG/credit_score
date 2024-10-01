import type { BaseTranslation } from '../i18n-types';

const pt_BR = {
	home: {
		credit_score_ai: 'Score  de Crédito IA',
		subtitle: {
			part1: 'Deixe um modelo de Machine Learning adivinhar seu Score.',
			part2: 'Dura apenas 2 minutos.'
		},
		check_default_profiles: 'Veja um exemplo clicando abaixo',
		warning:
			'Este projeto foi construído com o propósito de mostrar o conhecimento dos autores. Não podemos atestar a origem dos dados de treino, portanto não se surpreenda se o resultado diferir da realidade.'
	},
	validation: {
		required: "O campo '{field}' é obrigatório.",
		nonnegative: "O campo '{field}' deve ser positivo."
	},
	age: 'Idade',
	monthly_income: 'Renda mensal',
	sex: 'Sexo',
	education: 'Escolaridade',
	num_bank_accounts: 'Quantidade de contas bancárias',
	num_credit_card: 'Quantidade de cartões de crédito',
	num_of_loan: 'Quantidade de empréstimos',
	num_of_delayed_payment: 'Quantidade de pagamentos atrasados',
	outstanding_debt: 'Dívida total',
	credit_history_age: 'Histórico de Crédito em anos',
	total_emi_per_month: 'Parcela de financiamento de imóvel',

	male: 'Masculino',
	female: 'Feminino',

	high_school_diploma: 'Ensino Médio',
	associates_degree: 'Tecnólogo',
	bachelors_degree: 'Bacharelado',
	masters_degree: 'Mestrado',
	doctorate: 'Doutorado',

	submit: 'Enviar',
	reset: 'Limpar',
	return_home: 'Voltar para o Início',

	fill_form: 'Por favor, preencha o formulário',

	features_impact: 'Impacto das Características',

	how_it_works: {
		title1: 'Como funciona?',
		title2_goal: 'O objetivo',
		goal_text:
			'O objetivo deste projeto, além de mostrar as habilidades dos autores, é mostrar um pouco como um modelo de machine learning funciona com seus dados e como ele gera o resultado que você viu se você tivesse preenchido o formulário. A explicação a seguir é feita para o público em geral, portanto, ignora detalhes técnicos para uma melhor compreensão.',

		title2_data: 'Como os dados são enviados?',
		data_text:
			'Quando você pressiona o botão enviar após preencher o formulário, os dados são enviados para uma API neste formato:',

		title2_api: 'A API',
		api_text:
			'A API é escrita em Python e tem a tarefa de receber os dados passados pelo frontend e inseri-los nos modelos.',

		title3_first_model: 'O Primeiro Modelo',
		first_model_text1:
			"O primeiro modelo processa as características ['sexo', 'escolaridade', 'idade', 'renda'] e prevê se o seu score é 'baixo', 'médio' ou 'alto'. O motivo pelo qual o modelo não prevê o score de crédito em si é devido ao conjunto de dados em que foi treinado. O conjunto de dados não contém o score de crédito; ele apenas informa se o score de uma pessoa é 'baixo', 'médio' ou 'alto'. Um modelo que prevê uma classe é chamado de classificador.",
		first_model_text2:
			"O modelo utilizado nesse conjunto de dados é a regressão logística. A regressão logística é bastante semelhante a uma equação linear (y = mx + b), mas resulta em um número entre 0 e 1, por isso a saída é uma probabilidade. Por exemplo, para um conjunto específico de características, o resultado do modelo é a probabilidade de obter 'baixo', 'médio' ou 'alto'.",

		first_model_text3:
			"O modelo alcança essas probabilidades calculando a frequência de cada classe para as observações do conjunto de dados que são semelhantes à entrada. Por exemplo, imagine que você tenha um conjunto específico de características, o modelo encontrará observações (linhas do conjunto de dados) que tenham características semelhantes, e contará as aparições de cada classe. Se a classe 'baixo' aparecer em 70% das linhas, sua probabilidade será de 70%, e assim por diante.",
		first_model_text4:
			'É importante dizer que o modelo não é 100% preciso se comparado ao próprio conjunto de dados, e é ainda menos preciso se comparado ao mundo real.',

		title3_second_model: 'O Segundo Modelo',
		second_model_text:
			"O segundo modelo funciona de maneira semelhante ao primeiro. Ele processa as características ['quantidade de contas bancárias', 'quantidade de cartões de crédito', 'quantidade de empréstimos', 'quantidade de pagamentos atrasados', 'dívida total', 'histórico de crédito', 'parcela de financiamento'] e prevê uma classe.",

		title3_transform_class: 'Como ele transforma uma classe em um número de score de crédito?',
		transform_class_text1:
			"Ambos os modelos prevêem uma classe cuja probabilidade é a maior. Portanto, um modelo pode prever um score de crédito 'baixo' e o outro um score de crédito 'alto'.",
		transform_class_text2:
			"Cada uma das classes tem um número de score de crédito associado a elas. Por exemplo, a classe 'baixo' tem um número de score de crédito de 300, a classe 'médio' tem um número de score de crédito de 600, e a classe 'alto' tem um número de score de crédito de 900.",
		transform_class_text3:
			'Quando o modelo prevê uma classe, ele retornará o número de score de crédito associado a essa classe. Mas como temos dois modelos, ele retornará a média ponderada do número de score de crédito dos dois modelos, sendo os pesos a precisão dos modelos.',
		transform_class_text4:
			"Por exemplo, se a precisão do primeiro modelo for de 70% e a precisão do segundo modelo for de 80%, e as classes forem 'baixo' e 'alto', a média ponderada será ((70% * 300) + (80% * 900)) / (70% + 80%) = 650."
	}
} satisfies BaseTranslation;

export default pt_BR;
