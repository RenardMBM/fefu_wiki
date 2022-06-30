<script lang="ts">
import {defineComponent, PropType, ref} from "vue";
import BaseTitle from "@/components/Content/BaseTitle.vue";
import BasePost from "@/components/Content/Post/BasePost.vue";
import Post from "@/models/PostModel";
import BaseButton from "@/components/UI/BaseButton.vue";
import BaseDialog from "@/components/UI/BaseDialog.vue";
import BaseAreaInput from "@/components/UI/BaseAreaInput.vue";
import sendSolution from "@/hooks/editRequests/sendSolution";
import {useRouter} from "vue-router";
import ModifiedPost from "@/models/ModifiedPostModel";
export default defineComponent({
  name: "BaseEditRequest",
  components:{
    BaseAreaInput,
    BaseButton,
    BaseTitle,
    BasePost,
    BaseDialog
  },
  props:{
    modifiedPost:{
      type: Object as PropType<ModifiedPost>,
      required: true
    },
    post:{
      type: Object as PropType<Post>,
      required: true
    }
  },
  setup(props){
    const router = useRouter();

    const post = ref(props.post);
    const modifiedPost = ref(props.modifiedPost);
    const isModifiedVisible = ref<boolean>(true);
    function changeVersion(){
      isModifiedVisible.value = !isModifiedVisible.value;
    }
    const cancelDialog = ref<boolean>(false);
    const reason = ref<string> ("");
    function acceptModification(){
      sendSolution(modifiedPost.value.post_id, true, "");
      router.push(`/editRequests/institute`)
    }
    function sendReason(){
      sendSolution(modifiedPost.value.post_id, false, reason.value);
      cancelDialog.value = false;
      router.push(`/editRequests/institute`)
    }
    return {
      post,
      modifiedPost,
      isModifiedVisible,
      changeVersion,
      acceptModification,
      cancelDialog,
      reason,
      sendReason
    }
  }
})
</script>

<template>
  <base-button @click="changeVersion">Меняем версию</base-button>
  <base-post v-if="isModifiedVisible" :id="modifiedPost.id" :post="modifiedPost"></base-post>
  <base-post v-else :id="post.id" :post="post"></base-post>

  <base-button @click="acceptModification">Принять</base-button>
  <base-button @click="cancelDialog=true">Отклонить</base-button>
  <base-dialog v-model:show="cancelDialog">
    <base-title>Причина отказа:</base-title>
    <base-area-input :v-model="reason"></base-area-input>
    <base-button @click="sendReason">Отправить</base-button>
  </base-dialog>
</template>

<style scoped>

</style>