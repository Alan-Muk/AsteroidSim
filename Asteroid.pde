class Asteroid {

  float a, e, i, Omega, omega, M0;
  float n;

  Asteroid(float a_, float e_, float i_, float O_, float o_, float M_) {
    a = a_;
    e = e_;
    i = radians(i_);
    Omega = radians(O_);
    omega = radians(o_);
    M0 = radians(M_);

    n = sqrt(1.0 / (a * a * a));
  }

  PVector getPosition(float t) {
    float M = M0 + n * t;

    float E = math.solveKepler(M, e);

    float x = a * (cos(E) - e);
    float y = a * sqrt(1 - e*e) * sin(E);
    float z = 0;

    PVector v = new PVector(x, y, z);

    math.rotateZ(v, omega);
    math.rotateX(v, i);
    math.rotateZ(v, Omega);

    return v;
  }
}
