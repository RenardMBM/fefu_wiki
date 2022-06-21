<template>
  <the-header></the-header>
  <the-navbar></the-navbar>
  <div class="app">
    <router-view></router-view>
  </div>
</template>

<script lang="ts">
import TheNavbar from "@/components/TheNavbar.vue";
import TheHeader from "@/components/TheHeader.vue";

import {defineComponent} from "vue"

export default defineComponent({
  components: {TheHeader, TheNavbar}
})
</script>

<style>
* {
  font-size: inherit;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: sans-serif;
}
.app {
  margin: 7em 0 0 10em;
  border-top: 1px solid #bdbdbd;
  padding: 20px;
  /*height: 100%;*/
}
@media only screen and (max-width : 800px){
  .app {
     margin-left: 0;
  }
}
button{
  margin: 0;
  padding: 0;
  border: 0;
}
</style>