<script lang="ts">
import {defineComponent, PropType, ref} from "vue";
import useCompiledMarkdown from "@/hooks/useCompiledMarkdown";
import MyButton from "@/components/UI/MyButton.vue";
import ContentBlock from "@/components/UI/ContentBlock.vue";
import MyPost from "@/components/Post/MyPost.vue";
import PageTitle from "@/components/UI/PageTitle.vue";
import MyInput from "@/components/UI/MyInput.vue";

import Post from "@/models/PostModel";
import Info from "@/models/InfoModel";

export default defineComponent({
  name: "EditForm",
  components: {
    MyButton,
    ContentBlock,
    MyPost,
    PageTitle,
    MyInput
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
    const post_info = ref<Info>({img: props.post.info.img, blocks: []});
    props.post.info.blocks.forEach(val => post_info.value.blocks.push(Object.assign({}, val)));

    function addRaw(){
      post_info.value.blocks.push({title: "", value: ""})
    }
    function removeRaw(event: any){
      const index: number = parseInt(event.target.id.match(/\d+/))
      if (index > -1) {
        post_info.value.blocks.splice(index, 1)
      }
    }
    return {
      postMarkdown,
      compiledMarkdown,
      isEditMode,
      title,
      post_info,
      addRaw,
      removeRaw
    }
  }
})
</script>

<template>
  <div class="edit-form">
    <div v-if="isEditMode" class="edit-form-block">
      <div class="edit-post-block">
        <page-title class="edit-post-title"><my-input v-model="title"></my-input></page-title>
        <textarea v-model="postMarkdown"></textarea>
      </div>
      <div class="edit-info-block">
        <div class="info-raw" v-for="(block, block_i) in post_info.blocks">
          <div class="info-raw-title"><my-input v-model="block.title"></my-input></div>
          <div class="info-raw-value"><my-input v-model="block.value"></my-input></div>
          <button class="info-raw-remove" :id="`info-raw-${block_i}`" @click="removeRaw">X</button>
        </div>
        <my-button class="info-raw-add" @click="addRaw">Добавить блок</my-button>
      </div>
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
    </div>
    <my-button @click="isEditMode= !isEditMode">
      режим ред {{isEditMode}}
    </my-button>

    <div class="edit-btns">
      <my-button @click="$emit('send', {
            id: $props.post.id,
            title: title,
            text: postMarkdown,
            info: post_info
             })">Внести изменения</my-button>
      <my-button @click="$emit('cancel')">Отменить изменения</my-button>
    </div>
  </div>
</template>
<style scoped>
.edit-post-title{
  margin-bottom: 0.5em;
}
.edit-form{
  /*height: 100%;*/
}
.edit-btns{
  display: flex;
}
</style>