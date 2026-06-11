# 貢獻指南 (Contributing Guide)

感謝您對本專案的興趣！我們歡迎各種形式的貢獻。

Thank you for your interest in this project! We welcome contributions in various forms.

## 🤝 貢獻方式 (Ways to Contribute)

### 1. 報告 Bug (Report Bugs)

如果您發現了 Bug，請提交一個 GitHub Issue：

- 描述問題的詳細信息
- 提供復現問題的步驟
- 分享預期行為和實際行為
- 包括您的環境信息（OS、Browser、Node.js 版本等）

### 2. 建議新功能 (Suggest Features)

新功能的建議總是受歡迎的：

- 清楚地描述功能的用途
- 提供使用案例和好處
- 考慮與現有功能的相容性

### 3. 提交代碼 (Submit Code)

我們歡迎 Pull Request！

## 📋 貢獻流程 (Contribution Process)

### Step 1: Fork 倉庫

```bash
# 點擊 GitHub 頁面上的 "Fork" 按鈕
```

### Step 2: 克隆您的 Fork

```bash
git clone https://github.com/YOUR_USERNAME/vite-bible.git
cd vite-bible
```

### Step 3: 建立特性分支

```bash
git checkout -b feature/your-feature-name
# 或用於修復 bug
git checkout -b fix/bug-description
```

### Step 4: 安裝依賴

```bash
npm install
```

### Step 5: 進行更改

進行您的代碼更改。請遵循以下準則：

- **代碼風格** - 保持與現有代碼一致
- **命名規範** - 使用清晰、有意義的名稱
- **注釋** - 為複雜邏輯添加必要的注釋
- **類型安全** - 使用 TypeScript 類型註解

### Step 6: 測試您的更改

```bash
# 啟動開發伺服器並測試您的更改
npm run dev

# 構建生產版本
npm run build

# 預覽生產構建
npm run preview
```

### Step 7: 提交您的更改

```bash
# 暫存更改
git add .

# 使用清晰的提交訊息
git commit -m "feat: add new feature" 
# 或
git commit -m "fix: resolve issue with ..."
```

### Step 8: 推送到您的 Fork

```bash
git push origin feature/your-feature-name
```

### Step 9: 提交 Pull Request

1. 訪問原始倉庫
2. 點擊 "New Pull Request" 按鈕
3. 選擇您的分支進行比較
4. 填寫 PR 描述（包括更改內容、測試方式等）
5. 提交 PR

## 📝 提交訊息約定 (Commit Message Convention)

請使用以下格式提交訊息以保持歷史清晰：

```
type(scope): subject

body

footer
```

**Type:**
- `feat` - 新功能
- `fix` - Bug 修復
- `docs` - 文件更新
- `style` - 代碼格式（不影響功能）
- `refactor` - 代碼重構
- `test` - 添加或修改測試
- `chore` - 構建過程、依賴管理等

**Example:**
```
feat(search): add phrase search capability

Add support for phrase search in quotes.
Users can now search for exact phrases using quotes.

Closes #123
```

## 🎯 代碼準則 (Code Guidelines)

### Vue 3 與 TypeScript

- 使用 `<script setup>` 語法
- 為所有 props 和 emits 添加類型
- 使用 TypeScript 進行類型檢查

### 文件組織

```
src/
├── components/     # 可復用組件
│   ├── Button.vue
│   └── SearchBar.vue
├── views/         # 頁面組件
│   ├── Home.vue
│   └── SearchPage.vue
├── types/         # TypeScript 類型定義
├── utils/         # 工具函數
└── assets/        # 靜態資源
```

### 樣式

- 使用 BEM 命名約定
- 優先使用 CSS 變數
- 確保移動設備響應性

### 無障礙性 (Accessibility)

- 為交互元素添加適當的 ARIA 標籤
- 確保鍵盤導航可用
- 檢查色彩對比度

## 🧪 測試 (Testing)

雖然此專案尚無正式的測試套件，但請確保：

- 手動測試您的更改
- 在不同瀏覽器中測試
- 在移動設備上測試
- 驗證您的更改不會破壞現有功能

## 📚 文件更新 (Documentation)

如果您的更改影響用戶體驗或 API：

- 更新相關的 README 或指南
- 在 USAGE_GUIDE.md 中添加新功能說明
- 為新代碼添加代碼注釋

## 🐛 Bug 修復檢查清單 (Bug Fix Checklist)

- [ ] 確認 Bug 已復現
- [ ] 進行代碼修改
- [ ] 測試修復
- [ ] 添加或更新相關文件
- [ ] 提交清晰的 PR 說明問題和解決方案

## ✨ 新功能檢查清單 (New Feature Checklist)

- [ ] 功能符合專案目標
- [ ] 代碼遵循準則
- [ ] 進行了充分測試
- [ ] 更新了相關文件
- [ ] 提交了清晰的 PR 說明

## 🚀 部署 (Deployment)

主要提交將自動構建並部署。確保：

- 所有測試通過
- 代碼遵循準則
- 文件已更新

## 📞 需要幫助？ (Need Help?)

- 查看現有的 Issues 和 Discussions
- 在 PR 中提出問題
- 參與項目 Discussions

## 🙏 致謝 (Acknowledgments)

感謝所有貢獻者的支持！每個貢獻，無論大小，都幫助使本專案變得更好。

---

**Happy coding! 編碼愉快！** 💻✨
