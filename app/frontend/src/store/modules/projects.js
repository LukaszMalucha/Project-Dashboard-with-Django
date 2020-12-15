import api from "../../api/api.js";
import router from "../../router.js"


const state = {
    projectList: [],
    project: {},
    teamRequirements: null,
    teamComposition: null,
    teamMembership: null,
    projectMessages: null,
};

const getters = {
    getProjectList: state => state.projectList,
    getProject: state => state.project,
    getTeamRequirements: state => state.teamRequirements,
    getTeamComposition: state => state.teamComposition,
    getTeamMembership: state => state.teamMembership,
    getProjectMessages: state => state.projectMessages
};


const actions = {
    async fetchProjectList({ commit }) {
      const response = await api.projectData();
      if (!response)  {
          commit("setError", "Something went wrong. Try again later")
      }  else {
          commit("setProjectList", response.results)
      }
    },
    async performCreateProject({ commit, dispatch }, payload) {
      const response = await api.createProject(payload);
      if (!response)  {
          commit("setError", "Something went wrong. Try again later")
      }  else {
          dispatch("fetchProjectList");
          router.push('/');
      }
    },
    performDeleteProject({ dispatch, commit  }, project) {
      const response = api.deleteProject(project);
      if (!response)  {
        commit("setError", "Something went wrong. Try again later")
      }  else {
        dispatch("fetchProjectList");
        router.push('/');
      }
    },
    async fetchProjectDetails({ commit }, project) {
      const response = await api.projectDetails(project);
      if (!response)  {
        commit("setError", "Something went wrong. Try again later")
      }  else {
        commit("setProject", response);
        commit("setTeamRequirements", response.team_requirements);
        commit("setTeamComposition", response.project_team_composition);
        commit("setTeamMembership", response.team_membership);
        commit("setProjectMessages", response.project_messages);
        router.push('/');
      }
    },
    performAdvanceProject({commit}, payload) {
      const response = api.advanceProject(payload.project, payload.phase);
      if (!response)  {
        commit("setError", "Something went wrong. Try again later")
      }  else {
        commit("setMessage", "OK");
        router.push(`/projects/${payload.project}`);
      }
    },
    performCompleteProject({dispatch, commit }, project) {
      const response = api.completeProject(project);
      if (!response)  {
        commit("setError", "Something went wrong. Try again later")
      }  else {
        dispatch("fetchProjectList");
        router.push('/');
      }
    },
    defineTeamRequirements({commit}, payload){
      const response = api.teamRequirements(payload.project, payload.html, payload.css, payload.js, payload.db, payload.python);
      if (!response)  {
        commit("setError", "Something went wrong. Try again later")
      }  else {
        commit("setMessage", "OK");
        router.push(`/projects/${payload.project}`);
      }
    },
    performTeamReject({commit}, payload ) {
      const response = api.teamReject(payload.project, payload.member);
      if (!response)  {
        commit("setError", "Something went wrong. Try again later")
      }  else {
        commit("setMessage", "OK");
        router.push(`/projects/${payload.project}`);
      }
    },
    performTeamJoin({commit}, payload ) {
      const response = api.teamJoin(payload.project, payload.member, payload.committed_skill);
      if (!response)  {
        commit("setError", "Something went wrong. Try again later")
      }  else {
      commit("setMessage", "OK");
      router.push(`/projects/${payload.project}`);
      }
    },
};


const mutations = {
  setProjectList: (state, projectList) => {
    state.projectList = projectList
  },
  setProject: (state, project) => {
    state.project = project
  },
  setTeamRequirements: (state, teamRequirements) => {
    state.teamRequirements = teamRequirements
  },
  setTeamComposition: (state, teamComposition) => {
    state.teamComposition = teamComposition
  },
  setTeamMembership: (state, teamMembership) => {
    state.teamMembership = teamMembership
  },
  setProjectMessages: (state, projectMessages) => {
    state.projectMessages = projectMessages
  }
};



export default {
  state,
  getters,
  actions,
  mutations
}