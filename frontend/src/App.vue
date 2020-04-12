<template>
  <v-app>
    <router-view v-bind:key="$route.fullPath"></router-view>
  </v-app>
</template>

<script>
export default {
  name: 'App'
}
</script>
