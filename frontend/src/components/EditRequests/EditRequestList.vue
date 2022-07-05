<script lang="ts">
import {defineComponent, PropType} from "vue";
import EditRequestItem from "@/components/EditRequests/EditRequestItem.vue";
import ContentBlock from "@/components/Content/ContentBlock.vue";
import ShortPost from "@/models/ShortPostModel";

export default defineComponent({
  name: "EditRequestList",
  components: {
    EditRequestItem,
    ContentBlock
  },
  props:{
    editRequests:{
      type: Object as PropType<Array<ShortPost>>,
      default: []
    },
    typeRequest:{
      type: String,
      required: true
    },
    title:{
      type: String,
      required: true
    }
  }
})
</script>

<template>
  <content-block class="edit-requests-block">
    <div class="edit-requests-title">
      {{title}}
    </div>
    <div class="edit-requests-list" v-if="editRequests.length > 0">
      <edit-request-item class="top-list-item"
                         v-for="editRequest in editRequests"
                         :edit-request="editRequest"
                         :type-request="typeRequest"
      />
    </div>
    <div class="edit-requests-list" v-else >
      Список пуст
    </div>
  </content-block>
</template>

<style scoped>

</style>