<!-- Home.vue -->
<template>
  <div class="home">
    <h1>聖經閱讀</h1>
    <div class="bible-container">
      <div class="selectors">
        <VersionSelector @version-changed="updateVersion" />
        <BookSelector @book-selected="updateBook" />
        <ChapterSelector :selectedBook="selectedBook" @chapter-selected="updateChapter" />
      </div>
      <ChapterViewer :selectedVersion="selectedVersion" :selectedBook="selectedBook"
        :selectedChapter="Number(selectedChapter)" :key="`${selectedBook}${selectedVersion}${selectedChapter}`" />
    </div>
  </div>
</template>

<script>
import VersionSelector from '../components/VersionSelector.vue';
import BookSelector from '../components/BookSelector.vue';
import ChapterViewer from '../components/ChapterViewer.vue';
import ChapterSelector from '../components/ChapterSelector.vue';

export default {
  name: 'Home',
  components: {
    VersionSelector,
    BookSelector,
    ChapterViewer,
    ChapterSelector
  },
  data() {
    return {
      selectedVersion: 'cuv',
      selectedBook: '創',
      selectedChapter: 1,
    };
  },
  methods: {
    updateVersion(version) {
      this.selectedVersion = version;
    },
    updateBook(book) {
      this.selectedBook = book;
    },
    updateChapter(chapter) {
      this.selectedChapter = chapter;
    }
  },
};
</script>

<style scoped>
.home {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  text-align: center;
  margin-bottom: 30px;
}

.bible-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.selectors {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  align-items: baseline;
  /* Change to baseline alignment */
}

.selectors>* {
  flex: 1;
  /* Distribute space evenly */
  min-width: 150px;
  /* Minimum width for each selector */
}

@media (max-width: 600px) {
  .selectors {
    flex-direction: column;
    gap: 10px;
  }
}
</style>
