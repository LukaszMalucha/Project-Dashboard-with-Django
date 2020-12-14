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
      commit("setProjectList", response.results)
    },
    async performCreateProject({ commit }, payload) {
      await api.createProject(payload);
      commit("setMessage", "OK");
      router.push('/');
    },
    performDeleteProject({ commit }, project) {
      api.deleteProject(project);
      commit("setMessage", "OK");
      router.push('/');
    },
    async fetchProjectDetails({ commit }, project) {
      const response = await api.projectDetails(project);
      commit("setProject", response);
      commit("setTeamRequirements", response.team_requirements);
      commit("setTeamComposition", response.project_team_composition);
      commit("setTeamMembership", response.team_membership);
      commit("setProjectMessages", response.project_messages);
      window.console.log(response)
    },
    performAdvanceProject({commit}, payload) {
      api.advanceProject(payload.project, payload.phase);
      commit("setMessage", "OK");
      router.push(`/projects/${payload.project}`);
    },
    performCompleteProject({commit}, project) {
      api.completeProject(project);
      commit("setMessage", "OK");
      router.push('/');
    },
    defineTeamRequirements({commit}, payload){
      api.teamRequirements(payload.project, payload.html, payload.css, payload.js, payload.db, payload.python);
      commit("setMessage", "OK");
      router.push(`/projects/${payload.project}`);
    },
    performTeamReject({commit}, payload ) {
      api.teamReject(payload.project, payload.member)
      commit("setMessage", "OK");
      router.push(`/projects/${payload.project}`);
    },
    performTeamJoin({commit}, payload ) {
      api.teamJoin(payload.project, payload.member, payload.committed_skill)
      commit("setMessage", "OK");
      router.push(`/projects/${payload.project}`);
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