<script lang="ts">
import {defineComponent, PropType, ref} from "vue";
import BaseButton from "@/components/UI/BaseButton.vue";
import BaseDialog from "@/components/UI/BaseDialog.vue";
import EditForm from "@/components/Content/Post/EditForm.vue";
import Post from "@/models/PostModel";
import sendEditData from "@/hooks/requests/sendEditData";
import router from "@/router";
import store from "@/store";

export default defineComponent({
  name: "EditPost",
  components: {
    BaseButton,
    BaseDialog,
    EditForm
  },
  props:{
    post:{
      type: Object as PropType<Post>,
      required: true
    }
  },
  setup(){
    const editDialogVisible = ref(false);
    const status = ref<Number>(0)
    function cancelEdit(){
      editDialogVisible.value = false;
    }
    function sendEdit(post: Post){
      sendEditData(`${router.currentRoute.value.fullPath}`, post);
      cancelEdit();
    }
    return{
      editDialogVisible,
      cancelEdit,
      sendEdit,
      status
    }
  },
  computed: {
    permission() {
      return (store.state.user.permission > 1);
    }
  },
})
</script>


<template>
  <div v-if="permission" class="edit-block" style="margin-bottom: 10px">
    <base-button @click="editDialogVisible=true">Изменить</base-button>
    <base-dialog v-model:show="editDialogVisible">
      <edit-form :post="$props.post"
                 @send="sendEdit" @cancel="cancelEdit"
      />
    </base-dialog>
  </div>
</template>

<style scoped>
.edit-block{
  height: min-content;
}
</style>