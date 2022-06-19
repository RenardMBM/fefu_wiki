<template>
  <my-header></my-header>
  <navbar></navbar>
  <div class="app">
    <router-view></router-view>
  </div>
</template>

<script lang="ts">
import Navbar from "@/components/Navbar.vue";
import MyHeader from "@/components/Header.vue";
import {defineComponent} from "vue"

export default defineComponent({
  components: {MyHeader, Navbar}
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

  margin: 7em 0  0 10em;
  border-top: 1px solid black;

  padding: 20px;
  /*height: 100%;*/
}
button{
  margin: 0;
  padding: 0;
  border: 0;
}
</style>