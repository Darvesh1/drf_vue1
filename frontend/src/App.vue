<template>
  <div id="app">

    <table class="table">
      <thead>
            <th>Name</th>
            <th>Course</th>
            <th>Rating</th>
      </thead>
      <tbody>
      <tr>
            <td></td>
            <td></td>
            <td></td>
      </tr>
      </tbody>
    </table>

  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      msg: 'hello world!'
    }
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
