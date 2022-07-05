<script lang="ts">
import {defineComponent} from "vue"
import store from "@/store"
import NavButton from "@/components/UI/NavButton.vue";

export default defineComponent({
  name: "BaseNavbar",
  components: {NavButton},
  computed: {
    permission() {
      return store.state.user.permission
    }
  }
})
</script>

<template>
  <div class="navbar">
    <div style="cursor: pointer" @click="$router.push('/')"><img class="logo" src="@/assets/logo.png" alt="FEFU wiki"></div>
    <div class="navbar__btns">
      <nav-button style="border-top: 1px solid #bdbdbd;" @click="$router.push('/institutes')">Институты и школы</nav-button>
      <nav-button  @click="$router.push('/teachers')">Наши преподаватели</nav-button>
      <div v-if="permission > 1" class="navbar__moder_btns">
        <nav-button @click="$router.push('/editRequests')">Заявки на модерацию</nav-button>
        <nav-button @click="">Создание преподавателя</nav-button>
        <nav-button @click="">Создание института</nav-button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.navbar{
  display: block;
  height: 100%;
  width: 10em;
  left: 0;
  top: 0;
  /*display: block!important;*/
  position: absolute;
  border-right: 1px solid #bdbdbd;
  /*padding-left: 0.5em;*/
}

.navbar__btns{
  display: flex;
  justify-content: center;
  align-content: center;
  align-items: center;
  flex-direction: column;
  /*width: 9em;*/
  width: 100%;
  font-size: 80%;
}
.navbar__moder_btns {
  display: flex;
  justify-content: center;
  align-content: center;
  align-items: center;
  flex-direction: column;
  /*width: 9em;*/
  width: 100%;
}

.logo{
  width: 100%;
  height: auto;
}

</style>