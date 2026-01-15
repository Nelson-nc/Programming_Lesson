# 🖥️ OS Internals: The Ghost in the Machine

**Professor:** *Dims the lights and starts a projector showing a kernel diagram.*
"We know how to write code. But where does it live? The Operating System is the government of your computer. It manages resources, schedules tasks, and protects programs from each other. To be a master engineer, you must understand the OS."

---

## 🟢 Module 1: The Process

### 1.1 What is a Process?
A program in execution. It has:
*   **Code (Text):** The instructions.
*   **Data:** Global variables.
*   **Heap:** Dynamic memory.
*   **Stack:** Function calls.

### 1.2 Threads
Lightweight processes within a process. They share memory (dangerous!) but run independently.

---

## 🟡 Module 2: Memory Management

### 2.1 Virtual Memory
Your program thinks it has 4GB of RAM all to itself. It's a lie! The OS maps "Virtual Addresses" to physical RAM.
*   **Paging:** Swapping chunks of memory to the hard drive when RAM is full.

### 2.2 Stack vs Heap
*   **Stack:** Fast, ordered, small. Local variables.
*   **Heap:** Slower, chaotic, large. `malloc`/`new`.

---

## 🟠 Module 3: Concurrency & Locks

### 3.1 Race Conditions
Two threads try to change the same variable at the same time. Chaos ensues.

### 3.2 Locks (Mutex)
"Only one person in the bathroom at a time."
```c
lock(mutex);
// Critical section: Update shared data
unlock(mutex);
```

### 3.3 Deadlocks
Thread A waits for B. Thread B waits for A. Both wait forever.

---

## 🎓 Professor's Concept Check
"The OS is a manager. It creates the illusion that your browser, music player, and code editor are all running at the exact same time on a single CPU.
**Research:** Look up 'Context Switching'. How does the CPU freeze one process and start another so quickly?"

---

## 📚 Official Documentation & Resources
*   [Osd органами (OSDev Wiki)](https://wiki.osdev.org/Main_Page) - The ultimate resource for OS development.
*   [Linux Kernel Archives](https://www.kernel.org/) - Source code of the world's most popular open-source OS.
*   [Windows Internals Book](https://docs.microsoft.com/en-us/sysinternals/resources/windows-internals) - The definitive guide to how Windows works.