# ☕ Java Programming: The Universal Language

**Professor:** *Sips coffee from a mug with the Java logo.*
"Write Once, Run Anywhere. That is the promise of Java. It runs on 3 billion devices. From Android phones to banking servers to Minecraft. It is verbose, it is strict, and it is incredibly stable."

---

## 🟢 Module 1: The Basics

### 1.1 Hello World
Everything lives in a class.
```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello Java");
    }
}
```

### 1.2 Types & Control Flow
Standard C-style syntax.
```java
int count = 10;
String text = "Java is strict";
if (count > 5) {
    System.out.println(text);
}
```

---

## 🟡 Module 2: OOP Core (Intermediate)

### 2.1 Interfaces
Defining a contract.
```java
interface Animal {
    void makeSound();
}

class Cat implements Animal {
    public void makeSound() {
        System.out.println("Meow");
    }
}
```

### 2.2 Collections Framework
Lists, Sets, and Maps.
```java
import java.util.ArrayList;

ArrayList<String> list = new ArrayList<>();
list.add("Apple");
list.add("Banana");
```

---

## 🟠 Module 3: Advanced Java

### 3.1 Streams API
Functional programming in Java.
```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
names.stream()
     .filter(n -> n.startsWith("A"))
     .forEach(System.out::println);
```

### 3.2 Concurrency
Java was built for multithreading.
```java
Thread t = new Thread(() -> {
    System.out.println("Running in a new thread");
});
t.start();
```

---

## 🎓 Professor's Final Exam
"Java is the backbone of the enterprise world.
**Assignment:** Create a class `BankAccount`. Add methods to `deposit` and `withdraw`. Use an Interface to enforce these rules. Then, try to simulate two threads accessing the account at the same time!"

---

## 📚 Official Documentation & Resources
*   [Oracle Java Documentation](https://docs.oracle.com/en/java/) - The official API specification.
*   [Baeldung](https://www.baeldung.com/) - Excellent, high-quality tutorials for modern Java and Spring.
*   [Spring Framework](https://spring.io/projects/spring-framework) - The most popular framework for enterprise Java.