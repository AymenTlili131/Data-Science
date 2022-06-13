

object TestPoint extends App
{
  val p:Point = new Point()
  p.x= -2
  p.x_=(-2)
  println (p.setX(-2))
}

class Point {
  var x :Int=0
  def getX = x
  def setX(a: Int) ={

    if (a<0)
      throw new Exception("Erreur1")
    else
      x=a
  }
}
