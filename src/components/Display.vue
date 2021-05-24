<template>
  <div class="p-grid">
    <div class="p-md-1 p-col-3 text-right">
      <h4>節</h4>
    </div>
    <div class="p-md-11 p-col-9">
      <h4>內容</h4>
    </div>
  </div>

  <div class="p-grid" v-if="matchVerse != null && matchVerse.length > 0">
    <div
      class="p-md-1 p-col-3 text-right"
      :style="{
        'white-space': 'nowrap',
        'overflow-x': 'scroll',
        fontSize: selectedFontSize + 'px',
      }"
    >
      <div v-for="entry in matchVerse" :key="entry.verse">
        <span>
          {{ entry.book }}
        </span>
        <span
          :style="{
            fontSize: selectedFontSize - 4 + 'px',
          }"
        >
          {{ entry.chapter }}
        </span>
        :
        <span
          :style="{
            fontSize: selectedFontSize - 4 + 'px',
          }"
          >{{ entry.verse }}
        </span>
      </div>
    </div>
    <div
      class="p-md-11 p-col-9"
      :style="{
        'white-space': 'nowrap',
        'overflow-x': 'scroll',
        fontSize: selectedFontSize + 'px',
      }"
    >
      <div v-for="entry in matchVerse" :key="entry.verse" v-html="entry.content" />
    </div>
  </div>
</template>

<script>
export default {
  name: "display",
  props: {
    selectedFontSize: {
      type: Number,
      default: 20,
      required: false,
    },
    source: {
      type: String,
      required: true,
    },
    matchVerse: {
      type: Object,
    },
  },
  setup() {
    const maxLength = (arr) => {
      return Math.max(0, ...arr.map((s) => s.length));
    };

    const pad = (length, str) => {
      if (typeof str === "undefined") return " ".repeat(length);
      return (" ".repeat(length) + str).slice(-length);
    };

    return { maxLength, pad };
  },
};
</script>

<style></style>
