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
      permission: 0, //TODO: =1
      email: ""
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
        request_url: "easy__rate"
      },
      {
        id: 2,
        title: "Самые строгие",
        request_url: "-easy__rate"
      }
    ]
  },
  mutations:{
    signIn(state: State, data: User){
      state.user.permission = data.permission;
      state.user.email = data.email;
    },
    mobileFormat(state:State, payload){
      state.format.isMobile = payload.isMobile;
    }
  },
  getters:{
    getTypesOfTops(state: State){
      return state.typesOfTops;
    }
  }
})