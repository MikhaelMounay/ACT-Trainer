<template>
  <div class="passage-container p-3">
    <p class="fw-bold" v-if="TestType != 'MathTest'">
      Passage {{ PassageNumber }}
    </p>
    <p class="fw-bold" v-if="PassageTitle" v-html="PassageTitle"></p>
    <div v-html="PassageContent_data" class="passage-content"></div>
  </div>
</template>

<script>
import { MathJax, renderByMathjax } from "mathjax-vue3";
// import VueMathjax from "vue-mathjax-next";

export default {
  name: "PassageContainer",
  // components: { VueMathjax },
  // eslint-disable-next-line vue/no-unused-components
  components: { MathJax },
  props: [
    "PassageNumber",
    "PassageContent",
    "PassageTitle",
    "QuestionNumber",
    "QNumbertoPassage",
    "TestType",
  ],
  data: function () {
    return {
      PassageContent_data: this.PassageContent.replace(
        `id="${this.QNumbertoPassage}" class="underline-passage"`,
        `id="${this.QNumbertoPassage}" class="underline-passage-colored"`
      ),
      MathJaxOptions: { showMathMenu: false },
    };
  },
  mounted() {
    // MathJax
    renderByMathjax(document.getElementById("app"));
    // end
  },
  updated() {
    // MathJax
    renderByMathjax(document.getElementById("app"));
    // end
    this.PassageContent_data = this.PassageContent.replace(
      `id="${this.QNumbertoPassage}" class="underline-passage"`,
      `id="${this.QNumbertoPassage}" class="underline-passage-colored"`
    );
  },
};
</script>

<style lang="scss">
.passage-container {
  user-select: none;
  overflow: auto;
  height: calc(100vh - 70px);
  .passage-content {
    font-size: 14px;
    color: #333333;
    line-height: 20px;
    text-underline-offset: 3px;
    padding-bottom: 5rem;
    .underline-passage {
      text-decoration: underline;
    }
    .underline-passage-colored {
      text-decoration: underline;
      background-color: #ffff7b;
    }
    img {
      margin-top: 1rem;
      margin-bottom: 1rem;
    }
  }
}
</style>
