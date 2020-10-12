
// catalog is a fixed size set of objects.
// cannot extend a class
public catalog Cards {

    // <-- must be declared with the constant qualifier -->
    constant string name;
    constant int rank;
    constant int suit;
    constant int color;

} AceSpades = new Cards(1,2), ...;

private function (int rank, int suit) returns Cards {
    new Cards card;
    card.name = ...;
    card.rank = rank;
    ...
    return card;
} same as new Cards(rank, suit);







