<template>
  <div class="navItem" 
  @click='selectProductType'>
    <ul>
      <li>
        <slot>{{ productType.ChName }}</slot>
      </li>
    </ul>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: "NavItem",
  props: ["productType"],
  data() {
    return {
    //   dataIndex: 100,
    };
  },

  methods: {
    selectProductType() {
      if(this.productType){
        this.$store.commit("SelectProductType", this.productType)
      }
    },      
  },
  mounted() {
    console.log("mounted")
  },
};
</script>

<style scoped>
ul {
  float: left;
  padding: 0px 0px 0px 0px;
  margin: 0 0;
  height: 40px;
  text-align: center;
}
ul li {
  /* positon，可使li展现在其他元素上面 */
  position: relative;
  list-style: none;
  height: 40px;
  line-height: 40px;
  font-size: 20px;
  line-height: 40px;
  height: 40px;
  list-style: none;
  padding: 0px 25px;
  font-weight: 700;
}
li:hover {
  color: white;
  text-decoration: none;
  cursor: pointer;
}
.active {
  cursor: pointer;
  color: white;
}
</style>
