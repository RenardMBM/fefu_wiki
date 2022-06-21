<script lang="ts">
import {defineComponent, ref} from "vue";
import EditPost from "@/components/Post/EditPost.vue";
import MyPost from "@/components/Post/MyPost.vue";
import {useRoute} from "vue-router";
import getInstituteData from "@/hooks/getInstituteData";
export default defineComponent({
  name: "InstituteView",
  components: {EditPost, MyPost},
  setup(){
    const route = useRoute();
    const id = ref<number>(Number(route.params.id as string));

    if (id) {
      const {institute} = getInstituteData(id.value);
      return {id, institute}
    }
    const institute = ref(undefined);
    return {id, institute}
  }
})
</script>

<template>
  <edit-post v-if="!isNaN(id)" :post="institute"></edit-post>
  <my-post :id="id" :post="institute"></my-post>
</template>

<style scoped>

</style>