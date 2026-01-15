# 🌐 JavaScript: The Language of the Web

**Professor:** *Opens a web browser and inspects the console.*
"If C is the engine room, JavaScript is the storefront. It runs everywhere—your phone, your laptop, your fridge. It started as a toy language for browsers but has grown into a giant. It is asynchronous, dynamic, and everywhere."

---

## 🟢 Module 1: Browser Basics (Beginner)

### 1.1 Variables
Use `let` and `const`. Avoid `var` (it's the old way).
```javascript
const pi = 3.14; // Cannot change
let count = 0;   // Can change
```

### 1.2 The DOM (Document Object Model)
JavaScript sees the HTML page as a tree of objects.
```javascript
// Change the text of an element
document.getElementById("title").innerText = "Hello JS!";
```

### 1.3 Functions
```javascript
function greet(name) {
    return `Hello, ${name}`;
}
// Arrow syntax (Modern)
const add = (a, b) => a + b;
```

---

## 🟡 Module 2: Async & The Event Loop (Intermediate)

### 2.1 Callbacks & Promises
JavaScript doesn't wait. It keeps running.
```javascript
console.log("Start");

setTimeout(() => {
    console.log("Wait for me!");
}, 1000);

console.log("End");
// Output: Start -> End -> Wait for me!
```

### 2.2 Async / Await
Making async code look synchronous.
```javascript
async function getData() {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    console.log(data);
}
```

---

## 🟠 Module 3: Modern JS & Node.js

### 3.1 Node.js
Running JS outside the browser (Backend).
```javascript
const fs = require('fs');
fs.writeFileSync('note.txt', 'JS on the server!');
```

### 3.2 Frameworks
*   **React/Vue:** Building UIs with components.
*   **Express:** Building web servers.

---

## 🎓 Professor's Project
"The web is interactive.
**Task:** Create a simple HTML button. When you click it, use JavaScript to fetch a random joke from an API and display it on the page."

---

## 📚 Official Documentation & Resources
*   [MDN Web Docs (Mozilla)](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - The best JavaScript documentation on the internet.
*   [Node.js Docs](https://nodejs.org/en/docs/) - Official reference for server-side JS.
*   [ECMAScript Specification](https://tc39.es/ecma262/) - The official standard (very technical).