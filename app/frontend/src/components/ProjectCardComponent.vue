<template>
  <div class="card project-card" :class="project.phase">
      <div class="row plain-element project-card-top">
          <div class="col s8 m8 l9 plain-element left-align">
              <h6>{{ project.name|truncatechars(20) }}</h6>

          </div>
          <div class="col s4 m4 l3 plain-element right-align">
              <img :src="project.portrait" class="img responsive portrait plain-element">
          </div>
      </div>
      <br>
      <div class="row plain-element project-card-bottom">
          <div class="col s8 m8 l9 plain-element left-align">
              <p>{{ project.description|truncatechars(52) }}</p>
          </div>
          <div class="col s4 m4 l3 plain-element right-align">
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