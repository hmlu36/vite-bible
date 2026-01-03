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
    },
    chapter: {
      type: Number,
      default: 1
    }
  },
  data() {
    return {
      chapterCount: 0,
      selectedChapterNum: this.chapter
    };
  },
  watch: {
    selectedBook(newBook) {
      this.updateChapterCount(newBook);
      // 當書卷改變時，如果沒有傳入特定的章節（例如從父組件），重置為第一章
      // 但如果是父組件傳入的改變，這裡可能不需要額外處理，因為下面的 watch chapter 會處理
      // 不過通常換書卷會重置為第一章，除非外部有強制指定
    },
    chapter(newVal) {
      if (newVal) {
        this.selectedChapterNum = newVal;
      }
    }
  },
 methods: {
    updateChapterCount(bookAbbr) {
      const book = books.find(b => b.abbr === bookAbbr);
      if (book) {
        this.chapterCount = book.chapters;
        // 確保選擇的章節在有效範圍內
        if (this.selectedChapterNum > this.chapterCount) {
          this.selectedChapterNum = 1;
          this.onChapterChange();
        }
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
