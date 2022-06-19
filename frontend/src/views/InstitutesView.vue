<script>
import {defineComponent} from "vue"

import PageTitle from "@/components/UI/PageTitle";
import InstitutesList from "@/components/InstitutesList";

export default defineComponent({
  name: "InstitutesView",
  components: {
    PageTitle,
    InstitutesList
  }
})
</script>

<template>
  <page-title>Институт и школы Лучшего университета</page-title>
  <institutes-list></institutes-list>
</template>

<style scoped>

</style>