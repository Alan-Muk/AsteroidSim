class MPCLoader {

  void load(String filename, ArrayList<Asteroid> out, int limit) {

    String[] lines = loadStrings(filename);

    for (int i = 40; i < lines.length; i++) {

      try {
        String line = lines[i];

        float a = parse(line, 92, 103);
        float e = parse(line, 70, 79);
        float inc = parse(line, 59, 68);
        float node = parse(line, 48, 57);
        float peri = parse(line, 37, 46);
        float M = parse(line, 26, 35);

        if (a > 1.5 && a < 6.0) {
          out.add(new Asteroid(a, e, inc, node, peri, M));
        }

        if (out.size() >= limit) break;

      } catch (Exception e) {
        continue;
      }
    }
  }

  float parse(String line, int a, int b) {
    if (line.length() < b) return 0;
    return float(trim(line.substring(a, b)));
  }
}
