import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/pages/Index.vue'
import Register from '@/components/Register.vue'
Vue.use(Router)
const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Index,
      meta: {
        requiresAuth: false

      }
    },
    {
      path: '/order',
      name: 'order',
      component: Register

    }
  ]
})
export default router
