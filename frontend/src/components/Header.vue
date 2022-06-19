<script lang="ts">
import {defineComponent} from "vue"
import MyButton from "@/components/UI/MyButton.vue";
import MyInput from "@/components/UI/MyInput.vue";
import store from "@/store"

export default defineComponent({
  name: "my-header",
  components: {
    MyInput,
    MyButton,
  },
  data() {
    return {
      searchQuery: '',
      accountName: ''
    }
  },
  methods:{
    updateAccount(){
      if (store.state.user.isAuth){
        this.accountName = store.state.user.account
      }
      else{
        this.accountName = 'Вы не представились системе';
      }
    }
  },
  mounted() {
    this.updateAccount();
  }
})
</script>

<template>
  <div class="header-block">
    <div class="right-header">
      <div class="account-block">
        <div style="margin-right: 0.5em" class="account">
          <img src="https://img.icons8.com/fluency-systems-filled/344/guest-male.png" alt="">
          <div>{{accountName}}
          </div>
        </div>
        <my-button>Войти</my-button>
      </div>
      <div class="search-block">
        <my-input class="search-input"
          v-model="searchQuery"
          placeholder="Поиск...."
        />
        <my-button>Search</my-button>
      </div>
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
.account{
  display: flex;
}
.account img{
  height: 20px;
  width: 20px;
  margin-right: 0.2em;
}
.search-block{
  display: flex;
  margin-top: 0.5em;
  justify-content: flex-end
}
.search-block .search-input{
  margin-right: 0.5em;
}
</style>