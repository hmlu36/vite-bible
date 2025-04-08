<template>
  <div id="app">
    <header>
      <nav>
        <router-link to="/">聖經閱讀</router-link> | 
        <router-link to="/search">搜尋經文</router-link>
      </nav>
    </header>
    
    <main>
      <router-view />
    </main>
    
    <footer>
      <p>聖經閱讀應用 &copy; {{ new Date().getFullYear() }}</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
#app {
  font-family: 'Microsoft JhengHei', 'PingFang TC', 'Heiti TC', 'Apple LiGothic', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  padding: 0;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

body {
  margin: 0;
  padding: 0;
}

header {
  background-color: #f8f9fa;
  padding: 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

nav {
  padding: 10px 0;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  margin: 0 10px;
}

nav a.router-link-exact-active {
  color: #42b983;
}

main {
  flex: 1;
  padding: 20px;
}

footer {
  background-color: #f8f9fa;
  padding: 15px;
  font-size: 0.9em;
  color: #6c757d;
}
</style>
