<template>
  <div class="card project-card">
      <div class="row plain-element project-card-top">
          <div class="col-xs-9 col-sm-9 col-md-9 plain-element text-left">
              <h6>{{ project.name|truncatechars(20) }}</h6>

          </div>
          <div class="col-xs-3 col-sm-3 col-md-3 plain-element text-right">
              <img :src="project.portrait" class="img responsive portrait plain-element">
          </div>
      </div>
      <br>
      <div class="row plain-element project-card-bottom">
          <div class="col-xs-10 col-sm-10 col-md-10 plain-element text-left">
              <p>{{ project.description|truncatechars(45) }}</p>
          </div>
          <div class="col-xs-2 col-sm-2 col-md-2 plain-element text-right">
              <router-link :to="{name: 'project-details', params: { id: project.id }}"
                      class="btn btn-success btn-card" type="submit">
                  <i class="fas fa-sign-in-alt"></i>
              </router-link>
          </div>
      </div>
  </div>
</template>


<script>

export default {
  name: "ProjectCardComponent",
  props: {
    project: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
    }
  },
  filters: {
      truncatechars (value, limit) {
          if (value.length > limit) {
              value = value.substring(0, limit) + "...";
          }
          return value
      }
  },
  methods: {
  },
  created() {
  }

}
</script>