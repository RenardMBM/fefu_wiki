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
  background-color: #F5F5F5;
}
.info-img-block{
  width: 100%;
  height: auto;
  text-align: center;
  border: 1px solid #bdbdbd;
}
.info-img{
  max-width: 90%;
  max-height: 90%;
  border-radius: 20%;
  margin: 5%;
}
.info-raw{
  display: flex;
  justify-content: space-between;
  border: 1px solid #bdbdbd;
  border-top: 0;
}
.info-raw-title{
  padding: 0.5em;
  border-right: 1px solid #bdbdbd;
  min-width: 100px;
  max-width: 100px;
  text-align: center;
  background-color: #D9D9D9;
  font-weight: bold;
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