<script lang="ts">
import {defineComponent, PropType} from "vue";
import Info from "@/models/InfoModel";

export default defineComponent({
  name: "InfoColumn",
  props: {
    data: {
      type:Object as PropType<Info>,
      required: true
    }
  }
})
</script>

<template>
  <div class="info-column">
    <div class="info-img-block">
      <img class="info-img" :src="data.img" alt="post img :(">
    </div>
    <div class="info-raw" v-for="block in data.blocks">
      <div class="info-raw-title">{{ block.title }}</div>
      <div class="info-raw-value">{{ block.value }}</div>
    </div>
  </div>
</template>

<style scoped>
.info-column{
  display: flex;
  flex-direction: column;
  width: 300px;
}
.info-img-block{
  width: 100%;
  height: auto;
  text-align: center;
  border: 1px solid black;
}
.info-img{
  max-width: 100%;
  max-height: 100%;
}
.info-raw{
  display: flex;
  justify-content: space-between;
  border: 1px solid black;
  border-top: 0;
}
.info-raw-title{
  padding: 0.5em;
  border-right: 1px solid black;
  min-width: 100px;
  max-width: 100px;
  text-align: center;
}
.info-raw-value{
  padding: 0.5em;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  align-content: center;
}
</style>