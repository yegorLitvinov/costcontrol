Cypress.Commands.add('init', () => {
  cy.exec('source .envrc && source .direnv/python-3.6.3/bin/activate && python backend/manage.py cypress --init 1')
})

Cypress.Commands.add('destroy', () => {
  cy.exec('source .envrc && source .direnv/python-3.6.3/bin/activate && python backend/manage.py cypress --destroy 1')
})

Cypress.Commands.add('login', () => {
  return cy.request({
    method: 'POST',
    url: '/api/accounts/login/',
    headers: {
      Authorization: 'Basic dGVzdEBleGFtcGxlLmNvbTpwYXNzd29yZDEyMw=='
    }
  })
    .then((response) => {
      sessionStorage.setItem('token', response.body.token || '')
      sessionStorage.setItem('userId', String(response.body.user.id || ''))
      return response
    })
})

Cypress.Commands.add('logout', () => {
  sessionStorage.removeItem('token')
  sessionStorage.removeItem('userId')
})
