import Vue from 'vue'
import Router from 'vue-router'
import Hello from '../components/HelloWorld'
import Template from '../components/Template'

Vue.use(Router)
Vue.config.silent = true

export default new Router({
  routes: [
    {
      path: '/',
      name: '',
      component: Hello
    },
    {
      path: '/template',
      name: 'Template',
      component: Template
    }
  ]
})