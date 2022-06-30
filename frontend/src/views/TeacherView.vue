<script lang="ts">
import {defineComponent, ref} from "vue";
import { useRoute } from 'vue-router'
import getTeacherData from "@/hooks/requests/getTeacherData";
import BasePost from "@/components/Content/Post/BasePost.vue";
import EditPost from "@/components/Content/Post/EditPost.vue";

export default defineComponent({
  name: "TeacherView",
  components: {EditPost, BasePost},
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
  <base-post :id="id" :post="teacher"></base-post>
</template>

<style scoped>

</style>