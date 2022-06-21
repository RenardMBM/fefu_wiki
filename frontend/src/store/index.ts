import {createStore} from "vuex";
import User from "@/models/UserModel"
import AppFormat from "@/models/AppFormatModel";
export interface State {
  user: User,
  format: AppFormat
}

export default createStore<State>({
  state: {
    user: {
      isAuth:false,
      permission:2,
      account:""
    },
    format: {
      isMobile: false,
    }
  },
  mutations:{
    signIn(state: State, data: User){
      state.user.isAuth = (data.permission > 0);
      state.user.permission = data.permission;
      state.user.account = data.account;
    },
    mobileFormat(state:State, isMobile: boolean){
      state.format.isMobile = isMobile;
    }
  }
})