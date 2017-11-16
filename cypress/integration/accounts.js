describe('Auth', () => {
  before(() => {
    cy.init()
  })

  after(() => {
    cy.destroy()
  })

  afterEach(() => {
    cy.logout()
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

  it('Unauthorized Access', () => {
    cy.server()
    cy.visit('/#/dashboard/')

    cy.location('hash').should('include', 'login')
  })

  it.only('Reload Statistics Success', () => {
    cy.server()
    cy.login().then((response) => {
      cy.visit('/#/dashboard/')
    })

    cy.get('.sidebar a').contains('Statistics').click()
    cy.get('.custom-select').first().select('2017')
    cy.get('.chartjs-size-monitor')

    cy.reload()

    cy.get('.custom-select').first().select('2017')
    cy.get('.chartjs-size-monitor')
  })
})
