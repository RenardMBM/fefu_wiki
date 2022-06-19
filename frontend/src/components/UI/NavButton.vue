<script lang="ts">
import {defineComponent} from "vue";

export default defineComponent({
  name: "nav-button"
})
</script>

<template>
    <button class="nav-btn">
      <slot></slot>
    </button>
</template>

<style scoped>
.nav-btn {
  width: 10em;
  padding: 1em 0;
  background: none;
  color: teal;
  border-bottom: 1px solid teal;
  cursor: pointer;
  /*border: 1px solid teal;*/
}
</style>