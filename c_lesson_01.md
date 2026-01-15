# 💻 C Programming: The Mother of Modern Languages

**Professor:** *Rolls up sleeves and points to a memory diagram.*
"Welcome to the engine room! C is where you learn how computers *really* work. It is not about fancy tricks; it is about raw power and control. If Python is driving an automatic car, C is rebuilding the transmission. Let's get our hands dirty."

---

## 🟢 Module 1: The Basics (Beginner)

### 1.1 Structure of a C Program
Every C program needs a `main` function.
```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0; // Return 0 means "Success"
}
```

### 1.2 Variables & Types
C is statically typed. You must declare the type!
```c
int age = 25;
float height = 5.9;
char grade = 'A';
```

### 1.3 Control Flow
Similar to other languages, but watch your syntax.
```c
if (age >= 18) {
    printf("Adult\n");
} else {
    printf("Minor\n");
}

for (int i = 0; i < 5; i++) {
    printf("%d ", i);
}
```

---

## 🟡 Module 2: Memory Mastery (Intermediate)

### 2.1 Pointers (The Heart of C)
A pointer is a variable that stores the **address** of another variable.
```c
int x = 10;
int *ptr = &x; // ptr holds the address of x

printf("%p", ptr); // Prints a memory address (e.g., 0x7ffee...)
printf("%d", *ptr); // Dereference: Go to that address and get the value (10)
```

### 2.2 Arrays & Strings
In C, strings are just arrays of characters ending with a null terminator `\0`.
```c
char name[] = "Alice"; // 'A', 'l', 'i', 'c', 'e', '\0'
int numbers[3] = {1, 2, 3};
```

### 2.3 Structs
Grouping related data.
```c
struct Point {
    int x;
    int y;
};

struct Point p1;
p1.x = 10;
p1.y = 20;
```

---

## 🟠 Module 3: System Level (Advanced)

### 3.1 Dynamic Memory (The Heap)
You must ask for memory manually and **give it back**.
```c
#include <stdlib.h>

int *arr = (int*) malloc(5 * sizeof(int)); // Allocate array of 5 ints
if (arr != NULL) {
    arr[0] = 100;
}
free(arr); // CRITICAL: Prevent memory leaks!
```

### 3.2 Function Pointers
Variables that store functions.
```c
void say_hello() { printf("Hello!"); }
void (*func_ptr)() = say_hello;
func_ptr(); // Calls say_hello
```

### 3.3 Bitwise Operations
Manipulating individual bits.
```c
int flags = 0b0010;
int mask = 0b0001;
int result = flags | mask; // 0b0011 (Bitwise OR)
```

---

## 🎓 Professor's Challenge
"To truly learn C, you must manage your own memory.
**Task:** Write a program that uses `malloc` to create an array of numbers based on user input, sums them up, and then `free`s the memory."

---

## 📚 Official Documentation & Resources
*   [cppreference.com (C)](https://en.cppreference.com/w/c) - The best reference for C (and C++) standards.
*   [ISO/IEC 9899](https://www.iso.org/standard/74528.html) - The official C standard (paid, but drafts are free online).
*   [The C Programming Language (K&R)](https://en.wikipedia.org/wiki/The_C_Programming_Language) - The classic book by the creators of C.