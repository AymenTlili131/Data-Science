object td extends App {
  def combination(x: Int, y: Int, f: (Int, Int) => Int) = print(f(x, y))

  combination(23, 12, _ * _)
}