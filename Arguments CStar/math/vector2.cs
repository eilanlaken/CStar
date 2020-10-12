page vector2 chapter vectors;

@managed
@pooled
@ordered(by: length2())
public primitive class vector2 {
    float x;
    float y;
}

@constructor
public function () returns vector2 {
    new vector2 v;
    v.x = 0;
    v.y = 0;
    return v;
} same as new vector2();

@constructor
public function (float x, float y) returns vector2 {
    new vector2 v;
    v.x = x;
    v.y = y;
    return v;
} same as new vector2(x, y);

@constructor
public function (vector2 other) returns vector2 {
    new vector2 v;
    v.x = other.x;
    v.y = other.y;
    return v;
} same as new vector2(other);

public function (vector2 left, vector2 right) {
    if (left == null) left = new vector2(right);
    else {
        left.x = right.x;
        left.y = right.y;
    }
} same as left = right;

public function (vector2 left, vector2 right) returns boolean {
    if (left == right) return true;
    else {
        if (left == null and right != null) or (left != null and right == null) return false;
        if (left.x != right.x) or (left.y != right.y) return false;
    }
    return true;
} same as left == right;

public function (vector2 c, vector2 a, vector2 b) {
    if (c == null) c = new vector2(a.x + b.x, a.y + b.y)
    else {
        c.x = a.x + b.x;
        c.y = a.y + b.y;
    }
} same as c = a + b;

// should yield compile error: primitive classes cannot have object methods.
public function print() vector2 v {
    print("[" + v.x + "," + v.y + "]");
}

// this version of print should compile with no errors:
public function print(vector2 v) {
    print("[" + v.x + "," + v.y + "]");
}

