<template>
  <the-header></the-header>
  <the-navbar></the-navbar>
  <div class="app">
    <router-view :key="$route.path"></router-view>
  </div>
  <screen-size></screen-size>
</template>

<script lang="ts">
import TheNavbar from "@/components/TheNavbar.vue";
import TheHeader from "@/components/TheHeader.vue";
import ScreenSize from "@/components/UILogics/ScreenSize.vue";
import store from "@/store"

import {defineComponent} from "vue"
import userDataToUser from "@/hooks/converters/userDataToUser";

export default defineComponent({
  components: {TheHeader, TheNavbar, ScreenSize},
  setup(){
    const dataElem = document.getElementById('djangoData');
    const data = dataElem?.textContent
    if (data) {
      store.commit('signIn', userDataToUser(JSON.parse(JSON.parse(data))))
    }
    if (dataElem){
      dataElem.remove()
    }

  }
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