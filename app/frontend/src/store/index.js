import Vuex from 'vuex';
import Vue from 'vue';
import user from './modules/user';
import charity from './modules/charity';
import projects from './modules/projects';

// Connect Vue with Vuex
Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    user,
    charity,
    projects,
  }
});