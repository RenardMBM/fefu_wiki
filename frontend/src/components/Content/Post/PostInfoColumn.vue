<script lang="ts">
import {defineComponent, PropType, ref} from "vue";
import PostInfoColumnData from "@/models/PostInfoColumnModel";
import BaseStarRating from "@/components/UI/BaseStarRating.vue";

export default defineComponent({
  name: "PostInfoColumn",
  components: {
    BaseStarRating,
  },
  props: {
    data: {
      type: Object as PropType<PostInfoColumnData>,
      required: true
    }
  },
  setup() {
    const rating = ref<number>(3.73);
    return {
      rating,
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
      <div class="info-raw-value">{{ block.text }}</div>
    </div>
    <div class="info-raw">
      <div class="info-raw-title">Халявность</div>
      <div class="info-raw-value"><BaseStarRating :rating="rating"></BaseStarRating></div>
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