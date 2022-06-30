<script lang="ts">
import {defineComponent, PropType, ref} from "vue"
import ContentBlock from "@/components/Content/ContentBlock.vue";
import CommentData from "@/models/CommentModel";

export default defineComponent({
  name: "CommentItem",
  components: {
    ContentBlock,
  },
  props: {
    comment: {
      type: Object as PropType<CommentData>,
      required: true,
    },
    userName: {
      type: String,
      required: true,
    }
  },
  setup(props) {
    const imgNum = ref<number>(props.comment.userId ? props.comment.userId % 6 + 1 : 0)
    return {imgNum};
  }
});
</script>

<template>
  <content-block>
    <img class="info-img" :src="require('@/assets/usersPic/' + 'Pic' + imgNum + '.png')" alt="comment img :(">
    <div class="userName">{{ userName ? userName : "Неавторизованный пользователь" }}</div>
    <div class="likes">{{comment.likes}}</div>
    <div class="likes">{{comment.dislikes}}</div>
    <div class="date">{{comment.date}}</div>
    <div class="text">{{comment.text}}</div>
  </content-block>
</template>

<style scoped>

</style>