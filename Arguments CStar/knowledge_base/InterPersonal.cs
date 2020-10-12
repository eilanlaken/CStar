
public relation knows(Person x, Person y) {

}

public relation friends(Person x, Person y) {
    friends(x,y) -> knows(x,y) and knows(y,x);
    friends(x,y) -> not foes(x,y);
}

public relation foes(Person x, Person y) {
    foes(x,y) -> knows(x,y) and knows(y,x);
    foes(x,y) -> not friends(x,y);
}

public relation owes(Person x, Person y, int n) {

}