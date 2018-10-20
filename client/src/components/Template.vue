<template>
  <div class="template_model" style="position:relative">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Template',
  props: {
    widgets: [],
    widget_mapper: {},
    parent,
  },
  methods: {
    //loop through all the widgets and add them to the html
    renderAllWidgets(){
        for (let i=0;i<this.widgets.length;i++){
            this.renderWidget(this.widgets[i])
        }
    },
    // height: "300.00"
    // id: 1
    // image: null
    // left_position: "0.00"
    // text: ""
    // title: "Hello World!"
    // top_position: "0.00"
    // type: "Header"
    // width: "200.00"
    renderWidget(widget){
        let node = document.createElement(this.widget_mapper[widget['type']]['w_type'])
        node.style.position = "absolute"        
        node.style.display = "block"
        node.style.overflow = "hidden"
        node.style.top = `${widget['top_position']}px`
        node.style.left = `${widget['left_position']}px`
        // node.style.backgroundColor = "red"
        node.style.width = `${widget['width']}px`
        node.style.height = `${widget['height']}px`

        this.set_default(widget, node)
        this.parent.appendChild(node)
    },
    set_default(widget, node){
        if (node.tagName === "IMG"){
            node.src = widget['image']
        } else if (node.tagName === "P") {
            node.innerHTML = widget['text']
        } else if (node.tagName === "DIV") {
            node.innerHTML = `<img src=${widget['image']}></img>`
        }
    }
  },
  created() {
    //TODO: get a list of all the elements
  },
  mounted() {
    this.parent = document.getElementsByClassName('template_model')[0]
    axios.get('http://ramen.serveo.net/widgets').then((response) => {
        this.widgets = response.data
        this.widget_mapper = {
            'Header':{
                'w_type':'div'
            },
            'Image':{
                'w_type':'img'
            },
            'Text':{
                'w_type':'p'
            }
        }
        this.renderAllWidgets()
    })      
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
