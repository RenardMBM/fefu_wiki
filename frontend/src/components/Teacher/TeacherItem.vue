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
  <div class="short-post" @click="$router.push(`/teacher/${teacher.id}`)">
    <div><strong>{{ teacher.title }}</strong> </div>
    <div class="sub-info" v-for="block in teacher.blocks">{{ block.title }}: {{ block.content }}</div>
  </div>
</template>

<style scoped>
.short-post {
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
.short-post:hover {
  background-color: #DBDEDF;
  transition-duration: 0.3s;
}
.short-post:active {
  background-color: #CBCECF;
  transform: translateY(1px);
}
</style>