# print
Stdout üzerinde çıktır vereyi sağlar.

|Varargs|Description|
|-------|-----------|
|objects|Verilen değerleri yazdırır. Varargs olarak değerler alır.|
|end|Default da \n olarak tanımlıdır.|
|sep|Default da boşluk olarak tanımlıdır.|
|*objects|verilen her karakteri tek tek gezerek yazar.|

# Syntax
```python
print(*objects, sep=' ', end='\n');
```

# Examples
```python
print("Hello World!");
print("Hello World!", end=" ");
print("01", "01", "2025", sep="/");
print(*"Hello World");
```