<script lang="ts">
import {defineComponent, PropType, ref} from "vue"
import BaseButton from "@/components/UI/BaseButton.vue";
import BaseInput from "@/components/UI/BaseInput.vue";
import SearchPostLine from "@/components/SearchPostLine.vue";
import store from "@/store"
import Post from "@/models/PostModel";
import BaseDialog from "@/components/UI/BaseDialog.vue";
import EditForm from "@/components/Content/Post/EditForm.vue";
import LoginForm from "@/components/Content/loginForm.vue";
import Login from "@/models/LoginModel";

export default defineComponent({
  name: "TheHeader",
  components: {
    BaseInput,
    BaseButton,
    SearchPostLine,
    BaseDialog,
    EditForm,
    LoginForm,
  },
  computed: {
    accountName(){
      if (store.state.user.permission > 0){
         return  store.state.user.email
      }
      else{
         return  'Вы не представились системе';
      }
    }
  },
  props: {
    UserId: {
      type: Object as PropType<Login>,
      default: "",
    }
  },
  setup(){
    const loginDialogVisible = ref(false);
    const status = ref<Number>(0)
    function cancelEdit(){
      loginDialogVisible.value = false;
    }
    return{
      loginDialogVisible: loginDialogVisible,
      cancelEdit,
      status
    }
  },
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
        <base-button @click="loginDialogVisible=true">Войти</base-button>
        <base-dialog v-model:show="loginDialogVisible">
          <login-form :UserId="$props.UserId"
                     @send="sendEdit" @cancel="cancelEdit"
          />
        </base-dialog>
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