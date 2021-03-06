import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify)

export default new Vuetify({
  theme: {
    primary: '#D3C3BC',
    secondary: '#BFADA5',
    accent: '#D8EBF1',
    info: '#5B5C79'
  },
  iconfont: 'mdi'
})
