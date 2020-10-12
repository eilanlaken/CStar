// need globally used relations.
// entities: a bundle of classes + relations.
public entity Car {

    private relation observes;
    private relation attached;

}

public function (matrix4 transform) returns Car {
    Plate plate = new Plate();
    for (int i = 0...plate.anchors.last) {
        Wheel wheel = new Wheel(UPRIGHT, plate.anchors[i].location);
        observes += (wheel, plate)
        observes += (plate, wheel)
        attached += (plate, wheel)
    }
    Body body = new Body();
    attached(body, plate);
} same as new Car(transform);

