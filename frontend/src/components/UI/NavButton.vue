<template>
    <button class="nav-btn">
      <slot></slot>
    </button>
</template>

<script>
export default {
  name: "nav-button"
}
</script>

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