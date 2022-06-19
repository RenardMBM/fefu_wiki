<script lang="ts">
import {defineComponent, ref} from "vue";
import useCompiledMarkdown from "@/hooks/useCompiledMarkdown";
import sendEditData from "@/hooks/sendEditData";
import store from "@/store";
import MyDialog from "@/components/UI/MyDialog.vue";
import EditForm from "@/components/EditForm.vue";
import MyButton from "@/components/UI/MyButton.vue";
import {useRouter} from "vue-router";

export default defineComponent({
  name: "MarkDown",
  components: {
    MyButton,
    MyDialog,
    EditForm
  },
  props:{
    text: {
      type: String,
      required: true
    }
  },

  computed: {
    permission() {
      return store.state.user.permission
    },
    sendEdit(text: string){ // why is sent to open the page?
      // const router = useRouter();
      // sendEditData(`${router.currentRoute.value.fullPath}/edit`, text);
    }
  },
  setup(props) {
    const {postMarkdown, compiledMarkdown} = useCompiledMarkdown(props.text)
    const editDialogVisible = ref(false);
    function cancelEdit(){
      editDialogVisible.value = false;
    }

    return {
      compiledMarkdown,
      editDialogVisible,
      cancelEdit,
    }
  }
})
</script>

<template>
  <div v-if="permission > 1" class="edit-block">
    <my-button @click="editDialogVisible=true">Edit</my-button>
    <my-dialog v-model:show="editDialogVisible">
      <edit-form :text="$props.text"
                 @send="sendEdit" @cancel="cancelEdit"
      />
    </my-dialog>
  </div>

  <div v-html="compiledMarkdown"></div>
</template>

<style scoped>

</style>