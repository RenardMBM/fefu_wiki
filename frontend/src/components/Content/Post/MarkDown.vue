<script lang="ts">
import {defineComponent} from "vue";
import useCompiledMarkdown from "@/hooks/useCompiledMarkdown";
import BaseDialog from "@/components/UI/BaseDialog.vue";
import BaseButton from "@/components/UI/BaseButton.vue";

export default defineComponent({
  name: "MarkDown",
  components: {
    BaseButton,
    BaseDialog,
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