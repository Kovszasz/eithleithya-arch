<template>
  <v-app>
    <core-toolbar />

    <core-view />

    <core-footer />
  </v-app>
</template>

<script>
export default {
  name: 'Index',
  components: {
    CoreFooter: () => import('@/components/core/Footer'),
    CoreToolbar: () => import('@/components/core/Toolbar'),
    CoreView: () => import('@/components/core/View')
  }
}
</script>
