import Vuex from 'vuex';
import Vue from 'vue';
import user from './modules/user';
import charity from './modules/charity';

// Connect Vue with Vuex
Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
    charity,
  }
});