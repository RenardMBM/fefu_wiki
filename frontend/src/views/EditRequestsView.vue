<script lang="ts">
import {defineComponent} from "vue";
import EditRequestList from "@/components/EditRequests/EditRequestList.vue";
export default defineComponent({
  name: "EditRequestsView",
  components: {
    EditRequestList
  },
  setup(){
    // const { editRequestsTeachers } = ;
    // const { editRequestsInstitutes } = ;
    return {
      // editRequestsTeachers,
      // editRequestsInstitutes
    }
  }
})
</script>

<template>
  <edit-request-list
      :title="`Заявки на преподавателей`"
      :type-request="`teacher`"
      :edit-requests="editRequestsTeachers" />
  <edit-request-list
      :title="`Заявки на институты`"
      :type-request="`institutes`"
      :edit-requests="editRequestsInstitutes" />
</template>

<style scoped>

</style>