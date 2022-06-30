<script lang="ts">
import {defineComponent, ref} from "vue";
import EditPost from "@/components/Content/Post/EditPost.vue";
import BasePost from "@/components/Content/Post/BasePost.vue";
import {useRoute} from "vue-router";
import getInstituteData from "@/hooks/requests/getInstituteData";
export default defineComponent({
  name: "InstituteView",
  components: {EditPost, BasePost},
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
  <base-post :id="id" :post="institute"></base-post>
</template>

<style scoped>

</style>