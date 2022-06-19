<script lang="ts">
import ContentBlock from "@/components/UI/ContentBlock.vue";
import Institute from "@/models/InstituteModel";
import {defineComponent, PropType} from "vue";

export default defineComponent({
  name: "InstituteItem",
  components: {
    ContentBlock
  },
  props: {
    institute: {
      type: Object as PropType<Institute>,
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