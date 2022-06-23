<script lang="ts">

import {defineComponent} from "vue"
import ContentBlock from "@/components/Content/ContentBlock.vue";
import InstituteItem from "@/components/Institute/InstituteItem.vue";
import getInstitutes from "@/hooks/getInstitutes"

export default defineComponent({
  name: "InstitutesList",
  components: {
    InstituteItem,
    ContentBlock
  },
  setup(){
    const {institutes} = getInstitutes();
    return {
      institutes,
    }
  },
})
</script>

<template>
  <content-block class="institutes-block">
    <institute-item v-for="institute in institutes" :institute="institute"/>
  </content-block>
</template>

<style scoped>
.institutes-block{
  /*max-width: 50em;*/
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  padding: 0.4em;
}
</style>