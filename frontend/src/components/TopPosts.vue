<script lang="ts">
import { defineComponent } from 'vue';
import PostItem from "@/components/PostItem.vue";
import ContentBlock from "@/components/UI/ContentBlock.vue";
import PageTitle from "@/components/UI/PageTitle.vue";
import MySubtitle from "@/components/UI/MySubtitle.vue";

export default defineComponent({
  name: "TopPosts",
  components: {
    PostItem,
    ContentBlock,
    PageTitle,
    MySubtitle
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
})
</script>

<template>
  <content-block class="top-column">
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
  </content-block>
</template>

<style scoped>
.top-title{
  font-size: 18px;
  text-align: center;
}
.top-column{
  padding-bottom: 0.5em;
  width: fit-content!important;
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