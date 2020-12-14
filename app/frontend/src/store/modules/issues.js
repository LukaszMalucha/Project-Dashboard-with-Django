import api from "../../api/api.js";
import router from "../../router.js"


const state = {
  issueCount: null,

};

const getters = {
  getIssueCount: state => state.issueCount,
};


const actions = {
    async performReportIssue({ commit }, payload) {
      await api.reportIssue(payload.project, payload.name, payload.description, payload.cost);
      commit("setMessage", "OK");
      router.push(`/projects/${payload.project}`);
    },
    async performIssueCount({ commit }) {
      const response = await api.issueCount()
      commit("setIssueCount", response.issue_count)
    }

};


const mutations = {
    setIssueCount: (state, issueCount) => {
      state.issueCount = issueCount
    },

};



export default {
  state,
  getters,
  actions,
  mutations
}