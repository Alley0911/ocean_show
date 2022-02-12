import Vue from 'vue'
import Vuex from 'vuex'
// import data from '../src/assets/data/data.json'
import axios from "axios"

Vue.use(Vuex)

function getData(){
  let p = new Promise((resolve, reject) =>{
    axios.get("http://10.28.16.192/products/config_ini/data.json").then(
      response => {
        resolve(response.data) 
      },
      error => {
        reject(error)
      }
  )
  })
  return p
}

// 数据初始化
var selectors = [
  {
    id: '001',
    ChName: "起报时间",
    EnName: "iniTime",
    selectorWidth: "140px"
  },
  {
    id: '002',
    ChName: "预报时效",
    EnName: "leadTime",
    selectorWidth: "65px"
  },
  {
    id: '003',
    ChName: "层次",
    EnName: "level",
    selectorWidth: "120px"
  }
]

export default new Vuex.Store({
  state: {
    selectors,
    productTypes : null,
    productType : null,
    products : null,
    product : null,
    iniTime : null,
    leadTime : null,
    level : null,
  },

  mutations: {
    SelectProductType(state, productTypeObj) {
      state.productType = productTypeObj
      state.products = state.productType.products,
        state.product = state.products[0]
      state.iniTime = state.products[0].iniTimes[0]
      state.leadTime = state.products[0].leadTimes[0]
      state.level = state.products[0].levels[0]
    },
    SelectProduct(state, productObj) {
      state.product = productObj

      // 如果更换产品后，新产品没有对应的iniTime等，会自动设为索引为0的值
      if (!state.product.iniTimes.includes(state.iniTime)) {
        state.iniTime = state.product.iniTimes[0]
      }
      if (!state.product.leadTimes.includes(state.leadTime)) {
        state.leadTime = state.product.leadTimes[0]
      }
      if (!state.product.levels.includes(state.level)) {
        state.level = state.product.levels[0]
      }
    },
    ChangeSelector(state, optionsObj) {
      state[optionsObj.selectorName] = optionsObj.newValue
    },
    InitialData(state, data) {
      console.log(data)
      state.productTypes = data;
      state.productType = data[0];
      state.products = data[0].products;
      state.product = data[0].products[0];
      state.iniTime = data[0].products[0].iniTimes[0];
      state.leadTime = data[0].products[0].leadTimes[0];
      state.level = data[0].products[0].levels[0];
    }
  },

  actions: {
    async initialData(context) {
      let res = await getData();
      console.log(res)
      context.commit("InitialData", res);
    },
  }
})