
 // <- x is the father of y ->
public relation father(Person x, Person y) {

}

// <- x is the mother of y ->
public relation mother(Person x, Person y) {

}

// <- x and y are siblings ->
public relation siblings(Person x, Person y) {
    siblings(x,y) -> siblings(y,x);
    siblings(x,y) <-> mother(m,x) and mother(m,y);
}





