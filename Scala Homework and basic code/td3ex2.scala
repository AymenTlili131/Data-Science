case class Rectangle(private var _x:Int,private var _y:Int=8) {
  def x=_x //get de x
  def x_=(a:Int): Unit ={
    if(a<0)
      println("largeur doit etre >= 0 !!!")
    else
      _x=a
  }
  def y=_y
  def y_=(a:Int): Unit ={
    if(a<0)
      println("longueur doit etre >= 0 !!!")
    else
      _y=a
  }

  //override def toString: String = "Rectangle("+ _x +","+_y+")"

  //override def equals(obj: Any): Boolean = if(_x== (Rectangle) obj._x && _y==obj.y) true else false

}
object Test extends App{
  val R1 = Rectangle(2, 8)
  println(R1) // Rectangle(2,8)
  R1.x = -4 // largeur doit etre >= 0 !!!
  R1.y = -7 // longueur doit etre >= 0 !!!
  println(R1) // Rectangle(2,8)
  val R2 = Rectangle(2)
  println(R2) // Rectangle(2,8)
  if(R1 == R2) println("equals") else println("not equals") // equals
  val R3 = R2.copy()
  println(R3) // Rectangle(5,8)
  if(R3 == R2) println("equals") else println("not equals") // equals
  R3.x=3
  println(R2) // Rectangle(5,8)
  println(R3) // Rectangle(3,8)
}
