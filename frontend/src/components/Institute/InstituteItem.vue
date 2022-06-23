<script lang="ts">
import ContentBlock from "@/components/Content/ContentBlock.vue";
import ShortPost from "@/models/ShortPostModel";
import {defineComponent, PropType} from "vue";

export default defineComponent({
  name: "InstituteItem",
  components: {
    ContentBlock
  },
  props: {
    institute: {
      type: Object as PropType<ShortPost>,
      required: true,
    }
  }
})
</script>

<template>
  <div class="institute"
       @click="$router.push(`/institute/${institute.id}`)"
  >
    <div>{{ institute.title }}</div>
    <div v-for="block in institute.blocks">{{ block.title }}: {{ block.content }}</div>

  </div>
</template>

<style scoped>
.institute{
  cursor: pointer;
  text-align: center;
}
</style>