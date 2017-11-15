Cypress.Commands.add('adduser', () => {
  cy.exec('source .envrc && source .direnv/python-3.6.3/bin/activate && python backend/manage.py cypress --adduser 1')
})

Cypress.Commands.add('rmuser', () => {
  cy.exec('source .envrc && source .direnv/python-3.6.3/bin/activate && python backend/manage.py cypress --rmuser 1')
})
