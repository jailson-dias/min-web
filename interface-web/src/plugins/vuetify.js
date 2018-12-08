import Vue from "vue";
import Vuetify from "vuetify/lib";
import "vuetify/src/stylus/app.styl";

Vue.use(Vuetify, {
  iconfont: "md",
  theme: {
    primary: "#0ED0CE",
    secondary: "#FFFFFF",
    tertiary: "#0000dd",
    accent: "#00dd00",
    error: "#b71c1c"
  }
});
