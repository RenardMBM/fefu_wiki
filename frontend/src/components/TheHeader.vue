<script lang="ts">
import {defineComponent, ref} from "vue"
import BaseButton from "@/components/UI/BaseButton.vue";
import BaseInput from "@/components/UI/BaseInput.vue";
import SearchPostLine from "@/components/SearchPostLine.vue";
import store from "@/store"

export default defineComponent({
  name: "TheHeader",
  components: {
    BaseInput,
    BaseButton,
    SearchPostLine
  },
  computed: {
    accountName(){
      if (store.state.user.isAuth){
         return  store.state.user.account
      }
      else{
         return  'Вы не представились системе';
      }
    }
  }
})
</script>

<template>
  <div class="header-block">
    <div class="right-header">
      <div class="account-block">
        <div style="margin-right: 0.5em" class="account">
          <i class="bi bi-person-circle"></i>&nbsp;
          <div>{{accountName}}</div>
        </div>
        <base-button>Войти</base-button>
      </div>
      <search-post-line/>
    </div>
  </div>
</template>

<style scoped>
.header-block{
  margin-top: 0.5em;
  position: absolute;
  height: 7em;
  width: 100%;
  padding-left: 10em;
  top:0;
}
.right-header{
  margin-left: 1em;
  padding-right: 0.5em;
  position: absolute;
  right: 0;
  top: 0;
  /*display: flex;*/
}
.account-block{
  display: flex;
  align-items: center;
  right: 0;
  justify-content: flex-end;
}
@media only screen and (max-width : 800px){
  .account-block{
    font-size: small;
  }
  .header-block{
    padding-left: 0;
  }
}
.account{
  display: flex;
}
.account img{
  height: 20px;
  width: 20px;
  margin-right: 0.2em;
}
</style>