<template>
  <div>
    <!-- 顶部横幅 -->
    <Banner />
    <!-- 顶部产品类型导航 -->
    <Nav />
    <!-- 产品导航 -->
    <ProductNav/>
    <!-- 右侧内容区 -->
    <Exhibition/>
  </div>
</template>

<script>
// @ is an alias to /src
import Banner from "@/components/Banner.vue";
import Nav from "@/components/Nav/Nav.vue";
import Exhibition from "@/components/Exhibition/Exhibition.vue";
import ProductNav from "@/components/ProductNav.vue";

export default {
  name: "Home",
  components: {
    Banner,
    Nav,
    ProductNav,
    Exhibition,
  },
  beforeCreate() {
    this.$store.dispatch("initialData");
  },
};
</script>

<style scoped>
</style>