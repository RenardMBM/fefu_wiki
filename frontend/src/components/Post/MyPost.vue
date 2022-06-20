<script lang="ts">
import { defineComponent, PropType } from "vue";

import Post from "@/models/PostModel";

import PageTitle from "@/components/UI/PageTitle.vue";
import ContentBlock from "@/components/UI/ContentBlock.vue";
import ErrorView from "@/views/ErrorView.vue";
import InfoColumn from "@/components/Post/InfoColumn.vue";
import MarkDown from "@/components/Post/MarkDown.vue";

export default defineComponent({
  name: "MyPost",
  components: {
    MarkDown,
    PageTitle,
    ContentBlock,
    ErrorView,
    InfoColumn,
  },
  props: {
    id: {
      type: Number,
      required: true
    },
    post: {
      type: Object as PropType<Post | undefined>,
      required:true
    }
  }
})
</script>

<template>
  <error-view v-if="isNaN(id)"></error-view>
  <div v-else class="post">
    <div class="post-main-content">
      <page-title class="post-title">{{ post.title }}</page-title>
      <content-block>
        <mark-down :text="post.text"></mark-down>
      </content-block>
    </div>
    <info-column :data="post.info"></info-column>
  </div>
</template>

<style scoped>
.post{
  display: flex;
  flex-wrap: wrap-reverse;
}

.post-main-content{
  width: 70%;
  padding-right: 5em;
}
.post-text{
  width: initial;
  margin-left: 0;
}
.post-title{
  margin-left: 0.5em;
}
</style>