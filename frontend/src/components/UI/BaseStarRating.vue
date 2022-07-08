<script lang="ts">
import {defineComponent, ref} from "vue"
import Dot from "@/components/UILogics/dot"

export default defineComponent({
  name: 'BaseStarRating',
  props: {
    rating: {
      type: Number,
      required: true,
    }
  },
  setup (props) {
    const ratingTmp = ref<number>(props.rating);
    const sizeStars = ref<number>(20);
    function dot(rating: number, size: number, num: number): Dot {
      return new Dot(rating, size, num);
    }
    return{
      dot,
      sizeStars,
      ratingTmp,
    }
  },
  directives: {
    "draw": function(canvasElement, binding) {
      // casting because custom directives accept an `Element` as the first parameter
      binding.value.draw(canvasElement as HTMLCanvasElement);
    }
  },
 })
</script>

<template>
  <div class="stars">
    <canvas v-draw="dot(ratingTmp, sizeStars, 1)" class="mask"
            @mouseover="ratingTmp = 1" @mouseleave="ratingTmp = rating"></canvas>
    <canvas v-draw="dot(ratingTmp, sizeStars, 2)" class="mask"
            @mouseover="ratingTmp = 2" @mouseleave="ratingTmp = rating"></canvas>
    <canvas v-draw="dot(ratingTmp, sizeStars, 3)" class="mask"
            @mouseover="ratingTmp = 3" @mouseleave="ratingTmp = rating"></canvas>
    <canvas v-draw="dot(ratingTmp, sizeStars, 4)" class="mask"
            @mouseover="ratingTmp = 4" @mouseleave="ratingTmp = rating"></canvas>
    <canvas v-draw="dot(ratingTmp, sizeStars, 5)" class="mask"
            @mouseover="ratingTmp = 5" @mouseleave="ratingTmp = rating"></canvas>
    <span class="ratingText">{{ rating }}</span>
  </div>
</template>

<style scoped>
.mask{
  mask-image: url("@/assets/star-svgrepo-com.svg");
  /*TODO: path to media */
}
.stars{
  display: flex;
  justify-content: center;
  align-items: center;
  align-content: center;
}
.ratingText{
  margin-right: 5px;
}
</style>
