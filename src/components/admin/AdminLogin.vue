<template>
  <v-card
    class="mx-auto"
    max-width="500"
  >
    <v-card-title class="title font-weight-regular justify-space-between">
      <span>Admin Login</span>
      <v-avatar
        color="primary lighten-2"
        class="subheading white--text"
        size="24"
        v-text="step"
      />
    </v-card-title>
    <v-card-text>
      <v-text-field
        v-model="payload.email"
        placeholder="Email"
        value="email..."
      />
      <v-text-field
        v-model="payload.password"
        placeholder="Password"
        value="password..."
        type="password"
      />
      <v-btn @click="login">
        Login
      </v-btn>
    </v-card-text>
  </v-card>
</template>
<script>

import api from '../../api.js'
import axios from 'axios'

export default {
  name: 'AdminLogin',
  props: {
  },
  data: () => ({
    step: 0,
    payload: {
      email: '',
      password: ''
    },
    state: ''
  }),
  methods: {
    async login () {
      console.log(this.$store)
     await axios.post('/api/token/', this.payload)
          .then(response => {
            this.$store.state.accessToken = response.data.access
            this.$store.state.refreshToken = response.data.refresh
            this.$router.push({ name: 'admin' })
          })
      }
  }
}
</script>
<style scoped>

</style>
