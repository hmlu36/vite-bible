<template>
  <div class="card">
    <div class="p-fluid p-grid">
      <div class="p-md-2 p-col-12">
        <Dropdown
          v-model="selectedBookObj"
          :options="books"
          optionLabel="name"
          :filter="true"
          placeholder="書"
          :showClear="true"
        />
      </div>
      <div class="p-md-2 p-col-12">
        <Dropdown
          v-model="selectedChapterObj"
          :options="chapters"
          :filter="true"
          optionLabel="label"
          placeholder="章"
          :showClear="true"
        />
      </div>
    </div>
    <Display source="home" :matchVerse="readBible" />
  </div>
</template>

<script>
import { inject, ref, computed } from "vue";
import Display from "../components/Display.vue";

export default {
  components: {
    Display,
  },
  setup() {
    const selectedBookObj = ref();
    const selectedChapterObj = ref();
    const books = inject("books");
    const bible = inject("bible");

    const chapters = computed(() =>
      selectedBookObj.value == null
        ? [{ label: "", value: null }]
        : [...Array(selectedBookObj.value.verse).keys()]
            .map((i) => ++i)
            .map((key) => {
              return { label: key, value: key };
            })
    );

    const readBible = computed(() => {
      if (!!selectedBookObj.value && !!selectedChapterObj.value) {
        let matchVerse = [];
        let selectedBook = selectedBookObj.value.abbr;
        let selectedChapter = selectedChapterObj.value.value;
        //console.log(selectedBook);
        //console.log(selectedChapter);
        bible[selectedBook + selectedChapter].forEach((verse, index) => {
          matchVerse.push({
            book: selectedBook,
            chapter: selectedChapter,
            verse: index + 1,
            content: verse,
          });
        });
        //console.log(JSON.stringify(matchVerse));
        return matchVerse;
      }
    });

    return {
      selectedBookObj,
      selectedChapterObj,
      books,
      chapters,
      readBible,
    };
  },
};
</script>
