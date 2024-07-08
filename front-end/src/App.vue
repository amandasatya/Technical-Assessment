<template>
  <div id="app">
    <RatingsPage msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
import RatingsPage from "./components/RatingsPage.vue";

export default {
  name: "App",
  components: {
    RatingsPage,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  padding: 20px;
}
</style>
