<template>
  <div class="chapter-viewer">
    <div v-if="bibleData && bibleData[`${selectedBook}${parseInt(selectedChapter)}`]">
      <h3>{{ books.find(book => book.abbr == selectedBook)?.name || '' }} 第 {{ selectedChapter }} 章</h3>
      <div class="verses">
        <p v-for="(verse, index) in bibleData[`${selectedBook}${parseInt(selectedChapter)}`]" :key="index"
          class="verse">
          <span class="verse-number">
            {{ getVerseNumber(verse) }}
          </span>
          <span class="verse-text" v-html="getHighlightedText(getVerseText(verse))">
          </span>
        </p>
      </div>
    </div>
    <div v-else>Loading...</div>
  </div>
</template>

<script>
import { ref, reactive, toRefs, computed, onMounted, watch } from 'vue';
import books from '../assets/books.json';
import bible_cuv from '../assets/bible_cuv.json';
import bible_ccb from '../assets/bible_ccb.json';
import bible_cunp from '../assets/bible_cunp.json';

export default {
  props: {
    selectedBook: {
      type: String,
      required: true
    },
    selectedVersion: {
      type: String,
      required: true,
      default: 'cuv'
    },
    selectedChapter: {
      type: Number,
      required: false,
      default: 1
    },
    highlightKeyword: {
      type: String,
      default: ''
    }
  },
  setup(props) {
    const bibleData = computed(() => {
      switch (props.selectedVersion) {
        case 'cuv':
          return bible_cuv;
        case 'ccb':
          return bible_ccb;
        case 'cunp':
          return bible_cunp;
        default:
          return bible_cuv;
      }
    });

    // 取得節號
    const getVerseNumber = (verse) => {
      const match = verse.match(/^(\d+(-\d+)?\.)/); // 匹配節號（如 "1." 或 "1-2."）
      return match ? match[1] : ''; // 如果匹配成功，返回節號，否則返回空字串
    };

    // 取得節內容
    const getVerseText = (verse) => {
      return verse.replace(/^(\d+(-\d+)?\.)\s*/, ''); // 移除節號，返回剩餘的內容
    };

    // 高亮關鍵字
    const getHighlightedText = (text) => {
      if (!props.highlightKeyword) return text;
      const regex = new RegExp(`(${props.highlightKeyword})`, 'g');
      return text.replace(regex, '<span class="highlight">$1</span>');
    };

    return {
      books,
      bibleData,
      getVerseNumber,
      getVerseText,
      getHighlightedText
    };
  }
};
</script>

<style scoped>
.chapter-viewer {
  margin-top: 20px;
}

.chapter-content {
  text-align: left;
  margin-top: 20px;
  padding: 15px;
  background-color: #f9f9f9;
  border-radius: 5px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.chapter-content h3 {
  font-weight: bold;
  margin-bottom: 20px;
  text-align: left;
  color: #333;
}

.verses {
  line-height: 1.6;
  text-align: left;
  /* 新增靠左對齊 */
}

.verse {
  margin: 10px 0;
  display: flex;
}

.verse-number {
  font-weight: bold;
  color: #666;
  min-width: 25px;
  margin-right: 5px;
  /* 禁止選取節號 */
  user-select: none;
}

.verse-text {
  flex: 1;
}

:deep(.highlight) {
  background-color: yellow;
  font-weight: bold;
}
</style>
