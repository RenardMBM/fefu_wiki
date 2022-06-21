<script>
import {defineComponent} from "vue"

import BaseTitle from "@/components/Content/BaseTitle";
import InstitutesList from "@/components/Institute/InstitutesList";

export default defineComponent({
  name: "InstitutesView",
  components: {
    BaseTitle,
    InstitutesList
  }
})
</script>

<template>
  <base-title>Институт и школы Лучшего университета</base-title>
  <institutes-list></institutes-list>
</template>

<style scoped>

</style>