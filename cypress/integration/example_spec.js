describe('Auth', () => {
  before(() => {
    cy.adduser()
  })

  after(() => {
    cy.rmuser()
  })

  it('Login Fail', () => {
    cy.server()
    cy.visit('/')
    cy.get('input[name=email]').type('test@example.com')
    cy.get('input[type=password]').type('password')
    cy.get('button').contains('Login').click()

    cy.get('input[name=email]').should('have.class', 'is-invalid')
    cy.get('input[type=password]').should('have.class', 'is-invalid')
    cy.location('hash').should('include', 'login')
  })

  it('Login Success', () => {
    cy.server()
    cy.visit('/')
    cy.get('input[name=email]').type('test@example.com')
    cy.get('input[type=password]').type('password123')
    cy.get('button').contains('Login').click()

    cy.location('hash').should('include', 'dashboard')
  })
})
