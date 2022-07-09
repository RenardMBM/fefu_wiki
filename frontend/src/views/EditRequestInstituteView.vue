<script lang="ts">
import {defineComponent, ref} from "vue";
import ErrorView from "@/views/ErrorView.vue";
import getModifiedInstituteData from "@/hooks/requests/editRequests/getModifiedInstituteData";
import {useRoute} from "vue-router";
import getInstituteData from "@/hooks/requests/institutes/getInstituteData";
import BaseEditRequest from "@/components/EditRequests/BaseEditRequest.vue";

export default defineComponent({
  name: "EditRequestInstituteView",
  components:{
    ErrorView,
    BaseEditRequest
  },
  setup(){
    const route = useRoute();
    const requestId = ref<number>(Number(route.params.requestId as string));
    const typeRequest = ref<string>("university")
    if (requestId) {
      const { modifiedInstitute } = getModifiedInstituteData(requestId.value);
      console.log(modifiedInstitute.value)
      const { institute } = getInstituteData(modifiedInstitute.value.post_id);
      console.log(modifiedInstitute.value, institute.value)
      return { requestId, modifiedInstitute, institute, typeRequest};
    }
    const modifiedInstitute = ref(undefined);
    const institute = ref(undefined);
    return { requestId, modifiedInstitute, institute, typeRequest};
  }
})
</script>

<template>
  <error-view v-if="isNaN(requestId) || modifiedInstitute === undefined || institute === undefined"></error-view>
  <base-edit-request v-else :post="institute" :modified-post="modifiedInstitute" :type-request="typeRequest"/>
</template>

<style scoped>

</style>