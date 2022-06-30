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
    <div class="comment-info">
      <img class="info-img" :src="require('@/assets/usersPic/' + 'Pic' + imgNum + '.png')" alt="comment img :(">
      <div style="display: flex; flex-direction: column; flex-grow: 1">
      <strong class="userName">{{ userName ? userName : "Неавторизованный пользователь" }}</strong>
      <div class="date">{{comment.date.toLocaleDateString()}}</div>
      </div>
      <div style="display: flex">
        <button class="btn-icon">
          <i v-if="comment.voted !== 1" class="bi bi-hand-thumbs-up"></i>
          <i v-else class="bi bi-hand-thumbs-up-fill"></i></button>
        <div class="likes">{{comment.likes}}</div>
        <button class="btn-icon">
          <i v-if="comment.voted !== -1" class="bi bi-hand-thumbs-down"></i>
          <i v-else class="bi bi-hand-thumbs-down-fill"></i></button>
        <div class="likes">{{comment.dislikes}}</div>
      </div>
    </div>
    <div class="text">{{comment.text}}</div>
  </content-block>
</template>

<style scoped>
.comment-info {
  display: flex;
}
.info-img {
  width: 100px;
  height: 100px;
  border-radius: 10px;
}
.userName {
  margin: 0 10px 0 10px;
}
.likes {
  margin: 0 10px 0 3px;
}
.btn-icon {
  background: none;
  top: 0;
  margin-bottom: 80px;
  cursor: pointer;
}
.date {
  margin: 10px;
  color: #606b8d;
}
.text {
  margin: 10px 10px 0 10px;
}
</style>