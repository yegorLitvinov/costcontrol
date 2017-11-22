import Vue from 'vue'
import { MutationTree } from 'vuex'
import axios from 'axios'

import { CostcontrolState, BalanceRecord } from '../../types'

export const insert = (state: CostcontrolState, payload: {what: string, where: string}) => {
  // @ts-ignore
  state[payload.where] = payload.what
}

// Append record to history
export const appendRecord = (state: CostcontrolState, record: BalanceRecord) => {
  state.history.unshift(record)
}

export default <MutationTree<CostcontrolState>> {
  insert, appendRecord
}
