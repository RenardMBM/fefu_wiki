<script lang="ts">
import {defineComponent, PropType, ref} from "vue";
import MyButton from "@/components/UI/MyButton.vue";
import MyDialog from "@/components/UI/MyDialog.vue";
import EditForm from "@/components/Post/EditForm.vue";
import Post from "@/models/PostModel";
import sendEditData from "@/hooks/sendEditData";
import router from "@/router";
import store from "@/store";

export default defineComponent({
  name: "EditPost",
  components: {
    MyButton,
    MyDialog,
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
      return store.state.user.permission
    }
  },
})
</script>


<template>
  <div v-if="permission > 1" class="edit-block">
    <my-button @click="editDialogVisible=true">Edit</my-button>
    <my-dialog v-model:show="editDialogVisible">
      <edit-form :post="$props.post"
                 @send="sendEdit" @cancel="cancelEdit"
      />
    </my-dialog>
  </div>
</template>

<style scoped>
.edit-block{
  height: min-content;
}
</style>