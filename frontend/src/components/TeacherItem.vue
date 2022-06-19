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
  line-height: 20px;
  border: 1px solid teal;
  border-radius: 10px;
  background-color: #EBEEEF;
  /*margin-top: 15px;*/
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  flex-direction: column;
  cursor: pointer;
}
.teacher:hover {
  background-color: #DBDEDF;
  transition-duration: 0.3s;
}
.teacher:active {
  background-color: #CBCECF;
  transform: translateY(1px);
}
</style>