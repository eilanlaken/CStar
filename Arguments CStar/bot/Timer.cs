
public class Timer completes ObservedObject is Updated {

    public float elapsedTime;
    public float resetPeriod;
    private boolean awake;

}

public constant int MSG_CODE_RESET = 0;

public function (float resetPeriod) returns Timer {
    new Timer t;
    t.elapsedTime = 0;
    t.resetPeriod = resetPeriod;
    t.awake = false;
} same as new Timer(resetPeriod);

public function start() Timer t {
    t.awake = true;
}

public function stop() Timer t {
    t.awake = false;
}

public function reset() Timer t {
    t.elapsedTime = 0;
    t.broadcast(MSG_CODE_RESET, null);
}

public function update(float deltaTime) Timer t {
    elapsedTime += deltaTime;
    if (elapsedTime >= resetPeriod) {
        t.reset();
    }
}