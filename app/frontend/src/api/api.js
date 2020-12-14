import { apiService } from "@/common/api.service.js";
import axios from 'axios';
import { CSRF_TOKEN } from "@/common/csrf_token.js"

export default {
  userInfo() {
    let endpoint = "/auth/current-user/";
    return apiService(endpoint);
  },
  charityData() {
    let endpoint = "charity/charities/";
    return apiService(endpoint);
  },
  deleteCharity(charity) {
    let endpoint = `/charity/charities/${charity.id}/`;
    return apiService(endpoint, "DELETE");
  },
  createCharity(payload) {
    const formData = new FormData();
    formData.append("name", payload.charityName);
    formData.append("description", payload.charityDescription);
    formData.append("image", payload.charityImage)

    return axios.post("charity/charities/", formData,
      { headers: { 'Content-Type': undefined,'X-CSRFTOKEN': CSRF_TOKEN} }
    )
  },
  projectData() {
    let endpoint = "/api/projects/projects/";
    return apiService(endpoint);
  },
  deleteProject(project) {
    let endpoint = `/api/projects/projects/${project}/`;
    return apiService(endpoint, "DELETE");
  },
  createProject(payload) {
    const formData = new FormData();
    formData.append("name", payload.projectName);
    formData.append("description", payload.projectDescription);
    formData.append("image_schedule", payload.projectSchedule);

    return axios.post("/api/projects/projects/", formData,
      { headers: { 'Content-Type': undefined,'X-CSRFTOKEN': CSRF_TOKEN} }
    )
  },
  projectDetails(project) {
    let endpoint = `/api/projects/projects/${project}/`;
    return apiService(endpoint);
  },
  advanceProject(project, phase) {
    let endpoint = `/api/projects/${project}/project-phase/`;
    return apiService(endpoint, "PATCH", {phase: phase});
  },
  completeProject(project) {
    let endpoint = `/api/projects/${project}/project-complete/`;
    return apiService(endpoint, "POST");
  },
  teamRequirements(project, html, css, js, db, python) {
    let endpoint = `/api/projects/${project}/team-requirements/`;
    return apiService(endpoint, "PUT", {html:html, css:css, js:js, db:db, python:python});
  },
  teamReject(project, member) {
    let endpoint = `/api/projects/${project}/team-reject/${member}/`;
    return apiService(endpoint, "DELETE");
  },
  teamJoin(project, member, committed_skill) {
    let endpoint = `/api/projects/${project}/team-join/`;
    return apiService(endpoint, "POST", {project: project, member: member, committed_skill: committed_skill});
  },
  reportIssue(project, name, description, cost) {
    let endpoint = `/api/projects/${project}/issue-create/`;
    return apiService(endpoint, "POST", {project: project, name: name, description: description, cost: cost});
  },
  issueCount() {
    let endpoint = "/api/projects/issue-count/";
    return apiService(endpoint);
  }


}
