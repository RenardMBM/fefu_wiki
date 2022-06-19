<script lang="ts">
import {defineComponent} from "vue"
export default defineComponent({
  name: 'my-input',
  props: {
    modelValue: String
  },
  methods: {
    updateInput(event: any) {
      // console.log(event.target.value);
      this.$emit('update:modelValue', event.target.value)
    }
  }
})
</script>

<template>
  <input :value="modelValue" @input="updateInput" class="input" type="text">
</template>

<style scoped>
.input {
  width: 100%;
  border: 1px solid teal;
  padding: 10px 15px;
  /*margin-top: 15px;*/
}

</style>
