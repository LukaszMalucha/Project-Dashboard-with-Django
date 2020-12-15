import api from "../../api/api.js"

const state = {
  token: window.localStorage.getItem('token'),
  username: window.localStorage.getItem('username'),
  position: window.localStorage.getItem('position'),
  error: null
};


const getters = {
// Check if token exists or not
  isLoggedIn: state => !!state.token || !!state.username,
  getUsername: state => state.username,
  getPosition: state => state.position,
  getToken: state => state.token,
  getError: state => state.error,
};


const actions = {
  async getUserInfo({ commit }) {
    const response = await api.userInfo();
    if (response["email"]) {
      const username = response["email"];
      const position = response["position"];
      commit('setUsername', username);
      commit('setPosition',  position);
      window.localStorage.setItem('username', username);
      window.localStorage.setItem('position', position);
    }
    else {
      commit('setUsername', null);
    }

  },
};


const mutations = {
// Update user
  setUsername: (state, username) => {
    state.username = username
  },
  setPosition: (state, position) => {
    state.position = position
  },
  setError: (state, error) => {
    state.error = error
  }

};


export default {
  state,
  getters,
  actions,
  mutations
}