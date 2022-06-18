<template>
  <div class="navbar">
    <div style="cursor: pointer" @click="$router.push('/')"><img class="logo" src="@/assets/logo.png" alt="FEFU wiki"></div>
    <div class="navbar__btns">
      <nav-button style="border-top: 1px solid;" @click="$router.push('/institutes')">Институты и школы</nav-button>
      <nav-button  @click="$router.push('/teachers')">Наши преподаватели</nav-button>
    </div>
  </div>
</template>

<script>
import NavButton from "@/components/UI/NavButton";
export default {
  name: "Navbar",
  components: {NavButton}
}
</script>

<style scoped>
.navbar{
  height: 100%;
  width: 10em;
  left: 0;
  top: 0;
  /*display: block!important;*/
  position: absolute;
  border-right: 1px solid black;
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

.logo{
  width: 100%;
  height: auto;
}
</style>