<script lang="ts">
	const profileExample = {
		age: 30,
		sex: 'male',
		education: 'bachelors_degree',
		monthly_income: 2000,
		num_bank_accounts: 1,
		num_credit_card: 1,
		num_of_loan: 3,
		num_of_delayed_payment: 5,
		outstanding_debt: 15000,
		credit_history_age: 4,
		total_emi_per_month: 600
	};

	const cs1ModelPredictOutput = {
		low: 0.7,
		average: 0.2,
		high: 0.1
	};
</script>

<h1>How it works</h1>

<h2>The goal</h2>

<p>
	The goal of this project, besides showing the skills of the authors, is to show a bit how a
	machine learning model works with your data and how it brings the result that you saw if you had
	filled out the form. The forward explanation is made for a general public, so it ignores technical
	details for better understanding.
</p>

<h2>How the data is sent?</h2>

<p>
	When you press the button send after filling the form, the data is sent to a python API in this
	format:
</p>

<pre>	
{JSON.stringify(profileExample, null, 2)}
</pre>

<h2>The API</h2>

<p>
	The API is written in Python and has the task of taking the data passed by the frontend and input
	into the models.
</p>

<h3>The First Model</h3>

<p>
	The first model processes the ['sex', 'education', 'age', 'income'] features and predicts if your
	score is 'low', 'average', or 'high'. The reason that the model does not predict the credit score
	itself is due to the
	<a href="https://www.kaggle.com/datasets/sujithmandala/credit-score-classification-dataset">
		dataset
	</a>
	it is trained on. The dataset does not contain the credit score; it just tells if a person's credit
	score is 'low', 'average', or 'high'. A model that predicts a class is called a classifier.
</p>

<p>
	The model used on this dataset is the logistic regression. The logistic regression is quite
	similar to a linear equation, but it results in a number between 0 and 1, hence the output is a
	probability. For example, for a specific set of features, the output of the model is the
	probability of getting "low", "average", or "high".
</p>

<pre>
{JSON.stringify(cs1ModelPredictOutput, null, 2)}
</pre>

<p>
	The model reaches these probabilities through calculating the frequency of each class for the
	dataset observations that are similar to the input. For example, imagine that you have a specific
	set of features, the model will find observations (rows of the dataset) that have similar
	features. and it will count the appearances of each class, if the "low" class appears in 70% of
	the rows, its probability will be 70%, and so on.
</p>

<p>
	It is important to say that the model is not 100% accurate if compared to the dataset itself. even
	less accurate if compared with the real world.
</p>

<h3>The Second Model</h3>

<p>
	The second model works in a similar way as the first one. It processes the ['num_bank_accounts',
	'num_credit_card', 'num_of_loan', 'num_of_delayed_payment', 'outstanding_debt',
	'credit_history_age', 'total_emi_per_month'] features and predicts a class.
</p>

<h3>How it transfoms a class in a credit score number?</h3>

<p>
	Both models predict a class which the probability is the highest. So one model can predict a "low"
	credit score and other a "high" credit score.
</p>

<p>
	Each of the class has a credit score number associated with them. For example, the "low" class has
	a credit score number of 300, the "average" class has a credit score number of 600, and the "high"
	class has a credit score number of 900.
</p>

<p>
	When the model predicts a class, it will return the credit score number associated with that
	class. But as we have two models, it will return the weighted average credit score number of the
	two models, with the weights being the accuracy of the models.
</p>

<p>
	For example, if the accuracy of the first model is 70% and the accuracy of the second model is
	80%, and the classes are "low" and "high", the weighted average will be ((70% * 300) + (80% *
	900)) / (70% + 80%) = 650.
</p>
