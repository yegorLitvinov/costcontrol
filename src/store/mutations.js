  // Change state (redux reducer)

export const insert = (state, opts) => {
  state[opts.where] = opts.what
}

export const changeDate = (state, date) => {
  state['date'] = date
}

// Append record to history
export const appendRecord = (state, record) => {
  record.sign = record.type === 'spending' ? '-' : '+'
  const recordCategory = state[record.type + 'Categories'].find(
    category => category.id === record.category
  )
  record.category__name = recordCategory.name
  state.history.unshift(record)
}
