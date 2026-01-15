# 🚀 C++ Programming: High Performance with High Abstraction

**Professor:** *Picks up a complex blueprint.*
"C gave us power. C++ gives us power *and* structure. It allows us to build massive systems—game engines, browsers, trading platforms—without losing our minds. We keep the speed of C but add 'Classes' and 'Templates' to manage complexity."

---

## 🟢 Module 1: Better C (Beginner)

### 1.1 IO Streams
No more `printf` (unless you want to). We use streams.
```cpp
#include <iostream>

int main() {
    std::cout << "Hello C++" << std::endl;
    int x;
    std::cin >> x; // Input
    return 0;
}
```

### 1.2 References
Safer than pointers. It's an alias for a variable.
```cpp
void addOne(int &ref) {
    ref++;
}

int a = 5;
addOne(a); // a becomes 6
```

### 1.3 The Standard Library (STL)
Don't write your own arrays. Use Vectors.
```cpp
#include <vector>
std::vector<int> nums = {1, 2, 3};
nums.push_back(4);
```

---

## 🟡 Module 2: OOP & Memory (Intermediate)

### 2.1 Classes & RAII
**R**esource **A**cquisition **I**s **I**nitialization.
When an object is created (Constructor), we grab memory. When it goes out of scope (Destructor), we release it.
```cpp
class Game {
public:
    Game() { std::cout << "Game Started"; }  // Constructor
    ~Game() { std::cout << "Game Over"; }    // Destructor
};
```

### 2.2 Smart Pointers
Modern C++ avoids `malloc/free`.
```cpp
#include <memory>
// Automatically deletes itself when done. No leaks!
std::unique_ptr<int> ptr = std::make_unique<int>(10);
```

---

## 🟠 Module 3: Advanced Features

### 3.1 Templates
Write code that works for ANY type.
```cpp
template <typename T>
T add(T a, T b) {
    return a + b;
}

add(5, 10);      // Works for ints
add(5.5, 2.1);   // Works for floats
```

### 3.2 Move Semantics
Optimizing performance by "stealing" resources instead of copying them.
```cpp
std::vector<int> v1 = {1, 2, 3};
std::vector<int> v2 = std::move(v1); // v1 is now empty, v2 has the data. fast!
```

---

## 🎓 Professor's Advice
"C++ is a beast. Don't try to learn every feature at once. Focus on **Modern C++ (C++11 and newer)**.
**Goal:** Rewrite a C program using `std::vector` and `std::string` instead of raw arrays."

---

## 📚 Official Documentation & Resources
*   [cppreference.com (C++)](https://en.cppreference.com/w/cpp) - The gold standard community wiki.
*   [isocpp.org](https://isocpp.org/) - The official home of C++.
*   [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) - Best practices maintained by Bjarne Stroustrup (creator of C++) and Herb Sutter.