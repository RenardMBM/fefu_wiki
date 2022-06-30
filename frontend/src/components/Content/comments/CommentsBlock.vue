<script lang="ts">
import {defineComponent, PropType, ref} from "vue"
import CommentData from "@/models/CommentModel";
import BaseButton from "@/components/UI/BaseButton.vue";
import CommentItem from "@/components/Content/comments/CommentItem.vue";


interface Dictionary<T> {
  [Key: string]: T;
}


export default defineComponent({
  name: "CommentsBlock",
  components: {BaseButton, CommentItem},
  props: {
    title: {
      type: String,
      required: true,
    },
    comments: {
      type: Array as PropType<Array<CommentData>>,
      required: true,
    }
  },
  methods: {
    giveName(userId: number | null){
      if (userId == null){
        return null;
      }else{
        let strId = userId.toString();
        if (!this.dict[strId]){
          this.dict[strId] = this.usersCount++;
        }
        return "Авторизованный пользователь " + this.dict[strId].toString();
      }
    }
  },
  setup() {
    const dict = ref<Dictionary<number>>({});
    const usersCount = ref<number>(1);
    return {dict, usersCount};
  }
});
</script>

<template>
  <div class="commentBlock">
    <div class="comment-title"> {{title}} </div>
    <base-button>Оставить коментарий</base-button>
    <div class="comment-list" v-if="comments.length > 0">
      <comment-item class="comment-item"
                    v-for="comment in comments"
                    :comment="comment"
                    :user-name="this.giveName(comment.userId)"
      />
    </div>
    <div class="comment-item" v-else >
      Пока что комментариев нет
    </div>
  </div>
</template>


<style scoped>

</style>