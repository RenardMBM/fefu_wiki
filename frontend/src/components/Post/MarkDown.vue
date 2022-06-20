<script lang="ts">
import {defineComponent} from "vue";
import useCompiledMarkdown from "@/hooks/useCompiledMarkdown";
import MyDialog from "@/components/UI/MyDialog.vue";
import MyButton from "@/components/UI/MyButton.vue";

export default defineComponent({
  name: "MarkDown",
  components: {
    MyButton,
    MyDialog,
  },
  props:{
    text: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const {postMarkdown, compiledMarkdown} = useCompiledMarkdown(props.text)
    return {
      compiledMarkdown,
    }
  }
})
</script>

<template>
  <div v-html="compiledMarkdown"></div>
</template>

<style scoped>

</style>