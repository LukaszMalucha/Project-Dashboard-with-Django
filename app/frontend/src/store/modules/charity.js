import api from "../../api/api.js";
import router from "../../router.js"

const state = {
    charityList: [],
    message: null
};

const getters = {
    getCharityList: state => state.charityList,
    getMessage: state => state.message,
};


const actions = {
    async fetchCharityList({ commit }) {
      const response = await api.charityData();
      commit("setCharityList", response.results)
    },
    async performCreateCharity({ dispatch }, payload) {
      await api.createCharity(payload);
      dispatch("fetchCharityList");
      router.push('/charity');
    },
    performDeleteCharity({ dispatch }, charity) {
      api.deleteCharity(charity);
      dispatch("fetchCharityList");
    }
};


const mutations = {
  setCharityList: (state, charityList) => {
    state.charityList = charityList
  },
  setMessage: (state, message) => {
    state.message = message
  }
};


export default {
  state,
  getters,
  actions,
  mutations
}