<template>
  <div class="middle">
    <div class="productNav">
      <div class="ProductTitle">
        {{ productType.ChName }}
      </div>
      <div class="ProductBody">
        <ul>
          <li
            v-for="item in products"
            @click="selectProduct(item)"
            :key="item.id"
            :value="item.ChName"
            :class="{ active: product.ChName == item.ChName }"
          >
            {{ item.ChName }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters } from "vuex";

export default {
  name: "productNav",
  props: [],
  data() {
    return {
    };
  },
  computed: {
    ...mapState(["productType", "products", "product"]),
  },
  methods: {
      selectProduct(productObj){
          this.$store.commit("SelectProduct", productObj)
      }
  },
};
</script>

<style>
div.productNav {
  float: left;
  width: 280px;
  margin-right: 20px;
  margin-top: 10px;
  background-color: #ffffff;
}
div.chooseTy {
  height: 60px;
  line-height: 60px;
  font-size: 16px;
  font-weight: 800;
}
div.ProductTitle {
  background-color: #2d97db;
  height: 40px;
  line-height: 40px;
  padding-left: 20px;
  font-size: 19px;
  box-shadow: 0px 2px 3px #888888;
  font-weight: 800;
}
div.ProductBody ul {
  margin: 5px 0px;
}
div.ProductBody ul li {
  padding: 0px 0px;
  font-size: 14px;
  font-weight: 800;
}
div.ProductBody ul li:hover {
  cursor: pointer;
  color: orange;
  font-weight: 800;
}
li.active {
  font-weight: 800;
  color: orange;
}
</style>
