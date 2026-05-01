# 👤 Younger Person Comparison (Python – Java Style Logic)

## 📌 Description

This program demonstrates how to **compare two objects** and return the **younger person**, following logic similar to Java (returning an object reference).

---

## 🚀 Features

* Uses a `Person` class
* Compares two objects
* Returns one object from a method
* Mimics Java-style object comparison

---

## 🛠️ How It Works

1. A class `Person` is created with:

   * `name`
   * `age`

2. Method `younger(t)`:

   * Compares current object (`self`) with another object (`t`)
   * Returns the object with smaller age

3. In main:

   * `p1` and `p2` are created
   * `younger()` is called
   * Result is stored in `y`
   * `y.getInfo()` prints the younger person

---

## 💻 Code

```python id="m9x2pt"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getInfo(self):
        print("Name   :", self.name)
        print("Age    :", self.age)

    def younger(self, t):
        if self.age < t.age:
            return self
        else:
            return t


# Main program
p1 = Person("Akshay", 26)
p2 = Person("Saurabh", 30)

y = p1.younger(p2)

print("Younger person")
y.getInfo()
```

---

## ▶️ Output

```id="k4q8zn"
Younger person
Name   : Akshay
Age    : 26
```

---

## 🧠 Important Concept

* `self` → current object (`p1`)
* `t` → passed object (`p2`)
* Method returns an **object**, not just a value

👉 Same concept as Java:

```java id="c7l2vm"
Person younger(Person t)
```

---

## 🎯 Key Learning

This is important because:

* You are **returning object references**
* This is heavily used in:

  * Comparators
  * Sorting logic
  * Data structures

---

## ⚡ Cleaner Python Version (Advanced)

You can simplify this using Python’s `min()`:

```python id="p3x7ls"
y = min([p1, p2], key=lambda p: p.age)
y.getInfo()
```

---

## 🔧 Future Improvements

* Compare multiple persons (list)
* Find oldest person
* Sort list of persons by age
* Add more attributes

---

## 📄 License

This project is open-source and free to use.
