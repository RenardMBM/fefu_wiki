<script lang="ts">
import {defineComponent} from "vue"
export default defineComponent({
  name: 'BaseButton'
})
</script>

<template>
  <button class="btn">
    <slot></slot>
  </button>
</template>

<style scoped>
.btn {
  border-radius: 7px;
  padding: 7px 45px;
  background: none;
  color: black;
  border: 1px solid black;
  cursor: pointer;
}
.btn:hover {
  background-color: #003F74;
  color: white;
  transition-duration: 0.3s;
  border: 1px solid #003F74;
}
.btn:active {
  transition-duration: 0.05s;
  transform: translateY(1.5px);
}
</style>
