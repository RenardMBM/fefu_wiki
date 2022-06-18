<template>
  <div class="my-subtitle">
    <strong>
    <slot></slot>
    </strong>
  </div>
</template>

<script>
export default {
  name: "my-subtitle",
}
</script>

<style scoped>
.my-subtitle{
  font-size: 22px;
  width: 100%;
  padding: 0.5em 0 0.5em 1em;
}
</style>