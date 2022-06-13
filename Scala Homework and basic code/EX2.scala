import scala.io.StdIn._
object EX2 extends App{
  print("Donner nom étudiant ")
  val nom:String=readLine()
  print("Donner age etudiant ")
  val age:Int=readInt()
  print("Donner moyenne etudiant ")
  val moyenne:Float=readFloat()
  println("étudiant [nom= "+nom+" , age= "+age+" , moyenne = "+moyenne+"]")
  printf("étudiant [nom= %s , age= %d  moyenne = %.2f]",nom,age,moyenne)
  println(s"\nétudiant [nom= $nom , age= ${age+10} , moyenne = $moyenne]")

}
