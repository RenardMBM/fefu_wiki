<script lang="ts">
import {defineComponent, PropType, ref} from "vue";
import useCompiledMarkdown from "@/hooks/useCompiledMarkdown";
import MyButton from "@/components/UI/MyButton.vue";
import ContentBlock from "@/components/UI/ContentBlock.vue";
import MyPost from "@/components/Post/MyPost.vue";
import Post from "@/models/PostModel";
import Info from "@/models/InfoModel";

export default defineComponent({
  name: "EditForm",
  components: {
    MyButton,
    ContentBlock,
    MyPost
  },
  props: {
    post: {
      type: Object as PropType<Post>,
      required: true
    },
    edit:{
      type: Boolean,
      required: false,
      default: true
    }
  },
  setup(props){
    const {postMarkdown, compiledMarkdown} = useCompiledMarkdown(props.post.text)
    const title = ref<String>(props.post.title)
    const isEditMode = ref<Boolean>(props.edit);
    const post_info = ref<Info>(props.post.info)
    return {
      postMarkdown,
      compiledMarkdown,
      isEditMode,
      title,
      post_info
    }
  }
})
</script>

<template>
  <div class="edit-form">
    <div v-if="isEditMode" class="edit-form-block">
      <textarea v-model="postMarkdown"></textarea>
    </div>
    <div v-else class="preview-form-block">
      <my-post
          :id="$props.post.id"
          :post="{
            id: $props.post.id,
            title: title,
            text: postMarkdown,
            info: post_info
             }"
      >
      </my-post>
<!--      <page-title>-->
<!--        {{title}}-->
<!--      </page-title>-->
<!--      <content-block>-->
<!--        <div v-html="compiledMarkdown"></div>-->
<!--      </content-block>-->
    </div>
    <my-button @click="isEditMode= !isEditMode">
      режим ред {{isEditMode}}
    </my-button>

    <div class="edit-btns">
      <my-button @click="$emit('send', postMarkdown)">Внести изменения</my-button>
      <my-button @click="$emit('cancel')">Отменить изменения</my-button>
    </div>
  </div>
</template>
<style scoped>
.edit-form{
  /*height: 100%;*/
}
.edit-btns{
  display: flex;
}
</style>