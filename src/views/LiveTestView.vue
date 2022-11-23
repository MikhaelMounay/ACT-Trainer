<template>
  <header
    class="container-fluid d-flex align-items-center justify-content-between p-3"
  >
    <div class="d-flex align-items-center justify-content-between">
      <p class="mb-0 mx-2">
        <router-link
          to="/"
          class="text-decoration-none text-white"
          @click="stopTimer()"
          ><svg
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            id="Layer_1"
            data-name="Layer 1"
            viewBox="0 0 856.8 97.93"
            width="130"
            fill="white"
          >
            <defs>
              <filter
                id="luminosity-noclip"
                x="47"
                y="147"
                width="55"
                height="24"
                filterUnits="userSpaceOnUse"
                color-interpolation-filters="sRGB"
              >
                <feFlood flood-color="#fff" result="bg" />
                <feBlend in="SourceGraphic" in2="bg" />
              </filter>
              <mask
                id="mask"
                x="26.16"
                y="45.55"
                width="55"
                height="24"
                maskUnits="userSpaceOnUse"
              >
                <g style="filter: url(#luminosity-noclip)">
                  <g transform="translate(-20.84 -101.45)">
                    <image
                      width="55"
                      height="24"
                      transform="translate(47 147)"
                      xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADcAAAAYCAYAAABeIWWlAAAACXBIWXMAAAsSAAALEgHS3X78AAAAtUlEQVRYR93XQRKAIAhAUWi6/5VtZZE5AgYJ/bULnzg1IgAU+Gk7t8C7Uq6zRcTBSn0IzpOjm7dIcwDmOGsM1whrci2/Bkmbnlw0UG+Calw0VBtFiq9ldFSvjVsAkAtG9zqcXCZUTXQto8I0/7kubjVMAxj1wK2AWWHaxF9Ly7wwbTec59S+AtFOnAdsBYhmfi1Xg2gmuEgg2itcVFRtChcdVRPjsoBoLC4jqqZ+z2VK9OTJ2gHVrDNOxSv85AAAAABJRU5ErkJggg=="
                    />
                  </g>
                </g>
              </mask>
            </defs>
            <path
              d="M55,152c-.31.79-3.14,7.81-3.89,9.62s-1.59,3.92-2.54,6.32-2,4.87-3,7.43-2,5-2.89,7.2-1.57,4.15-2.12,5.72a15,15,0,0,0-.83,2.83c0,1.42.41,2.26,1.24,2.54s1.71.61,2.66,1v1.18l-1.07.59q-10.26.12-20.76.71l-.36-.24-.59-1.18,1.06-.7a11.79,11.79,0,0,0,7-2.78,17.69,17.69,0,0,0,4.72-6v.12Q37.84,176,42,165.69T50.11,145l11-28.2q1.29-3.3,2.42-6.84a38.76,38.76,0,0,1,2.77-6.61,1,1,0,0,1,1.18-.59,2.28,2.28,0,0,1,1.3.59q8.15,20.78,15.81,41.48t16.52,41.24a16,16,0,0,0,4.72,6.13A12.26,12.26,0,0,0,113,195l1.3,1.53-1.06.59q-6.37-.36-12.81-.47t-12.8-.36l-.47-.35-.59-1.18.94-.59a3.29,3.29,0,0,0,2.18-1.06,2.77,2.77,0,0,0,.77-2.24,8,8,0,0,0-.77-2.54c-.59-1.53-1.31-3.42-2.18-5.66s-1.83-4.7-2.89-7.38-2.08-5.21-3.07-7.61-1.83-4.5-2.53-6.31-2.78-8.76-3-9.39m0,0L65.21,125.4q-2.59,6.48-5,13C58.68,142.7,56.81,147.75,55,152"
              transform="translate(-20.84 -101.45)"
            />
            <path
              d="M194.77,187.46a38.78,38.78,0,0,1-7.84,5.08,41.39,41.39,0,0,1-8.09,2.89,50.48,50.48,0,0,1-8.55,1.3q-4.42.28-9.26.29a71.93,71.93,0,0,1-20.6-3,44.31,44.31,0,0,1-16.16-8.73,40,40,0,0,1-10.62-14.63,52.26,52.26,0,0,1-4-20.59,49.62,49.62,0,0,1,3.71-20.47A39.71,39.71,0,0,1,124.15,115a47.35,47.35,0,0,1,16.28-8.85A69.44,69.44,0,0,1,160.91,103q4.71,0,8.91.23a47.66,47.66,0,0,1,8.2,1.18,43.91,43.91,0,0,1,7.84,2.66,42.49,42.49,0,0,1,7.73,4.54l.48.83c0,.39,0,1.18-.06,2.36s-.1,2.44-.18,3.77-.16,2.56-.24,3.66a6.66,6.66,0,0,1-.23,1.77l-1,.59-1.18-.47a33.9,33.9,0,0,0-13.45-11,40.06,40.06,0,0,0-17.11-3.42,40.77,40.77,0,0,0-16,3.07,36.89,36.89,0,0,0-12.45,8.5,38.79,38.79,0,0,0-8.08,12.8,43.4,43.4,0,0,0-2.89,16,41.68,41.68,0,0,0,2.65,15.46,37.13,37.13,0,0,0,8.68,13.21h-.12a35.2,35.2,0,0,0,10.15,7.67,38.45,38.45,0,0,0,11.86,3.72A41.6,41.6,0,0,0,167,190a45,45,0,0,0,12.1-3.72H179a35.34,35.34,0,0,0,7.38-5.19,39.76,39.76,0,0,0,6-6.84l.35-.24h1.18l.83,1,.47,11.68Z"
              transform="translate(-20.84 -101.45)"
            />
            <path
              d="M273.18,110.88c-3.34.08-6.59.2-9.73.36s-5.66.23-7.55.23q-.12,19-.24,37.88t.12,37.88a8.68,8.68,0,0,0,2.24,5.66,6.75,6.75,0,0,0,5.55,2.24l1.06.59L264,196.9l-.47.36H249.88q-6.84,0-13.69.12l-1.06-.59.12-1.18.94-.36a6.09,6.09,0,0,0,3.07-.53,8.64,8.64,0,0,0,4.31-4.36,7.77,7.77,0,0,0,.65-3.13q.59-19,.41-37.94t-.41-37.94q-6.15,0-11.86.3a79.21,79.21,0,0,1-11.86-.3,2.94,2.94,0,0,0-.95,0,2.29,2.29,0,0,0-.94.53,3.05,3.05,0,0,0-1.3,1.53l.12-.12a12.41,12.41,0,0,0-.94,2.54,22.93,22.93,0,0,1-.83,2.54l-1.18.7-.89-.41A1.27,1.27,0,0,1,213,118q.35-3.18.53-6.43c.11-2.16.25-4.31.41-6.43.16-.16.35-.37.59-.65s.47-.33.71-.18q9.08.6,17.23.59h17.34c.87,0,2.4,0,4.6,0s4.72-.1,7.56-.18,5.8-.14,8.9-.18"
              transform="translate(-20.84 -101.45)"
            />
            <path
              d="M428.42,199.38q-3.54-.94-8-1.83a38.62,38.62,0,0,1-7.79-2.3,16,16,0,0,1-3.07-1.77c-1.1-.78-2.18-1.63-3.24-2.53s-2.09-1.85-3.07-2.84l-2.54-2.53Q391.5,176.25,382.4,167t-18.29-18.47l.12-1.18.59-.23a1.92,1.92,0,0,1,.59-.12,50.07,50.07,0,0,0,8.09-1.47,18.71,18.71,0,0,0,7.13-4.08,16.34,16.34,0,0,0,4.31-5.84,19.36,19.36,0,0,0,1.65-6.9,18,18,0,0,0-1.06-7,17.27,17.27,0,0,0-3.83-6.2,14.46,14.46,0,0,0-5.25-3.59,26.2,26.2,0,0,0-6.08-1.54,39.41,39.41,0,0,0-6.43-.29c-2.17.08-4.31.11-6.43.11q.35,13,.53,25.85t.06,25.84q-.12,6.13-.3,12.27t-.18,12.27a8.29,8.29,0,0,0,2.13,5.55,6.5,6.5,0,0,0,5.43,2.36l.82.35.24,1.06-1.18.59q-6.84.12-13.63.3t-13.63.53a1.72,1.72,0,0,1-.59-.77l-.35-.76L338,195a7.79,7.79,0,0,0,5.54-2.66,9.44,9.44,0,0,0,2.36-5.72q.6-9.44.65-18.88t.06-18.88q0-8.85-.06-17.7t-.65-17.7a9.63,9.63,0,0,0-2.48-5.84A7.61,7.61,0,0,0,337.8,105a9.07,9.07,0,0,0-1-.41c-.36-.12-.42-.49-.18-1.12.08-.24.43-.39,1.06-.47q9.21.34,18.35.59t18.35.35a23.53,23.53,0,0,1,9.2,1.83,24.14,24.14,0,0,1,7.62,5,23.29,23.29,0,0,1,5.07,7.44,23,23,0,0,1,1.83,9.2,24.1,24.1,0,0,1-1.42,8.14,22.42,22.42,0,0,1-4.13,7.2,23.56,23.56,0,0,1-5.37,4.6,24,24,0,0,1-6.43,2.84Q387.13,157.5,392,163t8.73,9.62q3.9,4.13,7.14,7.31t6.49,6q3.26,2.83,6.85,5.61t8.2,6.07Z"
              transform="translate(-20.84 -101.45)"
            />
            <path
              d="M527.07,197.14c-3-.16-6-.27-9-.35l-9-.24q-1.89-.12-3.78-.06a23.75,23.75,0,0,1-3.77-.18,1,1,0,0,1-.71-.7c-.16-.4-.28-.67-.36-.83l1-.59a2.5,2.5,0,0,0,2.18-1.06,7.38,7.38,0,0,0,.77-2.24,20.31,20.31,0,0,0-.83-2.54q-.83-2.29-2.12-5.66c-.87-2.25-1.83-4.7-2.89-7.38s-2.07-5.21-3-7.61-1.79-4.5-2.54-6.31-1.24-3-1.47-3.66h-24.9c-.32.79-.85,2.08-1.6,3.89s-1.61,3.88-2.59,6.2-2,4.76-3.07,7.31-2,5-2.89,7.2-1.58,4.17-2.12,5.78a8.45,8.45,0,0,0-.71,3c.15,1.5.57,2.36,1.24,2.6l2.65.94v1.18l-1.06.59q-5.31.12-10.44.42t-10.33.29c-.16,0-.47-.47-.94-1.42l1.06-.7a11.76,11.76,0,0,0,7-2.78,17.45,17.45,0,0,0,4.72-6v.12q5.9-14,11.33-28t11-28.15l7.2-18.88c.55-1.25,1.06-2.61,1.54-4.07a24.29,24.29,0,0,1,1.65-4,1.27,1.27,0,0,1,1.18-.59,1.4,1.4,0,0,1,1.3.59l2.12,5.31,7.08,18.76q5.67,14.76,11.21,29.44t11.92,29.21a16.65,16.65,0,0,0,4.78,6.19,12.15,12.15,0,0,0,7.13,2.78l1.3,1.53ZM479,125.4q-2.6,6.48-5,13T469,151.24q5,.12,10,.06t10-.06Z"
              transform="translate(-20.84 -101.45)"
            />
            <path
              d="M573.09,197a93.88,93.88,0,0,0-25.72,0,1.2,1.2,0,0,1-.65-.59,8.18,8.18,0,0,1-.42-.71l1.07-.82a8.54,8.54,0,0,0,5.25-3,8.42,8.42,0,0,0,2.18-5.61v-72a8.64,8.64,0,0,0-2.18-5.66,7.93,7.93,0,0,0-5.25-3L546.3,104l1.07-.47a99.9,99.9,0,0,0,12.86.82,87.61,87.61,0,0,0,12.86-.94,1.33,1.33,0,0,1,.65.59c.19.31.33.55.41.71l-1.06.82a9.18,9.18,0,0,0-5.25,3.07,8.29,8.29,0,0,0-2.18,5.66v72a8.37,8.37,0,0,0,2.18,5.61,8.49,8.49,0,0,0,5.25,3l1.06,1.53Z"
              transform="translate(-20.84 -101.45)"
            />
            <path
              d="M684.48,104.75a7.9,7.9,0,0,0-5.6,2.71,10.23,10.23,0,0,0-2.54,5.9,91.1,91.1,0,0,0-.47,9.44c0,3.15,0,6.25-.12,9.32q-.24,10.86-.24,21.6t.36,21.59q.11,4,.23,8t.36,8c.07.94.17,1.87.29,2.77a11.89,11.89,0,0,1,.06,2.66,1,1,0,0,1-1,1,2,2,0,0,1-1.36-.3,21.39,21.39,0,0,1-3.3-3.3q-1.67-2-3.19-3.66-3.78-4-7.43-8t-7.44-8.14Q642,162.1,631,149.23T609,124q.24,10.38.29,21.36t0,21.36c-.08,3.14-.22,6.47-.42,10a93.61,93.61,0,0,0-.06,9.73q.24,3.78,2.13,5.37a14,14,0,0,0,5.31,2.54l.94.23v1.18l-1.06.71c-3.78,0-7.57.08-11.39.24l-11.38.47a.89.89,0,0,1-.65-.65l-.3-.88,1.06-.59a8.68,8.68,0,0,0,5.61-2.66,9.52,9.52,0,0,0,2.54-5.72,82.31,82.31,0,0,0,.41-9.32q-.06-4.73.06-9.44.22-10.74.17-22t-.29-22c-.08-2.67-.16-5.33-.24-8s-.19-5.33-.35-8.09a20.12,20.12,0,0,0-.18-2.65,12.5,12.5,0,0,1-.06-2.66,1.12,1.12,0,0,1,1-1,1.32,1.32,0,0,1,1.3.3,28.23,28.23,0,0,1,3.24,3.3q1.59,1.89,3.13,3.54,3.76,4.14,7.43,8.14t7.44,8.14q11.09,12.17,22.06,25T668.67,175q-.24-10.5-.3-20.83t.18-20.83c.08-3.3.22-6.59.41-9.85s.26-6.55.18-9.85a8.92,8.92,0,0,0-.53-3,9.33,9.33,0,0,0-1.48-2.66,6.62,6.62,0,0,0-2.3-1.83,6.27,6.27,0,0,0-3.12-.53l-.71-.23-.24-1.18,1.06-.59c3.86-.16,7.67-.3,11.45-.42s7.59-.25,11.45-.41Z"
              transform="translate(-20.84 -101.45)"
            />
            <path
              d="M767.73,185.64c-.28,1.29-.57,2.65-.89,4.07s-.63,2.73-.94,3.95-.55,2.06-.71,2.54a.92.92,0,0,1-.65.41,4.34,4.34,0,0,0-.77.18q-15.1-.6-30-.59t-30,.82a.65.65,0,0,1-.65-.53c-.12-.35-.22-.65-.29-.88l1.06-.71a7.79,7.79,0,0,0,5.49-2.72,9.4,9.4,0,0,0,2.41-5.66q.6-9.44.53-18.82t0-18.82v-17.7q0-8.85-.48-17.7a7.85,7.85,0,0,0-2.36-5.67A13.74,13.74,0,0,0,704,105a2.4,2.4,0,0,1-.89-.41.81.81,0,0,1-.29-.89c.08-.23.43-.51,1.06-.82q9.21.58,18.41.82t18.41.12q4.25-.1,8.67-.41a71.67,71.67,0,0,1,8.79-.06,1,1,0,0,1,.77.35,5.51,5.51,0,0,0,.53.59c0,.71,0,1.64-.06,2.78s-.06,2.3-.06,3.48,0,2.34-.06,3.48-.06,2.06-.06,2.77a1.3,1.3,0,0,1-1.3,1,1.52,1.52,0,0,1-1.41-.83q-.12-.7-.36-1.83a17.49,17.49,0,0,0-.59-2.18,8.24,8.24,0,0,0-.88-1.89,1.88,1.88,0,0,0-1.24-.94,27.21,27.21,0,0,0-4.78-.06c-1.61.12-3.2.22-4.78.29q-10.26.12-20.41,0,.12,8.85.23,17.64t.12,17.64h16.4a6.52,6.52,0,0,0,4.43-1.71,8.58,8.58,0,0,0,2.65-4.07l.71-.59,1.18-.12.83.95v17.82c0,.7-.38,1-1.12.88a2.88,2.88,0,0,1-1.6-.65,8.16,8.16,0,0,0-2.53-4.13,6.56,6.56,0,0,0-4.55-1.77h-16.4q0,9.45-.12,18.76t-.23,18.77q7.79-.24,15.46-.12l15.45.23a13.08,13.08,0,0,0,7.08-2.06,9.77,9.77,0,0,0,4.37-5.84l.83-.47,1.18.23.59,1.06C768.22,183.38,768,184.34,767.73,185.64Z"
              transform="translate(-20.84 -101.45)"
            />
            <path
              d="M876.7,199.38q-3.54-.94-8-1.83a38.51,38.51,0,0,1-7.78-2.3,15.39,15.39,0,0,1-3.07-1.77c-1.1-.78-2.18-1.63-3.25-2.53s-2.08-1.85-3.06-2.84L849,185.58q-9.21-9.33-18.29-18.59t-18.29-18.47l.12-1.18a5.66,5.66,0,0,1,.59-.23,1.87,1.87,0,0,1,.59-.12,49.94,49.94,0,0,0,8.08-1.47,18.67,18.67,0,0,0,7.14-4.08,16.46,16.46,0,0,0,4.31-5.84,19.57,19.57,0,0,0,1.65-6.9,18.13,18.13,0,0,0-1.06-7,17.43,17.43,0,0,0-3.84-6.2,14.3,14.3,0,0,0-5.25-3.59,26.07,26.07,0,0,0-6.08-1.54,39.36,39.36,0,0,0-6.43-.29c-2.16.08-4.31.11-6.43.11q.36,13,.53,25.85t.06,25.84q-.12,6.13-.29,12.27t-.18,12.27A8.33,8.33,0,0,0,808,192a6.51,6.51,0,0,0,5.43,2.36l.83.35.23,1.06-1.18.59q-6.84.12-13.63.3t-13.62.53a1.73,1.73,0,0,1-.6-.77c-.15-.35-.27-.6-.35-.76l1.18-.59a7.83,7.83,0,0,0,5.55-2.66,9.5,9.5,0,0,0,2.36-5.72q.59-9.44.65-18.88t0-18.88q0-8.85,0-17.7t-.65-17.7a9.69,9.69,0,0,0-2.48-5.84,7.62,7.62,0,0,0-5.66-2.66,9.25,9.25,0,0,0-1-.41c-.35-.12-.41-.49-.18-1.12.08-.24.44-.39,1.07-.47q9.19.34,18.35.59t18.34.35a23.58,23.58,0,0,1,9.21,1.83,24,24,0,0,1,7.61,5,23.29,23.29,0,0,1,5.07,7.44,23,23,0,0,1,1.83,9.2,24.34,24.34,0,0,1-1.41,8.14,22.61,22.61,0,0,1-4.13,7.2,24.2,24.2,0,0,1-11.8,7.44q6.36,7.32,11.21,12.8T849,172.6q3.88,4.13,7.14,7.31t6.49,6q3.24,2.83,6.84,5.61t8.2,6.07Z"
              transform="translate(-20.84 -101.45)"
            />
            <path
              d="M296,107.21c-.07,12.67-.15,29.3-.23,41.88s0,25.21.12,37.88a8.58,8.58,0,0,0,2.24,5.66,6.74,6.74,0,0,0,5.54,2.25l1.07.59-.59,1.18-.48.35H290q-6.86,0-13.69.12l-1.06-.59.11-1.18.95-.36a6.11,6.11,0,0,0,3.07-.53,8.5,8.5,0,0,0,2.53-1.77,8.28,8.28,0,0,0,1.77-2.59,7.6,7.6,0,0,0,.65-3.13q.6-19,.42-37.94c-.12-12.62-.26-29.27-.42-41.93"
              transform="translate(-20.84 -101.45)"
            />
            <path
              d="M233,105c2.2,0,55.14-.78,58-.85s5.8-.14,8.91-.18l8.67-.12q4-.06,6.72-.06a21.87,21.87,0,0,1,3.19.12q1.89,2.48,3.78,4.9t3.89,4.78l-.12,1.18-1.3.7-.82-.23a12.12,12.12,0,0,0-5.67-3.9,25.65,25.65,0,0,0-6.54-.88q-4.43-.18-9.44-.06c-3.35.08-6.59.2-9.74.35S267.89,111,266,111"
              transform="translate(-20.84 -101.45)"
            />
            <path
              d="M89.71,157a126.87,126.87,0,0,0-37,12s-4.42.55-3.15-4.9c0,0,1.57-6.88,13.56-11.57,0,0,11.89-5,21.82-3a7.09,7.09,0,0,1,5.79.65,2,2,0,0,1,1.58.55A2.18,2.18,0,0,1,94,151s1,.11-.4.88l-.1.43a12.66,12.66,0,0,1,4.94,1.49l.17.48a.25.25,0,0,1,0,.43l.14.36s.48-.49,1,.45a12.85,12.85,0,0,1-6.6,1.27A14.73,14.73,0,0,1,89.71,157Z"
              transform="translate(-20.84 -101.45)"
              style="fill: #ef3a40"
            />
          </svg>
        </router-link>
      </p>
      <button class="btn main-btn mx-2" @click="previous">Prev</button>
      <button
        class="btn main-btn mx-2"
        data-bs-toggle="modal"
        data-bs-target="#navigation_menu"
        @click="getStateFlagNav"
      >
        Nav
      </button>
      <button class="btn main-btn mx-2" @click="next">Next</button>
    </div>
    <div class="d-flex align-items-center justify-content-between">
      <div>
        <button
          class="btn main-btn dropdown-toggle mx-2 disabled"
          data-bs-toggle="dropdown"
        >
          Tools
        </button>
        <ul class="dropdown-menu">
          <li :class="magnifierState ? 'on' : 'off'">
            <button class="dropdown-item disabled" @click="toggleMagnifier">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 448 512"
                v-if="magnifierState"
              >
                <path
                  d="M438.6 105.4C451.1 117.9 451.1 138.1 438.6 150.6L182.6 406.6C170.1 419.1 149.9 419.1 137.4 406.6L9.372 278.6C-3.124 266.1-3.124 245.9 9.372 233.4C21.87 220.9 42.13 220.9 54.63 233.4L159.1 338.7L393.4 105.4C405.9 92.88 426.1 92.88 438.6 105.4H438.6z"
                />
              </svg>
              Magnifier
            </button>
          </li>
          <li><button class="dropdown-item disabled">Highlighter</button></li>
          <li><button class="dropdown-item disabled">Line Reader</button></li>
          <li>
            <button class="dropdown-item disabled">Answer Eliminator</button>
          </li>
          <li>
            <button class="dropdown-item disabled">Answer Masking</button>
          </li>
        </ul>
      </div>
      <div class="btn-group">
        <button
          type="button"
          class="btn main-btn"
          @click="changeBodyScale('-')"
        >
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
            <!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
            <path
              d="M504.1 471l-134-134C399.1 301.5 416 256.8 416 208C416 93.13 322.9 0 208 0S0 93.13 0 208S93.13 416 208 416c48.79 0 93.55-16.91 129-45.04l134 134C475.7 509.7 481.9 512 488 512s12.28-2.344 16.97-7.031C514.3 495.6 514.3 480.4 504.1 471zM208 368c-88.22 0-160-71.78-160-160s71.78-160 160-160s160 71.78 160 160S296.2 368 208 368zM288 184H127.1C114.7 184 104 194.7 104 208s10.73 24 23.1 24h160C301.3 232 312 221.3 312 208S301.3 184 288 184z"
            />
          </svg>
        </button>
        <button
          type="button"
          class="btn main-btn"
          @click="changeBodyScale('0')"
        >
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
            <!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
            <path
              d="M496 72v128C496 213.3 485.3 224 472 224h-128c-13.19 0-24-10.66-24-23.98c0-6.247 2.432-12.39 7.033-16.99L379.2 130.9C346.9 99.29 303.1 80 256 80C158.1 80 80 158.1 80 256s78.97 176 176 176c81.21 0 107.1-46.34 127.1-46.34c10.18 0 24.02 8.003 24.02 24.01c0 25.11-75.1 70.27-152.1 70.27c-123.5 0-223.9-100.4-223.9-223.9s100.4-223.1 223.9-223.1c60.03 0 116 24.58 157.1 64.95l41.1-41.1c4.601-4.601 10.74-7.019 16.99-7.019C485.4 48.01 496 58.83 496 72z"
            />
          </svg>
        </button>
        <button
          type="button"
          class="btn main-btn"
          @click="changeBodyScale('+')"
        >
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
            <!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
            <path
              d="M504.1 471l-134-134C399.1 301.5 416 256.8 416 208C416 93.13 322.9 0 208 0S0 93.13 0 208S93.13 416 208 416c48.79 0 93.55-16.91 129-45.04l134 134C475.7 509.7 481.9 512 488 512s12.28-2.344 16.97-7.031C514.3 495.6 514.3 480.4 504.1 471zM208 368c-88.22 0-160-71.78-160-160s71.78-160 160-160s160 71.78 160 160S296.2 368 208 368zM288 184H231.1V128c0-13.26-10.74-24-23.1-24S184 114.7 184 128v56H127.1C114.7 184 104 194.7 104 208s10.73 24 23.1 24H184V288c0 13.26 10.73 24 23.1 24c13.26 0 23.1-10.74 23.1-24V232h56C301.3 232 312 221.3 312 208S301.3 184 288 184z"
            />
          </svg>
        </button>
      </div>
      <div class="ms-2">
        <button class="btn main-btn disabled">Clear Highlight</button>
      </div>
      <div class="ms-2">
        <button class="btn main-btn" @click="endSection()">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512">
            <!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
            <path
              d="M310.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L160 210.7 54.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L114.7 256 9.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 301.3 265.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L205.3 256 310.6 150.6z"
            />
          </svg>
          &nbsp;End Section
        </button>
      </div>
      <div class="ms-2 main-btn timer" @click="toggleTimer()">
        <div></div>
        <span>
          {{ String(Math.floor(timer)).padStart(2, "0") }}:{{
            String(Math.floor((timer - Math.floor(timer)) * 60, 10)).padStart(
              2,
              "0"
            )
          }}
        </span>
        <p>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
            <!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
            <path
              d="M232 120C232 106.7 242.7 96 256 96C269.3 96 280 106.7 280 120V243.2L365.3 300C376.3 307.4 379.3 322.3 371.1 333.3C364.6 344.3 349.7 347.3 338.7 339.1L242.7 275.1C236 271.5 232 264 232 255.1L232 120zM256 0C397.4 0 512 114.6 512 256C512 397.4 397.4 512 256 512C114.6 512 0 397.4 0 256C0 114.6 114.6 0 256 0zM48 256C48 370.9 141.1 464 256 464C370.9 464 464 370.9 464 256C464 141.1 370.9 48 256 48C141.1 48 48 141.1 48 256z"
            />
          </svg>
        </p>
      </div>
    </div>
  </header>
  <div class="row g-0">
    <passage-container
      v-if="
        testData && testData.Questions[`Question_${questionNum}`].PassageRel
      "
      class="col-6"
      :TestType="testType"
      :PassageNumber="getPassageLetter()"
      :PassageTitle="
        testData.Passages[
          `Passage_${
            testData.Questions[`Question_${questionNum}`].PassageRel
          }_title`
        ]
      "
      :PassageContent="
        testData.Passages[
          `Passage_${
            testData.Questions[`Question_${questionNum}`].PassageRel
          }_content`
        ]
      "
      :QuestionNumber="questionNum"
      :QNumbertoPassage="
        testData.Questions[`Question_${questionNum}`].QNumbertoPassage
      "
    />
    <question-container
      v-if="testData"
      class="col-6"
      :TestId="testId"
      :TestType="testType"
      :Question="testData.Questions[`Question_${questionNum}`].Question"
      :Choices="testData.Questions[`Question_${questionNum}`].Choices"
      :QuestionNum="questionNum"
      :Magnifier="magnifierState"
    />
  </div>
  <footer v-if="testData">
    <div class="row g-0">
      <div class="col-11 d-flex align-items-end nav-footer-container">
        <nav aria-label="Page navigation example">
          <ul class="pagination pagination-sm">
            <li class="page-item">
              <a
                class="page-link"
                href="#"
                aria-label="Previous"
                @click.prevent="previousNavPage"
              >
                <span aria-hidden="true">&laquo;</span>
              </a>
            </li>
            <li
              class="page-item"
              v-for="n in navItemsToRender"
              :key="n"
              :class="[
                questionNum == n + navItemsToRender * navCurrentPage
                  ? 'active'
                  : '',
                n + navItemsToRender * navCurrentPage > testData.NumofQuestions
                  ? 'removeMe'
                  : `page-item-${n + navItemsToRender * navCurrentPage}`,
              ]"
            >
              <!-- :to="{
              name: 'livetest',
              params: {
                testId: testId,
                testType: testType,
                questionNum: n + navItemsToRender * navCurrentPage,
              },
            }" -->
              <span
                v-if="
                  n + navItemsToRender * navCurrentPage <=
                  testData.NumofQuestions
                "
                :class="[
                  'flag-footer',
                  `flag-footer-${n + navItemsToRender * navCurrentPage}`,
                ]"
              >
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                  <!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
                  <path
                    d="M64 32V480c0 17.7-14.3 32-32 32s-32-14.3-32-32V32C0 14.3 14.3 0 32 0S64 14.3 64 32zm40.8 302.8c-3 .9-6 1.7-8.8 2.6V13.5C121.5 6.4 153 0 184 0c36.5 0 68.3 9.1 95.6 16.9l1.3 .4C309.4 25.4 333.3 32 360 32c26.8 0 52.9-6.8 73-14.1c9.9-3.6 17.9-7.2 23.4-9.8c2.7-1.3 4.8-2.4 6.2-3.1c.7-.4 1.1-.6 1.4-.8l.2-.1c9.9-5.6 22.1-5.6 31.9 .2S512 20.6 512 32V288c0 12.1-6.8 23.2-17.7 28.6L480 288c14.3 28.6 14.3 28.6 14.3 28.6l0 0 0 0-.1 0-.2 .1-.7 .4c-.6 .3-1.5 .7-2.5 1.2c-2.2 1-5.2 2.4-9 4c-7.7 3.3-18.5 7.6-31.5 11.9C424.5 342.9 388.8 352 352 352c-37 0-65.2-9.4-89-17.3l-1-.3c-24-8-43.7-14.4-70-14.4c-27.5 0-60.1 7-87.2 14.8z"
                  />
                </svg>
              </span>
              <a
                class="page-link"
                v-if="
                  n + navItemsToRender * navCurrentPage <=
                  testData.NumofQuestions
                "
                @click="questionNum = n + navItemsToRender * navCurrentPage"
                >{{ n + navItemsToRender * navCurrentPage }}</a
              >
            </li>
            <li class="page-item">
              <a
                class="page-link"
                href="#"
                aria-label="Next"
                @click.prevent="nextNavPage"
              >
                <span aria-hidden="true">&raquo;</span>
              </a>
            </li>
          </ul>
        </nav>
      </div>
      <div class="col-1 d-flex align-items-end">
        <button class="flag-btn main-btn" @click="toggleFlag(questionNum)">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
            <!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
            <path
              d="M64 32V480c0 17.7-14.3 32-32 32s-32-14.3-32-32V32C0 14.3 14.3 0 32 0S64 14.3 64 32zm40.8 302.8c-3 .9-6 1.7-8.8 2.6V13.5C121.5 6.4 153 0 184 0c36.5 0 68.3 9.1 95.6 16.9l1.3 .4C309.4 25.4 333.3 32 360 32c26.8 0 52.9-6.8 73-14.1c9.9-3.6 17.9-7.2 23.4-9.8c2.7-1.3 4.8-2.4 6.2-3.1c.7-.4 1.1-.6 1.4-.8l.2-.1c9.9-5.6 22.1-5.6 31.9 .2S512 20.6 512 32V288c0 12.1-6.8 23.2-17.7 28.6L480 288c14.3 28.6 14.3 28.6 14.3 28.6l0 0 0 0-.1 0-.2 .1-.7 .4c-.6 .3-1.5 .7-2.5 1.2c-2.2 1-5.2 2.4-9 4c-7.7 3.3-18.5 7.6-31.5 11.9C424.5 342.9 388.8 352 352 352c-37 0-65.2-9.4-89-17.3l-1-.3c-24-8-43.7-14.4-70-14.4c-27.5 0-60.1 7-87.2 14.8z"
            />
          </svg>
          &nbsp;Flag
        </button>
      </div>
    </div>
  </footer>
  <div
    class="modal fade"
    id="navigation_menu"
    tabindex="-1"
    data-bs-backdrop="static"
  >
    <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title fw-bold">Item Navigation</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div>
            <table class="w-100">
              <thead>
                <tr>
                  <th></th>
                  <th>#</th>
                  <th class="state">State</th>
                  <th>Flagged</th>
                </tr>
              </thead>
              <tbody v-if="testData">
                <tr
                  v-for="n in testData.NumofQuestions"
                  :key="n"
                  :id="'n' + n"
                  @click="
                    questionNum = n;
                    closeNavModal();
                  "
                  :class="[questionNum == n ? 'current' : '']"
                >
                  <!-- data-bs-dismiss="modal" -->
                  <td class="arrow">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 256 512"
                    >
                      <!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
                      <path
                        d="M246.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-128-128c-9.2-9.2-22.9-11.9-34.9-6.9s-19.8 16.6-19.8 29.6l0 256c0 12.9 7.8 24.6 19.8 29.6s25.7 2.2 34.9-6.9l128-128z"
                      />
                    </svg>
                  </td>
                  <td class="number">{{ n }}</td>
                  <td class="state"></td>
                  <td class="flag">
                    <input type="checkbox" @click.stop="toggleFlag(n)" />
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" data-bs-dismiss="modal" class="close-btn">
            Close
          </button>
        </div>
      </div>
    </div>
  </div>
  <div
    class="modal fade"
    id="teststart_info"
    tabindex="-1"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
  >
    <div
      class="modal-dialog modal-dialog-centered modal-dialog-scrollable modal-fullscreen"
    >
      <div class="modal-content">
        <div class="modal-body">
          <div
            class="h-100 w-75 mx-auto d-flex flex-column align-items-center justify-content-center text-center"
          >
            <p class="fs-2">Welcome to the ACT Trainer!</p>
            <p>
              Normally, on the real test there will be two pages providing some
              information and instructions for the test. Since, this is only a
              training session, we will dive into the test questions directly.
              Feel free to press "<span class="fw-bold">Start Test</span>" when
              you are ready.
            </p>
            <p class="test-small text-danger">
              *Note* on the real test the timer will start counting on the
              "Instr" page.
            </p>
            <button
              type="button"
              data-bs-dismiss="modal"
              class="btn btn-danger"
              @click="startTimer()"
            >
              Start Test
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="modal fade"
    id="end_section"
    tabindex="-1"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
  >
    <div
      class="modal-dialog modal-dialog-centered modal-dialog-scrollable modal-fullscreen"
    >
      <div class="modal-content">
        <div class="modal-body">
          <div
            class="h-100 w-75 mx-auto d-flex flex-column align-items-center justify-content-center text-center"
          >
            <p class="fs-2 mb-4">Time is up!</p>
            <button
              type="button"
              data-bs-dismiss="modal"
              class="btn btn-danger mb-4"
              v-if="this.nextSection != 'end'"
            >
              <router-link
                :to="{
                  name: 'livetest',
                  params: { testId: testId, testType: nextSection },
                }"
                class="text-white text-decoration-none"
                >Go to Next Section</router-link
              >
            </button>
            <button
              type="button"
              data-bs-dismiss="modal"
              class="btn btn-danger"
            >
              <router-link
                :to="{
                  name: 'score_answers',
                  params: { testId: testId },
                }"
                class="text-white text-decoration-none"
                >Test Score & Answers (All Sections)</router-link
              >
              <!-- v-if="this.nextSection != 'end'" -->
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import QuestionContainer from "@/components/QuestionContainer.vue";
import PassageContainer from "@/components/PassageContainer.vue";
import { HTMLMagnifier } from "@/libs/html-magnifier";
import { ref } from "vue";
import cookie from "cookie_js/dist/cookie.umd.min.js";
import { Modal } from "bootstrap";

export default {
  name: "LiveTestView",
  components: { QuestionContainer, PassageContainer },
  data() {
    return {
      testData: null,
      testId: this.$route.params.testId,
      testType: this.$route.params.testType,
      nextSection: "end",
      questionNum: 1,
      numberOfNavPages: null,
      navCurrentPage: 0,
      magnifierState: false,
      magnifier: new HTMLMagnifier(),
      testKey: "testKey",
      bodyScale: 1,
      original_timer: 0,
      timer: 0,
      timer_interval: null,
    };
  },
  methods: {
    getPassageLetter() {
      switch (
        this.testData.Questions[`Question_${this.questionNum}`].PassageRel
      ) {
        case 1:
          return "I";
        case 2:
          return "II";
        case 3:
          return "III";
        case 4:
          return "IV";
        case 5:
          return "V";
        case 6:
          return "VI";
        case 7:
          return "VII";
      }
    },
    previous() {
      if (this.questionNum > 1) {
        this.questionNum--;
      }
    },
    next() {
      if (this.questionNum < this.testData.NumofQuestions) {
        this.questionNum++;
      }
    },
    previousNavPage() {
      if (this.navCurrentPage > 0) {
        this.navCurrentPage--;
      }
      setTimeout(function () {
        document.querySelectorAll(`li.page-item`).forEach((element) => {
          element.style.display = "block";
        });
      }, 100);
    },
    nextNavPage() {
      if (!(this.numberOfNavPages - 1 == this.navCurrentPage)) {
        this.navCurrentPage++;
      }
      if (this.numberOfNavPages - 1 == this.navCurrentPage) {
        setTimeout(function () {
          document.querySelectorAll(`.removeMe`).forEach((element) => {
            element.style.display = "none";
          });
        }, 100);
      }
    },
    getStateFlagNav() {
      if (cookie.get(this.testId + "_answers_" + this.testType) != null) {
        let answers = JSON.parse(
          cookie.get(this.testId + "_answers_" + this.testType)
        );
        for (let i = 1; i <= this.testData.NumofQuestions; i++) {
          let question_i_state = document.querySelector(
            `.modal table tbody tr#n${i} td.state`
          );
          let question_i_flag = document.querySelector(
            `.modal table tbody tr#n${i} td.flag input`
          );
          if (answers[`q_${i}`]) {
            question_i_state.innerHTML = "Answered";
          } else {
            question_i_state.innerHTML = "Unanswered";
          }
          if (answers[`f_${i}`] == "") {
            question_i_flag.checked = false;
          } else {
            question_i_flag.checked = true;
          }
        }
      } else {
        for (let i = 1; i <= this.testData.NumofQuestions; i++) {
          document.querySelector(
            `.modal table tbody tr#n${i} td.state`
          ).innerHTML = "Unanswered";
        }
      }
    },
    toggleFlag(number) {
      if (cookie.get(this.testId + "_answers_" + this.testType) != null) {
        let answers = JSON.parse(
          cookie.get(this.testId + "_answers_" + this.testType)
        );
        if (answers[`f_${number}`] == "") {
          answers[`f_${number}`] = "1";
        } else {
          answers[`f_${number}`] = "";
        }
        cookie.set(
          this.testId + "_answers_" + this.testType,
          JSON.stringify(answers),
          { path: "/" }
        );
      }
      this.updateFlags();
    },
    updateFlags() {
      if (cookie.get(this.testId + "_answers_" + this.testType) != null) {
        let answers = JSON.parse(
          cookie.get(this.testId + "_answers_" + this.testType)
        );
        for (let i = 1; i <= this.testData.NumofQuestions; i++) {
          if (answers[`f_${i}`] != "") {
            try {
              document
                .querySelector(`footer span.flag-footer-${i}`)
                .classList.add("flagged");
              // eslint-disable-next-line no-empty
            } catch (error) {}
          } else {
            try {
              document
                .querySelector(`footer span.flag-footer-${i}`)
                .classList.remove("flagged");
              // eslint-disable-next-line no-empty
            } catch (error) {}
          }
        }
      }
    },
    closeNavModal() {
      document.querySelector(".modal#navigation_menu button.close-btn").click();
    },
    updateNavAnswers() {
      if (cookie.get(this.testId + "_answers_" + this.testType) != null) {
        let answers = JSON.parse(
          cookie.get(this.testId + "_answers_" + this.testType)
        );
        for (let i = 1; i <= this.testData.NumofQuestions; i++) {
          if (answers[`q_${i}`] != "") {
            try {
              document
                .querySelector(`footer .page-item-${i} a.page-link`)
                .classList.add("page-link-answered");
              // eslint-disable-next-line no-empty
            } catch (error) {}
          } else {
            try {
              document
                .querySelector(`footer .page-item-${i} a.page-link`)
                .classList.remove("page-link-answered");
              // eslint-disable-next-line no-empty
            } catch (error) {}
          }
        }
      }
    },
    changeBodyScale(change) {
      if (change == "+") {
        document.querySelector(
          "body"
        ).style.transform = `scale(${(this.bodyScale += 0.2)})`;
        document.querySelector("body").style.transformOrigin = "left top";
      } else if (change == "-") {
        document.querySelector(
          "body"
        ).style.transform = `scale(${(this.bodyScale -= 0.2)})`;
        document.querySelector("body").style.transformOrigin = "left top";
      } else if (change == "0") {
        document.querySelector(
          "body"
        ).style.transform = `scale(${(this.bodyScale = 1)})`;
        document.querySelector("body").style.transformOrigin = "left top";
      }
    },
    create_test_cookies() {
      if (cookie.get(this.testId + "_answers_" + this.testType) == null) {
        let answers_initial_EnglishTest = {
          time_used: "90:00",
          q_1: "",
          f_1: "",
          q_2: "",
          f_2: "",
          q_3: "",
          f_3: "",
          q_4: "",
          f_4: "",
          q_5: "",
          f_5: "",
          q_6: "",
          f_6: "",
          q_7: "",
          f_7: "",
          q_8: "",
          f_8: "",
          q_9: "",
          f_9: "",
          q_10: "",
          f_10: "",
          q_11: "",
          f_11: "",
          q_12: "",
          f_12: "",
          q_13: "",
          f_13: "",
          q_14: "",
          f_14: "",
          q_15: "",
          f_15: "",
          q_16: "",
          f_16: "",
          q_17: "",
          f_17: "",
          q_18: "",
          f_18: "",
          q_19: "",
          f_19: "",
          q_20: "",
          f_20: "",
          q_21: "",
          f_21: "",
          q_22: "",
          f_22: "",
          q_23: "",
          f_23: "",
          q_24: "",
          f_24: "",
          q_25: "",
          f_25: "",
          q_26: "",
          f_26: "",
          q_27: "",
          f_27: "",
          q_28: "",
          f_28: "",
          q_29: "",
          f_29: "",
          q_30: "",
          f_30: "",
          q_31: "",
          f_31: "",
          q_32: "",
          f_32: "",
          q_33: "",
          f_33: "",
          q_34: "",
          f_34: "",
          q_35: "",
          f_35: "",
          q_36: "",
          f_36: "",
          q_37: "",
          f_37: "",
          q_38: "",
          f_38: "",
          q_39: "",
          f_39: "",
          q_40: "",
          f_40: "",
          q_41: "",
          f_41: "",
          q_42: "",
          f_42: "",
          q_43: "",
          f_43: "",
          q_44: "",
          f_44: "",
          q_45: "",
          f_45: "",
          q_46: "",
          f_46: "",
          q_47: "",
          f_47: "",
          q_48: "",
          f_48: "",
          q_49: "",
          f_49: "",
          q_50: "",
          f_50: "",
          q_51: "",
          f_51: "",
          q_52: "",
          f_52: "",
          q_53: "",
          f_53: "",
          q_54: "",
          f_54: "",
          q_55: "",
          f_55: "",
          q_56: "",
          f_56: "",
          q_57: "",
          f_57: "",
          q_58: "",
          f_58: "",
          q_59: "",
          f_59: "",
          q_60: "",
          f_60: "",
          q_61: "",
          f_61: "",
          q_62: "",
          f_62: "",
          q_63: "",
          f_63: "",
          q_64: "",
          f_64: "",
          q_65: "",
          f_65: "",
          q_66: "",
          f_66: "",
          q_67: "",
          f_67: "",
          q_68: "",
          f_68: "",
          q_69: "",
          f_69: "",
          q_70: "",
          f_70: "",
          q_71: "",
          f_71: "",
          q_72: "",
          f_72: "",
          q_73: "",
          f_73: "",
          q_74: "",
          f_74: "",
          q_75: "",
          f_75: "",
        };
        let answers_initial_MathTest = {
          time_used: "00:00",
          q_1: "",
          f_1: "",
          q_2: "",
          f_2: "",
          q_3: "",
          f_3: "",
          q_4: "",
          f_4: "",
          q_5: "",
          f_5: "",
          q_6: "",
          f_6: "",
          q_7: "",
          f_7: "",
          q_8: "",
          f_8: "",
          q_9: "",
          f_9: "",
          q_10: "",
          f_10: "",
          q_11: "",
          f_11: "",
          q_12: "",
          f_12: "",
          q_13: "",
          f_13: "",
          q_14: "",
          f_14: "",
          q_15: "",
          f_15: "",
          q_16: "",
          f_16: "",
          q_17: "",
          f_17: "",
          q_18: "",
          f_18: "",
          q_19: "",
          f_19: "",
          q_20: "",
          f_20: "",
          q_21: "",
          f_21: "",
          q_22: "",
          f_22: "",
          q_23: "",
          f_23: "",
          q_24: "",
          f_24: "",
          q_25: "",
          f_25: "",
          q_26: "",
          f_26: "",
          q_27: "",
          f_27: "",
          q_28: "",
          f_28: "",
          q_29: "",
          f_29: "",
          q_30: "",
          f_30: "",
          q_31: "",
          f_31: "",
          q_32: "",
          f_32: "",
          q_33: "",
          f_33: "",
          q_34: "",
          f_34: "",
          q_35: "",
          f_35: "",
          q_36: "",
          f_36: "",
          q_37: "",
          f_37: "",
          q_38: "",
          f_38: "",
          q_39: "",
          f_39: "",
          q_40: "",
          f_40: "",
          q_41: "",
          f_41: "",
          q_42: "",
          f_42: "",
          q_43: "",
          f_43: "",
          q_44: "",
          f_44: "",
          q_45: "",
          f_45: "",
          q_46: "",
          f_46: "",
          q_47: "",
          f_47: "",
          q_48: "",
          f_48: "",
          q_49: "",
          f_49: "",
          q_50: "",
          f_50: "",
          q_51: "",
          f_51: "",
          q_52: "",
          f_52: "",
          q_53: "",
          f_53: "",
          q_54: "",
          f_54: "",
          q_55: "",
          f_55: "",
          q_56: "",
          f_56: "",
          q_57: "",
          f_57: "",
          q_58: "",
          f_58: "",
          q_59: "",
          f_59: "",
          q_60: "",
          f_60: "",
        };
        let answers_initial_ReadingTest = {
          time_used: "00:00",
          q_1: "",
          f_1: "",
          q_2: "",
          f_2: "",
          q_3: "",
          f_3: "",
          q_4: "",
          f_4: "",
          q_5: "",
          f_5: "",
          q_6: "",
          f_6: "",
          q_7: "",
          f_7: "",
          q_8: "",
          f_8: "",
          q_9: "",
          f_9: "",
          q_10: "",
          f_10: "",
          q_11: "",
          f_11: "",
          q_12: "",
          f_12: "",
          q_13: "",
          f_13: "",
          q_14: "",
          f_14: "",
          q_15: "",
          f_15: "",
          q_16: "",
          f_16: "",
          q_17: "",
          f_17: "",
          q_18: "",
          f_18: "",
          q_19: "",
          f_19: "",
          q_20: "",
          f_20: "",
          q_21: "",
          f_21: "",
          q_22: "",
          f_22: "",
          q_23: "",
          f_23: "",
          q_24: "",
          f_24: "",
          q_25: "",
          f_25: "",
          q_26: "",
          f_26: "",
          q_27: "",
          f_27: "",
          q_28: "",
          f_28: "",
          q_29: "",
          f_29: "",
          q_30: "",
          f_30: "",
          q_31: "",
          f_31: "",
          q_32: "",
          f_32: "",
          q_33: "",
          f_33: "",
          q_34: "",
          f_34: "",
          q_35: "",
          f_35: "",
          q_36: "",
          f_36: "",
          q_37: "",
          f_37: "",
          q_38: "",
          f_38: "",
          q_39: "",
          f_39: "",
          q_40: "",
          f_40: "",
        };
        let answers_initial_ScienceTest = {
          time_used: "00:00",
          q_1: "",
          f_1: "",
          q_2: "",
          f_2: "",
          q_3: "",
          f_3: "",
          q_4: "",
          f_4: "",
          q_5: "",
          f_5: "",
          q_6: "",
          f_6: "",
          q_7: "",
          f_7: "",
          q_8: "",
          f_8: "",
          q_9: "",
          f_9: "",
          q_10: "",
          f_10: "",
          q_11: "",
          f_11: "",
          q_12: "",
          f_12: "",
          q_13: "",
          f_13: "",
          q_14: "",
          f_14: "",
          q_15: "",
          f_15: "",
          q_16: "",
          f_16: "",
          q_17: "",
          f_17: "",
          q_18: "",
          f_18: "",
          q_19: "",
          f_19: "",
          q_20: "",
          f_20: "",
          q_21: "",
          f_21: "",
          q_22: "",
          f_22: "",
          q_23: "",
          f_23: "",
          q_24: "",
          f_24: "",
          q_25: "",
          f_25: "",
          q_26: "",
          f_26: "",
          q_27: "",
          f_27: "",
          q_28: "",
          f_28: "",
          q_29: "",
          f_29: "",
          q_30: "",
          f_30: "",
          q_31: "",
          f_31: "",
          q_32: "",
          f_32: "",
          q_33: "",
          f_33: "",
          q_34: "",
          f_34: "",
          q_35: "",
          f_35: "",
          q_36: "",
          f_36: "",
          q_37: "",
          f_37: "",
          q_38: "",
          f_38: "",
          q_39: "",
          f_39: "",
          q_40: "",
          f_40: "",
        };
        switch (this.testType) {
          case "EnglishTest":
            cookie.set(
              this.testId + "_answers_" + this.testType,
              JSON.stringify(answers_initial_EnglishTest),
              { path: "/" }
            );
            break;
          case "MathTest":
            cookie.set(
              this.testId + "_answers_" + this.testType,
              JSON.stringify(answers_initial_MathTest),
              { path: "/" }
            );
            break;
          case "ReadingTest":
            cookie.set(
              this.testId + "_answers_" + this.testType,
              JSON.stringify(answers_initial_ReadingTest),
              { path: "/" }
            );
            break;
          case "ScienceTest":
            cookie.set(
              this.testId + "_answers_" + this.testType,
              JSON.stringify(answers_initial_ScienceTest),
              { path: "/" }
            );
            break;
        }
      }
    },
    startTimer() {
      this.timer = this.original_timer;
      this.timer_interval = setInterval(() => {
        this.timer -= 1 / 60;
        document.querySelector("header .timer div").style.width = `${
          (this.timer / this.original_timer) * 100
        }%`;
        if (this.timer <= 1 / 60) {
          this.endSection();
        }
      }, 1000);
    },
    toggleTimer() {
      if (
        window
          .getComputedStyle(document.querySelector("header .timer p"))
          .getPropertyValue("display") == "none"
      ) {
        document.querySelector("header .timer p").style.display = "block";
      } else {
        document.querySelector("header .timer p").style.display = "none";
      }
    },
    endSection() {
      clearInterval(this.timer_interval);
      const end_section_modal = new Modal("#end_section");
      end_section_modal.show();
      const time_used = this.original_timer - this.timer;
      let time_used_format =
        String(Math.floor(time_used)).padStart(2, "0") +
        ":" +
        String(
          Math.floor((time_used - Math.floor(time_used)) * 60, 10)
        ).padStart(2, "0");
      if (cookie.get(this.testId + "_answers_" + this.testType) != null) {
        let answers = JSON.parse(
          cookie.get(this.testId + "_answers_" + this.testType)
        );
        answers["time_used"] = time_used_format;
        cookie.set(
          this.testId + "_answers_" + this.testType,
          JSON.stringify(answers),
          { path: "/" }
        );
      }
    },
    stopTimer() {
      clearInterval(this.timer_interval);
    },
    toggleMagnifier() {
      this.magnifierState = !this.magnifierState;
      if (this.magnifierState) {
        this.magnifier.setZoom(2);
        this.magnifier.setShape("square");
        this.magnifier.setWidth(document.documentElement.clientWidth * 0.33);
        this.magnifier.setHeight(document.documentElement.clientHeight * 0.33);
        this.magnifier.show();
      } else {
        this.magnifier.hide();
      }
    },
  },
  setup() {
    let availableWidth = ref(document.documentElement.clientWidth * 0.85);
    let indivWidth = ref(30);
    let navItemsToRender = ref(
      Math.floor(availableWidth.value / indivWidth.value) - 2
    );
    return { navItemsToRender };
  },
  mounted() {
    fetch(
      `https://act-trainer-platform.glitch.me/${this.testId}_${this.testType}/`
    )
      .then((response) => response.json())
      .then((testData) => {
        this.testData = testData;
        this.numberOfNavPages = Math.ceil(
          testData.NumofQuestions / this.navItemsToRender
        );
        switch (this.testType) {
          case "EnglishTest":
            this.original_timer = 45;
            this.nextSection = "MathTest";
            break;
          case "MathTest":
            this.original_timer = 60;
            this.nextSection = "ReadingTest";
            break;
          case "ReadingTest":
            this.original_timer = 35;
            this.nextSection = "ScienceTest";
            break;
          case "ScienceTest":
            this.original_timer = 35;
            this.nextSection = "end";
            break;
        }
        this.create_test_cookies();
        const teststart_info_modal = new Modal("#teststart_info");
        teststart_info_modal.show();
      });
  },
  updated() {
    this.updateFlags();
    this.updateNavAnswers();
  },
};
</script>

<style lang="scss" scoped>
$my-red-color: #e42a22;

.main-btn {
  background-image: linear-gradient(#f7f8fa 0%, #e7e9ec 100%);
  border: 1px solid #bfbfbf;
  color: #333;
  font-size: 11px;
  line-height: 20px;
  padding: 7px 12px;
  border-radius: 5px;
  font-weight: bold;
  &:hover {
    background-position: 0px;
    background-image: linear-gradient(#e7eaf0 0%, #d9dce1 100%);
    background-color: #d8dde6;
    color: #333;
    border-color: #bfbfbf;
  }
  &:active,
  &:focus {
    background-image: none;
    background-color: #d8dde6;
    outline: 0;
    box-shadow: inset 0 2px 4px rgb(0 0 0 / 15%), 0 1px 2px rgb(0 0 0 / 5%);
    color: #333;
    border-color: #bfbfbf;
  }
  svg {
    width: 16px;
    height: 16px;
    fill: #333;
    padding-bottom: 2px;
  }
}

header {
  background-color: #001733;
  color: white;
  li.on {
    background-color: $my-red-color;
    button {
      color: white;
    }
  }
  li button:hover {
    background-color: $my-red-color;
    color: white;
  }
  button.dropdown-item {
    svg {
      width: 12px;
      margin-right: 0.2rem;
      fill: white;
    }
  }
  .btn-group {
    svg {
      width: 14px;
      height: 14px;
      fill: #333;
    }
  }
  .timer {
    width: 80px;
    height: 36px;
    font-size: 15px;
    background-image: none;
    background-color: #fff;
    color: #001733;
    text-align: center;
    user-select: none;
    cursor: pointer;
    position: relative;
    &:hover {
      background-image: none;
      background-color: #fff;
      div {
        background-color: #f1f1f1;
      }
    }
    div {
      background-color: #dddddd;
      border-radius: 5px;
      width: 100%;
      height: 100%;
      position: absolute;
      top: 0;
      left: 0;
    }
    span,
    p {
      position: absolute;
      top: 0;
      left: 50%;
      transform: translateX(-50%);
      padding: 7px 12px;
    }
    span {
      display: block;
    }
    p {
      display: none;
      background-color: #33455b;
      width: 100%;
      height: 100%;
      border-radius: 5px;
      &:hover {
        background-color: #4d5d70;
      }
      svg {
        width: 18px;
        height: 18px;
        fill: #fff;
      }
    }
  }
}

footer {
  position: fixed;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  width: 90vw;
  height: fit-content;
  background-color: transparent;
  overflow-x: auto;
  .nav-footer-container {
    height: 75px;
  }
  nav {
    ul {
      margin-bottom: 0;
      li.page-item {
        width: 30px;
        height: 28px;
        position: relative;
        span.flag-footer {
          display: block;
          position: absolute;
          top: -22.5px;
          left: -1px;
          background-color: #eceee9;
          width: 100%;
          height: 100%;
          text-align: center;
          border: 1px solid #dddddd;
          border-top-right-radius: 3px;
          border-top-left-radius: 3px;
          line-height: 20px;
          visibility: hidden;
          svg {
            width: 10px;
            height: 10px;
            fill: #333333;
          }
          &.flagged {
            visibility: visible;
          }
        }
        a {
          width: inherit;
          height: inherit;
          text-align: center;
          display: grid;
          place-items: center;
          font-weight: bold;
          color: #aaaaaa;
          font-size: 0.8rem;
          padding: 0.15rem 0;
          &:hover {
            background-color: $my-red-color;
            color: white;
          }
          &:focus {
            border: 2px solid black;
            box-shadow: unset;
            background-color: #fff;
            color: #aaaaaa;
          }
        }
        &.active {
          a {
            border: none;
            background-color: $my-red-color;
            color: white;
            background-image: url("@/assets/navbar-active.png");
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
          }
        }
        .page-link-answered {
          color: #4d4d4d;
          background-color: #e8e8e8;
        }
      }
    }
  }
  .flag-btn {
    display: block;
    margin-left: auto;
    font-size: 14px;
    svg {
      width: 12px;
      height: 12px;
      fill: #333;
    }
  }
}

.modal {
  --bs-modal-width: 95vw;
  .close-btn {
    background-image: linear-gradient(#f7f8fa 0%, #e7e9ec 100%);
    border: 1px solid #bfbfbf;
    color: #333;
    transition: 0s;
    border-radius: 5px;
    padding: 7px 12px;
    font-size: 11px;
    font-weight: bold;
    line-height: 20px;
    &:hover,
    &:active,
    &:focus {
      background-image: linear-gradient(#e7eaf0 0%, #d9dce1 100%);
      color: #333;
      border: 1px solid #bfbfbf;
    }
  }
  table {
    thead {
      th {
        padding: 8px;
        line-height: 20px;
        &.state {
          width: 150px;
        }
      }
    }
    tbody {
      tr {
        cursor: pointer;
        &:hover {
          background-color: #f5f5f5;
        }
      }
      td {
        padding: 8px;
        line-height: 20px;
        border-top: 1px solid #ddd;
      }
      td.arrow {
        width: 25px;
        svg {
          // visibility: hidden;
          display: none;
          width: 18px;
          height: 18px;
          line-height: 14px;
        }
      }
      td.number {
        width: 50px;
      }
      tr.current {
        background-color: #e0e0ff;
        td.arrow svg {
          display: block;
        }
      }
    }
  }
}

#teststart_info,
#end_section {
  font-family: "Bree Serif", serif;
}
</style>
