<script>
import {defineComponent} from "vue";

export default defineComponent({
  name: "my-subtitle",
})
</script>

<template>
  <div class="my-subtitle">
    <strong>
    <slot></slot>
    </strong>
  </div>
</template>

<style scoped>
.my-subtitle{
  font-size: 22px;
  width: 100%;
  padding: 0.5em 0 0.5em 1em;
}
</style>