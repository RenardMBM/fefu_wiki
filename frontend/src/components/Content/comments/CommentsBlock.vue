<script lang="ts">
import {defineComponent, PropType, ref} from "vue"
import CommentData from "@/models/CommentModel";
import BaseButton from "@/components/UI/BaseButton.vue";
import CommentItem from "@/components/Content/comments/CommentItem.vue";
import BaseTitle from "@/components/Content/BaseTitle.vue";
import ContentBlock from "@/components/Content/ContentBlock.vue";
import BaseAreaInput from "@/components/UI/BaseAreaInput.vue";


interface Dictionary<T> {
  [Key: string]: T;
}


export default defineComponent({
  name: "CommentsBlock",
  components: {BaseAreaInput, BaseButton, CommentItem, BaseTitle, ContentBlock},
  props: {
    title: {
      type: String,
      required: true,
    },
    comments: {
      type: Array as PropType<Array<CommentData>>,
      required: true,
    },
    newComm: {
      type: String,
      default: "",
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
  setup(props, {emit}) {
    const dict = ref<Dictionary<number>>({});
    const usersCount = ref<number>(1);

    const CommQuery = ref<string>(props.newComm)
    function onAddComm() {
      emit('addComment', CommQuery.value);
    }

    return {dict, usersCount, CommQuery, onAddComm};
  }
});
</script>

<template>
  <div class="commentBlock">
    <BaseTitle class="comment-title"> {{title}} </BaseTitle>
    <base-button class="btn" @click="onAddComm">Оставить коментарий</base-button>
    <base-area-input class="areaInp" v-model="CommQuery">

    </base-area-input>
    <div class="comment-list" v-if="comments.length > 0">
      <comment-item class="comment-item"
                    v-for="comment in comments"
                    :comment="comment"
                    :user-name="this.giveName(comment.userId)"
      />
    </div>
    <content-block v-else>
      Пока что комментариев нет
    </content-block>
  </div>
</template>


<style scoped>
.comment-title{
  margin-left: 12px;
}
.btn {
  margin: 10px;
}
.areaInp {
  margin-left: 10px;
  height: 100px;
}
</style>