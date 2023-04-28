import Vue from 'vue'
import App from './App'
import axios from 'axios'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import router from './router'

Vue.use(ElementUI)

//全局配置
// axios.defaults.baseURL = 'http://127.0.0.1:5000/api';
axios.defaults.baseURL = '/api';
// 重构 console.log 函数
const log = console.log
console.log = function(){
  // 如果是线上环境
  if (process.env.NODE_ENV !== "production"){
    log(...arguments)
  }else{
    axios.defaults.baseURL = '/api';
  }

}
Vue.prototype.$axios = axios
Vue.config.productionTip = false


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
