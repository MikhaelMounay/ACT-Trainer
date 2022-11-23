<template>
  <div class="mobile-restricted" v-if="isMobile">
    <p>
      Please, could you give your <span class="fw-bold">PC/Laptop</span> a try
      ?<br />
      Our platform works alot better with it.
    </p>
    <button @click="isMobile = !isMobile">Proceed anyway</button>
  </div>
  <router-view v-if="!isMobile" :key="$route.params" />
</template>

<script>
export default {
  data() {
    return {
      isMobile: this.$isMobile(),
    };
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Bree+Serif&display=swap");

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  //   text-align: center;
  color: #2c3e50;
}

.mobile-restricted {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  font-size: 1.2rem;
  padding: 1.2rem;
  text-align: center;
  button {
    color: rgba(0, 0, 0, 0.65);
    background: none;
    border: none;
    text-decoration: underline;
    font-size: 0.95rem;
  }
}
</style>
