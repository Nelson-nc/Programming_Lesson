# ⚙️ Assembly Language: Speaking to the Hardware

**Professor:** *Holds up a microchip.*
"We are going deeper. Below C, below the operating system, there is this. Assembly is the closest you can get to the processor without using a soldering iron. We don't have 'variables' here; we have **Registers**."

*Note: We will focus on x86_64 architecture for examples, as it's common on desktops.*

---

## 🟢 Module 1: The CPU's Workbench

### 1.1 Registers
These are tiny, super-fast storage slots inside the CPU.
*   `rax`, `rbx`, `rcx`, `rdx`: General purpose (often used for math/logic).
*   `rsp`: Stack Pointer (tracks the top of the stack).
*   `rip`: Instruction Pointer (tracks the next instruction to run).

### 1.2 Basic Instructions
*   `MOV`: Move data (Copy). `MOV rax, 5` (Put 5 into rax).
*   `ADD`: Math. `ADD rax, 3` (rax becomes 8).
*   `SUB`: Subtract.
*   `CMP`: Compare two values.

---

## 🟡 Module 2: Logic & Control

### 2.1 Jumps (The `if` statement of Assembly)
We compare, then we jump based on the result (Flags).
```asm
MOV rax, 10
CMP rax, 5      ; Compare rax to 5
JG greater_label ; Jump if Greater
; ... code runs if NOT greater ...
JMP end_label

greater_label:
    ; ... code runs if greater ...

end_label:
```

### 2.2 The Stack
Pushing and Popping data.
```asm
PUSH rax ; Save rax to stack
POP rbx  ; Restore it into rbx
```

---

## 🟠 Module 3: Reverse Engineering (C to Assembly)

### 3.1 How C maps to ASM
If you write this in C:
```c
int add(int a, int b) {
    return a + b;
}
```
The compiler generates something like this (simplified):
```asm
_add:
    mov eax, edi  ; Get first argument
    add eax, esi  ; Add second argument
    ret           ; Return result (in eax)
```

---

## 🎓 Professor's Insight
"Assembly teaches you *cost*. You realize that a simple line of Python might trigger thousands of CPU instructions.
**Experiment:** Write a tiny C program and run `gcc -S file.c` to see the assembly code it generates. It is enlightening!"

---

## 📚 Official Documentation & Resources
*   [Intel® 64 and IA-32 Architectures Software Developer Manuals](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html) - The definitive guide for x86.
*   [ARM Architecture Reference Manual](https://developer.arm.com/documentation) - For mobile and Apple Silicon chips.
*   [Godbolt Compiler Explorer](https://godbolt.org/) - An amazing online tool to see how C/C++ compiles to Assembly in real-time.