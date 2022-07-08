<script lang="ts">
import {defineComponent, PropType} from "vue"
import ShortPost from "@/models/ShortPostModel";

export default defineComponent({
  name: "TeacherItem",
  props: {
    teacher: {
      type: Object as PropType<ShortPost>,
      required: true,
    }
  }
})
</script>

<template>
  <div class="post-block" @click="$router.push(`/teacher/${teacher.id}`)">
    <div><strong>{{ teacher.title }}</strong> </div>
    <div class="sub-info" v-for="block in teacher.blocks">{{ block.title }}: {{ block.content }}</div>
  </div>
</template>

<style scoped>
.post-block {
  margin: 6px 0 6px 0;
  padding: 15px;
  line-height: 20px;
  border: 1px solid teal;
  border-radius: 10px;
  background-color: #d9dcff;
  /*margin-top: 15px;*/
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  flex-direction: column;
  cursor: pointer;
}
.post-block:hover {
  background-color: #c3c6e5;
  transition-duration: 0.3s;
}
.post-block:active {
  background-color: #afb2ce;
  transform: translateY(1px);
}
</style>