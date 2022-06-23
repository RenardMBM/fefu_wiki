<script lang="ts">
import { defineComponent, PropType } from "vue";

import Post from "@/models/PostModel";

import BaseTitle from "@/components/Content/BaseTitle.vue";
import ContentBlock from "@/components/Content/ContentBlock.vue";
import ErrorView from "@/views/ErrorView.vue";
import PostInfoColumn from "@/components/Content/Post/PostInfoColumn.vue";
import MarkDown from "@/components/Content/Post/MarkDown.vue";

export default defineComponent({
  name: "BasePost",
  components: {
    MarkDown,
    BaseTitle,
    ContentBlock,
    ErrorView,
    PostInfoColumn,
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
  <div v-else class="short-post">
    <div class="post-main-content">
      <base-title class="post-title">{{ post.title }}</base-title>
      <content-block>
        <mark-down :text="post.text"></mark-down>
      </content-block>
    </div>
    <post-info-column :data="post.info"></post-info-column>
  </div>
</template>

<style scoped>
.short-post{
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