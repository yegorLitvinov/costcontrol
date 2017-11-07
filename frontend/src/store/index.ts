import Vue from 'vue'
import Vuex from 'vuex'

import AccountsModule from './accounts'
import CostcontrolModule from './costcontrol'
import { RootState } from '../types'

Vue.use(Vuex)

export default new Vuex.Store<RootState>({
  modules: {
    accounts: new AccountsModule(),
    costcontrol: new CostcontrolModule(),
  }
})
