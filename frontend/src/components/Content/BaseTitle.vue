<script>
import {defineComponent} from "vue";

export default defineComponent({
  name: "BaseTitle"
})
</script>

<template>
  <div class="page-title">
    <slot></slot>
  </div>
</template>

<style scoped>
.page-title{
  width: 95%;
  font-family: "Newsreader", "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 24px;
  font-weight: 450;
  line-height: 1.2;
  color: #212529;
  border-bottom: 1px solid #bdbdbd;
  padding: 0.3em 0.5em 0.4em 0;
}
</style>