import scala.io.StdIn.readInt

object Ex6 extends App{
    val tab = new Array[Int](9)
    var n: Int = 0
    do{
      println("donner le nombre ")
      n=readInt()
    }while(n>10 || n<6)
  var somme:Int=0
  var min:Int=tab(0)
  var max:Int=tab(0)
    for(i<-0 until(n))
    {
      println(s"Tab[${i+1}]=")
      tab(i)=readInt()
      somme+=tab(i)
      if(tab(i)>max) max=tab(i)
      if(tab(i)<min) min=tab(i)
    }
    println("somme="+somme)
    println("moyenne="+somme/n)
    println("min="+min)
    println("max="+max)
}

/*def tri(tab: Array[Int]): Unit = {
  val taille = tab.length
  for (i <- 1 until taille) {
    val index = tab(i)
    var j = i - 1
    while ( {
      j >= 0 && tab(j) > index
    }) {
      tab(j + 1) = tab(j)
      j -= 1
    }
    tab(j + 1) = index
  }
}*/