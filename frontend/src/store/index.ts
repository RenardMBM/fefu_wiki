import {createStore} from "vuex";
import User from "@/models/UserModel"
import AppFormat from "@/models/AppFormatModel";
import TopType from "@/models/TopTypeModel";
export interface State {
  user: User,
  format: AppFormat,
  typesOfTops: Array<TopType>
}

export default createStore<State>({
  state: {
    user: {
      isAuth: false,
      permission:2,
      account:""
    },
    format: {
      isMobile: false,
    },
    typesOfTops:[
      {
        id: 0,
        title: "Ближайшие дни рожедения",
        request_url: "birthday"
      },
      {
        id: 1,
        title: "Самые халявные",
        request_url: "easy"
      },
      {
        id: 2,
        title: "Самые строгие",
        request_url: "hard"
      }
    ]
  },
  mutations:{
    signIn(state: State, data: User){
      state.user.isAuth = (data.permission > 0);
      state.user.permission = data.permission;
      state.user.account = data.account;
    },
    mobileFormat(state:State, payload){
      state.format.isMobile = payload.isMobile;
    }
  },
  getters:{
    isAuth(state: State){
      return state.user.isAuth;
    },
    getTypesOfTops(state: State){
      return state.typesOfTops;
    }
  }
})