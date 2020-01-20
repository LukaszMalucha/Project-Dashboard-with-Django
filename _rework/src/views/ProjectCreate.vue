<template>
<div v-if="requestUser != 'undefined'" class="row plain-element">
  <div class="row header details-header">
      <div class="col-md-2 text-right plain-element img-column">
          <img src="@/assets/img/propose-project.jpg" class="img responsive img-header">
      </div>
      <div class="col-md-8 text-left">
          <div class="box">
              <h5>Propose Project </h5>
          </div>
          <p>
            You can always create a new project from a template or another project. But if you need to start fresh,
            you can create a blank project by filling the form below. After your project is approved,
            you’ll be able to launch it and start gathering your team. After completing a project,
            Completion Reward will be distributed among team members.
          </p>
      </div>
  </div>
  <div class="dashboard-cards">
    <div class="row row-cards">
        <div class="col-md-5 no-padding">
            <div class="card insights-card">
                <div class="card-header">
                    <img src="@/assets/img/icons/gear.png" class="img-responsive">
                    <p><b> Propose Project </b></p>
                </div>
                 <form @submit.prevent="onSubmit" class="form-content form-wide" enctype="multipart/form-data">
                      <fieldset class="form-box">
                          <div id="formError" class="row row-error text-center">
                          {{ error }}
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Name:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input v-model="projectName" name="Name" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Description:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input v-model="projectDescription" name="Description" class="form-control"/>
                            </div>
                          </div>
                          <div class="row plain-element">
                            <div class="input-field col s4 text-right">
                                <h6>Project Schedule:</h6>
                            </div>
                            <div class="input-field col s8">
                                <input type="file" id="file" ref="file"
                                    v-on:change="handleFileUpload()"
                                      class="form-control file_input"  accept=".jpg,.png">
                            </div>
                          </div>
                          <div class="row"></div>
                          <button type="submit" class="btn-proceed"><span>Propose Project <i
                                  class="far fa-arrow-alt-circle-right"></i></span>
                          </button>
                      </fieldset>
                 </form>
            </div>
        </div>
    </div>
  </div>
</div>
<div v-else class="row plain-element">
    <NoPermissionComponent/>
</div>
</template>



<script>
import axios from 'axios'
import { CSRF_TOKEN } from "@/common/csrf_token.js"
import router from "@/router.js"
import NoPermissionComponent from "@/components/NoPermissionComponent.vue"

export default {
  name: 'project-create',
  components: {
    NoPermissionComponent
  },
  data() {
    return {
      error: "",
      requestUser: "",
      projectName: null,
      projectDescription: null,
      projectSchedule: null,
    }
  },
   methods: {
    setRequestUser() {
        this.requestUser = window.localStorage.getItem("email");
    },
    handleFileUpload() {
      this.projectSchedule = this.$refs.file.files[0];
    },
    onSubmit() {
      if (!this.projectName || !this.projectDescription || !this.projectSchedule) {
        this.error = "Fields can't be empty";
      } else {
        let formData = new FormData();
        formData.append("name", this.projectName);
        formData.append("description", this.projectDescription);
        formData.append("image_schedule", this.projectSchedule)
        axios.post('/api/projects/projects/', formData,
        { headers: { 'Content-Type': undefined,'X-CSRFTOKEN': CSRF_TOKEN} } )
          .then(response => {
            window.console.log(response);
            router.push({
              name: 'home',
            })
          })
          .catch(error => {
            window.console.log(error);
            document.getElementById("formError").textContent = error.response.data.non_field_errors[0]
          })
        }
    }
    
    
    
  },  
  created() {
    this.setRequestUser();
    document.title = "Start New Project";
  }
}
</script>