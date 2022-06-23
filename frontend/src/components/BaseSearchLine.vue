<script lang="ts">
import {defineComponent, ref} from "vue";
import BaseInput from "@/components/UI/BaseInput.vue";

export default defineComponent({
  name: "BaseSearchLine",
  components: {
    BaseInput
  },
  emits:[
      "search"
  ],
  props: {
    content: {
      type: String,
      default: ""
    }
  },
  setup(props, {emit}) {
    const searchQuery = ref(props.content)
    function onSearch() {
      emit('search', searchQuery.value)
    }
    return {
      searchQuery,
      onSearch
    }
  }
})
</script>

<template>
  <div class="search-block">
    <base-input class="search-input"
                v-model="searchQuery"
                placeholder="Поиск...."
    />
    <button @click="onSearch" class="icon"><i class="bi bi-search"></i></button>
  </div>
</template>

<style scoped>
.search-block{
  display: flex;
  margin-top: 0.5em;
  justify-content: flex-end
}
.search-block .search-input{
  margin-right: 0.5em;
}
.search-block .icon{
  cursor: pointer;
  background: none;
  position: absolute;
  top: 50%;
  margin-right: 18px;
  margin-top: 13px;
  z-index: 1;
}
.search-block .icon:active{
  transform: translateY(1px);
}
</style>