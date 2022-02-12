<template>
  <div class="nav">
    <div class="middle">
      <NavItem>
        <img src="@/assets/img/cloud.svg" />
      </NavItem>
      <NavItem 
      v-for="item in productTypes" 
      :productType="item" 
      :key='item.id'>
      </NavItem>
    </div>
  </div>
</template>

<script>
// import {updatePic, getIndexFromValue, pushRouter, changeByData} from 'assets/js/func.js'
import NavItem from "@/components/Nav/NavItem.vue";
import {mapState, mapGetters} from 'vuex'

// @ is an alias to /src
export default {
  name: "Nav",
  props: [],
  data() {
    return {
    };
  },
  components: {
    NavItem,
  },
  computed: {
    ...mapState(['productTypes'])
  },
  methods: {
    selectProductType() {
      console.log(this)
    },
  },
};
</script>

<style scoped>
div.nav {
  background-color: #2d97db;
  height: 40px;
  box-shadow: 0px 2px 3px #888888;
}
</style>
