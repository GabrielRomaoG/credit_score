import type { Translation } from '../i18n-types';

const en_US = {
	home: {
		credit_score_ai: 'Credit Score AI',
		subtitle: {
			part1: 'Let a Machine Learning model guess your credit score.',
			part2: 'Fill the form. It only takes 2 minutes.'
		},
		check_default_profiles: 'Check default profiles',
		form: {
			total_emi_per_month_info:
				'EMI, or Equated Monthly Installment, is a fixed payment amount paid by a borrower to a lender at a specified date each calendar month.',
			credit_history_age_info:
				'How long have you been a bank account or credit card holder in years.',
			features_impact_info:
				'Show how each feature affects the credit score. Two green arrows indicate a great positive impact, and two red arrows indicate a great negative impact.'
		},
		warning:
			"This project was built with the purpose of showcasing the authors' knowledge. We cannot attest to the origin of the training data, so do not be surprised if the result differs from reality."
	},
	validation: {
		required: "'{field}' is required.",
		nonnegative: "'{field}' must be positive.",
		lessThan: "'{field}' must be less than {lessThan}.",
		greaterThan: "'{field}' must be greater than {greaterThan}."
	},
	age: 'Age',
	monthly_income: 'Monthly Income',
	sex: 'Sex',
	education: 'Education',
	num_bank_accounts: 'Number of Bank Accounts',
	num_credit_card: 'Number of Credit Cards',
	num_of_loan: 'Number of Loans',
	num_of_delayed_payment: 'Number of Delayed Payments',
	outstanding_debt: 'Outstanding Debt',
	credit_history_age: 'Credit History Age',
	total_emi_per_month: 'Total EMI per Month',

	male: 'Male',
	female: 'Female',

	high_school_diploma: 'High School',
	associates_degree: 'Associate',
	bachelors_degree: 'Bachelor',
	masters_degree: 'Master',
	doctorate: 'Doctorate',

	submit: 'Submit',
	reset: 'Reset',
	return_home: 'Return to Home',

	fill_form: 'Please, fill the form',

	features_impact: 'Features Impact',

	how_it_works: {
		title1: 'How it works?',
		title2_goal: 'The goal',
		goal_text:
			'The goal of this project, besides showing the skills of the authors, is to show a bit how a machine learning model works with your data and how it brings the result that you saw if you had filled out the form. The forward explanation is made for a general public, so it ignores technical details for better understanding.',

		title2_data: 'How the data is sent?',
		data_text:
			'When you press the button send after filling the form, the data is sent to an API in this format:',

		title2_api: 'The API',
		api_text:
			'The API is written in Python and has the task of taking the data passed by the frontend and input into the models.',

		title3_first_model: 'The First Model',
		first_model_text1:
			"The first model processes the ['sex', 'education', 'age', 'income'] features and predicts if your score is 'low', 'average', or 'high'. The reason that the model does not predict the credit score itself is due to the dataset it is trained on. The dataset does not contain the credit score; it just tells if a person's credit score is 'low', 'average', or 'high'. A model that predicts a class is called a classifier.",
		first_model_text2:
			"The model used on this dataset is the logistic regression. The logistic regression is quite similar to a linear equation (y = mx + b), but it results in a number between 0 and 1, hence the output is a probability. For example, for a specific set of features, the output of the model is the probability of getting 'low', 'average', or 'high'.",

		first_model_text3:
			"The model reaches these probabilities through calculating the frequency of each class for the dataset observations that are similar to the input. For example, imagine that you have a specific set of features, the model will find observations (rows of the dataset) that have similar features, and it will count the appearances of each class. If the 'low' class appears in 70% of the rows, its probability will be 70%, and so on.",
		first_model_text4:
			'It is important to say that the model is not 100% accurate if compared to the dataset itself, even less accurate if compared with the real world.',

		title3_second_model: 'The Second Model',
		second_model_text:
			"The second model works in a similar way as the first one. It processes the ['num_bank_accounts', 'num_credit_card', 'num_of_loan', 'num_of_delayed_payment', 'outstanding_debt', 'credit_history_age', 'total_emi_per_month'] features and predicts a class.",

		title3_transform_class: 'How it transforms a class in a credit score number?',
		transform_class_text1:
			"Both models predict a class which the probability is the highest. So one model can predict a 'low' credit score and the other a 'high' credit score.",
		transform_class_text2:
			"Each of the classes has a credit score number associated with them. For example, the 'low' class has a credit score number of 300, the 'average' class has a credit score number of 600, and the 'high' class has a credit score number of 900.",
		transform_class_text3:
			'When the model predicts a class, it will return the credit score number associated with that class. But as we have two models, it will return the weighted average credit score number of the two models, with the weights being the accuracy of the models.',
		transform_class_text4:
			"For example, if the accuracy of the first model is 70% and the accuracy of the second model is 80%, and the classes are 'low' and 'high', the weighted average will be ((70% * 300) + (80% * 900)) / (70% + 80%) = 650."
	},
	github_link: 'Go to GitHub repository',
	authors: 'Authors'
} satisfies Translation;

export default en_US;
