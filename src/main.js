import Vue from 'vue'
import vuetify from './plugins/vuetify'
import './plugins/base'
import App from './App.vue'
import store from './store'
import router from '@/router'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import '@mdi/font/css/materialdesignicons.min.css'
import $ from 'jquery'
Vue.config.productionTip = false

new Vue({
  store,
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
