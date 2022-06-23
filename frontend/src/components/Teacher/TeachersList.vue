<script lang="ts">
import {defineComponent, PropType} from "vue";
import TeacherItem from "@/components/Teacher/TeacherItem.vue";
import ContentBlock from "@/components/Content/ContentBlock.vue";
import ShortPost from "@/models/ShortPostModel";

export default defineComponent({
  name: "TeachersList",
  components: {
    TeacherItem,
    ContentBlock
  },
  props:{
    teachers:{
      type: Object as PropType<Array<ShortPost>>,
      default: []
    }
  }
})
</script>

<template>
  <content-block class="teachers-block">
    <teacher-item v-for="teacher in teachers" :teacher="teacher"/>
  </content-block>
</template>

<style scoped>

</style>