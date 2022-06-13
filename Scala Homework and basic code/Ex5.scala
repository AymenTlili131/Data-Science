import scala.io.StdIn.readInt

object Ex5 extends  App {
    var n:Int=0
    var nb:Int=0
    var somme:Float=0
  var test:Boolean=true
    do{
      println("donner un entier")
      n=readInt()
      if(n == -1){
        test=false
      }else if(n>0){
        somme=somme+n
        nb=nb+1
      }
    }while(test)
    println(s"La moyenne  de ces $nb entiers vaut  "+somme/nb)
}