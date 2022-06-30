<script lang="ts">
import {defineComponent} from "vue";
export default defineComponent({
  name: "ContentBlock"
})
</script>

<template>
  <div class="content-block">
    <slot></slot>
  </div>
</template>

<style scoped>
.content-block{
  background-color: #EBEEFF;
  border-radius: 15px;
  width: 100%;
  padding: 1em;
  margin: 0.5em;
}
</style>