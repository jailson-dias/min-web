<template>
  <v-card width="240">
    <v-card-text> {{ textCard }} </v-card-text>
    <v-card-actions>
      <v-spacer></v-spacer>

      <v-btn
        color="#0ed0ce"
        class="button-open-site"
        flat="flat"
        @click="open(link)"
      >
        Abrir página
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: ["text", "link"],
  computed: {
    textCard() {
      if (this.text) {
        if (this.text.length > 250) {
          return this.text.slice(0, 247) + "...";
        } else {
          return this.text;
        }
      }
      return "";
    }
  },
  methods: {
    open(link) {
      window.open(link, "_blank");
    }
  }
};
</script>

<style></style>
