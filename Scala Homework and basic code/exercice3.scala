
abstract class forme{
   var surface:Float
  def calculSurface():Float;
}
trait colorable {
  def afficher(): Unit ={
    println("colorable")
  }
   def colorer(couleur:String):Unit
}
class Rectangle(largeur:Float, hauteur:Float) extends forme with colorable{

  override var surface: Float = calculSurface()

  override def calculSurface(): Float = largeur*hauteur

  def colorer(couleur: String): Unit = {
    println(couleur)
  }
}
class Cercle(rayon:Float) extends forme with colorable{
  val pi:Float=3.14f
  override var surface: Float = calculSurface()

  override def calculSurface(): Float = rayon*pi

  def colorer(couleur: String): Unit = {
    println(couleur)
  }
}
object exercice3 extends App{
  var rect1:Rectangle=new Rectangle(5,6)
  var cerc:Cercle=new Cercle(10)
  println("surface rectangle = "+rect1.surface)
  println("surface cercle = "+cerc.surface)

  rect1.colorer("Bleu")
  cerc.colorer("rouge")
}
