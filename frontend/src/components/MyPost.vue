<script lang="ts">
import { defineComponent, PropType, ref } from "vue";

import Post from "@/models/PostModel";

import PageTitle from "@/components/UI/PageTitle.vue";
import ContentBlock from "@/components/UI/ContentBlock.vue";
import ErrorView from "@/views/ErrorView.vue";
import InfoColumn from "@/components/InfoColumn.vue";
import MarkDown from "@/components/MarkDown.vue";
import MyDialog from "@/components/UI/MyDialog.vue";
import EditForm from "@/components/EditForm.vue";

import router from "@/router";
import sendEditData from "@/hooks/sendEditData";
import store from "@/store";

export default defineComponent({
  name: "MyPost",
  components: {
    MarkDown,
    PageTitle,
    ContentBlock,
    ErrorView,
    InfoColumn,
    MyDialog,
    EditForm
  },
  props: {
    id: {
      type: Number,
      required: true
    },
    post: {
      type: Object as PropType<Post | undefined>,
      required:true
    }
  },
  setup(){
    const editDialogVisible = ref(false);
    const status = ref<Number>(0)
    function cancelEdit(){
      editDialogVisible.value = false;
    }
    function sendEdit(text: string){
      sendEditData(`${router.currentRoute.value.fullPath}`, text);
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
  <error-view v-if="isNaN(id)"></error-view>
  <div v-else class="post">
    <div v-if="permission > 1" class="edit-block">
      <my-button @click="editDialogVisible=true">Edit</my-button>

      <my-dialog v-model:show="editDialogVisible">
        <edit-form :text="$props.post.text"
                   @send="sendEdit" @cancel="cancelEdit"
        />
      </my-dialog>
    </div>
    <div class="post-content">
      <div class="post-main-content">
        <page-title class="post-title">{{ post.title }}</page-title>
        <content-block>
          <mark-down :text="post.text"></mark-down>
        </content-block>
      </div>
      <info-column :data="post.info"></info-column>
    </div>
  </div>
</template>

<style scoped>
.post-content{
  display: flex;
  flex-wrap: wrap-reverse;
}

.post-main-content{
  width: 70%;
  padding-right: 5em;
}
.post-text{
  width: initial;
  margin-left: 0;
}
.post-title{
  margin-left: 0.5em;
}
.edit-block{
  height: min-content;
}
</style>