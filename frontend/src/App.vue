<template>
  <!-- <BaseHeader /> -->
  <!-- with a fallback: -->
  <Suspense>
    <template #default>
      <div>
        <BaseHeader />
        <Main />
      </div>
    </template>
    <template #fallback>
      <span>Loading...</span>
    </template>
  </Suspense>
</template>

<script setup>
import Main from "./components/Main.vue";
import BaseHeader from "./components/layouts/BaseHeader.vue";
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.el-menu{
  font-size: 25px;
  background-color: #41b8c0;
  color: white;
}
.el-menu-item {
  color: white !important;
  font-size: 20px;
}
.main {
   padding: 1rem;
}
.filters {
  /* display: flex;
  justify-content: space-between; */
  margin-top: 50px;
  border-top: 2px solid rgb(207, 207, 207);
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  border-left: 1px solid rgb(207, 207, 207);
  border-right: 1px solid rgb(207, 207, 207);
  max-width: 1700px;
  margin: auto;
  margin-top: 50px;
  margin-bottom: 50px;
}
.spaces {
  margin-left: 10px;
}
.filter-wrapper {
  margin-bottom: 10px;
}
.el-input__suffix {
top: 9px;
}

.el-select {
  margin-right: 10px;
}
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td,
th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

th {
  background-color: #dddddd;
}

input[type="text"],
select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 25px;
}
</style>
