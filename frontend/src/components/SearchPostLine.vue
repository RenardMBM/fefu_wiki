<script lang="ts">
import {defineComponent} from "vue";
import {useRouter} from "vue-router";
import BaseSearchLine from "@/components/BaseSearchLine.vue";
export default defineComponent({
  name: "SearchPostLine",
  components: {
    BaseSearchLine
  },
  props: {
    content: {
      type: String,
      default: ""
    }
  },
  setup(props){
    const router = useRouter();

    function search(searchQuery: string) {
      if (searchQuery != props.content) {
        router.push(`/search/${searchQuery}`)
      }
    }
    return{
      search
    }
  }
})
</script>

<template>
  <base-search-line @search="search" :content="$props.content"></base-search-line>
</template>

<style scoped>

</style>