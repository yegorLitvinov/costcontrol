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

// You get errors in the following lines because vuex does not support
// custom store type declaration.

declare module "vue/types/options" {
    // @ts-ignore
  interface ComponentOptions<V extends Vue> {
    // @ts-ignore
    store?: Store<RootState>;
  }
}

declare module "vue/types/vue" {
  interface Vue {
    // @ts-ignore
    $store: Store<RootState>;
  }
}
