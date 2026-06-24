ArrayList<Asteroid> asteroids = new ArrayList<Asteroid>();
MPCLoader loader;
OrbitMath math = new OrbitMath();

float t = 0;
float dt = 0.02;

float SCALE = 180;

void setup() {
  size(1000, 800, P3D);
  smooth(8);
  
  loader = new MPCLoader();
  loader.load("MPCORB.DAT", asteroids, 2000);

  println("Loaded: " + asteroids.size());
}

void draw() {
  background(0);
  lights();

  translate(width/2, height/2, 0);
  rotateX(PI/3);
  rotateZ(frameCount * 0.001);

  drawSun();
  drawAsteroids();

  t += dt;
}

void drawSun() {
  noStroke();
  fill(255, 200, 0);
  sphere(12);
}

void drawAsteroids() {
  stroke(255, 140);
  strokeWeight(2);

  for (Asteroid a : asteroids) {
    PVector p = a.getPosition(t);
    point(p.x * SCALE, p.y * SCALE, p.z * SCALE);
  }
}
