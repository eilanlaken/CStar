
public database CityDB {

    public City city;

    // schema
    public relation father(Person x, Person y); // <- x is the father of y
    public relation mother(Person x, Person y); // <- x is the mother of y
    public relation married(Person x, Person y);
    public relation parent(Person x, Person y); // <- x is either the father or the mother of y
    public relation siblings(Person x, Person y); // <- x and y are siblings, duh
    public relation knows(Person x, Person y); // <- x knows person y
    public relation friends(Person x, Person y);
    public relation foes(Person x, Person y);
    public relation owes(Person x, Person y, int n); // <- x owes y n amount of money

}

@constructor
public function (City city) returns CityDB {
    new CityDB cityDB;
    cityDB.city = city;
    return cityDB;
} same as new CityDB(city);

