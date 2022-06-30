<script lang="ts">
import {defineComponent, ref} from "vue";
import { useRoute } from 'vue-router'
import getTeacherData from "@/hooks/requests/getTeacherData";
import BasePost from "@/components/Content/Post/BasePost.vue";
import EditPost from "@/components/Content/Post/EditPost.vue";
import CommentsBlock from "@/components/Content/comments/CommentsBlock.vue";
import CommentData from "@/models/CommentModel";

export default defineComponent({
  name: "TeacherView",
  components: {CommentsBlock, EditPost, BasePost},
  setup(){
    const route = useRoute();
    const id = ref<number>(Number(route.params.id as string));

    const commTitle = ref<String>("Комментарии");
    const comments = ref<Array<CommentData>>([{userId: 1202, date: new Date("01-03-2003"), text: "Привет", dislikes: 0, likes: 1, voted: 0 },
      {userId: 123, date: new Date("2003-02-03"), text: "2003-01-01", dislikes: 0, likes: 1, voted: 0 },
      {userId: 11, date: new Date("01-01-2003"), text: "Привет", dislikes: 0, likes: 1, voted: 1 },
      {userId: 1202, date: new Date("01-01-2003"), text: "Привет", dislikes: 0, likes: 1, voted: 0 },
      {userId: null, date: new Date("01-01-2003"), text: "Привет", dislikes: 0, likes: 1, voted: -1 }])

    if (id) {
      const {teacher} = getTeacherData(id.value);
      return {id, teacher, commTitle, comments}
    }
    const teacher = ref(undefined);
    return {id, teacher, commTitle, comments}
  }
})
</script>

<template>
  <edit-post v-if="!isNaN(id)" :post="teacher"></edit-post>
  <base-post :id="id" :post="teacher"></base-post>
  <comments-block :title="commTitle" :comments="comments" ></comments-block>
</template>

<style scoped>

</style>