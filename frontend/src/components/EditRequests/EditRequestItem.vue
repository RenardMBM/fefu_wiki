<script lang="ts">
import {defineComponent, PropType} from "vue";
import ShortPost from "@/models/ShortPostModel";

export default defineComponent({
  name: "EditRequestItem",
  props: {
    editRequest: {
      type: Object as PropType<ShortPost>,
      required: true,
    },
    typeRequest:{
      type: String,
      required: true
    }
  }
})
</script>

<template>
  <div class="post-block" @click="$router.push(`/editRequests/${typeRequest}/${editRequest.id}`)">
    <div><strong>{{ editRequest.title }}</strong> </div>
    <div class="sub-info" v-for="block in editRequest.blocks">{{ block.title }}: {{ block.content }}</div>
  </div>
</template>

<style scoped>

</style>