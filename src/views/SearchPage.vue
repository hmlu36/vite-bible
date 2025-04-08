<!-- SearchPage.vue -->
<template>
  <div class="search-page">
    <h1>聖經搜尋</h1>
    <div class="search-container">
      <div class="search-controls">
        <label for="version">版本：</label>
        <select id="version" v-model="selectedVersion">
          <option v-for="version in versions" :key="version.id" :value="version.id">
            {{ version.name }}
          </option>
        </select>
        
        <div class="search-input">
          <label for="keyword">關鍵字：</label>
          <input 
            id="keyword" 
            v-model="keyword" 
            @input="debounceSearch"
            placeholder="請輸入搜尋關鍵字..."
          />
        </div>
      </div>
      
      <div v-if="loading" class="loading">
        搜尋中...
      </div>
      
      <div v-else-if="searchResults.length > 0" class="search-results">
        <h3>搜尋結果 ({{ searchResults.length }} 筆)</h3>
        <ul>
          <li v-for="(result, index) in searchResults" :key="index" class="result-item">
            <div class="result-reference">{{ result.book }} {{ result.chapter }}:{{ result.verse }}</div>
            <div class="result-text" v-html="highlightKeyword(result.text)"></div>
          </li>
        </ul>
      </div>
      
      <div v-else-if="keyword && !loading" class="no-results">
        找不到符合 "{{ keyword }}" 的經文
      </div>
      
      <div class="navigation">
        <router-link to="/" class="nav-link">返回閱讀</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchPage',
  data() {
    return {
      versions: [
        { id: "cuv", name: "中文和合本" },
        { id: "ccb", name: "當代譯本" }
      ],
      selectedVersion: "cuv",
      keyword: '',
      searchResults: [],
      loading: false,
      debounceTimeout: null
    };
  },
  methods: {
    debounceSearch() {
      clearTimeout(this.debounceTimeout);
      if (this.keyword.length < 2) {
        this.searchResults = [];
        return;
      }
      
      this.debounceTimeout = setTimeout(() => {
        this.searchBible();
      }, 500);
    },
    
    async searchBible() {
      if (!this.keyword || this.keyword.length < 2) return;
      
      this.loading = true;
      this.searchResults = [];
      
      try {
        const booksModule = await import('../assets/books.json');
        const books = booksModule.default;
        
        // 動態載入聖經資料
        const bibleModule = await import(`../assets/bible_${this.selectedVersion}.json`);
        const bibleData = bibleModule.default;
        
        // 搜尋所有經文
        for (const book of books) {
          const bookAbbr = book.abbr;
          const chaptersCount = book.chapters;
          
          for (let chapter = 1; chapter <= chaptersCount; chapter++) {
            const key = `${bookAbbr}${chapter}`;
            const verses = bibleData[key];
            
            if (verses) {
              verses.forEach((text, verseIndex) => {
                if (text.includes(this.keyword)) {
                  this.searchResults.push({
                    book: book.name,
                    chapter,
                    verse: verseIndex + 1,
                    text
                  });
                }
              });
            }
          }
        }
      } catch (error) {
        console.error('搜尋錯誤:', error);
      } finally {
        this.loading = false;
      }
    },
    
    highlightKeyword(text) {
      if (!this.keyword) return text;
      const regex = new RegExp(`(${this.keyword})`, 'g');
      return text.replace(regex, '<span class="highlight">$1</span>');
    }
  },
  watch: {
    selectedVersion() {
      if (this.keyword) {
        this.searchBible();
      }
    }
  }
};
</script>

<style scoped>
.search-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  text-align: center;
  margin-bottom: 30px;
}

.search-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.search-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 20px;
  align-items: baseline;
}

.search-controls > div,
.search-controls > label {
  display: inline-flex;
  align-items: center;
}

.search-controls > label {
  width: 5em;
  text-align: right;
  white-space: nowrap;
}

.search-input label {
  width: 5em;
  text-align: right;
  white-space: nowrap;
}

.search-input {
  flex: 1;
  min-width: 150px; /* Reduce minimum width */
}

input {
  padding: 8px;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 4px;
}

select {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.search-results {
  margin-top: 20px;
}

.result-item {
  margin-bottom: 15px;
  padding: 10px;
  border-bottom: 1px solid #eee;
  text-align: left;
}

.result-reference {
  font-weight: bold;
  margin-bottom: 5px;
}

.loading, .no-results {
  text-align: center;
  margin: 20px 0;
  color: #666;
}

.navigation {
  margin-top: 30px;
  text-align: center;
}

.nav-link {
  display: inline-block;
  padding: 8px 16px;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 4px;
}

.nav-link:hover {
  background-color: #45a049;
}

:deep(.highlight) {
  background-color: yellow;
  font-weight: bold;
}
</style>
