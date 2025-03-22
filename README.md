# 🖥️ Best-Fit Memory Manager

## 📖 Overview
This project is a **Best-Fit Memory Allocation Simulator** that efficiently assigns memory blocks to processes. It finds the smallest available memory space that fits the requested size, reducing fragmentation.

## 🔹 Key Features
- Parses **memory map** (`memmap.1`) and **process requests** (`reqs.1`).
- Implements **Best-Fit allocation** to optimize memory usage.
- Displays memory assignments and updates after allocation.
- Provides command-line execution with customizable options.
- Supports **testing with unittest**.

---

## 🧪 Running Tests
Before running tests, ensure you have set the `PYTHONPATH` correctly. Replace `<your-project-path>` with your actual directory.

**Windows**
```sh
SET PYTHONPATH=%PYTHONPATH%;<your-project-path>
```
**Linux/macOS**
```sh
export PYTHONPATH=$PYTHONPATH:<your-project-path>
```

Then, execute:
```sh
python -m unittest test/test_best_fit.py
```

---

## ⚡ Running the Simulator
### 🏃 Basic Execution
To execute the **memory allocation simulator**, run:
```sh
python cma.py --memmap ./resources/memmap/memmap_1.txt --reqs ./resources/reqs/reqs_1.txt
```

### 🎯 Running the Best-Fit Algorithm
To specifically use the **Best-Fit** strategy:
```sh
python cma.py --memmap ./resources/memmap/memmap_1.txt --reqs ./resources/reqs/reqs_1.txt --function best
```

### 🛠️ Custom Memory Block Positioning
You can choose a specific **position** in the memory list to allocate a request:
```sh
python cma.py --memmap ./resources/memmap/memmap_1.txt --reqs ./resources/reqs/reqs_1.txt --pos 3
```

---
🚀 *Happy coding!*