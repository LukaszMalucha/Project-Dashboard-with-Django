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
  }

}