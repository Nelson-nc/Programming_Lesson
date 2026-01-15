# 🔷 C# Programming: The Microsoft Powerhouse

**Professor:** *Points to a sleek, modern enterprise building.*
"C# (C-Sharp) is Java's younger, cooler sibling. It powers Windows apps, the Unity game engine, and massive enterprise systems. It is robust, strictly typed, and has some of the best tooling in the world (Visual Studio)."

---

## 🟢 Module 1: The Basics

### 1.1 Syntax
Very similar to Java and C++.
```csharp
using System;

class Program {
    static void Main() {
        Console.WriteLine("Hello C#");
        int age = 30;
    }
}
```

### 1.2 OOP
C# is purely Object-Oriented.
```csharp
public class Car {
    public string Model { get; set; } // Property

    public void Drive() {
        Console.WriteLine("Vroom!");
    }
}
```

---

## 🟡 Module 2: Intermediate Features

### 2.1 LINQ (Language Integrated Query)
Querying data like SQL, but inside code.
```csharp
int[] numbers = { 1, 5, 8, 10, 3 };

// Get all even numbers
var evens = from n in numbers
            where n % 2 == 0
            select n;
```

### 2.2 Delegates & Events
How buttons work (Callback system).
```csharp
public delegate void Notify();  // Define a signature
public event Notify ProcessCompleted; // Define an event
```

---

## 🟠 Module 3: Advanced .NET

### 3.1 Async / Await (Task Parallel Library)
C# pioneered this pattern.
```csharp
public async Task<string> GetDataAsync() {
    await Task.Delay(1000); // Simulate work
    return "Data Loaded";
}
```

### 3.2 Memory Management
C# has a Garbage Collector, but you can use `Span<T>` for high performance.

---

## 🎓 Professor's Recommendation
"If you want to make games, learn **Unity** (which uses C#). If you want to build websites, look at **ASP.NET Core**.
**Try this:** Use LINQ to filter a list of names to find only those starting with 'A'."

---

## 📚 Official Documentation & Resources
*   [Microsoft Learn (.NET/C#)](https://learn.microsoft.com/en-us/dotnet/csharp/) - World-class documentation and tutorials.
*   [Unity Learn](https://learn.unity.com/) - If you are interested in Game Development with C#.
*   [.NET Source Code](https://github.com/dotnet/runtime) - See how C# is built on GitHub.