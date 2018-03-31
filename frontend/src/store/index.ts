import Vue, { ComponentOptions } from 'vue'
import Vuex, { Store } from 'vuex'

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

// If you get errors in the following lines you need to remove
// ones from node_modules/vuex/types/vue.d.ts or wait for support
// of custom store type declaration in vuex

declare module "vue/types/options" {
  // @ts-ignore
  interface ComponentOptions<V extends Vue> {
    store?: Store<RootState>;
  }
}

declare module "vue/types/vue" {
  interface Vue {
    $store: Store<RootState>;
  }
}
