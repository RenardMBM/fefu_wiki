<script lang="ts">
import {defineComponent} from "vue"
import store from "@/store"
import NavButton from "@/components/UI/NavButton.vue";

export default defineComponent({
  name: "Navbar",
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
      <nav-button v-if="permission > 1" @click="">Заявки на модерацию</nav-button>
    </div>
  </div>
  <div class="dropdown">
    <button onclick="showNavbar()" class="drop-btn"><i class="bi bi-chevron-compact-right"></i></button>
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
@media only screen and (max-width : 800px){
.dropdown{
    display: inline-block !important;
}
.navbar{
   position: fixed;
   background-color: white;
   display: inline-block !important;
   left: -162px;
   transition: left 0.3s;
}
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

.logo{
  width: 100%;
  height: auto;
}

.drop-btn {
    padding: 20px 0 20px 0;
    background: none;
    color: black;
    font-size: 16px;
    border: none;
    cursor: pointer;
}
.dropdown {
    margin-top: calc(50vh - 7em - 20px);
    left: 0;
    transition: left 0.3s;
    position: fixed;
    display: none;
    transform:rotate(0deg);
}

</style>