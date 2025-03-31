DIFF_PYTHON = '''
```python
### mathweb/flask/app.py
<<<<<<< SEARCH
from flask import Flask
=======
import math
from flask import Flask
>>>>>>> REPLACE
```
'''

DIFF_JAVA = '''
```java
### src/bin/Main.java
<<<<<<< SEARCH
import java.io.Scanner;
=======
import java.io.Scanner;
import java.math.BigInteger;
>>>>>>> REPLACE
```
'''

DIFF_GO = '''
```go
### api/client.go
<<<<<<< SEARCH
import (
    "fmt"
)
=======
import (
    "fmt"
    "io"
)
>>>>>>> REPLACE
```
'''

DIFF_RUST = '''
```rust
### src/build.rs
<<<<<<< SEARCH
fn main() {
    let version = "1.0";
}
=======
fn main() {
    let version = "2.0";
}
>>>>>>> REPLACE
```
'''

DIFF_CPP = '''
```cpp
### src/main.cpp
<<<<<<< SEARCH
#include <cstdio>
=======
#include <cstdio>
#include <cstdlib>
>>>>>>> REPLACE
```
'''

DIFF_C = '''
```c
### src/main.c
<<<<<<< SEARCH
#include <cstdio>
=======
#include <cstdio>
#include <cstdlib>
>>>>>>> REPLACE
```
'''

DIFF_TYPESCRIPT = '''
```typescript
### src/main.ts
<<<<<<< SEARCH
import {
    foo
} from "./utils";
=======
import {
    foo
    bar
} from "./utils";
>>>>>>> REPLACE
```
'''

DIFF_JAVASCRIPT = '''
```javascript
### src/main.js
<<<<<<< SEARCH
import {
    foo
} from "./utils";
=======
import {
    foo
    bar
} from "./utils";
>>>>>>> REPLACE
```
'''