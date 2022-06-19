import {createStore} from "vuex";
import User from "@/models/UserModel"

export interface State {
  user: User
}

export default createStore<State>({
  state: {
    user: {
      isAuth:false,
      permission:0,
      account:""
    }
  },
  mutations:{
    signIn(state: State, data: User){
      state.user.isAuth = (data.permission > 0);
      state.user.permission = data.permission;
      state.user.account = data.account
    }
  }
})