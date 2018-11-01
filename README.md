[![Build Status](https://drone.tvgun.ga/api/badges/yegorLitvinov/costcontrol/status.svg)](https://drone.tvgun.ga/yegorLitvinov/costcontrol)

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
    - [X] Disable eslint in <script lang="ts"> block
    - [X] Cypress lint errors (eslint)
    - [X] Cypress tests; django command before, after, beforeEach test
    - [X] Disable buttons when submit sent
    - [X] Configure BundleAnalyzerPlugin
    - [X] Source maps for styles
    - [X] Class-Style Components (not so easy, no profit)
    - [X] Category name in history
    - [ ] Cool transactions
    - [ ] Progress bar
    - [ ] Setup tslint
    - [ ] Doughnut charts equal size

- Backend
    - [X] Filled-months and history urls are not protected
    - [X] Remove api app (views, urls, serializers -> specific apps)
    - [X] User id in cache key
    - [X] Reorganizate the structure of models
    - [X] py.test
    - [X] Owner Mixin -> permissions
    - [X] UpdateCacheMixin -> Model hooks
    - [x] Am I using djanog filters right?
    - [X] History pagination
    - [X] ~~Use redis~~ Disable caching
    - [X] ~~Fix 3a.m. filled_monthes test bug~~ Remove filled monthes cache
    - [ ] Secret key -> environment
    - [ ] HistoryView -> BalanceRecordViewSet + django_filters

- Devops
    - [X] Build frontend on local machine
    - [X] ~~Ansible buildin vault~~ env variables
    - [X] Make backup
    - [X] ~~Docker service -> docker~~ No docker
    - [X] Restart gunicorn takes a lot of time
    - [X] Travis CI badges to github
    - [X] Drone integration
    - [ ] Sentry integration
    - [ ] Backend error log

- Editor
    - [X] Python format on save
    - [ ] Eslint feat. Prettier
