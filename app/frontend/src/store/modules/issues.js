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
      const response = await api.reportIssue(payload.project, payload.name, payload.description, payload.cost);
      if (!response)  {
          commit("setError", "Something went wrong. Try again later")
      }  else {
          commit("setMessage", "OK");
          commit("setError", null);
          router.push(`/projects/${payload.project}`);
      }
    },
    async performIssueCount({ commit }) {
      const response = await api.issueCount()
      commit("setIssueCount", response.issue_count)
    },
    async performAssignIssue({ dispatch }, issue) {
      await api.assignIssue(issue)
      dispatch("fetchProjectDetails")

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