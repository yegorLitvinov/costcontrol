import Vue from 'vue'

import BootstrapVue from 'bootstrap-vue'

Vue.use(BootstrapVue)

// Регистрируем глобальную пользовательскую директиву `v-focus`
Vue.directive('focus', {
  // Когда привязанный элемент вставлен в DOM...
  inserted: function(el) {
    // Переключаем фокус на элемент
    el.focus()
  }
})
