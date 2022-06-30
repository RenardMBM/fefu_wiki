<script lang="ts">
import {defineComponent} from "vue";
import store from "@/store"
import BaseNavbar from "@/components/BaseNavbar.vue";
import TheMobileNavbar from "@/components/TheMobileNavbar.vue";
export default defineComponent({
  name: "TheNavbar",
  components: {
    BaseNavbar,
    TheMobileNavbar
  },
  computed: {
    mobileMode() {
      return store.state.format.isMobile;
    }
  }
})
</script>

<template>
  <the-mobile-navbar v-if="mobileMode"/>
  <base-navbar v-else/>
</template>

<style scoped>

</style>