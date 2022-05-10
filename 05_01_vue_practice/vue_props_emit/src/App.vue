<template>
  <div id="app">
    <h1>This is App</h1>
    <p>Appdata {{ appData }}</p>
    <input v-model="appData" type="text">

    <p>ParentData: {{ parentData }}</p>
    <p>ChildData: {{ childData }}</p>
    <!-- 자식에게 데이터 넘김 -->
    <!-- :넘기는이름="넘길값" -->
    <MyParent :appData="appData" @parent-input="inputParent" @child-input="inputChild"/>
  </div>
</template>

<script>
import MyParent from './components/MyParent.vue'

export default {
  name: 'App',
  data: function () {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  },
  methods: {
    inputParent: function(data) {
      this.parentData = data
    },
    inputChild: function(data) {
      this.childData = data
    }
  },
  components: {
    MyParent,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
