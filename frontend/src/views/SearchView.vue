<script lang="ts">
import {defineComponent, ref} from "vue";
import { useRoute } from 'vue-router'
import BaseTitle from "@/components/Content/BaseTitle.vue";
import SearchPostLine from "@/components/SearchPostLine.vue";
import TeachersList from "@/components/Teacher/TeachersList.vue";
import searchPost from "@/hooks/requests/seacrhPost"

export default defineComponent({
  name: "SearchView",
  components: {
    BaseTitle,
    SearchPostLine,
    TeachersList
  },
  setup(){
    const route = useRoute();
    const searchQuery = ref<string>(route.params.searchQuery as string);
    const { posts } = searchPost(searchQuery.value)
    return {
      searchQuery,
      posts
    }
  }
})
</script>

<template>
  <base-title>
    <search-post-line :content="searchQuery"/>
  </base-title>
  <teachers-list :teachers="posts"></teachers-list>
</template>

<style scoped>

</style>