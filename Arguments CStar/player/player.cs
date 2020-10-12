
@states(idle, walk, dead)
public class Player {

    constant string name;
    vector2 transform;

}

@constructor
public function (string name, vector2 transform) returns Player {
    new Player p;
    p.name = name;
    p.transform = transform;
    return p;
} same as new Player(name,transform);

@idle
public function update(float deltaTime) Player p {

}

@walk
public function update(float deltaTime) Player p {

}