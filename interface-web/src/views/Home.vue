<template>
  <v-app>
    <v-navigation-drawer class="mt" permanent width="200" left app>
      <v-layout align-center justify-center column>
        <v-img
          :src="require('../assets/followup.jpeg')"
          aspect-ratio="1"
          class="image-logo"
        ></v-img>
      </v-layout>
      <v-list>
        <v-list-tile
          v-for="item in items"
          :key="item.title"
          @click="changeCategory(item.category)"
          :class="{
            'category-active': selected == item.title,
            'category-inactive': selected != item.title
          }"
        >
          <!-- <v-list-tile-action> </v-list-tile-action> -->
          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-content>
      <v-container>
        <v-layout align-center justify-start row wrap>
          <card
            v-for="(card, index) in cardsList"
            :key="index"
            class="cards"
            :text="card.text"
            :link="card.url"
          ></card>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Card from "../components/Card";

import data from "../labelsjson2";

export default {
  data() {
    return {
      selected: "cirurgia_bariatrica",
      items: [
        { title: "Cirurgia Bariátrica", category: "cirurgia_bariatrica" },
        { title: "Diabetes", category: "diabetes" },
        { title: "Hipertensão", category: "hipertensao" },
        { title: "Alimentação", category: "alimentacao" }
      ]
    };
  },
  components: { Card },
  computed: {
    cardsList() {
      let d = data.filter(i => i.watsonLabel == this.selected);
      // console.log(this.selected, data);
      return d;
    }
  },
  methods: {
    changeCategory(category) {
      // console.log(category);
      this.selected = category;
    }
  }
};
</script>

<style scoped>
.image-logo {
  width: 80%;
  height: 3em;
  align-self: center;
  margin-top: 2em;
  margin-bottom: 1em;
}

.category-active {
  background-color: #21c8c91c;
}

.category-active div {
  font-size: small;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  color: #0ed0ce;
}

.category-inactive {
  background-color: #ffffff;
}

.category-inactive div {
  font-size: small;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  color: #000000;
}

.cards {
  margin: 0.4em;
}

.button-open-site {
  text-transform: none !important;
}
</style>
