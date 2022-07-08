<script lang="ts">
import {defineComponent} from "vue"
import BaseTitle from "@/components/Content/BaseTitle.vue";
import TeachersList from "@/components/Teacher/TeachersList.vue";
import getTeachers from "@/hooks/requests/teachers/getTeachers";

export default defineComponent({
  name: "TeachersView",
  components: {
    BaseTitle,
    TeachersList,
  },
  setup(){
    const { teachers } = getTeachers();
    return {
      teachers,
    }
  }
})
</script>

<template>
<base-title>Преподаватели Лучшего университета</base-title>
  <teachers-list :teachers="teachers"></teachers-list>
</template>

<style scoped>

</style>