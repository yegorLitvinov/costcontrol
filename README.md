## Backend Build Setup

``` bash
# allow to load env variables from .envrc file
direnv allow

# install dependencies
pipenv install --dev

# create database
django-admin sqlcreate | psql

# migrate
django-admin migrate

# start dev server
django-admin runserver

# create user
django-admin createsuperuser
```

## Frontend Build Setup

``` bash
# install dependencies
yarn install

# serve with hot reload at localhost:8080
yarn run dev

# build for production with minification
yarn run build
```

For detailed explanation on how things work, checkout the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

## .envrc example
```bash
# Django
layout python python3.6
export DJANGO_SETTINGS_MODULE=config.settings.dev
export PYTHONPATH=`pwd`/backend

# Node
layout node

# Ansible
export ADMIN_EMAIL=test@mail.ru
export USER_PASS=password
export WEB_DOMAIN=example.com
export REPO=https://bitbucket.org/team/project/
```

## TODO:
- Frontend
    - [X] Disable source maps for production
    - [X] Move to /frontend
    - [X] Authenticate after reloading page
    - [X] Fix different date in activity
    - [X] Remove default js tests
    - [X] Upgrade vue up to 2.5.3
    - [X] Typescript + js (weak @types support)
    - [X] Vuex devide into modules
    - [ ] Cool transactions
    - [ ] Cypress tests; django command before, after, beforeEach test
    - [ ] Configure BundleAnalyzerPlugin
    - [ ] Progress bar
    - [ ] Disable eslint in <script lang="ts"> block

- Backend
    - [X] Filled-monthes and history urls are not protected
    - [X] Remove api app (views, urls, serializers -> specific apps)
    - [X] User id in cache key
    - [X] Reorganizate the structure of models
    - [ ] Owner Mixin -> permissions
    - [ ] py.test
    - [ ] Secret key -> environment
    - [ ] UpdateCacheMixin -> Model hooks
    - [ ] HistoryView -> BalanceRecordViewSet + django_filters

- Devops
    - [X] Build frontend on local machine
    - [X] ~~Ansible buildin vault~~ env variables
    - [X] Make backup
    - [X] ~~Docker service -> docker~~ No docker
    - [X] Restart gunicorn takes a lot of time
    - [ ] Sentry integration
    - [ ] Backend error log
    - [ ] Jenkins badges to github

- Editor
    - [ ] Eslint feat. Prettier
    - [ ] Python format on save
    - [ ] Cypress lint errors
