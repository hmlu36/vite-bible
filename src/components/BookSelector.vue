<!-- BookSelector.vue -->
<template>
  <div class="book-selector">
    <div class="selector-container">
      <label for="book">書卷：</label>
      <select id="book" v-model="selectedBook" @change="onBookChange">
        <option value="">請選擇書卷</option>
        <optgroup v-for="(group, index) in bookGroups" :key="index" :label="group.name">
          <option v-for="book in group.books" :key="book.abbr" :value="book.abbr">
            {{ book.name }}
          </option>
        </optgroup>
      </select>
    </div>
  </div>
</template>

<script>
import books from '../assets/books.json';

export default {
  props: {
    selectedVersion: {
      type: String,
      default: 'cuv'
    },
    book: {
      type: String,
      default: '創'
    }
  },
  data() {
    return {
      books: books,
      selectedBook: this.book,
      bookGroups: [
        {
          name: '摩西五經',
          books: books.slice(0, 5)
        },
        {
          name: '歷史書',
          books: books.slice(5, 17)
        },
        {
          name: '詩歌智慧書',
          books: books.slice(17, 22)
        },
        {
          name: '大先知書',
          books: books.slice(22, 27)
        },
        {
          name: '小先知書',
          books: books.slice(27, 39)
        },
        {
          name: '福音書',
          books: books.slice(39, 43)
        },
        {
          name: '使徒行傳',
          books: books.slice(43, 44)
        },
        {
          name: '保羅書信',
          books: books.slice(44, 57)
        },
        {
          name: '一般書信',
          books: books.slice(57, 64)
        },
        {
          name: '啟示錄',
          books: books.slice(64)
        }
      ]
    };
  },
  watch: {
    book(newVal) {
      if (newVal) {
        this.selectedBook = newVal;
      }
    }
  },
  mounted() {
    // 只有在沒有選擇書卷時才設置默認值
    if (!this.selectedBook) {
      this.selectedBook = '創';
      this.onBookChange();
    }
  },
  methods: {
    onBookChange() {
      this.$emit('book-selected', this.selectedBook);
    }
  }
};
</script>

<style scoped>
.book-selector {
  margin-bottom: 15px;
}

.selector-container {
  display: flex;
  align-items: center;
  gap: 10px;
}

select {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  min-width: 150px;
}

@media (max-width: 600px) {
  .selector-container {
    flex-direction: column;
    align-items: flex-start;
  }
  
  select {
    width: 100%;
  }
}
</style>
