<script lang="ts">
import { defineComponent } from 'vue';

import BaseTitle from "@/components/Content/BaseTitle.vue";
import BaseSubtitle from "@/components/Content/BaseSubtitle.vue";
import TopTeachers from "@/components/Teacher/TopTeachers.vue";
import InstitutesList from "@/components/Institute/InstitutesList.vue";

import getTopsPosts from "@/hooks/requests/tops/getTopsPosts";

export default defineComponent({
  name: "HomeView",
  components: {
    InstitutesList,
    BaseTitle,
    BaseSubtitle,
    TopTeachers
  },
  setup(){
    const {tops} = getTopsPosts([0, 1, 2]);
    return{
      tops
    }
  }
})
</script>

<template>
  <div class="home">
    <base-title>Добро пожаловать на ДВФУ Вики: сайт о преподавателях ДВФУ и не только!</base-title>
  </div>
  <div class="institutes-block">
    <base-subtitle>Институты и школы</base-subtitle>
    <institutes-list></institutes-list>
  </div>
  <div class="top-block">
    <base-subtitle>Топ преподавателей</base-subtitle>
    <div class="top-list">
      <top-teachers v-for="top in tops"
                 :title="top.title" :teachers="top.posts"></top-teachers>
    </div>
  </div>
</template>

<style>
.top-list{
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}
</style>
