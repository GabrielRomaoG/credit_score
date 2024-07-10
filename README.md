# Credit Score and Recommendation Model

A full-stack project that aims to predict the credit score and gives loan recommendation based on the client characteristics using a trained Machine Learning model.

## Datasets

You can find more information and download the datasets that i used to train the models through the links below:

- credit_score_data_1.csv: https://www.kaggle.com/datasets/sujithmandala/credit-score-classification-dataset
- credit_score_data_2.csv: https://www.kaggle.com/datasets/parisrohan/credit-score-classification/data 

## Installation
These steps only account for the global folder, for specific project installations, read the docs inside of each one.

### Mookme - Git hooks

For this particular installation, it already installs a lot of resources needed for the frontend project.

[Mookme](https://mookme.org/) is a Git hook manager. We chose it because it is designed for monorepos.

First, install [nvm](https://github.com/nvm-sh/nvm):

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# verify installation (you might need to restart your terminal)
command -v nvm
```

Then, use it to download and install [Node.js](https://nodejs.org/en/download/package-manager/current)

```bash
nvm install 22

# verify node and npm installation (you might need to restart your terminal)
node -v # should print `v22.3.0`

npm -v # should print `10.8.1`
```

Finally, use npm to install the mookme dependency

```bash
npm install
```