import Vue from 'vue'
import { MutationTree } from 'vuex'
import axios from 'axios'
import keyBy from 'lodash-es/keyBy'

import { CostcontrolState, BalanceRecord, FilledMonthes } from '../../types'

export const insert = (state: CostcontrolState, payload: {what: string, where: string}) => {
  // @ts-ignore
  state[payload.where + 'Entities'] = keyBy(payload.what, (entity) => entity.id)
  // @ts-ignore
  state[payload.where + 'OrderedIds'] = payload.what.map((entity) => entity.id)
}

export const insertAsIs = (state: CostcontrolState, payload: {what: string, where: string}) => {
  // @ts-ignore
  state[payload.where] = payload.what
}

export const insertFilledMonthes = (state: CostcontrolState, filledMonthes: FilledMonthes) => {
  state.filledMonthes = filledMonthes
}

// Append record to history
export const appendRecord = (state: CostcontrolState, record: BalanceRecord) => {
  state.historyOrderedIds.unshift(record.id)
  state.historyEntities[record.id] = record;
}

export default <MutationTree<CostcontrolState>> {
  insert, insertAsIs, insertFilledMonthes, appendRecord
}
