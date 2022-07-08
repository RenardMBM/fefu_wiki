<script lang="ts">
import {defineComponent, PropType} from "vue";
import PostInfoColumnData from "@/models/PostInfoColumnModel";
import BaseStarRating from "@/components/UI/BaseStarRating.vue";
import InstituteItem from "@/components/Institute/InstituteItem.vue";

export default defineComponent({
  name: "PostInfoColumn",
  components: {
    BaseStarRating,
    InstituteItem
  },
  props: {
    data: {
      type: Object as PropType<PostInfoColumnData>,
      required: true
    }
  },
})
</script>

<template>
  <div class="info-column">
    <div class="info-img-block">
      <img class="info-img" :src="data.img" alt="post img :(">
    </div>
    <div v-for="block in data.blocks">
      <div v-if="block.type==='date'" class="info-raw" >
        <div class="info-raw-title">{{ block.title }}</div>
        <div class="info-raw-value">{{ block.content }}</div>
      </div>
      <div v-else-if="block.type==='string'" class="info-raw" >
        <div class="info-raw-title">{{ block.title }}</div>
        <div class="info-raw-value">{{ block.content }}</div>
      </div>
      <div v-else-if="block.type==='rates'" >
        <div class="info-raw" v-for="rate in block.content">
          <div class="info-raw-title">{{ rate.title }} </div>
          <div class="info-raw-value">
            <BaseStarRating :rating="rate.rate"/>
          </div>
        </div>
      </div>
      <div v-else-if="block.type==='list_InstituteItem'">
        <div class="info-raw">
          <div class="info-raw-title"> {{ block.title }} </div>
          <div class="info-raw-value" style="display: flex; flex-direction: column;">
            <div v-for="institute in block.content" style="margin-bottom: 0.1em; margin-top: 0.1em">
              <institute-item :institute="institute"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.info-column{
  display: flex;
  flex-direction: column;
  width: 300px;
  background-color: #F5F5F5;
  height: fit-content;
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
  justify-content: center;
  display: flex;
  align-items: center;
  padding: 0.5em;
  border-right: 1px solid #bdbdbd;
  min-width: 120px;
  max-width: 120px;
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