<!-- ChapterSelector.vue -->
<template>
  <div class="chapter-selector">
    <label for="chapter">章節：</label>
    <select id="chapter" v-model="selectedChapterNum" @change="onChapterChange">
      <option v-for="chapterNum in chapterCount" :key="chapterNum" :value="chapterNum">
        第 {{ chapterNum }} 章
      </option>
    </select>
  </div>
</template>

<script>
import books from '../assets/books.json';

export default {
  props: {
    selectedBook: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      chapterCount: 0,
      selectedChapterNum: 1
    };
  },
  watch: {
    selectedBook(newBook) {
      this.updateChapterCount(newBook);
    }
  },
 methods: {
    updateChapterCount(bookAbbr) {
      const book = books.find(b => b.abbr === bookAbbr);
      if (book) {
        this.chapterCount = book.chapters;
      }
    },
    onChapterChange() {
      this.$emit('chapter-selected', this.selectedChapterNum);
    }
  },
  mounted() {
    this.updateChapterCount(this.selectedBook);
  }
};
</script>

<style scoped>
.chapter-selector {
  margin-bottom: 15px;
}

select {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  min-width: 100px;
}
</style>
