import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/pages/Index.vue'
import Register from '@/components/Register.vue'
import AdminLogin from '@/components/admin/AdminLogin.vue'
import AdminIndex from '@/components/admin/AdminIndex.vue'
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

    },
    {
      path: '/admin/login',
      name: 'login',
      component: AdminLogin
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdminIndex,
      meta: {
        requiresAuth: true
      }
    }
  ]
})
export default router
