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

## .envrc example
```bash
# Django
layout python python3.6
export DJANGO_SETTINGS_MODULE=config.settings.dev
export PYTHONPATH=`pwd`/backend

# Ansible
export ADMIN_EMAIL=test@mail.ru
export USER_PASS=password
export WEB_DOMAIN=example.com
```

## TODO:
- [X] Disable source maps for production
- [X] Filled-monthes and history urls are not protected
- [X] Build frontend on local machine
- [X] Authenticate after reloading page
- [X] Move to /frontend
- [X] ~~Ansible buildin vault~~ env variables
- [X] Remove api app (views, urls, serializers -> specific apps)
- [X] User id in cache key
- [X] Fix different date in activity
- [X] Make backup
- [ ] Owner Mixin -> permissions
- [ ] Cool transactions
- [ ] Restart gunicorn takes a lot of time
- [ ] Docker service -> docker
- [ ] Sentry integration
- [ ] Backend error log
- [ ] Cypress tests; django command before, after, beforeEach test
- [ ] Typescript
- [ ] TESTS!
- [ ] Secret key -> environment
- [ ] Eslint feat. Prettier
- [ ] Python format on save
- [ ] UpdateCacheMixin -> Model hooks
- [ ] Jenkins badges to github
- [ ] HistoryView -> BalanceRecordViewSet + django_filters
