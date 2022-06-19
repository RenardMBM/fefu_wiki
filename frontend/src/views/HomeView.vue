<script lang="ts">
import { defineComponent } from 'vue';
import PageTitle from "@/components/UI/PageTitle.vue";
import MySubtitle from "@/components/UI/MySubtitle.vue";
import TopPosts from "@/components/TopPosts.vue";
import InstitutesList from "@/components/InstitutesList.vue";

export default defineComponent({
  name: "HomeView",
  components: {
    InstitutesList,
    PageTitle,
    MySubtitle,
    TopPosts
  },
  data(){
    return{
      tops:[
        {
          title: "Ближайшие дни рожедения",
          posts: [
            {
              title: "Селезнев Тим Эдуардович",
              subtitle: "Дата рождения",
              value: "10.01.2002"
            },
            {
              title: "Cущенко Андрей Андреевич",
              subtitle: "Дата рождения",
              value: "10.01.2002"
            }
          ]
        },
        {
          title: "Самые халявные",
          posts: [
            {
              title: "Селезнев Тим Эдуардович",
              subtitle: "Халявность",
              value: "4.5"
            }
          ]
        },
        {
          title: "Самые строгие",
          posts: [
            {
              title: "Cущенко Андрей Андреевич",
              subtitle: "Халявность",
              value: "4"
            }
          ]
        },
      ],
    }
  }
})
</script>

<template>
  <div class="home">
    <page-title>Добро пожаловать на ДВФУ Вики: сайт о преподавателях ДВФУ и не только!</page-title>
  </div>
  <div class="institutes-block">
    <my-subtitle>Институты и школы</my-subtitle>
    <institutes-list></institutes-list>
  </div>
  <div class="top-block">
    <my-subtitle>Топ преподавателей</my-subtitle>
    <div class="top-list">
      <top-posts v-for="top in tops"
                 :title="top.title" :posts="top.posts"></top-posts>
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
