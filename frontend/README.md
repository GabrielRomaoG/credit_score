## Installing Node.js and npm

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

## Installing dependencies

Use npm to install all dependencies

```bash
npm install
```

## Running the project in a development server

Once you've installed dependencies, start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version:

```bash
npm run build
```

You can preview the production build with `npm run preview`.
