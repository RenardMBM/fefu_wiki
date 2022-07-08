<script lang="ts">
import {defineComponent} from "vue";
import EditRequestList from "@/components/EditRequests/EditRequestList.vue";
import getEditRequestsInstitutes from "@/hooks/requests/editRequests/getEditRequestsInstitutes";
import getEditRequestsTeacher from "@/hooks/requests/editRequests/getEditRequestsTeacher";
export default defineComponent({
  name: "EditRequestsView",
  components: {
    EditRequestList
  },
  setup(){
    const { editRequestsTeachers } = getEditRequestsTeacher() ;
    const { editRequestsInstitutes } = getEditRequestsInstitutes();
    console.log(editRequestsInstitutes.value)
    return {
      editRequestsTeachers,
      editRequestsInstitutes
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