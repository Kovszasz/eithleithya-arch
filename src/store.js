import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const state = {
     accessToken: localStorage.getItem('access_token') || '',
     refreshToken: localStorage.getItem('refresh_token') || ''
  }
const getters = {
    loggedIn: state => {
      return state.accessToken !== ''
    },
    locaStorage: state => {
      return state
    },
    IsAuthenticated: state => {
      return state.login
    }
  }
const mutations = {
    updateLocalStorage (state, { access, refresh }) {
      localStorage.setItem('access_token', access)
      localStorage.setItem('refresh_token', refresh)
      state.accessToken = access
      state.refreshToken = refresh
    },
    updateAccess (state, access) {
      state.accessToken = access
    },
    destroyToken (state) {
      state.accessToken = ''
      state.refreshToken = ''
    }
  }
const actions = {

    refreshToken (context) {
      return new Promise((resolve, reject) => {
        axios.post('/api/token/refresh/', {
          refresh: context.state.refreshToken
        })
          .then(response => {
            context.commit('updateAccess', response.data.access)
            resolve(response.data.access)
          })
          .catch(err => {
            reject(err)
          })
      })
    },
    logoutUser (context) {
      if (context.getters.loggedIn) {
        return new Promise((resolve, reject) => {
          axios.get('/api/users/user_logout/')
            .then(response => {
              context.commit('updateLocalStorage', { access: '', refresh: '' })
              context.commit('destroyToken')
              context.commit('updateUser', false, false)
            })
            .catch(err => {
              localStorage.setItem('user', {})
            //  localStorage.removeItem('user-token')
            context.commit('updateLocalStorage', { access: '', refresh: '' })
            context.commit('destroyToken')
            context.commit('updateUser', false, false)
            resolve(err)
            })
        })
      }
    },
    loginUser (context, credentials) {
      return new Promise((resolve, reject) => {
        axios.post('/api/token/', {
          email: credentials.email,
          password: credentials.password
        })
          .then(response => {
            console.log(response)
            context.commit('updateLocalStorage', { access: response.data.access, refresh: response.data.refresh }) //, token:response.data.user }) // store the access and refresh token in localstorage
            resolve()
          })
          .catch(err => {
            console.log('ERROR')
            reject(err)
          })
      })
    }
}
export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
  rules: {
      'no-console': 'off'
  }
}
