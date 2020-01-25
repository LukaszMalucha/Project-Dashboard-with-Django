<template>
<div class="row plain-element">
  <div id="errorContainer">
    <div id="mainContainer">
      <div class="company"><img src="https://s3-eu-west-1.amazonaws.com/flask-static-files/static/img/logo.png" width="380" height="80"
                             alt="Creo Labs Logo"/></div>
      <br clear="all"/>

      <div class="robot"><img src="https://s3-eu-west-1.amazonaws.com/flask-static-files/static/img/robot500.png" width="300" height="350"
                              alt="Robot 404"/></div>

      <div class="error-header"><span class="largeFont">Oops!</span> The you don't have a permission to visit that page</div>
      <br clear="right"/>

      <div class="mainContent">
          <p class="p-error">HTTP 403 Error - If it shouldn't be the case, please contact the admin </p>

          <p class="p-error"><strong>You can also try:</strong></p>
          <ul class="ul-error">
              <li>&#8226; Visit the <a href="/">Homepage</a>
              </li>
              <li>&#8226; Make sure that the you are logged in</li>
              <li>&#8226; Go to <a href="javascript:history.go(-1);">previous</a> page
              </li>
          </ul>
      </div>
    </div>
  </div>
</div>
</template>

<script>

export default {
  name: "NoPermissionComponent",
}
</script>