<template>
  <Tag class="p-mr-2" icon="pi pi-link" value="讀經小幫手" />
  <div class="content-section implementation">
    <TabMenu :model="items" />
    <router-view />
  </div>
</template>

<script>
import { provide, ref, readonly } from "vue";
import bibleJson from "./data/bible.json";
import booksJson from "./data/books.json";

export default {
  setup() {
    const items = ref([
      { label: "讀經", icon: "pi pi-fw pi-home", to: "/" },
      { label: "查詢", icon: "pi pi-fw pi-calendar", to: "/query" },
      /*{ label: "關於", icon: "pi pi-fw pi-pencil", to: "/about" },*/
    ]);
    provide("bible", readonly(bibleJson));
    provide("books", readonly(booksJson));

    return { items };
  },
};
</script>
<style>
@import url(https://fonts.googleapis.com/earlyaccess/cwtexfangsong.css);
/*@import url(https://fonts.googleapis.com/earlyaccess/cwtexming.css);
/*@import url(https://fonts.googleapis.com/earlyaccess/cwtexyen.css);*/
/*@import url(https://fonts.googleapis.com/earlyaccess/notosanstc.css);*/

@media (min-width: 1025px) {
  *,
  ::placeholder {
    font-family: "cwTeXFangSong", sans-serif;
    font-size: 20px;
    /*font-family: 'cwTeXMing', sans-serif;*/
    /*font-family: 'cwTeXYen', sans-serif;*/
    /*font-family: 'Noto Sans TC', sans-serif;*/
  }
}

@media (max-width: 1025px) {
  *,
  ::placeholder {
    font-size: 20px;
  }
}

.text-right {
  text-align: right;
}
</style>
