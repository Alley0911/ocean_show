<template>
  <div class="content">
      <Selector v-for="item in selectors" :selector="item" :key="item.id">
      </Selector>


    <div class="pic" style="overflow:hidden">
      <img id="result" :src="imgAdr" :onerror="defaultImg" />
    </div>
  </div>
</template>

<script>
import Selector from "@/components/Exhibition/Selector.vue";
import { mapState } from "vuex";
import errorImg from '@/assets/img/errorImg.png'

export default {
  name: "Exhibition",
  components: {
    Selector,
  },
  props: [],
  data() {
    return {
      imgAdr:null,
      defaultImg: 'this.src="' + errorImg + '"'
    };
  },
  computed: {
    ...mapState(["productType", "product", "selectors",'iniTime','leadTime','level']),
  },
  methods: {
    updateImg(){
      let tmp = 'http://10.28.16.192/products/'
      tmp += this.productType.EnName + "/"
      tmp += this.product.EnName + "/"
      tmp += this.iniTime + "/"
      this.imgAdr = tmp + this.product.EnName + "_" + this.level + "_" + this.iniTime + "_" + this.leadTime + ".png"
    },
  },
  mounted(){
    this.updateImg();
  },
  watch:{
    productType(oldValue, newValue){
      this.updateImg()
    },
    product(oldValue, newValue){
      this.updateImg()
    },
    iniTime(oldValue, newValue){
      this.updateImg()
    },
    leadTime(oldValue, newValue){
      this.updateImg()
    },
    level(oldValue, newValue){
      this.updateImg()
    },
  }

};
</script>

<style scoped>
div.content {
  float: left;
  width: 1050px;
  height: 700px;
  margin-top: 10px;
  background-color: #ffffff;
  /* border: 2px solid #eeeeee; */
}

div.selector{

  background-color: green;
}

div.pic{
  width: 900px;
  height: 600px;
  margin: 60px auto;
  border: 1px solid #f3f3f3;
  text-align: center;
}
img#result{
  /*width: 900px;*/
  max-width: 900px;
  height: 600px;
}
</style>
