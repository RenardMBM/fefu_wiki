<script lang="ts">
import {defineComponent} from "vue"
export default defineComponent({
  name: 'my-input',
  props: {
    modelValue: String
  },
  methods: {
    updateInput(event: any) {
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
  display: block;
  width: 100%;
  height: calc(2.25rem + 2px);
  padding: 0.375rem 0.75rem;
  padding-right: 33px;
  font-family: inherit;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #212529;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #bdbdbd;
  border-radius: 0.25rem;
}
</style>
