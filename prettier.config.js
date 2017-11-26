var config = {
  printWidth: 100,
  tabWidth: 2,
  singleQuote: true,
  trailingComma: 'none',
  bracketSpacing: true,
  semi: false,
  useTabs: false,
  // prettier-eslint doesn't currently support
  // inferring these two (Pull Requests welcome):
  parser: 'babylon',
  jsxBracketSameLine: false
}

module.exports = config
