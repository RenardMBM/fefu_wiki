<script lang="ts">
import {defineComponent, ref} from "vue"
import BaseTitle from "@/components/Content/BaseTitle.vue";
import {useRoute} from "vue-router";
import searchPost from "@/hooks/requests/seacrhPost";
import TeachersList from "@/components/Teacher/TeachersList.vue";
import ShortPost from "@/models/ShortPostModel";
import SubInfo from "@/models/ShortPostModel";

export default defineComponent({
  name: "TeachersView",
  components: {
    BaseTitle,
    TeachersList,
  },
  setup(){
    const teachers = ref<Array<ShortPost>>([{id: 1, title: "Селезнев Тим Эдуардович", blocks: [{title: "Дата родения", content: "10.09.1920"}]},
      {id: 1, title: "Сущенко Андрей Андреевич", blocks: [{title: "Дата родения", content: "13.10.1913"}]},
        {id: 1, title: "Калиниченко Артем Александрович", blocks: [{title: "Дата родения", content: "02.11.1981"}]},
      {id: 1, title: "Кленин Александр Сергеевич", blocks: [{title: "Дата родения", content: "20.01.1932"}]}]);
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