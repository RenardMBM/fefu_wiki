<script lang="ts">
import {defineComponent} from "vue";
import store from "@/store";

export default defineComponent({
  name: "ScreenSize",
  data() {
    return{
      screenWidth: 0,
    }
  },
  created() {
    window.addEventListener('resize', this.updateWidth);
    this.updateWidth();
  },
  methods: {
    updateWidth() {
      this.screenWidth = window.innerWidth;
      if (!store.state.format.isMobile && this.screenWidth <= 800){
        store.commit("mobileFormat", {
          isMobile: true
        })
      }
      else if (store.state.format.isMobile && this.screenWidth > 800) {
        store.commit("mobileFormat", {
          isMobile: false
        })
      }
    }
  }
})
</script>

<style scoped>

</style>