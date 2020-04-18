<template>
  <v-app>
    <p
      v-for="i in adat"
      :key="i"
    >
      {{ szam }}
    </p>
  </v-app>
</template>

<script>
export default {
  name: 'AdminIndex',
  components: {
  },
  data() {
    return {
      adat: ['helo', 'belo'],
      szam: 0
    }
  }
}
</script>
