import Vue from 'vue'

// Cards
import bCard from 'bootstrap-vue/es/components/card/card'
import bCardHeader from 'bootstrap-vue/es/components/card/card-header'
import bCardBody from 'bootstrap-vue/es/components/card/card-body'
// Layout
import bRow from 'bootstrap-vue/es/components/layout/row'
import bCol from 'bootstrap-vue/es/components/layout/col'
// Forms
import bForm from 'bootstrap-vue/es/components/form/form'
import bFormInvalidFeedback from 'bootstrap-vue/es/components/form/form-invalid-feedback'
import bFormGroup from 'bootstrap-vue/es/components/form-group/form-group'
import bFormInput from 'bootstrap-vue/es/components/form-input/form-input'
import bFormSelect from 'bootstrap-vue/es/components/form-select/form-select'
// Buttons
import bButton from 'bootstrap-vue/es/components/button/button'

// Cards
Vue.component('b-card', bCard)
Vue.component('b-card-header', bCardHeader)
Vue.component('b-card-body', bCardBody)
// Layout
Vue.component('b-row', bRow)
Vue.component('b-col', bCol)
// Forms
Vue.component('b-form', bForm)
Vue.component('b-form-invalid-feedback', bFormInvalidFeedback)
Vue.component('b-form-group', bFormGroup)
Vue.component('b-select', bFormSelect)
Vue.component('b-input', bFormInput)
// Buttons
Vue.component('b-button', bButton)
