<template>
  <div class="question-container container-fluid p-3 ms-0" :key="Magnifier">
    <p class="question" v-if="Question" v-html="Question"></p>
    <!-- <math-jax latex="\frac{1}{9}"></math-jax> -->
    <div>
      <div v-for="(choice, objKey) in Choices" :key="objKey">
        <label :for="objKey.split('_')[1]">
          <input
            :id="objKey.split('_')[1]"
            type="radio"
            :name="`question_${QuestionNum}`"
            @change="answerUpdate"
          />
          <span v-html="objKey.split('_')[1] + '. ' + choice"></span> </label
        ><br />
      </div>
    </div>
  </div>
</template>

<script>
import cookie from "cookie_js/dist/cookie.umd.min.js";
import { MathJax, renderByMathjax } from "mathjax-vue3";
// import VueMathjax from "vue-mathjax-next";

export default {
  name: "QuestionContainer",
  // components: { VueMathjax },
  // eslint-disable-next-line vue/no-unused-components
  components: { MathJax },
  props: [
    "TestId",
    "TestType",
    "QuestionNum",
    "Question",
    "Choices",
    "Magnifier",
  ],
  data() {
    return {
      // MathJaxOptions: { showMathMenu: false },
    };
  },
  methods: {
    answerUpdate() {
      let checked = document.querySelector(
        `input[type="radio"][name="question_${this.QuestionNum}"]:checked`
      );
      let answers = JSON.parse(
        cookie.get(this.TestId + "_answers_" + this.TestType)
      );
      answers[`q_${this.QuestionNum}`] = checked.id;
      cookie.set(
        this.TestId + "_answers_" + this.TestType,
        JSON.stringify(answers),
        { path: "/" }
      );
    },
  },
  mounted() {
    // MathJax
    renderByMathjax(document.getElementById("app"));
    // end
    if (cookie.get(this.TestId + "_answers_" + this.TestType) != null) {
      try {
        document.querySelector(
          `input[type="radio"][name="question_${this.QuestionNum}"][id="${
            // eslint-disable-next-line prettier/prettier
            JSON.parse(cookie.get(this.TestId + "_answers_" + this.TestType))[
              // eslint-disable-next-line prettier/prettier
              `q_${this.QuestionNum}`
            ]
          }"]`
        ).checked = true;
      } catch (err) {
        document
          .querySelectorAll(
            `input[type="radio"][name="question_${this.QuestionNum}"]`
          )
          .forEach((element) => {
            element.checked = false;
          });
      }
    }
  },
  updated() {
    // MathJax
    renderByMathjax(document.getElementById("app"));
    // end
    if (cookie.get(this.TestId + "_answers_" + this.TestType) != null) {
      try {
        document.querySelector(
          `input[type="radio"][name="question_${this.QuestionNum}"][id="${
            // eslint-disable-next-line prettier/prettier
            JSON.parse(cookie.get(this.TestId + "_answers_" + this.TestType))[
              // eslint-disable-next-line prettier/prettier
              `q_${this.QuestionNum}`
            ]
          }"]`
        ).checked = true;
      } catch (err) {
        document
          .querySelectorAll(
            `input[type="radio"][name="question_${this.QuestionNum}"]`
          )
          .forEach((element) => {
            element.checked = false;
          });
      }
    }
  },
};
</script>

<style lang="scss" scoped>
.question-container {
  user-select: none;
  height: calc(100vh - 70px);
  label {
    padding-left: 1rem;
    font-size: 14px;
    line-height: 20px;
    margin-bottom: 15px;
    cursor: pointer;
    vertical-align: center;
    white-space: nowrap;
    input[type="radio"] {
      width: 20px;
      height: 20px;
      vertical-align: top;
      display: inline-block;
    }
    span {
      white-space: normal;
      display: inline-block;
      margin-left: 20px;
      max-width: 40vw;
    }
  }
}
</style>
