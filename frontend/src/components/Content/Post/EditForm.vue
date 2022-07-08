<script lang="ts">
import {defineComponent, PropType, ref} from "vue";
import useCompiledMarkdown from "@/hooks/useCompiledMarkdown";
import BaseButton from "@/components/UI/BaseButton.vue";
import ContentBlock from "@/components/Content/ContentBlock.vue";
import BasePost from "@/components/Content/Post/BasePost.vue";
import BaseTitle from "@/components/Content/BaseTitle.vue";
import BaseInput from "@/components/UI/BaseInput.vue";
import BaseDate from "@/components/UI/BaseDate.vue";

import Post from "@/models/PostModel";
import PostInfoColumnData from "@/models/PostInfoColumnModel";
import BaseAreaInput from "@/components/UI/BaseAreaInput.vue";

export default defineComponent({
  name: "EditForm",
  components: {
    BaseAreaInput,
    BaseButton,
    ContentBlock,
    BasePost,
    BaseTitle,
    BaseInput,
    BaseDate
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
    },
    is_colum:{
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
        <h1 class="edit-post-title" style="text-align: center">{{title}}</h1>
        <base-area-input v-model="postMarkdown" style="height: 75px"></base-area-input>
      </div>
      <div class="edit-info-block" v-if="is_colum">
        <div class="info-raw" v-for="(block, block_i) in post_info.blocks" :key="block_i">
          <div class="info-raw-title" v-if="block.type !== 'rates' && block.type !== 'list_InstituteItem'">
            <div style="margin: 15px 10px 2px 0">{{block.title}}</div>
          </div>
          <div class="info-raw-value" v-if="block.type !== 'rates' && block.type !== 'list_InstituteItem'">
            <base-input v-if="block.type === 'string'" v-model="block.content"/>
            <base-date v-else-if="block.type==='date'" v-model="block.content"/>
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
          :is_colum="is_colum"
      >
      </base-post>
    </div>
    <button class="btn-icon" @click="isEditMode= !isEditMode"><i v-if="isEditMode" class="bi bi-eye"></i>
      <i v-else class="bi bi-eye-slash"></i></button>
    <div class="edit-btns">
      <base-button @click="$emit('send', {
            id: $props.post.id,
            title: title,
            text: postMarkdown,
            info: post_info
             })" style="width: 50%; margin-right: 5px">Внести изменения
      </base-button>
      <base-button @click="$emit('cancel')" style="width: 50%; margin-left: 5px" >Отменить изменения</base-button>
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
.btn-icon {
  margin: 5px 5px 0 calc(50% - 15px);
  background: none;
  font-size: 30px;
}
</style>