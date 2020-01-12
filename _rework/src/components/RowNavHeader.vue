<template>
  <div class="row nav-header">
      <div class="row top-menu">
        <div class="col-sm-12 col-md-12 col-lg-12 plain-element">
          <ul>
            <li>
              <router-link :to="{name: 'home'}">Data Extraction</router-link>
            </li>
            <li>
              <router-link :to="{name: 'home'}">Course Statistics</router-link>
            </li>
            <li>
              <router-link :to="{name: 'home'}">Online Degrees</router-link>
            </li>
           <li>
              <router-link :to="{name: 'home'}">The Fastest Diploma</router-link>
            </li>
              <router-link :to="{name: 'home'}">The Fastest Bsc.</router-link>
          </ul>
        </div>
      </div>
    </div>
</template>

<script>
export default {
    name: "RowHeaderComponent"
}

</script>