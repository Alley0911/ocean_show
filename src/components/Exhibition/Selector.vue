<template>
    <div class="selection">
      <div class="selecterName">{{selector.ChName}}:</div>
      <div class="selectBody">
        <select :style="'width:' + selector.selectorWidth" v-model="value">
          <option v-for="(item, index) in options" :key="index" :value="item">
            {{ item }}
          </option>
        </select>
      </div>
    </div>

</template>

<script>
export default {
  name: "Selector",
  props: ["selector"],
  data() {
    return {
      w: 40
    };
  },
  computed: {
    options(){
      return this.$store.state.product[this.selector.EnName + 's']
    },
    //v-model的值
    value:{
      get(){
        return this.$store.state[this.selector.EnName]
      },
      set(newValue){
        let optionsObj = {
          selectorName: this.selector.EnName,
          newValue: newValue
        }
        this.$store.commit("ChangeSelector", optionsObj)
      }
    }
  },
  methods: {},
};
</script>

<style scoped>
div.selection{
  float: left;
  height: 40px;
  line-height: 38px;
  font-size: 18px;
  border-radius: 4px;
}
div.selecterName {
  padding-left: 20px;
  float: left
}

div.selectBody {
  float: left
}

option {
  display: block;
  height: 30px;
  width: 30px;
  /* padding: 0px 10px */
}
select{
  padding: 2px 3px;
  border: 1px solid #2d97db;
  height: 39px;
  width: 65px;
  outline:none;
  font-size: 18px;
  border-radius: 4px;
}
</style>
