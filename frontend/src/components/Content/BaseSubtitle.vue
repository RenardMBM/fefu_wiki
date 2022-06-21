<script>
import {defineComponent} from "vue";

export default defineComponent({
  name: "BaseSubtitle",
})
</script>

<template>
  <div class="base-subtitle">
    <strong>
    <slot></slot>
    </strong>
  </div>
</template>

<style scoped>
.base-subtitle{
  //font-family: Verdana;
  font-size: 22px;
  width: 100%;
  padding: 0.5em 0 0.5em 1em;
}
</style>