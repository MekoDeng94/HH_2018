<template>
  <div class="template_model">
    <button v-on:click=sendToBackend()>Upload a picture</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
  },
  methods: {
    //TODO: a method to upload a file and make api call to the backend (to run the machine learning process)
    sendToBackend() {

    }
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
