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
  data() {
    return {
      navbarLeft: 0,
      buttonLeft: 0,
      btnR: 0,
    }
  },
  setup(){
    const mobileNavbarVisible = ref(false);
    function switchMobileNavbarVisible() {
      mobileNavbarVisible.value = !mobileNavbarVisible.value;
    }
    return {
      mobileNavbarVisible,
      switchMobileNavbarVisible,
    }
  },
  methods: {
    beforeEnter: function () {
      this.navbarLeft = -160;
      this.buttonLeft = 160;
      this.btnR = 180;
    },
    afterEnter: function () {
      this.navbarLeft = 0;
    },
    beforeLeave: function () {
      this.btnR = 0;
      this.buttonLeft  = 0;
    }
  }
})
</script>

<template>
      <transition name="fade"
                  v-on:before-enter="beforeEnter"
                  v-on:after-enter="afterEnter"
                  v-on:before-leave="beforeLeave">
        <base-navbar v-if="mobileNavbarVisible" v-bind:style="{left: navbarLeft + 'px'}" class="SwitchNavbar"></base-navbar>
      </transition>
      <button @click="switchMobileNavbarVisible" v-bind:style="{left: buttonLeft + 'px', transform: 'rotate(' + btnR + 'deg)'}" class="switchBtn">
        <i class="bi bi-chevron-compact-right"/>
      </button>
</template>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: 1s;
}
.fade-leave-to {
  transform: translateX(-160px);
}
.fade-enter-to, .fade-leave {
  transform: translateX(160px);
}
.switchBtn {
  position: fixed;
  margin-top: calc(50vh - 7em - 20px);
  transition: 1s;
  background: none;
}
.SwitchNavbar {
  background: white;
  position: fixed;
}
</style>