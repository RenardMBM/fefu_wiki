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
  color: #003F74;
  border-bottom: 1px solid #bdbdbd;
  cursor: pointer;
  /*border: 1px solid teal;*/
}
</style>