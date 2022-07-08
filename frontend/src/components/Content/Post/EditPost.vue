<script lang="ts">
import {defineComponent, PropType, ref} from "vue";
import BaseButton from "@/components/UI/BaseButton.vue";
import BaseDialog from "@/components/UI/BaseDialog.vue";
import EditForm from "@/components/Content/Post/EditForm.vue";
import Post from "@/models/PostModel";
import store from "@/store";

export default defineComponent({
  name: "EditPost",
  emits:[
    "send",
  ],
  components: {
    BaseButton,
    BaseDialog,
    EditForm
  },
  props:{
    post:{
      type: Object as PropType<Post>,
      required: true
    },
    is_column:{
      type: Boolean,
      required: false,
      default: true
    }
  },
  setup(props, {emit}){
    const editDialogVisible = ref(false);
    const status = ref<Number>(0)
    function cancelEdit(){
      editDialogVisible.value = false;
    }
    function sendEdit(post: Post){
      cancelEdit();
      emit('send', post)
      // sendEditData(`${router.currentRoute.value.fullPath}`, post);
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
      <edit-form :post="$props.post" :is_column="is_column"
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