<!-- VersionSelector.vue -->
<template>
  <div>
    <label for="version">版本：</label>
    <select id="version" v-model="selectedVersion" @change="updateVersion">
      <option v-for="version in versions" :key="version.id" :value="version.id">
        {{ version.name }}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  data() {
    return {
      versions: [
        { id: "cuv", name: "中文和合本" },
        { id: "cunp", name: "新標點和合本-神版" },
        { id: "ccb", name: "當代譯本" },
      ],
      selectedVersion: "cuv"
    };
  },
  methods: {
    updateVersion() {
      this.$emit("version-changed", this.selectedVersion);
    }
  }
};
</script>
