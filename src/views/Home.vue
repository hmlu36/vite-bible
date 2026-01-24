<!-- Home.vue -->
<template>
  <div class="home">
    <h1>聖經閱讀</h1>
    <div class="bible-container">
      <div class="selectors">
        <VersionSelector @version-changed="updateVersion" />
        <BookSelector :book="selectedBook" @book-selected="updateBook" />
        <ChapterSelector :selectedBook="selectedBook" :chapter="Number(selectedChapter)" @chapter-selected="updateChapter" />
      </div>
      <div class="navigation-buttons">
        <button @click="previousChapter" :disabled="!canGoPrevious" class="nav-btn" title="上一章">
          <span class="nav-icon">‹</span>
        </button>
        <button @click="nextChapter" :disabled="!canGoNext" class="nav-btn" title="下一章">
          <span class="nav-icon">›</span>
        </button>
      </div>
      <ChapterViewer :selectedVersion="selectedVersion" :selectedBook="selectedBook"
        :selectedChapter="Number(selectedChapter)" :highlightKeyword="highlightKeyword"
        :key="`${selectedBook}${selectedVersion}${selectedChapter}`" />
    </div>
  </div>
</template>

<script>
import VersionSelector from '../components/VersionSelector.vue';
import BookSelector from '../components/BookSelector.vue';
import ChapterViewer from '../components/ChapterViewer.vue';
import ChapterSelector from '../components/ChapterSelector.vue';
import booksData from '../assets/books.json';

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
      highlightKeyword: '',
      books: booksData,
    };
  },
  computed: {
    currentBookIndex() {
      return this.books.findIndex(book => book.abbr === this.selectedBook);
    },
    currentBook() {
      return this.books[this.currentBookIndex];
    },
    canGoPrevious() {
      // 如果不是第一本書的第一章，就可以往前
      return !(this.currentBookIndex === 0 && this.selectedChapter === 1);
    },
    canGoNext() {
      // 如果不是最後一本書的最後一章，就可以往後
      const isLastBook = this.currentBookIndex === this.books.length - 1;
      const isLastChapter = this.selectedChapter === this.currentBook.chapters;
      return !(isLastBook && isLastChapter);
    }
  },
  created() {
    // 從 URL 參數讀取書卷和章節
    const { book, chapter, version, highlight } = this.$route.query;
    if (book) {
      this.selectedBook = book;
    }
    if (chapter) {
      this.selectedChapter = Number(chapter);
    }
    if (version) {
      this.selectedVersion = version;
    }
    if (highlight) {
      this.highlightKeyword = highlight;
    }
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
    },
    previousChapter() {
      if (!this.canGoPrevious) return;
      
      if (this.selectedChapter > 1) {
        // 在同一本書中往前一章
        this.selectedChapter--;
      } else {
        // 跳到上一本書的最後一章
        const previousBook = this.books[this.currentBookIndex - 1];
        this.selectedBook = previousBook.abbr;
        this.selectedChapter = previousBook.chapters;
      }
    },
    nextChapter() {
      if (!this.canGoNext) return;
      
      if (this.selectedChapter < this.currentBook.chapters) {
        // 在同一本書中往後一章
        this.selectedChapter++;
      } else {
        // 跳到下一本書的第一章
        const nextBook = this.books[this.currentBookIndex + 1];
        this.selectedBook = nextBook.abbr;
        this.selectedChapter = 1;
      }
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

.navigation-buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.nav-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 50px;
  height: 50px;
  background: rgba(255, 255, 255, 0.9);
  color: #2c3e50;
  border: 2px solid rgba(44, 62, 80, 0.2);
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.nav-icon {
  font-size: 28px;
  font-weight: bold;
  line-height: 1;
  color: #2c3e50;
}

.nav-text {
  font-size: 16px;
}

.nav-btn:hover:not(:disabled) {
  background: rgba(52, 152, 219, 0.15);
  border-color: rgba(52, 152, 219, 0.5);
  transform: scale(1.1);
  box-shadow: 0 4px 12px rgba(52, 152, 219, 0.3);
}

.nav-btn:hover:not(:disabled) .nav-icon {
  color: #3498db;
}

.nav-btn:active:not(:disabled) {
  transform: scale(1.05);
}

.nav-btn:disabled {
  background: rgba(200, 200, 200, 0.3);
  border-color: rgba(200, 200, 200, 0.3);
  cursor: not-allowed;
  opacity: 0.4;
  box-shadow: none;
}

.nav-btn:disabled .nav-icon {
  color: #999;
}

@media (max-width: 600px) {
  .selectors {
    flex-direction: column;
    gap: 10px;
  }

  .navigation-buttons {
    gap: 15px;
  }

  .nav-btn {
    width: 45px;
    height: 45px;
  }

  .nav-icon {
    font-size: 24px;
  }

  .nav-text {
    display: none;
  }
}
</style>
