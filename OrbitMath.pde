class OrbitMath {

  float solveKepler(float M, float e) {
    float E = M;

    for (int i = 0; i < 6; i++) {
      E = E - (E - e*sin(E) - M) / (1 - e*cos(E));
    }

    return E;
  }

  void rotateX(PVector v, float a) {
    float y = v.y*cos(a) - v.z*sin(a);
    float z = v.y*sin(a) + v.z*cos(a);
    v.y = y;
    v.z = z;
  }

  void rotateZ(PVector v, float a) {
    float x = v.x*cos(a) - v.y*sin(a);
    float y = v.x*sin(a) + v.y*cos(a);
    v.x = x;
    v.y = y;
  }
}
