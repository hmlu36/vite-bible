<!-- Search.vue -->
<template>
  <div>
    <label for="keyword">輸入關鍵字：</label>
    <input id="keyword" v-model="keyword" @input="onSearch" />
    <ul>
      <li v-for="result in searchResults" :key="result.id">
        {{ result.book }} {{ result.chapter }}:{{ result.verse }} - {{ result.text }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      keyword: '',
      searchResults: [],
    };
  },
  methods: {
    async onSearch() {
      const books = await import('../assets/books.json');
      const results = [];
      for (const book of books) {
        const bibleData = await import(`../assets/${book.abbr}.json`);
        for (const chapter in bibleData) {
          for (const [verseIndex, verseText] of bibleData[chapter].entries()) {
            if (verseText.includes(this.keyword)) {
              results.push({
                book: book.name,
                chapter,
                verse: verseIndex + 1,
                text: verseText,
              });
            }
          }
        }
      }
      this.searchResults = results;
    },
  },
};
</script>
