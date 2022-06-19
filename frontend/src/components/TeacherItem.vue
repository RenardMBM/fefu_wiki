<script lang="ts">
import {defineComponent, PropType} from "vue"
import TeacherItem from "@/models/TeacherItemModel";

export default defineComponent({
  name: "TeacherItem",
  props: {
    teacher: {
      type: Object as PropType<TeacherItem>,
      required: true,
    }
  }
})
</script>

<template>
  <div class="teacher" @click="$router.push(`/teacher/${teacher.id}`)">
    <div><strong>{{ teacher.title }}</strong> </div>
    <div>{{ teacher.subtitle }}: {{ teacher.value }}</div>
  </div>
</template>

<style scoped>
.teacher {
  padding: 15px;
  border: 2px solid teal;
  border-radius: 10px;
  /*margin-top: 15px;*/
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  flex-direction: column;
  cursor: pointer;
}
</style>