<script lang="ts">
import {defineComponent, ref} from "vue";
import { useRoute } from 'vue-router'
import getTeacherData from "@/hooks/requests/teachers/getTeacherData";
import BasePost from "@/components/Content/Post/BasePost.vue";
import EditPost from "@/components/Content/Post/EditPost.vue";
import CommentsBlock from "@/components/Content/comments/CommentsBlock.vue";
import Post from "@/models/PostModel";
import sendComments from "@/hooks/requests/comments/sendComment";
import sendTeacherEdit from "@/hooks/requests/teachers/sendTeacherEdit";
import getComments from "@/hooks/requests/comments/getComments";

export default defineComponent({
  name: "TeacherView",
  components: {CommentsBlock, EditPost, BasePost},
  setup(){
    const route = useRoute();
    const id = ref<number>(Number(route.params.id as string));

    const commTitle = ref<String>("Комментарии");
    const { comments } = getComments(id.value);

    function send(post: Post) {
      sendTeacherEdit(post)
    }

    function createComment(text: string) {
      sendComments(id.value, text)
    }

    if (id) {
      const {teacher} = getTeacherData(id.value);
      return {id, teacher, commTitle, comments, send, createComment}
    }
    const teacher = ref(undefined);
    return {id, teacher, commTitle, comments, send, createComment}
  }
})
</script>

<template>
  <edit-post v-if="!isNaN(id)" @send="send" :post="teacher"></edit-post>
  <base-post :id="id" :post="teacher"></base-post>
  <comments-block :title="commTitle" :comments="comments" @addComment="createComment"></comments-block>
</template>

<style scoped>

</style>