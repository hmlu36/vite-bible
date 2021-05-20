<template>
  <div class="card">
    <div class="p-fluid p-grid">
      <div class="p-md-2 p-col-12">
        <Dropdown
          v-model="startBookObj"
          :options="books"
          :filter="true"
          placeholder="開始"
          optionLabel="name"
        />
      </div>
      <div class="p-md-2 p-col-12">
        <Dropdown
          v-model="endBookObj"
          :options="books"
          :filter="true"
          placeholder="結束"
          optionLabel="name"
        />
      </div>
      <div class="p-md-2 p-col-12">
        <InputText v-model="queryObj" placeholder="關鍵字" />
      </div>
      <div class="p-md-2 p-col-12">
        <Button label="查詢" @click="query" />
      </div>
    </div>
    <Display source="query" :matchVerse="queryResult" />
  </div>
</template>
<script>
import { inject, ref, computed, reactive } from "vue";
import Display from "../components/Display.vue";

export default {
  components: {
    Display,
  },
  setup() {
    const startBookObj = ref(null);
    const endBookObj = ref(null);
    const queryObj = ref(null);
    const queryResult = ref([]);
    const books = inject("books");
    const bible = inject("bible");

    const query = () => {
      let startbook = !!startBookObj.value ? startBookObj.value.abbr : "";
      let endbook = !!endBookObj.value ? endBookObj.value.abbr : "";
      let queryField = !!queryObj.value ? queryObj.value : "";
      //console.log("startbook:" + startbook);
      //console.log("endbook:" + endbook);
      //console.log("queryField:" + queryObj.queryField);

      let startIndex = 0 || books.findIndex((book) => book.abbr === startbook);
      let endIndex = 0 || books.findIndex((book) => book.abbr === endbook);

      // 起始章節沒選
      if (startIndex == -1) {
        startIndex = 0;
      }

      // 結束章節沒選
      if (endIndex == -1) {
        endIndex = books.length;
      }

      if (startIndex > endIndex) {
        alert("開始書卷不能大於結束書卷");
      }
      if (!queryField) {
        alert("查詢欄位不可為空");
      } else {
        queryResult.value = [];
        // 書卷 loop
        books.slice(startIndex, endIndex + 1).forEach((item) => {
          // 章 loop
          for (let i = 1; i <= item.verse; i++) {
            // 節 loop
            //console.log(item.abbr + i);
            bible[item.abbr + i].forEach((verse, index) => {
              if (verse.indexOf(queryField) >= 0) {
                //console.log(verse);
                queryResult.value.push({
                  book: item.abbr,
                  chapter: i,
                  verse: index + 1,
                  content: verse.replace(
                    queryField,
                    `<span class="p-error">${queryField}</span>`
                  ),
                });
              }
            });
          }
        });
        //console.log(JSON.stringify(queryResult.value));
      }
    };

    return {
      books,
      startBookObj,
      endBookObj,
      queryObj,
      query,
      queryResult,
    };
  },
};
</script>
