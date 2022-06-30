<script lang="ts">
import {defineComponent, PropType, ref} from "vue";
import useCompiledMarkdown from "@/hooks/useCompiledMarkdown";
import BaseButton from "@/components/UI/BaseButton.vue";
import ContentBlock from "@/components/Content/ContentBlock.vue";
import BasePost from "@/components/Content/Post/BasePost.vue";
import BaseTitle from "@/components/Content/BaseTitle.vue";
import BaseInput from "@/components/UI/BaseInput.vue";

import Post from "@/models/PostModel";
import PostInfoColumnData from "@/models/PostInfoColumnModel";

export default defineComponent({
  name: "EditForm",
  components: {
    BaseButton,
    ContentBlock,
    BasePost,
    BaseTitle,
    BaseInput
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
    const post_info = ref<PostInfoColumnData>({img: props.post.info.img, blocks: []});
    props.post.info.blocks.forEach(val => post_info.value.blocks.push(Object.assign({}, val)));
    return {
      postMarkdown,
      compiledMarkdown,
      isEditMode,
      title,
      post_info,
    }
  }
})
</script>

<template>
  <div class="edit-form">
    <div v-if="isEditMode" class="edit-form-block">
      <div class="edit-post-block">
        <base-title class="edit-post-title"><base-input v-model="title"></base-input></base-title>
        <textarea v-model="postMarkdown"></textarea>
      </div>
      <div class="edit-info-block">
        <div class="info-raw" v-for="(block, block_i) in post_info.blocks" :key="block_i">
          <div class="info-raw-title">
            <content-block>{{block.title}}</content-block>
          </div>
          <div class="info-raw-value">
            <base-input v-model="block.text"></base-input>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="preview-form-block">
      <base-post
          :id="$props.post.id"
          :post="{
            id: $props.post.id,
            title: title,
            text: postMarkdown,
            info: post_info
             }"
      >
      </base-post>
    </div>
    <base-button @click="isEditMode= !isEditMode">
      режим ред {{isEditMode}}
    </base-button>

    <div class="edit-btns">
      <base-button @click="$emit('send', {
            id: $props.post.id,
            title: title,
            text: postMarkdown,
            info: post_info
             })">Внести изменения
      </base-button>
      <base-button @click="$emit('cancel')">Отменить изменения</base-button>
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