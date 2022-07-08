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
    const request_id = ref<number>(Number(route.params.requestId as string));
    if (request_id) {
      const { modifiedInstitute } = getModifiedInstituteData(request_id.value);
      const { institute } = getInstituteData(modifiedInstitute.value.id);

      return { request_id, modifiedInstitute, institute};
    }
    const modifiedInstitute = ref(undefined);
    const institute = ref(undefined);

    return { request_id, modifiedInstitute, institute};
  }
})
</script>

<template>
  <error-view v-if="isNaN(request_id) || modifiedInstitute === undefined || institute === undefined"></error-view>
  <base-edit-request v-else :post="institute" :modified-post="modifiedInstitute"/>
</template>

<style scoped>

</style>