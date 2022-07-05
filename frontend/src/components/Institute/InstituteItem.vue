<script lang="ts">
import ContentBlock from "@/components/Content/ContentBlock.vue";
import {defineComponent, PropType} from "vue";
import ShortPost from "@/models/ShortPostModel";

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
  </div>
</template>

<style scoped>
.institute{
  cursor: pointer;
  text-align: center;
}
</style>