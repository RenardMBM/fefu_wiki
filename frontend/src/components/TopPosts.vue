<template>
  <div class="top-column">
    <div class="top-title">
      {{title}}
    </div>
    <div class="top-list" v-if="posts.length > 0">
      <post-item class="top-list-item"
          v-for="post in posts"
          :post="post"
      />
    </div>
    <div class="top-list-item" v-else >
      Список пуст
    </div>
  </div>
</template>

<script>
import PostItem from "@/components/PostItem";
export default {
  name: "TopPosts",
  components: {
      PostItem
  },
  props: {
    title: {
      type: String,
      required: true,
    },
    posts: {
      type: Array,
      required: true,
    }
  }
}
</script>

<style scoped>
.top-title{
  font-size: 18px;
  text-align: center;
  /*width: 100%;*/
  /*padding: 0.5em 0 0.5em 1em;*/
}
.top-column{
  background-color: #EBEEFF;
  border-radius: 30px;
  padding: 1em 1em 0.5em 1em;
  width: fit-content;
}
.top-list{
  padding-top: 1em;
  display: inline-block;
  /*padding: 1em;*/
}
.top-list-item{
  margin-bottom: 0.5em;
}
</style>