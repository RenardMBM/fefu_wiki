<template>
  <div class="post">
    <div><strong>{{ post.title }}</strong> </div>
    <div>{{ post.subtitle }}: {{ post.value }}</div>
  </div>
</template>

<script>
export default {
  name: "PostItem",
  props: {
    post: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style scoped>
.post {
  padding: 15px;
  border: 2px solid teal;
  border-radius: 10px;
  /*margin-top: 15px;*/
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  flex-direction: column;
}
</style>