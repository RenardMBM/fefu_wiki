<script lang="ts">
import {defineComponent, PropType, ref} from "vue";

import BaseButton from "@/components/UI/BaseButton.vue";
import ContentBlock from "@/components/Content/ContentBlock.vue";
import BaseTitle from "@/components/Content/BaseTitle.vue";
import BaseInput from "@/components/UI/BaseInput.vue";

import Login from "@/models/LoginModel";

export default defineComponent({
  name: "LoginForm",
  components: {
    BaseButton,
    ContentBlock,
    BaseTitle,
    BaseInput
  },
  props: {
    UserId: {
      type: Object as PropType<Login>,
      required: true
    },
  },
  setup() {
    const isRegistration = ref(false);
    return {isRegistration};
  }
})
</script>

<template>
  <div class="login-form">
    <div v-if="!isRegistration">
    <div class="email">
      Почта
      <base-input type="email"></base-input>
    </div>
    <br>
    <div class="password">
      Пароль
      <base-input type="password"></base-input>
    </div>
    <base-button style="margin-top: 10px; width: 100%">Войти</base-button>
    </div>
    <div v-else>
      <div class="email">
      Почта
      <base-input type="email"></base-input>
      </div>
      <br>
      <div class="password">
      Пароль
      <base-input type="password"></base-input>
        <br>
      Повторите пароль
      <base-input type="password"></base-input>
      </div>
    <base-button style="margin-top: 10px; width: 100%">Зарегистрироваться</base-button>
    </div>
    <button class="btn-reg" @click="isRegistration = !isRegistration" style="margin-top: 10px; width: 100%">{{ !isRegistration ? "Регистрация" : "Вход"}}</button>
  </div>
</template>

<style scoped>
.btn-reg {
  color: gray;
  background: none;
  cursor: pointer;
}
</style>