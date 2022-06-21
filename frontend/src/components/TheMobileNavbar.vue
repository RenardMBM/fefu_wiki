<script lang="ts">
import {defineComponent, ref} from "vue";
import BaseNavbar from "@/components/BaseNavbar.vue";
import BaseDialog from "@/components/UI/BaseDialog.vue";
import BaseButton from "@/components/UI/BaseButton.vue";
export default defineComponent({
  name: "TheMobileNavbar",
  components: {
    BaseNavbar,
    BaseDialog,
    BaseButton
  },
  setup(){
    const mobileNavbarVisible = ref(true);
    function switchMobileNavbarVisible() {
      mobileNavbarVisible.value = !mobileNavbarVisible.value;
    }
    return {
      mobileNavbarVisible,
      switchMobileNavbarVisible
    }
  }
})
</script>

<template>
      <base-navbar></base-navbar>
      <base-button @click="switchMobileNavbarVisible" style="position:absolute; left: 160px" class="drop-btn">
        <i class="bi bi-chevron-compact-right"/>
      </base-button>
</template>

<style scoped>

</style>