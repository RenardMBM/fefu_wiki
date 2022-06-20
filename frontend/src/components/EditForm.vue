<script lang="ts">
import {defineComponent, ref} from "vue";
import useCompiledMarkdown from "@/hooks/useCompiledMarkdown";
import MyButton from "@/components/UI/MyButton.vue";

export default defineComponent({
  name: "EditForm",
  components: {MyButton},
  props: {
    text: {
      type: String,
      default: "#pass"
    },
    edit:{
      type: Boolean,
      required: false,
      default: false
    }
  },
  setup(props){
    const {postMarkdown, compiledMarkdown} = useCompiledMarkdown(props.text)
    const isEditMode = ref<Boolean>(props.edit);
    return {
      postMarkdown,
      compiledMarkdown,
      isEditMode
    }
  }
})
</script>

<template>
  <div class="edit-form">
    <textarea v-if="isEditMode" v-model="postMarkdown"></textarea>
    <div v-else v-html="compiledMarkdown"></div>
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