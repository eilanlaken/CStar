
// attributes are shared or public.
@states(resting, extending, retracting)
public class RobotArm extends ObserverObject can be Updated {
    shared ArmSegment a;
    shared ArmSegment b;
    shared ArmSegment c;
}

// becomes:

public base class RobotArm__base is ObserverObject can be updated {


}

public base class RobotArm__resting is RobotArm__base {

}

public base class RobotArm__extending is RobotArm__resting {

}

public base class RobotArm_retracting is RobotArm__extending {

}

public class RobotArm is RobotArm__retracting {


}