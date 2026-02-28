<!-- BookSelector.vue -->
<template>
  <div class="book-selector" ref="container">
    <div class="selector-container">
      <label for="book-input">書卷：</label>
      <div class="combobox-wrapper">
        <input
          id="book-input"
          ref="input"
          v-model="inputText"
          autocomplete="off"
          placeholder="請輸入或選擇書卷"
          @focus="openDropdown"
          @input="onInput"
          @keydown.down.prevent="highlightNext"
          @keydown.up.prevent="highlightPrev"
          @keydown.enter.prevent="selectHighlighted"
          @keydown.esc="closeDropdown"
        />
        <span class="combobox-arrow" @mousedown.prevent="toggleDropdown">▾</span>
        <div v-if="isOpen" class="dropdown">
          <template v-if="flatFiltered.length > 0">
            <template v-for="(group, gi) in filteredGroups" :key="gi">
              <div v-if="group.books.length > 0" class="group-label">{{ group.name }}</div>
              <div
                v-for="book in group.books"
                :key="book.abbr"
                class="dropdown-item"
                :class="{ highlighted: highlightedAbbr === book.abbr, selected: selectedBook === book.abbr }"
                @mousedown.prevent="selectBook(book)"
              >
                {{ book.name }}
              </div>
            </template>
          </template>
          <div v-else class="no-result">找不到符合的書卷</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import books from '../assets/books.json';

const bookGroups = [
  { name: '摩西五經', books: books.slice(0, 5) },
  { name: '歷史書', books: books.slice(5, 17) },
  { name: '詩歌智慧書', books: books.slice(17, 22) },
  { name: '大先知書', books: books.slice(22, 27) },
  { name: '小先知書', books: books.slice(27, 39) },
  { name: '福音書', books: books.slice(39, 43) },
  { name: '使徒行傳', books: books.slice(43, 44) },
  { name: '保羅書信', books: books.slice(44, 57) },
  { name: '一般書信', books: books.slice(57, 64) },
  { name: '啟示錄', books: books.slice(64) }
];

export default {
  props: {
    selectedVersion: {
      type: String,
      default: 'cuv'
    },
    book: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      books,
      bookGroups,
      selectedBook: '',
      inputText: '',
      isOpen: false,
      highlightedAbbr: null,
    };
  },
  computed: {
    filteredGroups() {
      const q = this.inputText.trim();
      if (!q) return bookGroups;
      return bookGroups.map(g => ({
        ...g,
        books: g.books.filter(b => b.name.includes(q) || b.abbr.includes(q))
      })).filter(g => g.books.length > 0);
    },
    flatFiltered() {
      return this.filteredGroups.flatMap(g => g.books);
    }
  },
  watch: {
    book(newVal) {
      if (newVal) {
        this.selectedBook = newVal;
        const found = books.find(b => b.abbr === newVal);
        this.inputText = found ? found.name : '';
      }
    }
  },
  mounted() {
    document.addEventListener('mousedown', this.onOutsideClick);
  },
  beforeUnmount() {
    document.removeEventListener('mousedown', this.onOutsideClick);
  },
  methods: {
    onInput() {
      this.isOpen = true;
      this.highlightedAbbr = null;
    },
    openDropdown() {
      this.isOpen = true;
    },
    closeDropdown() {
      this.isOpen = false;
      // 若輸入文字不是有效書卷名稱，恢復原本選擇
      const found = books.find(b => b.name === this.inputText || b.abbr === this.inputText);
      if (!found) {
        const current = books.find(b => b.abbr === this.selectedBook);
        this.inputText = current ? current.name : '';
      }
    },
    toggleDropdown() {
      if (this.isOpen) {
        this.closeDropdown();
      } else {
        this.isOpen = true;
        this.$nextTick(() => this.$refs.input.focus());
      }
    },
    selectBook(book) {
      this.selectedBook = book.abbr;
      this.inputText = book.name;
      this.isOpen = false;
      this.highlightedAbbr = null;
      this.$emit('book-selected', book.abbr);
    },
    highlightNext() {
      const list = this.flatFiltered;
      if (!list.length) return;
      const idx = list.findIndex(b => b.abbr === this.highlightedAbbr);
      this.highlightedAbbr = list[(idx + 1) % list.length].abbr;
      this.isOpen = true;
    },
    highlightPrev() {
      const list = this.flatFiltered;
      if (!list.length) return;
      const idx = list.findIndex(b => b.abbr === this.highlightedAbbr);
      this.highlightedAbbr = list[(idx - 1 + list.length) % list.length].abbr;
      this.isOpen = true;
    },
    selectHighlighted() {
      if (this.highlightedAbbr) {
        const book = books.find(b => b.abbr === this.highlightedAbbr);
        if (book) this.selectBook(book);
      }
    },
    onOutsideClick(e) {
      if (this.$refs.container && !this.$refs.container.contains(e.target)) {
        this.closeDropdown();
      }
    }
  }
};
</script>

<style scoped>
.combobox-wrapper {
  position: relative;
  display: inline-block;
}

#book-input {
  padding: 8px 28px 8px 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  min-width: 150px;
  font-size: 14px;
}

.combobox-arrow {
  position: absolute;
  right: 6px;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
  color: #666;
  pointer-events: all;
  user-select: none;
}

.dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  min-width: 100%;
  max-height: 260px;
  overflow-y: auto;
  background: #fff;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  z-index: 1000;
}

.group-label {
  padding: 4px 10px;
  font-size: 11px;
  font-weight: bold;
  color: #888;
  background: #f5f5f5;
  border-top: 1px solid #eee;
}

.dropdown-item {
  padding: 7px 14px;
  cursor: pointer;
  font-size: 14px;
}

.dropdown-item:hover,
.dropdown-item.highlighted {
  background: #e8f0fe;
}

.dropdown-item.selected {
  font-weight: bold;
  color: #1a56db;
}

.no-result {
  padding: 10px 14px;
  color: #aaa;
  font-size: 13px;
}

.selector-container {
  display: flex;
  align-items: center;
  gap: 10px;
}

@media (max-width: 600px) {
  .selector-container {
    flex-direction: column;
    align-items: flex-start;
  }

  .combobox-wrapper,
  #book-input {
    width: 100%;
  }
}
</style>
