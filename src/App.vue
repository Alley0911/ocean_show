<template>
  <div>
    <Home></Home>
  </div>
</template>

<script>
import Home from "@/views/Home.vue";
export default {
  name: "App",
  components: {
    Home,
  },
  created() {},
};
</script>

<style>
body {
  margin: 0px;
  padding: 0px;
  letter-spacing: 3px;
}
.middle {
  width: 1350px;
  margin: 0 auto;
}
</style>