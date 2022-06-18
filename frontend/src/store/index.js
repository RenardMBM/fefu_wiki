import {createStore} from "vuex";

export default createStore({
  state: {
    isAuth: false,
    permission: 0,
    account: ""
  }
})