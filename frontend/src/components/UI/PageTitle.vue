<template>
  <div class="page-title">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "PageTitle"
}
</script>

<style scoped>
.page-title{
  width: 100%;
  font-size: 24px;
  border-bottom: 1px solid black;
  padding-bottom: 0.2em;
}
</style>