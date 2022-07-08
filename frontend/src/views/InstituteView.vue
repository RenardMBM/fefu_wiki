<script lang="ts">
import {defineComponent, ref} from "vue";
import EditPost from "@/components/Content/Post/EditPost.vue";
import BasePost from "@/components/Content/Post/BasePost.vue";
import {useRoute} from "vue-router";
import getInstituteData from "@/hooks/requests/institutes/getInstituteData";
import sendInstituteEdit from "@/hooks/requests/institutes/sendInstituteEdit";
import Post from "@/models/PostModel";
export default defineComponent({
  name: "InstituteView",
  components: {EditPost, BasePost},
  setup(){
    const route = useRoute();
    const id = ref<number>(Number(route.params.id as string));
    function send(post: Post) {
      sendInstituteEdit(post)
    }
    if (id) {
      const {institute} = getInstituteData(id.value);
      return {id, institute, send}
    }
    const institute = ref(undefined);

    return {
      id,
      institute,
      send
    }
  }
})
</script>

<template>
  <edit-post v-if="!isNaN(id)" @send="send" :post="institute" :is_colum="false" ></edit-post>
  <base-post :id="id" :post="institute" :is_column="false"></base-post>
</template>

<style scoped>

</style>