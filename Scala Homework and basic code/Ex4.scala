import scala.io.StdIn.readInt

object Ex4 extends App{


    var n: Int=0
    do {
      print("donner n")
      n = readInt()
    }while(n<=20)
  val number:Int=n
    var test: Boolean = false
    for (i <- 2 until number) {
      for (j <- 2 until i) {
        if (i % j == 0) {
          test=true
        }
      }
      if (!test)
        println("le nombre " + i + " est premier")
      else
        println("le nombre " + i + " n'est pas premier")
      test=false
    }
}