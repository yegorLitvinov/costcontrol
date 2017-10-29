## Backend Build Setup

``` bash
# allow to load env variables from .envrc file
direnv allow

# install dependencies
pipenv install --dev
```

## Frontend Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

For detailed explanation on how things work, checkout the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).


## TODO:
- [ ] Disable source maps for production, but not for raven for example
- [X] Filled-monthes and history urls are not protected
- [ ] Cool transactions
- [ ] Make backup
- [ ] Restart gunicorn takes a lot of time
- [ ] Move to /frontend
- [ ] Docker service -> docker
- [ ] Sentry integration
- [X] Authenticate after reloading page
