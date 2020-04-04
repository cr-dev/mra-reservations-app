<template>
  <div id="app">
    <img class="logo" src="./assets/logo.jpg">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Open Sans', Helvetica, Arial, sans-serif;
  font-size: 16px;
  margin-top: 60px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
img.logo {
  height: 250px;
  width: 250px;
  border: 1px solid #ccc;
  padding: 2rem;
  border-radius: 100%;
  margin: 1rem;
  object-fit: cover;
  object-position: center;
}

.intro {
  padding: 1rem;
  text-align: justify;
  font-weight: bold;
}
</style>
