<template>
  <div id="app">
    <img class="logo" src="./assets/logo.jpg">
    <router-view/>
  </div>
</template>

<script>
import 'element-ui/lib/theme-chalk/reset.css'

export default {
  name: 'app',
  components: {
  }
}
</script>

<style>
/* #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */

#app {
   font-family: 'Open Sans', Helvetica, Arial, sans-serif;
  font-size: 16px;
  margin-top: 60px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.card-item p {
  padding: .125rem;
  margin: .125rem;
}
.card-title {
  font-size: 1.25rem;
  color:rgb(94, 0, 152);
}
.card-description {
  font-size: 1.125rem;
}
header.main-title {
  color: #600198;
  font-weight: bold;
  font-size: 1.5rem;
  text-transform: uppercase;
}
img.logo {
  height: 200px;
  width: 200px;
  padding: 2rem;
  margin: 1rem;
  object-fit: cover;
  object-position: center;
}
.intro {
  font-weight: bold;
  padding: 1rem;
  text-align: justify;
}
.grid-container {
  align-items: flex-start;
  border: 1px solid #ccc;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-evenly;
  margin: 2rem 0rem;
  padding: 1rem;
}
.card-item {
  border: 1px solid #ccc;
  color: rgb(78, 78, 78);
  display: block;
  flex-grow: 1;
  height: 200px;
  margin-left: .1rem;
  margin-right: .1rem;
  margin-top: .75rem;
  max-width: 225px;
  overflow: hidden;
  overflow-wrap: break-word;
  padding: 1rem;
  text-align: left;
  width: 200px;
  margin-left: .25rem;
  margin-right: .25rem;
}
.card-item i {
  width: 30px;
}
.card-item:hover {
  background-color: rgb(236, 245, 255);
  border: 1px solid #3a8ee6;
  color: #000;
  cursor: pointer;
}
.card-item p {
  margin: 4px;
}
</style>
