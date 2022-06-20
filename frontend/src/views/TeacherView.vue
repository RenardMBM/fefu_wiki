<script lang="ts">
import {defineComponent, ref} from "vue";
import { useRoute } from 'vue-router'
import getTeacherData from "@/hooks/getTeacherData";
import MyPost from "@/components/Post/MyPost.vue";
import EditPost from "@/components/Post/EditPost.vue";

export default defineComponent({
  name: "TeacherView",
  components: {EditPost, MyPost},
  setup(){
    const route = useRoute();
    const id = ref<number>(Number(route.params.id as string));

    if (id) {
      const {teacher} = getTeacherData(id.value);
      return {id, teacher}
    }
    const teacher = ref(undefined);
    return {id, teacher}
  }
})
</script>

<template>
  <edit-post v-if="!isNaN(id)" :post="teacher"></edit-post>
  <my-post :id="id" :post="teacher"></my-post>
</template>

<style scoped>

</style>